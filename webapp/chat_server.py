"""
Lightweight, self-contained web chat for the Cubyz Assistant -- built to replace Open WebUI for
this specific use case after Open WebUI's own chat UI proved unreliable (its frontend gives up
("Connection lost") after ~10s, well before the RAG retrieval + generation pipeline actually
finishes -- retrieval alone can take longer than that against the larger knowledge collections).

This reuses local_rag_chat.py's exact retrieval+generation logic directly (same embedding index,
same system prompt, same temperature=0 deterministic Ollama call -- the pipeline validated at
89% across this whole project's testing), wrapped in a minimal FastAPI server with a plain
HTML/JS frontend and SQLite-backed per-browser chat history. Zero changes to local_rag_chat.py
itself, so none of the validated behavior is at risk.

No login required -- each visitor gets a persistent history tied to a random session cookie.
Real accounts can be layered on top of this later without a rewrite: the sessions table already
exists, a login would just add a users table and swap the anonymous cookie for an authenticated
one.

Every assistant answer can be thumbs-up/thumbs-down'd from the UI; the vote is stored on the
message row (POST /api/feedback). Run export_feedback.py to pull every disliked question+answer
pair back out for review -- that's the actual point of collecting it, feeding wrong answers back
into fixing the knowledge_base/ chunks the same way this project's testing did all session.

Run (from anywhere -- all paths are anchored to this file's own location, not the cwd):
    pip install fastapi uvicorn
    python3 webapp/chat_server.py
Then open http://localhost:7001 . Moved off 7000 (2026-07-18) so this can run at the same time as
pipeline_crunching/server.py, which owns 7000 for the distributed crunching/audit campaigns --
the two used to have to run one at a time on the same port. It still binds to 0.0.0.0, so once the
router forwards 7001 to this machine, it's reachable from outside as a real shareable URL (your
public IP:7001, or a domain pointed at it) -- the router's forwarding rule needs updating to match
if it was set up for the old port 7000.
"""
import asyncio
import json
import sqlite3
import threading
import time
import uuid
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.concurrency import run_in_threadpool

import local_rag_chat

HOST = "0.0.0.0"
PORT = 7001
DB_PATH = str(Path(__file__).parent / "chat_history.db")
SESSION_COOKIE = "cubyz_session"
FRONTEND_PATH = Path(__file__).parent / "chat_frontend.html"

# Multiple visitors can hit /api/chat at the same time, but each generation call holds a big
# chunk of GPU memory for the duration (model weights + a 16384-token context per request). With
# no cap, enough simultaneous chats can OOM the GPU and take the whole server down for everyone.
# This is a concurrency *policy* choice, not a measured hardware limit -- 3 is a generous starting
# point for a single consumer GPU running one 4B model; adjust based on real VRAM headroom.
MAX_CONCURRENT_GENERATIONS = 3
_generation_semaphore = asyncio.Semaphore(MAX_CONCURRENT_GENERATIONS)
_active_generations = 0
_active_lock = asyncio.Lock()

# Which sessions are mid-compaction right now, so the frontend can show "Compacting..." instead
# of the normal typing indicator and hold off letting that visitor send another message while
# their history is actively being rewritten. Set/cleared from the worker thread doing the
# compaction (see _build_conversation_history), read from GET /api/compacting on the event loop --
# a plain threading.Lock rather than asyncio.Lock since the writer side runs in a thread, not a
# coroutine.
_compacting_sessions = set()
_compacting_lock = threading.Lock()

# Same-chat memory: each question is still answered by a fresh, independent RAG retrieval (that
# part never changes), but now the model also sees prior turns from *this* session, so "what about
# that one?" resolves. Kept bounded with a rolling compaction instead of sending the whole history
# forever, since that would eventually blow past num_ctx (16384, shared with the system prompt +
# retrieved chunks + this turn's answer) and either truncate silently or fail outright.
#
# HISTORY_CHAR_BUDGET is a rough char-count proxy for tokens (~4 chars/token for English text),
# not a real tokenizer -- no tokenizer dependency is wired up here. If prompt_tokens on live
# answers ever creeps uncomfortably close to num_ctx, tighten this rather than trusting the ratio
# blindly.
HISTORY_CHAR_BUDGET = 12000
_index = None  # embedding index, loaded once at startup and reused across all requests


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            feedback TEXT,
            feedback_note TEXT
        )
    """)
    # Migration for DBs created before these columns existed -- ALTER TABLE ADD COLUMN has no
    # "IF NOT EXISTS" in SQLite, so check first rather than swallowing the real error.
    cols = {row[1] for row in conn.execute("PRAGMA table_info(messages)").fetchall()}
    if "feedback" not in cols:
        conn.execute("ALTER TABLE messages ADD COLUMN feedback TEXT")
    if "feedback_note" not in cols:
        conn.execute("ALTER TABLE messages ADD COLUMN feedback_note TEXT")
    if "meta" not in cols:
        # JSON blob: {model, sources, prompt_tokens, response_tokens, elapsed_seconds}. Assistant
        # rows only -- lets history replay show the same "what answered this / what it used" info
        # a live answer gets, instead of that info only existing for the current page session.
        conn.execute("ALTER TABLE messages ADD COLUMN meta TEXT")
    # One row per session: the rolling recap of everything already folded out of the verbatim
    # window (see HISTORY_CHAR_BUDGET above), plus a pointer to the last message id it covers so
    # a later compaction only summarizes what's new instead of redoing the whole conversation.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS session_memory (
            session_id TEXT PRIMARY KEY,
            summary TEXT,
            compacted_through_id INTEGER NOT NULL DEFAULT 0
        )
    """)
    return conn


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _index
    print("[~] Loading RAG index (reusing local_rag_chat.py's cached embeddings)...")
    _index = local_rag_chat.load_index()
    print(f"[OK] Index ready ({len(_index)} chunks). Serving on http://{HOST}:{PORT}")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE) or str(uuid.uuid4())
    resp = HTMLResponse(FRONTEND_PATH.read_text())
    resp.set_cookie(SESSION_COOKIE, session_id, max_age=60 * 60 * 24 * 365, httponly=True)
    # The file is read fresh from disk on every request (no server-side caching), but without an
    # explicit no-store header, browsers can still serve a stale cached copy after a frontend edit
    # -- confirmed source of a real "the fix isn't working" false alarm. Frontend edits are
    # infrequent enough that re-fetching every load costs nothing noticeable.
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.get("/api/history")
async def history(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        return JSONResponse([])
    conn = db()
    rows = conn.execute(
        "SELECT id, role, content, feedback, feedback_note, meta FROM messages WHERE session_id = ? ORDER BY id ASC",
        (session_id,),
    ).fetchall()
    conn.close()
    return JSONResponse([
        {"id": i, "role": r, "content": c, "feedback": f, "feedback_note": n, "meta": json.loads(m) if m else None}
        for i, r, c, f, n, m in rows
    ])


@app.get("/api/status")
async def status():
    return JSONResponse({
        "model": local_rag_chat.ANSWER_MODEL,
        "embed_model": local_rag_chat.EMBED_MODEL,
        "chunks": len(_index) if _index is not None else 0,
        "active_generations": _active_generations,
        "max_concurrent_generations": MAX_CONCURRENT_GENERATIONS,
    })


@app.get("/api/compacting")
async def compacting(request: Request):
    # Polled by the frontend only while a message is in flight (see chat_frontend.html), to swap
    # the typing indicator for a "Compacting..." notice during the rare turns that trigger it.
    session_id = request.cookies.get(SESSION_COOKIE)
    with _compacting_lock:
        is_compacting = session_id in _compacting_sessions
    return JSONResponse({"compacting": is_compacting})


def _build_conversation_history(conn, session_id, exclude_id=None):
    """Returns (history_messages, was_compacted) for this session: history_messages is the list
    to hand to local_rag_chat.ask() as conversation_history -- an optional recap of everything
    older, followed by verbatim recent turns, oldest first. Compacts (one extra Ollama call) and
    persists the result to session_memory only when the verbatim window has grown past
    HISTORY_CHAR_BUDGET; a normal turn just reads what's already there.

    exclude_id: the just-inserted current question's row id, if any -- it's passed to ask()
    separately as the live `question` arg, so it must not also appear in conversation_history."""
    row = conn.execute(
        "SELECT summary, compacted_through_id FROM session_memory WHERE session_id = ?",
        (session_id,),
    ).fetchone()
    summary, compacted_through_id = row if row else (None, 0)

    pending = conn.execute(
        "SELECT id, role, content FROM messages WHERE session_id = ? AND id > ? AND id != ? ORDER BY id ASC",
        (session_id, compacted_through_id, exclude_id or -1),
    ).fetchall()

    total_chars = sum(len(content) for _, _, content in pending)
    was_compacted = False
    if total_chars > HISTORY_CHAR_BUDGET and len(pending) > 2:
        # Fold all but the most recent exchange (last user+assistant pair) into the recap --
        # always leaving at least one real exchange verbatim keeps the immediately-preceding
        # turn exact, which matters most for a direct follow-up question.
        to_fold, keep_verbatim = pending[:-2], pending[-2:]
        with _compacting_lock:
            _compacting_sessions.add(session_id)
        try:
            summary = local_rag_chat.summarize_conversation(
                summary, [{"role": r, "content": c} for _, r, c in to_fold]
            )
        finally:
            with _compacting_lock:
                _compacting_sessions.discard(session_id)
        compacted_through_id = to_fold[-1][0]
        conn.execute(
            "INSERT INTO session_memory (session_id, summary, compacted_through_id) VALUES (?, ?, ?) "
            "ON CONFLICT(session_id) DO UPDATE SET summary = excluded.summary, "
            "compacted_through_id = excluded.compacted_through_id",
            (session_id, summary, compacted_through_id),
        )
        conn.commit()
        pending = keep_verbatim
        was_compacted = True

    history = []
    if summary:
        history.append({"role": "system", "content": f"## Earlier in this conversation\n{summary}"})
    history.extend({"role": r, "content": c} for _, r, c in pending)
    return history, was_compacted


@app.post("/api/chat")
async def chat(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        return JSONResponse({"error": "no session cookie -- reload the page"}, status_code=400)

    body = await request.json()
    question = (body.get("message") or "").strip()
    if not question:
        return JSONResponse({"error": "empty message"}, status_code=400)

    conn = db()
    cursor = conn.execute(
        "INSERT INTO messages (session_id, role, content) VALUES (?, 'user', ?)",
        (session_id, question),
    )
    this_message_id = cursor.lastrowid
    conn.commit()
    conn.close()

    def build_history_and_ask():
        # Runs in the threadpool, not the event loop -- both compaction (an Ollama call,
        # occasional) and the main answer (an Ollama call, every turn) block on real network I/O,
        # so neither belongs on the async side. Reads history fresh each call: a brand-new
        # connection per thread, since sqlite3 connections aren't safe to share across threads.
        history_conn = db()
        try:
            conversation_history, _ = _build_conversation_history(
                history_conn, session_id, exclude_id=this_message_id
            )
        finally:
            history_conn.close()
        return local_rag_chat.ask(question, _index, False, True, conversation_history)

    # The semaphore below caps how many threads can be doing real GPU work (answer generation,
    # or the occasional compaction call) at once -- queued requests wait here (still responsive,
    # just not yet generating) rather than piling straight onto the GPU and risking an OOM that
    # would take the whole server down.
    global _active_generations
    async with _generation_semaphore:
        async with _active_lock:
            _active_generations += 1
        try:
            t0 = time.monotonic()
            result = await run_in_threadpool(build_history_and_ask)
            elapsed = round(time.monotonic() - t0, 2)
        finally:
            async with _active_lock:
                _active_generations -= 1
    answer = result["answer"]
    meta = {
        "model": result["model"],
        "embed_model": result["embed_model"],
        "sources": result["sources"],
        "prompt_tokens": result["prompt_tokens"],
        "response_tokens": result["response_tokens"],
        "elapsed_seconds": elapsed,
    }
    # HISTORY_CHAR_BUDGET is a char-count guess at a token budget, not a real count -- this checks
    # the guess against Ollama's own real prompt_tokens for this request, so a bad guess shows up
    # as a log line instead of silently truncating someone's context later. num_ctx itself
    # (local_rag_chat.NUM_CTX) already caps generation length; this is only an early warning.
    prompt_tokens = result.get("prompt_tokens")
    if prompt_tokens and prompt_tokens > 0.85 * local_rag_chat.NUM_CTX:
        print(
            f"[!] session {session_id[:8]}: prompt_tokens={prompt_tokens} is close to "
            f"num_ctx={local_rag_chat.NUM_CTX} -- consider lowering HISTORY_CHAR_BUDGET"
        )

    conn = db()
    cursor = conn.execute(
        "INSERT INTO messages (session_id, role, content, meta) VALUES (?, 'assistant', ?, ?)",
        (session_id, answer, json.dumps(meta)),
    )
    message_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return JSONResponse({"answer": answer, "message_id": message_id, **meta})


@app.post("/api/feedback")
async def feedback(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        return JSONResponse({"error": "no session cookie"}, status_code=400)

    body = await request.json()
    message_id = body.get("message_id")
    value = body.get("feedback")  # "like", "dislike", or null to clear a previous vote
    note = body.get("note")  # optional free-text explanation, only meaningful alongside "dislike"
    if value not in ("like", "dislike", None):
        return JSONResponse({"error": "feedback must be 'like', 'dislike', or null"}, status_code=400)
    if not isinstance(message_id, int):
        return JSONResponse({"error": "message_id must be an integer"}, status_code=400)
    if note is not None:
        if not isinstance(note, str):
            return JSONResponse({"error": "note must be a string"}, status_code=400)
        note = note.strip()[:2000] or None  # cap length; empty/whitespace-only note is no note
    if value is None:
        note = None  # clearing the vote clears any note that went with it

    conn = db()
    # Scoped to this session_id too -- a visitor can only vote on messages from their own chat,
    # not an arbitrary message_id belonging to someone else's conversation.
    cursor = conn.execute(
        "UPDATE messages SET feedback = ?, feedback_note = ? WHERE id = ? AND session_id = ? AND role = 'assistant'",
        (value, note, message_id, session_id),
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated == 0:
        return JSONResponse({"error": "message not found in your session"}, status_code=404)
    return JSONResponse({"ok": True})


@app.post("/api/new_chat")
async def new_chat():
    new_session_id = str(uuid.uuid4())
    resp = JSONResponse({"ok": True})
    resp.set_cookie(SESSION_COOKIE, new_session_id, max_age=60 * 60 * 24 * 365, httponly=True)
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
