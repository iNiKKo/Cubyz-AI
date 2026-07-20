# Cubyz AI

A local AI assistant that knows the [Cubyz](https://github.com/PixelGuys/Cubyz) codebase and
community — engine internals, keybindings, addon-creator tooling, PR review history — without
losing general competence. A deterministic RAG retrieval layer + a QLoRA fine-tune, both fed by a
distributed, volunteer-powered crunching pipeline.

---

## What's in this repo

### Client — `CUBYZ_FOLDING.py`

![Client screenshot placeholder](docs/images/client.png)
<!-- TODO: replace with a real screenshot -->

Run this to donate spare compute to whichever campaign is active.

- Connects to the server, receives assigned work, crunches it with local Ollama, submits results
- Auto-detects hardware (GPU/CPU model, VRAM/RAM) and picks a model that fits
- Runs multiple lanes at once when hardware allows (GPU + CPU, or several parallel workers)
- Auto-updates to the latest version
- Sends offline status on safe exit, instead of leaving a stale connection for the server to time out

### Server — `pipeline_crunching/server_textual.py`

![Server screenshot placeholder](docs/images/server.png)
<!-- TODO: replace with a real screenshot -->

The coordinator.

- Scans source material, chunks it, hands out work to connected clients
- Switches between RAG / Finetune / Audit campaigns live, no restart needed
- Interactive console for monitoring connections and controlling the active campaign
- Tracks per-volunteer stats and leaderboard

---

## Current stage

- **RAG:** complete (3,247/3,247 chunks). Knowledge base is live on the webapp.
- **Fine-tune:** complete (2,193/2,193 chunks). A new adapter is trained but **not yet
  re-benchmarked**.
- **Audit:** complete (3,247/3,247), re-runs automatically as chunks change. Run
  `python3 pipeline_crunching/analyze_audit.py` anytime for a live breakdown of what's failing and
  why.
- **Infra:** one client (`CUBYZ_FOLDING.py`), one server (`server_textual.py`). Old/duplicate
  versions archived, not deleted.

**Open items:** benchmark the new adapter; decide on `/disconnect`'s missing auth (known, not
fixed).

---

## History

Collapsed by default. Preserved because each dead end is why the current system works the way it
does — raw code for everything upstream lives in `archive/`.

<details>
<summary><strong>Prototype 1 — Fine-Tuning Only</strong> (unusable, shelved)</summary>

Direct LoRA fine-tune on the Cubyz codebase (`Qwen2.5-Coder-3B-Instruct`, bf16, no quantization),
no RAG, no general-data mixing.

**Result:** catastrophic forgetting. The model could talk about Cubyz but lost general
competence — reasoning, unrelated code, plain conversation all degraded. 100% domain-flavored
training data with nothing to counterbalance it.

**Lesson:** narrow full fine-tuning without general-data mixing forgets. Need adapter-only
training and/or real general instruction data in the mix.

Shelved. `archive/prototype_1_finetune_only/`.

</details>

<details>
<summary><strong>Prototype 2 — Early RAG</strong> (validated the approach)</summary>

Retrieval instead of retraining — a Chroma vector DB over one merged knowledge file, served via
`rag_server.py`. Zero forgetting risk since model weights are untouched.

**What worked:** clean factual lookups (creator, Discord, project history).

**What didn't:** code examples came back wrong — one undifferentiated markdown blob wasn't
fine-grained enough for retrieval to find the exact right passage.

**Lesson:** RAG quality is bottlenecked by chunk granularity and source coverage, not just having
a vector DB.

`archive/prototype_2_early_rag/`, `archive/prototype_2_review_extraction/`.

</details>

<details>
<summary><strong>Prototype 3 — Crunch-Party (Distributed Crunching)</strong> (bigger KB, introduced a bug found later)</summary>

Infrastructure to scale Prototype 2's knowledge base: a coordinator handed out source chunks
(wiki, codebase, addon-creator docs, PR reviews) to volunteers running a client, each processed
through a local LLM.

**What worked:** completed 1,134/1,134 chunks — a real, community-built knowledge base replacing
the single-file blob.

**What went wrong:** the crunching prompt let the model summarize *that* a topic was covered
without stating the actual value (e.g. "discusses the server port" without writing the port
number). Several facts were lost this way — not caught until Prototype 4's accuracy testing.

**Lesson:** fixed at the source in the crunching prompt (now requires verbatim fact preservation).

</details>

<details>
<summary><strong>Prototype 4 — Hybrid: Fine-Tune + RAG</strong> (89% on a 96-question benchmark)</summary>

Fine-tuning for voice/judgment, RAG for hard facts — combining what 1 and 2 each got right.
QLoRA on `Qwen2.5-Coder-7B-Instruct`, deterministic retrieval at temperature 0, Cubyz data mixed
with general instruction data (`OpenHermes-2.5`).

| Round | Approach | Score |
|---|---|---|
| 1 | Fine-tune alone | ~20-24% |
| 2 | Fine-tune alone, more data/epochs | ~27% |
| 3 | Fine-tune + RAG (first pass) | 58% |
| 4 (final) | + root-caused fixes | **89%** |

General capability held up fully every round — no forgetting. But fine-tuning alone couldn't hold
narrow facts, and more data/epochs bought only +3 points. Switching to hybrid retrieval jumped
27%→58% in one pass; every remaining wrong answer then traced back to one of three causes (docs
never chunked into the KB, the Prototype 3 fact-loss bug, a reproducible model bias on one
question cluster) and got fixed at the source.

**Lesson:** fine-tuning and RAG fail differently — fine-tuning forgets/hallucinates narrow facts,
RAG is only as good as its source coverage. Combining them and fixing root causes (not patching
outputs) closed almost the entire gap.

Served via a purpose-built webapp (`webapp/chat_server.py`) after Open WebUI's own retrieval
proved inconsistent and its frontend gave up on slow responses.

</details>

<details>
<summary><strong>Prototype 5 — Consolidation, Regression Hunt & TUI Migration</strong> (95.8% on an expanded 144-question benchmark)</summary>

Infrastructure cleanup, then re-verifying (and pushing past) Prototype 4's 89%.

**Infra:** three per-OS client scripts and two servers merged into one client
(`CUBYZ_FOLDING.py`) and one server, with live campaign-mode switching. Added a version gate,
auto-update, dual GPU+CPU lanes, parallel workers, real hardware detection (no fabricated
fallback numbers), and a `check_headroom()` pre-flight check before enabling anything hardware
can't actually support.

**Campaigns finished:** RAG 3,247/3,247, fine-tune 2,193/2,193. Rebuilding the knowledge base and
re-running the benchmark against the *unchanged* adapter then surfaced a regression: **89% →
71.9%**. Root cause wasn't context dilution (the first guess) — it was two real bugs: the
Prototype 3 fact-loss pattern still live in several chunks, and retrieved context ordered
worst-to-best (most relevant chunk buried furthest from the question). Fixed both, reaching
81.3%, then a full pass on every remaining wrong answer reached 97.9% (94/96). Expanding the
benchmark to 144 questions exposed the same bug class at scale; fixing those landed the **final
95.8% (138/144)**.

**Audit mode:** a third campaign mode automates the fact-loss hunt going forward — one
volunteer's LLM proposes a fix, a different volunteer's LLM independently reviews it, capped at 3
rounds before escalating to a human. Ran to completion once (3,247/3,247, 2,255 fixes, 168
escalations, all reviewed clean), then kept running re-passes as chunks change. Fixed two pipeline
gaps found along the way: fine-tune data wasn't actually picking up audit fixes, and a resolved
chunk was being re-offered forever instead of leaving the dispatch queue.

**TUI migration:** hand-rolled ANSI redraw logic kept breaking (5+ distinct bugs across dual-lane,
parallel workers, and the admin dashboard) — replaced with `textual` for both client and server.
A follow-up audit of that migration found and fixed three more real bugs (a missing import that
prevented the client from starting, dead duplicated auto-update code, and a background-thread
`sys.exit()` that didn't actually stop the app). Old/duplicate client and server files archived.

**Training:** a new QLoRA round (7,110 train / 374 val examples) is trained but not yet
re-benchmarked.

</details>

---

<details>
<summary><strong>Summary table</strong></summary>

| Prototype | Approach | Outcome |
|---|---|---|
| 1 | Fine-tune only | Lobotomized, unusable |
| 2 | RAG only, single-file KB | Facts good, code examples wrong |
| 3 | Distributed crunching | 1,134/1,134 chunks, bigger KB (fact-loss bug found later) |
| 4 | Fine-tune + RAG hybrid | 89% on 96-question benchmark, general capability intact |
| 5 | Consolidation & cleanup | Both campaigns complete; 89%→71.9% regression found and fixed; benchmark expanded to 144Q, reached 95.8%; audit mode added; client/server rebuilt on `textual` |

</details>
