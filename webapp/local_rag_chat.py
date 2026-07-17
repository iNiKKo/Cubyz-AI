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
# factual backstop. Run merge_adapter.py + convert to GGUF + `ollama create cubyz-assistant`
# before pointing this at the new name (see finetune/README.md "Current state").
ANSWER_MODEL = "cubyz-assistant"
KNOWLEDGE_DIR = os.path.join(REPO_ROOT, "knowledge_base")
CACHE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rag_index_cache.json")
GLOBAL_TOP_K = 8      # best chunks overall, regardless of collection
MIN_PER_COLLECTION = 2  # floor to guarantee small collections (docs, addon) get a fair look
EMBED_BATCH_SIZE = 20

SYSTEM_PROMPT = """You are the Cubyz Assistant, a technical expert on Cubyz, an open-source voxel sandbox game written in Zig. Answer directly and precisely, in the voice of a developer who already knows this codebase.

## Grounding rules
- Answer using the "Retrieved context" section below. Treat it as the authoritative, current source of fact -- if it conflicts with anything you'd otherwise say, the retrieved context wins, since it's pulled fresh from the real docs/codebase and your own training can be wrong on narrow specifics.
- Never invent function names, file paths, mechanics, dates, or names that aren't in the retrieved context.
- If the retrieved context doesn't answer the question, say so plainly instead of guessing -- do not fall back on general knowledge about other games, companies, or software just because a word (e.g. "addon", "history") sounds generic.
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
    result = http_post_json("/api/embed", {"model": EMBED_MODEL, "input": texts})
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


def build_index():
    print("[~] Building embedding index (one-time, cached to disk)...")
    entries = scan_files()
    print(f"[~] Embedding {len(entries)} chunks in batches of {EMBED_BATCH_SIZE}...")
    for i in range(0, len(entries), EMBED_BATCH_SIZE):
        batch = entries[i:i + EMBED_BATCH_SIZE]
        embeddings = embed_batch([e["text"] for e in batch])
        for e, emb in zip(batch, embeddings):
            e["embedding"] = emb
        done = min(i + EMBED_BATCH_SIZE, len(entries))
        if (i // EMBED_BATCH_SIZE) % 10 == 0 or done == len(entries):
            print(f"    ... {done}/{len(entries)}")

    with open(CACHE_FILE, "w") as f:
        json.dump(entries, f)
    print(f"[OK] Index cached to {CACHE_FILE}")
    return entries


def load_index(rebuild=False):
    if not rebuild and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            entries = json.load(f)
        if len(entries) == len(scan_files()):
            return entries
        print("[~] Cache stale (file count changed), rebuilding...")
    return build_index()


def retrieve(query, index, global_top_k=GLOBAL_TOP_K, min_per_collection=MIN_PER_COLLECTION):
    q_emb = embed_batch([query])[0]
    scored = sorted(index, key=lambda e: -cosine(q_emb, e["embedding"]))

    # Best chunks overall first -- this is what actually matters for relevance.
    hits = scored[:global_top_k]
    seen = {id(e) for e in hits}

    # Then top up any collection with zero/thin representation, so a small collection
    # (docs, addon) with a genuinely relevant chunk that just missed the global cut still
    # gets a look, without forcing in irrelevant filler from every collection unconditionally.
    by_collection = {}
    for e in scored:
        by_collection.setdefault(e["collection"], []).append(e)

    for entries in by_collection.values():
        have = sum(1 for e in entries if id(e) in seen)
        if have < min_per_collection:
            for e in entries:
                if id(e) not in seen:
                    hits.append(e)
                    seen.add(id(e))
                    have += 1
                    if have >= min_per_collection:
                        break
    return hits


def ask(question, index, verbose=True):
    hits = retrieve(question, index)
    context = "\n\n---\n\n".join(f"[{h['collection']}/{h['filename']}]\n{h['text']}" for h in hits)
    system = SYSTEM_PROMPT + f"\n\n## Retrieved context\n{context}"

    if verbose:
        print(f"[Retrieved {len(hits)} chunks: {', '.join(h['filename'] for h in hits)}]\n")

    result = http_post_json("/api/chat", {
        "model": ANSWER_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": question},
        ],
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
        "options": {"temperature": 0.0, "num_ctx": 16384},
    })
    return result["message"]["content"]


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
