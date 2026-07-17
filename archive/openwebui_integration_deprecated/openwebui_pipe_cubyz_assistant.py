"""
title: Cubyz Assistant (Deterministic RAG)
id: cubyz_assistant_deterministic_rag
description: Cubyz assistant that ALWAYS retrieves from the 4 Cubyz knowledge collections before
    answering, instead of relying on Open WebUI's native agentic tool-calling search (which
    testing on this project found unreliable -- skipped searches, fabricated tool call traces,
    broken collection scoping). This Pipe reimplements the exact retrieval + prompting logic
    from local_rag_chat.py (validated at 89% on a 96-question grounded test), so using this
    model in the normal Open WebUI chat UI gets the same tested behavior instead of a different,
    unvalidated code path.
author: cubyz-project
version: 1.0.0

Install: Admin Panel -> Functions -> + -> paste this file's contents -> Save.
Then open its Valves (gear icon on the function) and set OPEN_WEBUI_API_KEY to a fresh API key
(Settings -> Account -> API Keys -> Create). Everything else has a working default.

If retrieval or generation calls fail with a connection error, it's almost certainly because
OLLAMA_URL/OPEN_WEBUI_URL's default of localhost doesn't resolve to the right host from wherever
Open WebUI's own server process actually runs (e.g. a separate Docker container reaches Ollama at
"http://ollama:11434", not "http://localhost:11434") -- adjust those two Valves to match your
actual network setup.
"""
import json

import requests
from pydantic import BaseModel, Field


class Pipe:
    class Valves(BaseModel):
        OPEN_WEBUI_URL: str = Field(
            default="http://localhost:3000",
            description="Base URL this Open WebUI instance is reachable at from its own server process.",
        )
        OPEN_WEBUI_API_KEY: str = Field(
            default="",
            description="Required. Settings -> Account -> API Keys -> Create. Used to call this "
                        "instance's own retrieval API for the 4 Cubyz knowledge collections.",
        )
        OLLAMA_URL: str = Field(
            default="http://localhost:11434",
            description="Base URL for Ollama, reachable from Open WebUI's own server process.",
        )
        ANSWER_MODEL: str = Field(default="cubyz-assistant", description="Ollama model to generate with.")
        NUM_CTX: int = Field(default=16384, description="Context window -- must fit system prompt + retrieved chunks.")
        GLOBAL_TOP_K: int = Field(default=8, description="Best chunks overall, regardless of collection.")
        MIN_PER_COLLECTION: int = Field(default=2, description="Floor per collection so small ones aren't crowded out.")
        PER_COLLECTION_QUERY_K: int = Field(default=10, description="How many hits to fetch per collection before merging.")

        # Fixed at the values confirmed live in this Open WebUI instance during setup -- update
        # here if a collection is ever recreated (its id changes) or renamed.
        COLLECTION_IDS: dict = Field(default={
            "codebase": "191be434-afcc-4ee3-8536-6e3ee8c9b6fc",
            "docs": "bcad54ff-0bd5-4480-a95c-422f2218b75f",
            "addon_creator": "57c9ccf7-302c-48d4-a1d7-6876c9537fac",
            "reviews": "60ed51dd-fdeb-4377-a68f-b19f538c23ed",
        })

    def __init__(self):
        self.valves = self.Valves()

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

    def _query_collection(self, collection_id: str, collection_name: str, query: str) -> list:
        try:
            r = requests.post(
                f"{self.valves.OPEN_WEBUI_URL}/api/v1/retrieval/query/collection",
                headers={
                    "Authorization": f"Bearer {self.valves.OPEN_WEBUI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={"collection_names": [collection_id], "query": query, "k": self.valves.PER_COLLECTION_QUERY_K},
                # (connect, read) -- short connect timeout to fail fast on a wrong/blocked host,
                # but a generous read timeout: querying the larger collections (codebase has 1,477
                # embedded chunks) genuinely takes real time, confirmed via direct socket testing
                # that ruled out a networking hang -- this is legitimate compute time, not a stall.
                timeout=(3, 90),
            )
            r.raise_for_status()
            body = r.json()
        except Exception as e:
            return [{"collection": collection_name, "filename": f"[ERROR querying {collection_name}: {e}]", "text": "", "score": -1}]

        docs = (body.get("documents") or [[]])[0]
        metas = (body.get("metadatas") or [[]])[0]
        dists = (body.get("distances") or [[]])[0]
        hits = []
        for doc, meta, dist in zip(docs, metas, dists):
            hits.append({
                "collection": collection_name,
                "filename": meta.get("name") or meta.get("source") or "unknown",
                "text": doc,
                "score": dist,
            })
        return hits

    def _retrieve(self, query: str) -> list:
        # Mirrors local_rag_chat.py's retrieve(): best chunks overall by score first, then top up
        # any collection with thin representation so small collections (docs, addon_creator)
        # still get a fair look even if a big collection (codebase, reviews) dominates raw scores.
        all_hits = []
        for name, cid in self.valves.COLLECTION_IDS.items():
            all_hits.extend(self._query_collection(cid, name, query))

        scored = sorted(all_hits, key=lambda h: -h["score"])
        hits = scored[: self.valves.GLOBAL_TOP_K]
        seen = {id(h) for h in hits}

        by_collection = {}
        for h in scored:
            by_collection.setdefault(h["collection"], []).append(h)

        for entries in by_collection.values():
            have = sum(1 for h in entries if id(h) in seen)
            if have < self.valves.MIN_PER_COLLECTION:
                for h in entries:
                    if id(h) not in seen:
                        hits.append(h)
                        seen.add(id(h))
                        have += 1
                        if have >= self.valves.MIN_PER_COLLECTION:
                            break
        return hits

    def pipe(self, body: dict) -> str:
        if not self.valves.OPEN_WEBUI_API_KEY:
            return ("[X] This Pipe needs an Open WebUI API key. Open this function's Valves "
                    "(gear icon) and set OPEN_WEBUI_API_KEY -- generate one at "
                    "Settings -> Account -> API Keys -> Create.")

        messages = body.get("messages", [])
        user_messages = [m for m in messages if m.get("role") == "user"]
        if not user_messages:
            return "[X] No user message found."
        question = user_messages[-1]["content"]

        hits = self._retrieve(question)
        context = "\n\n---\n\n".join(f"[{h['collection']}/{h['filename']}]\n{h['text']}" for h in hits)
        system = self.SYSTEM_PROMPT + f"\n\n## Retrieved context\n{context}"

        try:
            r = requests.post(
                f"{self.valves.OLLAMA_URL}/api/chat",
                json={
                    "model": self.valves.ANSWER_MODEL,
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": question},
                    ],
                    "stream": False,
                    "options": {"temperature": 0.0, "num_ctx": self.valves.NUM_CTX},
                },
                timeout=180,
            )
            r.raise_for_status()
            answer = r.json()["message"]["content"]
        except Exception as e:
            return (f"[X] Ollama call failed: {e}\n\nIf this is a connection error, "
                    f"OLLAMA_URL ({self.valves.OLLAMA_URL}) probably doesn't resolve to Ollama "
                    f"from Open WebUI's own server process -- adjust that Valve to the correct "
                    f"host (e.g. a docker-compose service name like http://ollama:11434).")

        sources = ", ".join(sorted({h["filename"] for h in hits}))
        return f"{answer}\n\n---\n*Retrieved {len(hits)} chunks: {sources}*"
