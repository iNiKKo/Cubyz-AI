"""
Standalone Cubyz RAG test harness -- bypasses Open WebUI entirely.

Why this exists: Open WebUI's agentic "Knowledge Base" tool leaves it up to the model's own
discretion whether to search at all, which we've seen fail unpredictably (skipped searches,
fabricated tool call traces, silently-broken collection scoping). This script does retrieval
as plain deterministic Python instead -- it always runs, the model never gets a choice -- talking
directly to Ollama for both embeddings and generation. Fully transparent and fast to iterate on.

Usage:
    python3 local_rag_chat.py "Who made Cubyz?"
    python3 local_rag_chat.py --batch      # runs the standard test questions
    python3 local_rag_chat.py --rebuild "some question"   # force-rebuild the embedding cache first
"""
import os
import re
import sys
import json
import math
import urllib.request

# Anchored to the repo root (one level up from webapp/) rather than the process's cwd -- this
# script gets run from both the repo root and from inside webapp/ depending on habit, and a bare
# relative path silently resolves differently (and wrongly) depending on which. Same pattern
# already used throughout finetune/*.py.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "qwen3-embedding:4b"
# Switched from the generic devstral:24b to the QLoRA fine-tuned + merged Cubyz model (see
# finetune/README.md) once its own fact recall proved insufficient on its own (96-question test:
# 27% correct, 66% wrong, some regressions round over round) to serve standalone -- it's kept
# here specifically for the voice/judgment it DID learn reliably (review reasoning, debugging
# hypotheses, general capability), with this script's deterministic retrieval as the actual
# factual backstop. Run merge_adapter.py + convert to GGUF + `ollama create` before pointing this
# at a new name.
#
# Naming convention 2026-07-20 through Prototype 7: SNALE-AI-<prototype>-<params>, e.g.
# SNALE-AI-P6-0.6B -- P1/P5/P6 keep that prefix as an accurate historical record (see README.md's
# prototype history) and are not being renamed retroactively. 2026-07-21 onward: ASH-<prototype>
# -<params> -- "Snale" (also a real in-game Cubyz creature) drew negative feedback as the public
# assistant name, so the brand became "Ash" and new models follow suit. Every future trained
# model should follow this pattern -- update this constant (and `ollama create`/`ollama cp` the
# model under the matching name, and the Hugging Face repo) each time the active model changes,
# rather than reusing a generic name that hides which prototype/size actually produced an answer.
ANSWER_MODEL = "ASH-P7-4B"
KNOWLEDGE_DIR = os.path.join(REPO_ROOT, "knowledge_base")
CACHE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rag_index_cache.json")
GLOBAL_TOP_K = 8      # best chunks overall, regardless of collection
MIN_PER_COLLECTION = 2  # floor to guarantee small collections (docs, addon) get a fair look
# Below this cosine similarity, a chunk is empirically noise, not signal -- measured directly
# against this index: genuinely off-topic queries ("Hello!", "How are you?") top out around
# 0.30-0.35 with no real winner (a long flat tail, nothing actually relevant exists), while every
# real Cubyz question's best-matching chunk scored 0.50+, often 0.65+. Set well below that real
# floor for margin. Only gates the MIN_PER_COLLECTION top-up below, not the global top-K -- that
# selection is unchanged, since it's the exact mechanism this project's 99%-accuracy benchmark
# runs validated; only the "force-include a collection's chunk regardless of relevance" behavior
# needed fixing, not core retrieval.
MIN_SIMILARITY_FOR_TOPUP = 0.40
EMBED_BATCH_SIZE = 20
# Shared context-window size for both the answer call and the compaction/summarize call below --
# system prompt + RAG chunks + conversation history + this question + the response all have to
# fit in this. chat_server.py compares this against Ollama's own reported prompt_tokens to warn
# if a real request ever gets close to it, since the HISTORY_CHAR_BUDGET char-count budget there
# is a rough proxy, not an exact token count.
NUM_CTX = 16384

SYSTEM_PROMPT = """You are the Cubyz Assistant, a technical expert on Cubyz, an open-source voxel sandbox game written in Zig. Answer directly and precisely, in the voice of a developer who already knows this codebase.

## Grounding rules
- Answer using the "Retrieved context" section below. Treat it as the authoritative, current source of fact -- if it conflicts with anything you'd otherwise say, the retrieved context wins, since it's pulled fresh from the real docs/codebase and your own training can be wrong on narrow specifics.
- Never invent function names, file paths, mechanics, dates, or names that aren't in the retrieved context.
- If the retrieved context doesn't answer the question, say so plainly instead of guessing -- do not fall back on general knowledge about other games, companies, or software just because a word (e.g. "addon", "history") sounds generic. This applies even when the retrieved context contains a chunk that is merely topic-adjacent (mentions a similar item, a different platform, a different method with a similar name) -- retrieving something related is not the same as retrieving the answer, and answering from the nearest-sounding chunk anyway is a worse failure than admitting you don't know. If the question names a specific item/feature/person and no retrieved chunk names that exact thing, say plainly that Cubyz doesn't document it -- do not describe a different item/feature/person instead just because it's nearby in the same context.
- When you don't know something, say it the way a developer who genuinely doesn't know would: "Cubyz doesn't document that" or "I don't have information on X." Never describe your own retrieval process to get there -- phrases like "the provided text doesn't specify," "the retrieved context states," or "the instructions say" are never acceptable in an answer, whether you know the fact or not. The user never sees your context window and shouldn't be told about it.
- For a question with one exact right answer (a specific key, number, tool name, command, or setting): scan the retrieved context for the sentence that explicitly states that value for the specific thing being asked about, and answer with exactly that value. Do not substitute a value you already associate with the general topic (e.g. a different tool, key, or number from elsewhere in the same chunk) just because it feels familiar -- that substitution is the exact failure mode these grounding rules exist to prevent. If a question asks about one specific item among several similar ones covered in the same chunk (e.g. one tool among several, one key among several), double-check you're reading the line for that specific item, not a neighboring one.
- Hypothetical illustration of this exact failure mode (this example is NOT a real Cubyz fact, it never appears in retrieved context, and must never be used as an answer to any real question -- it exists only to show you the pattern to avoid): imagine a chunk states "widgets sharpen metal tools, gadgets sharpen wood tools." Asked "what sharpens wood tools," the wrong answer is "widget" (a different item from the same sentence, chosen by pattern-matching "something in this chunk sharpens tools" instead of reading which clause matches "wood"); the right answer is "gadget," because that's the clause that actually names "wood." The general lesson: before finalizing an answer, re-read the specific clause of the ACTUAL retrieved text below that names the exact item/field THIS question asks about, and quote its value -- don't answer from a general impression of the chunk's topic, and don't reuse wording from this instruction block itself as if it were retrieved content.
- When you state a fact, mention which source file it came from -- this is normal and expected here, not a hedge, so the user can verify or read further.
- Prefer being concise and direct for factual questions; expand only when the question calls for explanation or code.

## How to handle different question types
- Factual / history / "who made X" questions: answer straight, in 1-3 sentences, no padding. "Who made X" wants the creator(s) + current maintainer only; "history of X" wants the fuller narrative (renames, rewrite attempts, releases). Don't collapse both into the same answer.
- "How does X work" / mechanics / addon questions: explain the mechanism first, then give a concrete example (code or config) if the retrieved context includes one.
- Debugging help (user pastes code or an error): read it carefully, identify the specific Cubyz symbols/APIs involved, cross-reference the codebase/review context provided. State your best hypothesis and why, and a concrete next step. If unsure, say what additional info would help narrow it down.

## Project norm you must respect
Cubyz's own CONTRIBUTING.md asks contributors not to submit AI-generated pull requests, because the maintainer wants contributors to actually understand the code they submit. Your job is to explain, teach, and help debug -- not hand someone a finished feature to paste directly into a PR. Small illustrative snippets are fine; full unexplained patches are not.

## Style
Be technically precise, use correct Zig/Cubyz terminology exactly as it appears in the source, no filler, no disclaimers.
"""

BATCH_QUESTIONS = [
    "Who made Cubyz?",
    "What's the history of Cubyz?",
    "How do Addons work?",
]


def http_post_json(path, payload, timeout=180):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{OLLAMA_URL}{path}", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def embed_batch(texts):
    # Explicit, generous timeout -- http_post_json's 180s default is sized for a normal
    # GPU-backed embedding call, not a CPU-only, memory-bandwidth-bound one. Confirmed live: a
    # single batch of 20 embeddings legitimately took longer than 180s on a CPU-only deployment
    # (Threadripper, no usable GPU) and crashed the whole server's startup with a timeout, even
    # though Ollama itself was actively working the whole time (docker stats/logs showed
    # continuous real progress, not a hang). 20 minutes gives real headroom for slow hardware
    # without masking an actual hang forever.
    result = http_post_json("/api/embed", {"model": EMBED_MODEL, "input": texts}, timeout=1200)
    return result["embeddings"]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def scan_files():
    entries = []
    for collection in sorted(os.listdir(KNOWLEDGE_DIR)):
        coll_dir = os.path.join(KNOWLEDGE_DIR, collection)
        if not os.path.isdir(coll_dir):
            continue
        for fname in sorted(f for f in os.listdir(coll_dir) if f.endswith(".md")):
            with open(os.path.join(coll_dir, fname), encoding="utf-8") as f:
                entries.append({"collection": collection, "filename": fname, "text": f.read()})
    return entries


def build_index(existing_entries=None):
    # Incremental by default: a single chunk edit used to force a full re-embed of the entire
    # knowledge base (3000+ chunks, ~15-20 minutes) -- painfully slow for the actual common case of
    # fixing one or two chunks at a time. Reuse any cached embedding whose (collection, filename,
    # text) triple is unchanged; only call the embedding model for chunks that are genuinely new or
    # edited. Pass existing_entries=None (or use --rebuild) to force embedding everything from
    # scratch, e.g. if the embedding model itself changed or the cache is suspected corrupt.
    scanned = scan_files()
    cached_by_key = {}
    if existing_entries:
        cached_by_key = {(e["collection"], e["filename"]): e for e in existing_entries}

    final_entries = []
    to_embed = []
    for e in scanned:
        cached = cached_by_key.get((e["collection"], e["filename"]))
        if cached and cached["text"] == e["text"] and "embedding" in cached:
            e["embedding"] = cached["embedding"]
            final_entries.append(e)
        else:
            to_embed.append(e)

    reused = len(final_entries)
    if reused:
        print(f"[~] Reusing {reused} unchanged cached embeddings; embedding {len(to_embed)} new/changed chunks...")
    else:
        print(f"[~] Building embedding index from scratch: {len(to_embed)} chunks...")

    total_batches = -(-len(to_embed) // EMBED_BATCH_SIZE)  # ceil division
    # Aims for ~10-20 progress lines regardless of run size, instead of a fixed "every 10th
    # batch" -- that fixed interval was sized for a full from-scratch rebuild (150+ batches) and
    # went completely silent for a small incremental catch-up. Confirmed live: a 77-chunk/4-batch
    # run printed once after the first batch, then nothing until the very last one, looking
    # exactly like a hang for however long those middle batches actually took (each one is real,
    # possibly slow-on-CPU work -- see BENCHMARK_TIMEOUT_CPU's reasoning elsewhere in this
    # project -- just never reported).
    print_every = max(1, total_batches // 15)
    for i in range(0, len(to_embed), EMBED_BATCH_SIZE):
        batch = to_embed[i:i + EMBED_BATCH_SIZE]
        embeddings = embed_batch([e["text"] for e in batch])
        for e, emb in zip(batch, embeddings):
            e["embedding"] = emb
        done = min(i + EMBED_BATCH_SIZE, len(to_embed))
        if (i // EMBED_BATCH_SIZE) % print_every == 0 or done == len(to_embed):
            print(f"    ... {done}/{len(to_embed)}")
    final_entries.extend(to_embed)

    with open(CACHE_FILE, "w") as f:
        json.dump(final_entries, f)
    print(f"[OK] Index cached to {CACHE_FILE} ({len(final_entries)} total chunks)")
    return final_entries


def load_index(rebuild=False):
    existing = None
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            existing = json.load(f)
        if not rebuild:
            # Compares (collection, filename, text) identity, not just a count -- swapping N files
            # for a different N files (e.g. replacing a stale chunk with a corrected one under a
            # new filename) leaves the count unchanged, so a count-only check would silently keep
            # serving embeddings for deleted files while never picking up the new ones.
            cached = {(e["collection"], e["filename"]): e["text"] for e in existing}
            current = {(e["collection"], e["filename"]): e["text"] for e in scan_files()}
            if cached == current:
                return existing
            print("[~] Cache stale (files changed) -- incrementally re-embedding only what changed...")
    return build_index(existing_entries=None if rebuild else existing)


def retrieve(query, index, global_top_k=GLOBAL_TOP_K, min_per_collection=MIN_PER_COLLECTION,
             min_similarity_for_topup=MIN_SIMILARITY_FOR_TOPUP):
    q_emb = embed_batch([query])[0]
    for e in index:
        e["_score"] = cosine(q_emb, e["embedding"])
    scored = sorted(index, key=lambda e: -e["_score"])

    # Best chunks overall first -- this is what actually matters for relevance.
    hits = scored[:global_top_k]
    seen = {id(e) for e in hits}

    # Then top up any collection with zero/thin representation, so a small collection
    # (docs, addon) with a genuinely relevant chunk that just missed the global cut still
    # gets a look -- but only if that chunk actually clears min_similarity_for_topup. Without
    # this gate, a collection with nothing relevant to the query still got force-fed
    # min_per_collection chunks unconditionally (e.g. a plain "Hello!" pulling in 13-14 sources
    # total instead of 8), wasting context/generation time on noise the model then has to
    # correctly ignore.
    by_collection = {}
    for e in scored:
        by_collection.setdefault(e["collection"], []).append(e)

    for entries in by_collection.values():
        have = sum(1 for e in entries if id(e) in seen)
        if have < min_per_collection:
            for e in entries:
                if id(e) not in seen and e["_score"] >= min_similarity_for_topup:
                    hits.append(e)
                    seen.add(id(e))
                    have += 1
                    if have >= min_per_collection:
                        break
    return hits


def ask(question, index, verbose=True, return_meta=False, conversation_history=None):
    # Retrieval only ever sees `question` itself -- conversation_history is used below for
    # generation, but was never part of the embedding query, so a context-dependent follow-up
    # ("how is it different from one-hit modifier") could embed and search with none of the
    # actual subject ("single-use") anywhere in the query text. Confirmed live: that vague
    # follow-up got a wrong/hedgy answer; asking the equivalent standalone question ("difference
    # between single-use and one-hit modifiers") retrieved correctly. Folding the single
    # immediately-prior user turn into the retrieval query (not the full history -- that would
    # dilute the embedding with old, now-irrelevant subject matter) fixes exactly that gap without
    # changing retrieve()'s own logic or touching what the model is actually shown.
    retrieval_query = question
    if conversation_history:
        prior_questions = [m["content"] for m in conversation_history if m.get("role") == "user"]
        if prior_questions:
            retrieval_query = f"{prior_questions[-1]} {question}"
    hits = retrieve(retrieval_query, index)

    # Present the single best-matching chunk LAST, right next to the user's question, not first.
    # LLMs attend more reliably to the start and end of a long context than the middle ("lost in
    # the middle" -- Liu et al. 2023); with 10-14 chunks in context, burying the exact answer at
    # position 1 of 14 instead of the end measurably hurt single-fact lookups in manual testing
    # (e.g. flipping "left mouse button" -> "right mouse button" run to run with the correct chunk
    # present the whole time). Retrieval/ranking logic above is unchanged -- only presentation order.
    ordered = sorted(hits, key=lambda h: h["_score"])
    # Every chunk ends with its own "*Source: unknown | chunk_id: ...*" footer -- always literally
    # "unknown" since that field was never actually populated during crunching. It's meaningless to
    # the model but looks like real citation text, so it sometimes gets echoed back verbatim in an
    # answer (seen live: "what is Ashframe" was otherwise a correct answer, but ended with the raw
    # "*Source: unknown | chunk_id: docs_ashframe_overview.md_chunk_0*" line pasted in). Stripped
    # here rather than relied on via prompt instruction -- the bracketed [collection/filename]
    # header below already gives the model everything it needs for an accurate citation.
    strip_footer = re.compile(r"\n*\*Source:.*?\*\s*$")
    context = "\n\n---\n\n".join(f"[{h['collection']}/{h['filename']}]\n{strip_footer.sub('', h['text'])}" for h in ordered)
    system = SYSTEM_PROMPT + f"\n\n## Retrieved context\n{context}"

    if verbose:
        print(f"[Retrieved {len(hits)} chunks: {', '.join(h['filename'] for h in hits)}]\n")

    # conversation_history is the same-chat context chat_server.py builds up: prior user/assistant
    # turns (and a compaction summary standing in for older ones -- see summarize_conversation
    # below), inserted between the system prompt and this question so multi-turn references
    # ("what about that one?") resolve. Each retrieval call above is still independent of it --
    # RAG grounding runs fresh on `question` alone -- this only changes what the model sees, not
    # what gets retrieved.
    messages = [{"role": "system", "content": system}]
    if conversation_history:
        messages.extend(conversation_history)
    messages.append({"role": "user", "content": question})

    result = http_post_json("/api/chat", {
        "model": ANSWER_MODEL,
        "messages": messages,
        "stream": False,
        # Ollama defaults num_ctx far too low (often 2048-4096) for a system prompt plus ~14
        # retrieved chunks -- silent truncation there would drop exactly the grounding context
        # this whole script exists to guarantee gets to the model.
        #
        # temperature=0 (fully greedy) rather than 0.1 -- testing showed real run-to-run answer
        # flipping (correct <-> wrong) on identical retrieved context between otherwise-identical
        # runs of the 96-question batch test, which made it impossible to tell a real fix from
        # noise. Greedy decoding trades a little phrasing variety for reproducibility, which
        # matters more here since this is a fact-lookup assistant, not creative writing.
        "options": {"temperature": 0.0, "num_ctx": NUM_CTX, "seed": 42},
    })
    # .strip() -- Ollama chat responses often carry a leading/trailing newline from the model's
    # chat template. Harmless when rendered with normal white-space collapsing, but the frontend
    # uses white-space:pre-wrap (to keep code-block formatting intact), which renders that stray
    # newline as a literal blank line above the answer.
    answer = result["message"]["content"].strip()
    if not return_meta:
        return answer

    # Opt-in richer return for callers that want to show their work (chat_server.py's UI) --
    # default stays a bare string so the CLI/batch-test callers above are untouched. Sources use
    # the same `ordered` list already built for the prompt, not a fresh computation.
    return {
        "answer": answer,
        "model": ANSWER_MODEL,
        "embed_model": EMBED_MODEL,
        "sources": [
            {"collection": h["collection"], "filename": h["filename"], "score": round(h["_score"], 4)}
            for h in reversed(ordered)  # best match first for display, opposite of the prompt order
        ],
        # Ollama's own token counts, not a local re-tokenization -- present whenever the running
        # Ollama version reports them, None otherwise (older versions may omit these fields).
        "prompt_tokens": result.get("prompt_eval_count"),
        "response_tokens": result.get("eval_count"),
    }


SUMMARIZE_PROMPT = """You are compacting an ongoing chat conversation so it can keep going without re-sending every prior message. Write a compact recap of the conversation below.

Rules:
- Third person, past tense, plain prose -- not a transcript.
- Keep every specific fact, name, number, or file/setting the user gave or asked about.
- If the user corrected the assistant on something (told it a previous answer was wrong, or gave the right value after a wrong one), keep that correction explicitly and clearly -- it matters more than anything else here, since the point of this recap is that the assistant doesn't repeat the same mistake later in this chat.
- Drop pleasantries and anything not useful for understanding what's already been discussed.
- A few sentences is enough unless the conversation genuinely covered a lot of distinct ground.
"""


def summarize_conversation(prior_summary, messages):
    """Folds `messages` (a list of {"role","content"} dicts, oldest first) into a compact recap,
    carried forward alongside `prior_summary` (the recap of everything already compacted before
    this batch, or None on a chat's first compaction). One extra Ollama call, only made when
    chat_server.py decides the verbatim history has grown past its budget -- not on every turn."""
    transcript = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    user_content = transcript if not prior_summary else f"Existing recap so far:\n{prior_summary}\n\nNew messages to fold in:\n{transcript}"
    result = http_post_json("/api/chat", {
        "model": ANSWER_MODEL,
        "messages": [
            {"role": "system", "content": SUMMARIZE_PROMPT},
            {"role": "user", "content": user_content},
        ],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": NUM_CTX, "seed": 42},
    })
    return result["message"]["content"].strip()


def main():
    rebuild = "--rebuild" in sys.argv
    index = load_index(rebuild=rebuild)

    if "--batch" in sys.argv:
        for q in BATCH_QUESTIONS:
            print(f"\n{'=' * 70}\nQ: {q}\n{'=' * 70}")
            print(ask(q, index))
    else:
        args = [a for a in sys.argv[1:] if not a.startswith("--")]
        question = " ".join(args) if args else BATCH_QUESTIONS[0]
        print(f"Q: {question}\n")
        print(ask(question, index))


if __name__ == "__main__":
    main()
