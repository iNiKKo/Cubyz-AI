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
import sqlite3
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
    return resp


@app.get("/api/history")
async def history(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        return JSONResponse([])
    conn = db()
    rows = conn.execute(
        "SELECT id, role, content, feedback, feedback_note FROM messages WHERE session_id = ? ORDER BY id ASC",
        (session_id,),
    ).fetchall()
    conn.close()
    return JSONResponse([
        {"id": i, "role": r, "content": c, "feedback": f, "feedback_note": n}
        for i, r, c, f, n in rows
    ])


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
    conn.execute(
        "INSERT INTO messages (session_id, role, content) VALUES (?, 'user', ?)",
        (session_id, question),
    )
    conn.commit()
    conn.close()

    # Run in a thread so a slow retrieval+generation call doesn't block the event loop --
    # other requests (history, new_chat, someone else's /api/chat) stay responsive meanwhile.
    answer = await run_in_threadpool(local_rag_chat.ask, question, _index, False)

    conn = db()
    cursor = conn.execute(
        "INSERT INTO messages (session_id, role, content) VALUES (?, 'assistant', ?)",
        (session_id, answer),
    )
    message_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return JSONResponse({"answer": answer, "message_id": message_id})


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
