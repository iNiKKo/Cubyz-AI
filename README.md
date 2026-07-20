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
- **Fine-tune:** Prototype 5's round-2 result (`SNALE-AI-P5-7B`, Qwen2.5-Coder-7B-Instruct) is
  done and benchmarked. Prototype 6 (model-swap experiments, see History below) is in progress —
  `SNALE-AI-P6-0.6B` benchmarked at **16.4% overall accuracy (vs. the 7B's 36.8%)** on the same
  152-question test, a real capacity loss. Qwen3.5 (both 0.8B and 4B) is confirmed GPU-crash-prone
  on this hardware and ruled out entirely. Currently training `Qwen3-4B-Instruct-2507` (standard
  architecture, no crash risk) after a separate OOM+NaN bug hunt — root cause was `trl`'s
  `chunked_nll` loss nesting its own checkpoint call inside this script's model-level
  checkpointing; fixed via `loss_type="nll"`. Not yet benchmarked.
- **Audit:** complete (3,247/3,247), re-runs automatically as chunks change. Run
  `python3 pipeline_crunching/analyze_audit.py` anytime for a live breakdown of what's failing and
  why.
- **Infra:** one client (`CUBYZ_FOLDING.py`), one server (`server_textual.py`). Old/duplicate
  versions archived, not deleted.

**Open items:** benchmark `Qwen3-4B-Instruct-2507` once training finishes; if it doesn't close
enough of the gap back to the 7B, `ByteDance-Seed/Seed-Coder-8B-Instruct` (dense, MIT-licensed,
no architectural risk) is the researched next candidate; decide on `/disconnect`'s missing auth
(known, not fixed).

**[Live model leaderboard](https://claude.ai/code/artifact/4def066b-3b7d-4ef2-97ac-779689b6d7a4)**
— ranked domain-fact accuracy for every fine-tuned model, updated as new rounds are benchmarked.

---

## History

Collapsed by default. Preserved because each dead end is why the current system works the way it
does — raw code for everything upstream lives in `archive/`.

Every entry below follows the same layout: what changed in the **client/server**, whether the
**fine-tune data** or **RAG** knowledge base changed (and why), whether a **new model** came out
of it, whether that model actually used the new RAG/fine-tune data, and the **result**. Narrative
detail and lessons-learned follow beneath for entries where the story matters.

<details>
<summary><strong>Prototype 1 — Fine-Tuning Only</strong> (unusable, shelved)</summary>

- **Client/server:** none yet — pre-dates the current infra entirely.
- **Fine-tune data:** new. First dataset: raw Cubyz codebase text, 100% domain content, no
  general-instruction mixing.
- **RAG:** none.
- **New model:** yes — direct full LoRA fine-tune of `Qwen2.5-Coder-3B-Instruct` (bf16, no
  quantization).
- **New model uses:** N/A (no RAG or prior fine-tune to build on).
- **Result:** catastrophic forgetting — lobotomized, unusable.

The model could talk about Cubyz but lost general competence — reasoning, unrelated code, plain
conversation all degraded. 100% domain-flavored training data with nothing to counterbalance it.

**Lesson:** narrow full fine-tuning without general-data mixing forgets. Need adapter-only
training and/or real general instruction data in the mix.

Shelved. `archive/prototype_1_finetune_only/`.

</details>

<details>
<summary><strong>Prototype 2 — Early RAG</strong> (validated the approach)</summary>

- **Client/server:** none yet — served via a standalone `rag_server.py`.
- **Fine-tune data:** none — abandoned that approach after Prototype 1.
- **RAG:** new. First knowledge base: one merged markdown file in a Chroma vector DB.
- **New model:** no — base model only, retrieval instead of retraining.
- **New model uses:** N/A.
- **Result:** facts good, code examples wrong.

Zero forgetting risk since model weights are untouched. Clean factual lookups (creator, Discord,
project history) worked; code examples came back wrong — one undifferentiated markdown blob
wasn't fine-grained enough for retrieval to find the exact right passage.

**Lesson:** RAG quality is bottlenecked by chunk granularity and source coverage, not just having
a vector DB.

`archive/prototype_2_early_rag/`, `archive/prototype_2_review_extraction/`.

</details>

<details>
<summary><strong>Prototype 3 — Crunch-Party (Distributed Crunching)</strong> (bigger KB, introduced a bug found later)</summary>

- **Client/server:** new — first distributed crunching pipeline. A coordinator handed out source
  chunks (wiki, codebase, addon-creator docs, PR reviews) to volunteers running a client, each
  processed through a local LLM.
- **Fine-tune data:** none.
- **RAG:** scaled up — knowledge base grew from Prototype 2's single file to 1,134/1,134
  community-crunched chunks.
- **New model:** no.
- **New model uses:** N/A.
- **Result:** bigger KB, but introduced a fact-loss bug not caught until Prototype 4.

The crunching prompt let the model summarize *that* a topic was covered without stating the
actual value (e.g. "discusses the server port" without writing the port number). Several facts
were lost this way.

**Lesson:** fixed at the source in the crunching prompt (now requires verbatim fact preservation).

</details>

<details>
<summary><strong>Prototype 4 — Hybrid: Fine-Tune + RAG</strong> (89% on a 96-question benchmark)</summary>

- **Client/server:** no major infra change; served via a new purpose-built webapp
  (`webapp/chat_server.py`) after Open WebUI's own retrieval proved inconsistent and its frontend
  gave up on slow responses.
- **Fine-tune data:** new — Cubyz data mixed with general instruction data (`OpenHermes-2.5`),
  specifically to avoid Prototype 1's forgetting problem.
- **RAG:** reused Prototype 3's knowledge base, now paired with the fine-tune instead of standing
  alone.
- **New model:** yes — QLoRA on `Qwen2.5-Coder-7B-Instruct`.
- **New model uses:** yes — this is the first round the fine-tune and RAG were combined and
  served together, deterministic retrieval at temperature 0.
- **Result:** 89% on a 96-question benchmark (final round), general capability fully intact.

| Round | Approach | Score |
|---|---|---|
| 1 | Fine-tune alone | ~20-24% |
| 2 | Fine-tune alone, more data/epochs | ~27% |
| 3 | Fine-tune + RAG (first pass) | 58% |
| 4 (final) | + root-caused fixes | **89%** |

Fine-tuning alone couldn't hold narrow facts, and more data/epochs bought only +3 points.
Switching to hybrid retrieval jumped 27%→58% in one pass; every remaining wrong answer then
traced back to one of three causes (docs never chunked into the KB, the Prototype 3 fact-loss
bug, a reproducible model bias on one question cluster) and got fixed at the source.

**Lesson:** fine-tuning and RAG fail differently — fine-tuning forgets/hallucinates narrow facts,
RAG is only as good as its source coverage. Combining them and fixing root causes (not patching
outputs) closed almost the entire gap.

</details>

<details>
<summary><strong>Prototype 5 — Consolidation, Regression Hunt & TUI Migration</strong> (95.8% on an expanded 144-question benchmark)</summary>

- **Client/server:** major consolidation — three per-OS client scripts and two servers merged
  into one client (`CUBYZ_FOLDING.py`) and one server, with live campaign-mode switching. Added a
  version gate, auto-update, dual GPU+CPU lanes, parallel workers, real hardware detection (no
  fabricated fallback numbers), a `check_headroom()` pre-flight check, an audit-mode campaign
  type, and a full TUI rewrite on `textual`.
- **Fine-tune data:** new round — 7,110 train / 374 val examples (grew from Prototype 4's set).
- **RAG:** rebuilt/re-crunched knowledge base (3,247/3,247 chunks) plus the new audit-mode
  campaign that automates finding and fixing fact-loss bugs going forward.
- **New model:** yes — `SNALE-AI-P5-7B` (`Qwen2.5-Coder-7B-Instruct`).
- **New model uses:** yes — served with the rebuilt, audited RAG knowledge base.
- **Result:** 95.8% (138/144) on an expanded benchmark, after finding and fixing a regression.

Rebuilding the knowledge base and re-running the benchmark against the *unchanged* Prototype 4
adapter surfaced a regression: **89% → 71.9%**. Root cause wasn't context dilution (the first
guess) — it was two real bugs: the Prototype 3 fact-loss pattern still live in several chunks,
and retrieved context ordered worst-to-best (most relevant chunk buried furthest from the
question). Fixed both, reaching 81.3%, then a full pass on every remaining wrong answer reached
97.9% (94/96). Expanding the benchmark to 144 questions exposed the same bug class at scale;
fixing those landed the final 95.8%.

**Audit mode:** one volunteer's LLM proposes a fix, a different volunteer's LLM independently
reviews it, capped at 3 rounds before escalating to a human. Ran to completion once (3,247/3,247,
2,255 fixes, 168 escalations, all reviewed clean), then kept running re-passes as chunks change.
Fixed two pipeline gaps found along the way: fine-tune data wasn't actually picking up audit
fixes, and a resolved chunk was being re-offered forever instead of leaving the dispatch queue.

**TUI migration:** hand-rolled ANSI redraw logic kept breaking (5+ distinct bugs across dual-lane,
parallel workers, and the admin dashboard) — replaced with `textual` for both client and server.
A follow-up audit of that migration found and fixed three more real bugs (a missing import that
prevented the client from starting, dead duplicated auto-update code, and a background-thread
`sys.exit()` that didn't actually stop the app). Old/duplicate client and server files archived.

</details>

---

<details>
<summary><strong>Prototype 6 — Model-Size Experiments</strong> (in progress)</summary>

- **Client/server:** no changes — pure model/training experimentation.
- **Fine-tune data:** no changes — same dataset as Prototype 5's round 2 (7,110/374 examples);
  only the base model and training config changed.
- **RAG:** no changes.
- **New model:** yes, several attempts — `Qwen3.5-0.8B` (crashed), `SNALE-AI-P6-0.6B`
  (`Qwen3-0.6B`, benchmarked), `Qwen3.5-4B` (crashed), `Qwen3-4B-Instruct-2507` (training).
- **New model uses:** no — every benchmark this round tested each model's own standalone recall
  with RAG deliberately turned off, to isolate what the fine-tune alone learned. None of these
  models have been served with RAG yet.
- **Result so far:** `SNALE-AI-P6-0.6B` retained 37.5% of the 7B's domain-fact accuracy (12.5% vs
  33.3%) at 11.7x smaller — see the [live leaderboard](https://claude.ai/code/artifact/4def066b-3b7d-4ef2-97ac-779689b6d7a4)
  for the up-to-date ranking as more models are benchmarked. `Qwen3-4B-Instruct-2507` is training,
  not yet benchmarked.

Started 2026-07-20 when the 7B QLoRA run's ~4hrs/attempt made iterating on training-data/config
changes impractically slow, plus an unresolved resume bug (NaN loss on the very first step after
resuming from checkpoint-200, likely `paged_adamw_8bit` optimizer-state resume on this ROCm
nightly — never root-caused, just avoided by moving to a model small enough not to need it).

**First attempt, Qwen3.5-0.8B:** newest generation at the time, but hard-crashed the GPU driver on
step 1 of real training (`Memory access fault... Page not present`, core dump, required a full PC
reboot). Root cause: Qwen3.5's hybrid Gated DeltaNet attention needs `flash-linear-attention`/
`causal-conv1d` kernels; those aren't installed, transformers silently falls back to a torch
reimplementation of that path, and that fallback is what faulted. Confirmed `causal-conv1d` has
no official ROCm support for this RDNA4 chip class as of 2026 (upstream GitHub issue open,
unassigned) — this risk is architecture-inherent, not size-specific.

**Settled on Qwen3-0.6B** instead — standard dense transformer, no hybrid dependency. Also
switched QLoRA (4-bit) to plain bf16 LoRA and `paged_adamw_8bit` to `adamw_torch`, since VRAM is
no longer the constraint at this size.

**Found and fixed a real test-harness bug** in `test_inference.py`: a batch of Cubyz-specific
questions had been mistakenly added to the general-knowledge sanity-check list as
`(question, answer)` tuples, while that list's loop assumed plain strings — every one of those
questions was silently fed to the model as a stringified tuple instead of its actual text,
producing garbage answers that looked like model damage but weren't. Fixed by moving those
questions to the domain-fact list (where they belong) and adding real general-knowledge questions
in their place.

**Tried Qwen3.5-4B next** — a smoke test (one forward+backward pass) passed cleanly, but the real
training run hard-crashed the GPU driver on step 1 with the exact same fault as the 0.8B crash
above, across two different gradient-checkpointing modes. Two independent crashes from the same
architecture family, at two different sizes, confirms this is a fundamental Qwen3.5/ROCm
incompatibility, not a config problem or a fluke. **Rule going forward: no Qwen3.5+ (or anything
hybrid/linear-attention) on this hardware, full stop.**

**Switched to Qwen3-4B-Instruct-2507** (standard attention, no hybrid dependency) — this hit its
own, unrelated multi-stage bug hunt before training successfully:

1. *OOM at the original batch size (8/2)*, sized for the 0.6B's much smaller weights. Dropped to
   1/16 (the floor) — base weights alone consumed 8.31GB of the 15.92GB card before anything else.
2. *Missing-input-grad error* on backward — the classic missing-`enable_input_require_grads()`
   gap for gradient checkpointing on a frozen PEFT base model. Fixed by adding that call
   unconditionally.
3. *Same GPU hard-fault as the Qwen3.5 crashes*, under `use_reentrant=True` checkpointing (tried
   as a workaround for #2) — a red herring, unrelated to this model's architecture.
4. *Reproducible NaN divergence* on a fresh run — root cause found by reading `trl`'s own source:
   `SFTConfig` defaults to `loss_type="chunked_nll"`, which does its own internal
   `torch.utils.checkpoint` call nested inside this script's model-level checkpointing. Fixed via
   `loss_type="nll"`, confirmed by two isolated diagnostic scripts kept in `finetune/training/`
   for reuse on future model swaps.

**Researched but not yet tried:** no newer Coder-specialized model exists in Qwen's own lineup at
≤14B (Qwen3-Coder only ships as MoE or hybrid-attention variants, both disqualified the same way
as Qwen3.5). A broader cross-vendor search found `ByteDance-Seed/Seed-Coder-8B-Instruct` (dense,
MIT-licensed, standard transformer, beats Qwen2.5-Coder-7B-Instruct on BigCodeBench/MHPP/MBPP) as
the strongest next candidate if Qwen3-4B-Instruct-2507 doesn't close enough of the gap.

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
| 6 | Model-size experiments | Qwen3.5-0.8B/4B both GPU-crashed (confirmed hybrid-attention/ROCm incompatibility); Qwen3-0.6B only 44.6% of 7B's fact-recall accuracy; Qwen3-4B-Instruct-2507 hit an OOM+NaN bug hunt (root cause: `trl`'s `chunked_nll` loss nesting its own checkpoint call inside model-level checkpointing), fixed, training in progress; Seed-Coder-8B-Instruct identified as next candidate |

</details>
