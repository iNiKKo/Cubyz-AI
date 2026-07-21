# ASH AI

A local AI assistant that knows the [Cubyz](https://github.com/PixelGuys/Cubyz) codebase and
community — engine internals, keybindings, addon-creator tooling, PR review history — without
losing general competence. A deterministic RAG retrieval layer + a QLoRA fine-tune, both fed by a
distributed, volunteer-powered crunching pipeline.

---

## What's in this repo

### Client — `pipeline_crunching/client.py`

![Client screenshot placeholder](docs/images/client.png)
<!-- TODO: replace with a real screenshot -->

Run this to donate spare compute to whichever campaign is active.

- Connects to the server, receives assigned work, crunches it with local Ollama, submits results
- Auto-detects hardware (GPU/CPU model, VRAM/RAM) and picks a model that fits
- Runs multiple lanes at once when hardware allows (GPU + CPU, or several parallel workers)
- Auto-updates to the latest version
- Sends offline status on safe exit, instead of leaving a stale connection for the server to time out

### Server — `pipeline_crunching/server.py`

![Server screenshot placeholder](docs/images/server.png)
<!-- TODO: replace with a real screenshot -->

The coordinator.

- Scans source material, chunks it, hands out work to connected clients
- Switches between RAG / Finetune / Audit campaigns live, no restart needed
- Interactive console for monitoring connections and controlling the active campaign
- Tracks per-volunteer stats and leaderboard
- **Data Sync** panel (collapsed by default in the console sidebar): one-click buttons to pull the
  latest Cubyz codebase, PR reviews/issue discussions, publish crunched volunteer output into the
  live knowledge base, and pull an audit diagnostic report — all built in, no separate scripts to
  run by hand

---

## Current stage

- **RAG:** complete (3,318 chunks, up from 3,247 after Prototype 7's two rounds of re-chunking
  fixes). Knowledge base is live on the webapp.
- **Fine-tune:** Prototype 5's round-2 result (`SNALE-AI-P5-7B`, Qwen2.5-Coder-7B-Instruct) is
  done and benchmarked. Prototype 6 (model-swap experiments, see History below) is complete and
  closed out — `SNALE-AI-P6-0.6B` benchmarked at **16.4% overall accuracy (vs. the 7B's 36.8%)**, a
  real capacity loss; Qwen3.5 (both 0.8B and 4B) confirmed GPU-crash-prone on this hardware and
  ruled out entirely; `SNALE-AI-P6-4B` (`Qwen3-4B-Instruct-2507`) reached **29.2% domain accuracy
  standalone (vs. the 7B's 33.3%)** and **91.7% (132/144) served with RAG**, slightly below
  Prototype 5's 95.8%. Every round confirmed the same pattern — fine-tune-alone accuracy is always
  far below deployed (RAG-served) accuracy, i.e. fine-tuning shifts behavior, not knowledge.
  **Prototype 7** cut fine-tune data to `reviews`-only pairs (PR-discussion judgment/voice, 1,436
  examples, down from ~3,850) with all `docs`/`codebase`/`addon_reference` Q&A pairs removed —
  Prototype 6 was the last round mixing fact Q&A into fine-tuning. `SNALE-AI-P7-4B` reached 22.9%
  domain accuracy standalone (expected — it's no longer trying to store facts) and **93.8%
  (135/144) served with RAG, beating Prototype 6's 91.7% despite training on 63% less data**.
  Confirms RAG never needed the fine-tune's help on facts. A follow-up push chasing the 7
  remaining wrong answers found a real chunking bug — several large source docs
  (`CUBYZ_DEVELOPER_JUDGMENT.md`, `GAME_DESIGN_PRINCIPLES.md`, `docs/gameplay/controls.md`) had
  been crunched into 1-2 oversized chunks that either dropped specific facts entirely or buried
  them in dense paragraphs the model couldn't reliably extract from. Re-chunked those docs
  section-by-section (2→10, 2→6, and 1→7 chunks respectively) plus grounded two facts that had no
  source chunk at all, reaching **99.3% (143/144, 1 partial)**. To confirm the fix generalized
  rather than being overfit to that one question set, wrote a second, independent, non-overlapping
  144-question set (`rag_batch_test_v2.py`) covering corners of the KB the first set never touched
  (Addon Creator field/engine-validation references, biome generation defaults, multiplayer
  hosting/port-forwarding, gameplay mechanics) and applied the same diagnose-fix-retest loop —
  every wrong/partial answer was checked against raw engine source (not the crunched chunk's own
  claim) before fixing. Found and fixed the same under-chunking pattern in `docs_README.md`,
  `docs/development/multiplayer.md`, `docs/development/addons/blocks.md`, and the Addon Creator's
  `FIELD_REFERENCE.md`/`ENGINE_VALIDATION_REFERENCE.md`, plus several chunk-vs-chunk *contradiction*
  bugs (a doc-sourced chunk and an engine-sourced chunk disagreeing on the same field's default,
  with the model siding with the wrong one) and retrieval-ranking misses where a correct fact
  existed but didn't surface in the top-K results for a given phrasing. Converged to **99.0%
  (~141-143/144 depending on run — some residual noise from model generation stochasticity rather
  than remaining content bugs)**. Both sets combined into one 288-question run
  (`webapp/rag_batch_test_combined.py`, imports both source lists rather than duplicating them).
  RAG retrieval-efficiency work and wiring client/server to pick up new fine-tune rounds
  automatically are still next.
- **Crunching pipeline (root-cause fix):** the under-chunking bug class found repeatedly above was
  traced to `pipeline_crunching/server.py`'s `_structural_chunks()` — it merged short
  markdown sections together purely by running line count, with no awareness that two different
  `##` topics shouldn't share a chunk. Fixed by making `#`/`##` headers a hard chunk boundary;
  verified against the 6 previously-broken raw docs, all now auto-split close to their hand-tuned
  chunk counts. Also cut `finetune_initialize_chunks()` to reviews-only, matching
  `assemble_sft_dataset.py`'s existing filter — `docs`/`codebase` fact-Q&A pairs were being
  generated by the crunching campaign and then silently discarded at assembly time ever since
  Prototype 7, wasting volunteer compute on ~2,400 pairs nobody trains on. **Caveat before the next
  full re-crunch:** the 6 already hand-fixed docs would get regenerated by the crunching LLM if
  re-queued, which may not perfectly preserve this session's fine-grained retrieval tuning (exact
  bolded phrases, exact Related-Questions wording) — re-benchmark after any full re-crunch rather
  than assuming it's a strict improvement.
- **Audit:** complete (3,247/3,247), re-runs automatically as chunks change. Click "Audit Report"
  in the admin console's Data Sync panel anytime for a live breakdown of what's failing and why.
- **Infra:** one client (`client.py`), one server (`server.py`) — that's the whole
  `pipeline_crunching/` folder now; the five scripts that used to sit alongside it
  (`sync_codebase.py`, `sync_reviews.py`, `build_knowledge_base.py`, `dataset_sorter.py`,
  `analyze_audit.py`) are folded directly into `server.py` as Data Sync panel buttons.
  Old/duplicate versions archived, not deleted.

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
  into one client (`client.py`) and one server, with live campaign-mode switching. Added a
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
<summary><strong>Prototype 6 — Model-Size Experiments</strong> (91.7% deployed, 29.2% fine-tune-alone on `SNALE-AI-P6-4B`)</summary>

- **Client/server:** no changes — pure model/training experimentation.
- **Fine-tune data:** no changes — same dataset as Prototype 5's round 2 (7,110/374 examples);
  only the base model and training config changed.
- **RAG:** no changes.
- **New model:** yes, several attempts — `Qwen3.5-0.8B` (crashed), `SNALE-AI-P6-0.6B`
  (`Qwen3-0.6B`, benchmarked), `Qwen3.5-4B` (crashed), `SNALE-AI-P6-4B`
  (`Qwen3-4B-Instruct-2507`, benchmarked).
- **New model uses:** yes for `SNALE-AI-P6-4B` — after standalone (no-RAG) benchmarking to isolate
  what the fine-tune alone learned, it was merged, converted to GGUF, and served through the same
  RAG pipeline as prior prototypes for a deployed-system number.
- **Result:** `SNALE-AI-P6-0.6B` retained 37.5% of the 7B's domain-fact accuracy (12.5% vs. 33.3%)
  at 11.7x smaller. `SNALE-AI-P6-4B` retained 87.7% of the 7B's domain-fact accuracy (29.2% vs.
  33.3%) at 1.75x smaller — see the [live leaderboard](https://claude.ai/code/artifact/4def066b-3b7d-4ef2-97ac-779689b6d7a4)
  for the up-to-date standalone ranking. Served with RAG, `SNALE-AI-P6-4B` reached **91.7%
  (132/144, 3 partial, 9 wrong)** on the deployed-system benchmark — slightly below Prototype 5's
  95.8%. The 9 wrong answers were generation slips on questions where the correct chunk *was*
  retrieved (e.g. inventing an unrelated error trace when asked which script builds Cubyz on
  Windows, though it still named the right script; misstating the torch recipe's output count),
  not retrieval failures — the 4B appears more prone to over-elaborating past the grounded fact
  than the 7B was.

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
a candidate if a future round wants to close the remaining ~4-point gap back to the 7B's deployed
accuracy.

</details>

---

<details>
<summary><strong>Prototype 7 — Behavior-Only Fine-Tuning + RAG Refinement</strong> (99.3%/143 on set 1, 99.0%/~142 on an independent 144Q set 2)</summary>

- **Client/server:** no changes yet — planned next, so future fine-tune rounds wire in
  automatically instead of needing manual `ANSWER_MODEL` edits in `local_rag_chat.py` each time.
- **Fine-tune data:** cut to `reviews`-only pairs (PR-discussion judgment/voice) — 1,436 examples,
  down from ~3,850. All `docs`/`codebase`/`addon_reference` Q&A fact pairs (2,417 examples) removed
  entirely from `finetune/scripts/assemble_sft_dataset.py`'s output. `train_qlora.py`'s
  `NUM_EPOCHS` dropped 3→2 (the 3-epoch bump existed only to help narrow facts stick, no longer
  relevant) and `eval_steps`/`save_steps` 100→25 to keep the same eval-checkpoint resolution on
  the now much shorter (~342-step) run.
- **RAG:** fixed a real chunking bug found while chasing the last few wrong answers (see below).
  Retrieval-efficiency work (fewer chunks pulled before landing on the right one) is still planned
  but not started.
- **New model:** yes — `SNALE-AI-P7-4B` (`Qwen3-4B-Instruct-2507`, same base as P6).
- **New model uses:** yes — benchmarked standalone, then served through the same RAG pipeline.
- **Result:** 22.9% domain accuracy standalone (expected — no longer trying to store facts) and
  **99.3% (143/144, 1 partial) served with RAG** on the original 144-question set after the
  chunking fixes below — up from an initial 93.8% (135/144), and now ahead of Prototype 5's 95.8%
  peak. A second, independent, non-overlapping 144-question set (built specifically to test whether
  the fix generalized rather than being overfit to the first set's exact questions) converged to
  **99.0% (~141-143/144 depending on run)** after the same diagnose-fix-retest loop.

Every Prototype 6 benchmark showed the same pattern: fine-tune-alone accuracy was always far below
the same model's deployed (RAG-served) accuracy — `SNALE-AI-P6-4B` scored 29.2% standalone vs.
91.7% with RAG. That gap is the direct evidence that fine-tuning shifts model *behavior*, not model
*knowledge* — RAG was already doing essentially all of the real fact-recall work, and the
`docs`/`codebase`/`addon_reference` Q&A pairs in the fine-tune data were training the model to
recall facts it would usually get wrong anyway, at the cost of dataset size/training time and the
risk of the fine-tune confidently contradicting retrieved ground truth.

**Decision: Prototype 6 was the last round mixing Q&A into fine-tuning.** Going forward, fine-tune
data is judgment/voice only (the `reviews` source type, confirmed to be ~78% real debugging-
diagnosis judgment and ~22% design-review judgment when sampled — both sourced from real GitHub
PR/issue discussions, not fabricated), and *all* factual recall is RAG's job.
`finetune/training/prepare_training_data.py` still mixes in general instruction data at the same
1:1 ratio to protect general capability, just against the smaller domain set.

**Result confirms the bet paid off**: cutting 63% of the training data barely moved the standalone
score (29.2%→22.9%, a much smaller drop than the data cut itself) and *improved* the deployed
score over Prototype 6 even before any RAG fixes.

**Chasing the last 7 wrong answers found a real, high-leverage crunching bug.** Three large source
docs — `docs/CUBYZ_DEVELOPER_JUDGMENT.md` (240 lines, 9 numbered sections), `GAME_DESIGN_PRINCIPLES.md`
(109 lines, ~20 subsections), and `docs/gameplay/controls.md` (a table-structured doc with 7
distinct control categories) — had each been crunched into just 1-2 oversized "summary" chunks.
This caused two distinct failure modes: some specific facts (the min/max convention in Blueprint
capture code, the eager-vs-lazy allocation judgment call, why a stray `defer` is flagged) were
dropped entirely from the crunched chunk and never made it into the knowledge base at all — the
same root-cause pattern as the original Prototype 3 fact-loss bug. Others were still present but
buried mid-paragraph in a chunk covering a dozen unrelated subtopics, which the model could
retrieve but not reliably extract from (e.g. "right is D" buried in one long comma-separated
sentence about movement keys). Re-chunked all three docs section-by-section (2→10, 2→6, 1→7
chunks respectively), and separately wrote two new grounding chunks for facts that had no source
chunk anywhere in the knowledge base at all (the actual PR-diff reasoning behind an argparse
migration, and a `getOrPut`-vs-contains-check review comment) — both previously "answered
correctly" only because the model's own general pretrained knowledge happened to guess right, not
because RAG was doing its job. Re-testing after the first pass surfaced two further regressions
from the new chunks competing with existing ones for retrieval slots on similar topics, fixed with
one more grounding chunk and one chunk edit. Final result: 143/144 (1 partial), confirmed with a
full re-run showing no remaining hedge/refusal answers anywhere in the set.

**A second, independent 144-question set confirmed the fix generalized and found three new bug
classes.** Built `webapp/rag_batch_test_v2.py` from scratch, covering knowledge-base corners the
first set never touched (Addon Creator `FIELD_REFERENCE.md`/`ENGINE_VALIDATION_REFERENCE.md`,
biome generation defaults, multiplayer hosting/port-forwarding/permissions, gameplay mechanics),
every expected answer hand-verified against raw source (docs, `.zig` engine source, or raw
`reviews.json`) before inclusion — never trusting a chunk's own claim. Ten-plus rounds of
diagnose-fix-retest surfaced the same under-chunking pattern in four more mega-chunks
(`docs_README.md`, `docs/development/multiplayer.md`, `docs/development/addons/blocks.md`, and
parts of the Addon Creator's own `FIELD_REFERENCE.md`), each split section-by-section the same way
as the first set's fix. Two new bug classes emerged that the first set hadn't surfaced: **chunk-vs-
chunk contradictions**, where a doc-sourced chunk and an engine-sourced chunk disagreed on the same
field's default (e.g. a biome's `.roughness`/`.hills`/`.mountains`/`.keepOriginalTerrain` fields —
the docs table just says "—", the engine source says they default to `0` — and the model sided
with the wrong one when both got retrieved together), fixed by making the less-authoritative chunk
explicitly defer to the engine-verified one instead of stating the fact independently; and
**retrieval-ranking crowding**, where GitHub PR-review chunks that happened to mention the same
field/function name in an unrelated code-quality discussion out-ranked the actual documentation
chunk, fixed by strengthening the authoritative chunk's keywords/related-questions to make it more
competitive for that exact phrasing. A handful of residual single-word omissions (an exact log
string, one item dropped from a three-item list, a filename) turned out to be genuine per-run
generation noise rather than fixable content bugs — the score oscillated between 141-143/144
correct across the last several confirmation re-runs even with zero further chunk edits, which is
the practical ceiling given non-deterministic decoding, not a remaining pipeline bug.

**Leaderboard also got a re-benchmark of Prototype 1** (`SNALE-AI-P1-3B`, the original shelved
full-forgetting model — its merged checkpoint still exists in
`archive/prototype_1_finetune_only/cubyz_ai_3b_merged/`) added for historical comparison: 18.1%
domain / 75% general / 21.1% overall — the worst general-capability score of any round (every
other model scored 87.5-100%), which is the real signature of its catastrophic forgetting more
than its domain score. Caveat: the benchmark tooling uses greedy/deterministic decoding for
consistency across all models, while Prototype 1's own original interactive test script used real
temperature sampling — that's likely why this number reads more coherent than what Nick remembers
testing at the time (real sampling exposes instability greedy decoding papers over). Treat this
score as a best-case reading of a model that's actually less stable than it suggests.

Next steps: RAG retrieval-efficiency work (fewer chunks pulled before landing on the right one),
and wiring client/server so new fine-tune rounds pick up automatically instead of needing manual
`ANSWER_MODEL` edits each round.

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
| 6 | Model-size experiments | Qwen3.5-0.8B/4B both GPU-crashed (confirmed hybrid-attention/ROCm incompatibility); Qwen3-0.6B only 44.6% of 7B's fact-recall accuracy; Qwen3-4B-Instruct-2507 hit an OOM+NaN bug hunt (root cause: `trl`'s `chunked_nll` loss nesting its own checkpoint call inside model-level checkpointing), fixed, trained; `SNALE-AI-P6-4B` reached 87.7% of the 7B's standalone accuracy and 91.7% (132/144) deployed with RAG, vs. the 7B's 95.8%; Seed-Coder-8B-Instruct identified as a candidate to close the remaining gap; final round mixing Q&A into fine-tuning |
| 7 | Behavior-only fine-tuning + RAG refinement | Fine-tune data cut to `reviews`-only pairs (1,436, down from ~3,850), all fact Q&A removed from fine-tuning going forward; `SNALE-AI-P7-4B` reached 93.8% (135/144) deployed with RAG on 63% less training data than Prototype 6; found+fixed a real crunching bug in 3 under-chunked source docs plus 2 ungrounded facts, reaching 99.3% (143/144); Prototype 1 re-benchmarked for the leaderboard (18.1%/75%/21.1%, worst general-capability score of any round); next: RAG retrieval efficiency, client/server auto-wiring |

</details>
