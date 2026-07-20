# Cubyz AI

A local AI assistant that actually knows the [Cubyz](https://github.com/PixelGuys/Cubyz) codebase
and community — engine internals, keybindings, addon-creator tooling, GitHub PR review history —
without losing general competence along the way. Built by combining a deterministic RAG retrieval
layer with a QLoRA fine-tune, both fed by a distributed, volunteer-powered crunching pipeline
rather than one person hand-writing a knowledge base.

Four earlier prototypes explored fine-tuning alone, RAG alone, and distributed crunching before
landing on the current hybrid architecture. That history is preserved below, in case a future dead
end looks tempting again.

---

## What's in this repo

### Client — `CUBYZ_FOLDING.py`

![Client screenshot placeholder](docs/images/client.png)
<!-- TODO: replace with a real screenshot of the running client TUI -->

The volunteer-facing app. Anyone can run this to donate spare compute to whichever campaign
(RAG knowledge extraction, fine-tune pair generation, or knowledge-base auditing) is currently
active, using their own local Ollama install.

Current features:
- **Textual-based TUI** — sidebar menu, live per-lane status boxes, scrolling log, interactive
  prompts, no more hand-rolled ANSI redraw code.
- **Auto-detected hardware** — real GPU/CPU model names and VRAM/RAM readings (AMD sysfs, Windows
  WMI, Apple Silicon, Nvidia), never a fabricated fallback number when detection fails.
- **Dual-lane + parallel workers** — a machine with spare headroom can run a GPU lane and a
  CPU-only lane concurrently, plus multiple parallel worker identities hitting the same local
  Ollama instance, gated by a real pre-flight VRAM/RAM headroom check.
- **Auto-update** — checks the server every crunching cycle, downloads and restarts automatically
  (or prompts, depending on saved preference), with a hard version gate for outdated clients.
- **Clean disconnect** — notifies the server immediately on exit (`Ctrl+C`, quit keybind, or
  window close) instead of waiting out a stale-connection timeout.

### Server — `pipeline_crunching/server_textual.py`

![Server screenshot placeholder](docs/images/server.png)
<!-- TODO: replace with a real screenshot of the running admin console -->

The coordinator. Scans and chunks source material, hands out work to connected volunteers, tracks
progress/leaderboard stats, and hosts an interactive admin console for switching between campaign
modes live.

Current features:
- **Textual admin console** — sidebar Campaign Mode selector (Idle/RAG/Finetune/Audit), live
  per-machine connection panels (grouped by physical machine, folding dual-lane/parallel-worker
  identities together), a recent-events log, and a global campaign progress bar.
- **Three campaign modes on one process** — `CURRENT_MODE` switches live via the console or
  `POST /admin/mode`, with RAG/fine-tune/audit state kept fully separate.
- **Distributed audit mode** — one volunteer's LLM proposes a fix for a knowledge-base chunk that
  dropped a real fact, a different volunteer's LLM independently reviews it, capped at 3 rounds
  before escalating to a human — see [Current stage](#current-stage) below for where this actually
  stands.
- **Per-volunteer contribution tracking** — lifetime chunks/reviews/fixes per user, renamed/merged/
  deleted identities migrate their whole history instead of orphaning it.

---

## Current stage

- **RAG campaign:** complete (3,247/3,247 chunks), knowledge base rebuilt and serving the live
  webapp (`webapp/chat_server.py`).
- **Fine-tune campaign:** complete (2,193/2,193 chunks → 3,742 training pairs), and a further QLoRA
  training round on a larger mixed dataset has finished — `cubyz-assistant-f16.gguf` /
  `cubyz-assistant-q4.gguf` are built in `finetune/training/output/`, but **not yet loaded into
  Ollama or re-benchmarked** against the 144-question test. That's the next concrete step before
  calling this training round done.
- **Audit campaign:** actively running (re-passes continue as chunks change). As of the latest
  check: ~3,313 fixes applied, ~328 escalated to human review (~9% escalation rate). Two real
  process bugs were just found and fixed by mining the escalation logs instead of guessing:
  1. After a reviewer rejected a proposal, nothing actually stopped the *same* proposer from being
     reassigned the identical chunk and resubmitting a near-identical (wrong) diagnosis — 35% of
     the largest escalation bucket was exactly this loop. Fixed: rejected proposers are now
     excluded from re-proposing the same chunk.
  2. Fixes that needed more than one attempt to land discarded their whole deliberation history the
     moment they succeeded — only chunks that got escalated kept a record of what went wrong along
     the way. Fixed: that history is now persisted in `audit_applied_log.jsonl` for any fix that
     took more than one attempt.
  Run `python3 pipeline_crunching/analyze_audit.py` any time for a live breakdown of escalation
  reasons, attempt distribution, and per-proposer rejection rates.
- **Client/server infra:** consolidated onto one client (`CUBYZ_FOLDING.py`) and one server
  (`pipeline_crunching/server_textual.py`) as of 2026-07-20; the older plain-print server and a
  duplicate client file were archived, not deleted (`archive/`).

**Open goals**, roughly in order: get the new adapter benchmarked and confirm it clears the prior
95.8%/144 mark; keep an eye on `analyze_audit.py`'s escalation-reason breakdown as the campaign
keeps running to catch the next systemic bug the way the two above were found; decide on
`/disconnect`'s current lack of auth/validation (flagged, not yet fixed — deliberate open
decision, not an oversight).

---

## History

Each prototype below is collapsed by default — expand the one you want to read. Preserved in full
because each dead end is the reason the current system works the way it does; the raw code for
everything upstream of the current system lives in `archive/`, organized by prototype.

<details>
<summary><strong>Prototype 1 — Fine-Tuning Only</strong> (unusable, shelved)</summary>

**What it was:** Direct LoRA fine-tune on the Cubyz codebase, no RAG, no general-data mixing.

**Model:** `Qwen2.5-Coder-3B-Instruct`, plain LoRA, bf16 (no quantization). Dataset:
`cubyz_training.jsonl`, generated by walking the engine source through a local model
(`devstral:24b`) to produce instruction/output pairs.

**What went wrong:** Catastrophic forgetting ("lobotomy"). The model could talk about Cubyz but
lost general competence — basic reasoning, unrelated code, plain conversation all degraded.
100% Cubyz-flavored training data with nothing to counterbalance it.

**What was learned:** Narrow full fine-tuning without general-data mixing is a direct path to
forgetting. Needed either quantized/adapter-only training (smaller footprint = less drift) or a
real slice of general instruction data in the mix — ideally both.

**Result:** Unusable. Shelved. Preserved in `archive/prototype_1_finetune_only/`.

</details>

<details>
<summary><strong>Prototype 2 — Early RAG</strong> (validated the approach)</summary>

**What it was:** Retrieval instead of retraining — a Chroma vector DB over one merged knowledge
file (`cubyz_master_knowledgebase.md`), served via `rag_server.py`. Model weights untouched, so
zero forgetting risk. Alongside it, `extract_reviews.py` started pulling real GitHub PR review
comments as a separate dataset.

**What went right:** Clean factual lookups worked — creator, Discord, project history.

**What went wrong:** Code examples came back wrong. One undifferentiated markdown blob wasn't
fine-grained enough for retrieval to reliably find the *exact right* passage instead of something
merely nearby.

**What was learned:** RAG quality is bottlenecked by chunk granularity and source coverage, not
just having a vector DB at all.

**Result:** Validated the RAG approach; no comparable accuracy number since the 96-question
benchmark didn't exist yet. Preserved in `archive/prototype_2_early_rag/` and
`archive/prototype_2_review_extraction/`.

</details>

<details>
<summary><strong>Prototype 3 — Crunch-Party (Distributed Data Crunching)</strong> (bigger KB, introduced a bug found later)</summary>

**What it was:** Not a model — infrastructure to scale Prototype 2's knowledge base. A
coordinator (`server.py`, now in `pipeline_crunching/`) handed out source chunks (wiki, codebase,
addon-creator tooling, PR reviews) to community volunteers running a client, each processed
through a local LLM and reported back via lock files, hashes, and a live leaderboard.

**What went right:** Completed 1,134/1,134 chunks — replacing Prototype 2's single-file blob
with a real, community-built knowledge base.

**What went wrong:** A systemic bug wasn't caught until Prototype 4's accuracy testing: the
crunching prompt let the LLM summarize *that* a topic was covered without stating the actual
value (e.g. confirming "this page discusses the server port" without writing the port number
itself). Several important facts were lost this way.

**What was learned:** Fixed at the source in the crunching prompt (now requires verbatim fact
preservation) so future campaign runs don't repeat it.

**Result:** Bigger, broader knowledge base; introduced a fact-loss bug that stayed invisible
until real testing in Prototype 4.

</details>

<details>
<summary><strong>Prototype 4 — Hybrid: Fine-Tune + RAG (production model)</strong> (89% on the 96-question benchmark)</summary>

**What it was:** Fine-tuning for voice and judgment (how a Cubyz dev reasons, reviews code,
debugs), RAG for hard facts (keybindings, defaults, protocol details) — combining what Prototype
1 and Prototype 2 each got right.

**Model:** QLoRA fine-tune on `Qwen2.5-Coder-7B-Instruct` (dropped from an initial 14B attempt
after repeated CUDA OOM crashes), merged and quantized, paired with a deterministic retrieval
layer (`local_rag_chat.py`) that always retrieves — no model discretion — at temperature 0 for
reproducibility. Training data mixed Cubyz examples with general instruction data
(`OpenHermes-2.5`) to avoid repeating Prototype 1's mistake.

**Benchmark:** fixed 96-question test — keybindings, engine internals, addon-creator edge cases,
developer judgment calls.

| Round | Approach | Score |
|---|---|---|
| 1 | Fine-tune alone | ~20-24% |
| 2 | Fine-tune alone, more data/epochs | ~27% |
| 3 | Fine-tune + RAG (first pass) | 58% |
| 4 (final) | Fine-tune + RAG, root-caused fixes | **89%** |

**What went wrong (rounds 1-2):** General capability held up fully every round — no lobotomy,
ever. But narrow facts didn't stick from fine-tuning alone, and round 2's extra training
data/epochs bought only +3 points for a lot of extra compute, with a couple of regressions —
a ceiling, not a data-volume problem.

**What went right (round 3 onward):** Switching to the hybrid architecture jumped accuracy
27% → 58% in one pass. From there, every remaining wrong answer was traced to one of three root
causes and fixed at the source:
1. Reference docs that existed but were never chunked into the knowledge base — pipeline gap.
2. The Prototype 3 crunching bug (topic mentioned, value never stated) — fixed in the affected
   chunks and in the crunching prompt itself.
3. A reproducible model bias on a small cluster of similar tool-type questions, confirmed at
   temperature 0 — not fixable with more RAG content since correct context was already present.

**What was learned:** Fine-tuning and RAG fail in different, complementary ways — fine-tuning
forgets/hallucinates narrow facts, RAG is only as good as its source coverage. Combining them
and fixing root causes (not just patching outputs) closed almost the entire gap. The last two
points of the remaining 11% are artifacts of how the training data itself was generated, not
real documented Cubyz facts — not worth fabricating a source to chase.

**Serving it:** Originally planned for Open WebUI, but its native retrieval left searching up to
the model's own discretion (inconsistent grounding) and its frontend gave up on slow responses
("Connection lost"). Replaced with a purpose-built lightweight webapp (`webapp/chat_server.py` +
`chat_frontend.html`) reusing the same validated retrieval directly, plus persistent chat history
and like/dislike feedback with an optional note — real user-flagged issues feed straight back
into fixing the knowledge base.

</details>

<details>
<summary><strong>Prototype 5 — Consolidation, Regression Hunt & TUI Migration</strong> (95.8% on the expanded 144-question benchmark)</summary>

Before extending Prototype 4's system further, a pass to pay down accumulated maintenance debt in
the project's infrastructure, then use that cleaner base to re-verify (and push past) Prototype
4's 89% benchmark.

#### Infrastructure consolidation

- **Client scripts merged.** Each campaign shipped three ~85-90%-identical per-OS scripts
  (`client_{linux,mac,windows}.py`); merged into one cross-platform script per campaign
  (`RAG_FOLDING.py`, `FINETUNE_FOLDING.py`), then merged those two into a single unified client,
  **`CUBYZ_FOLDING.py`** (repo root). The server now assigns which campaign a volunteer runs (a
  `"mode"` field on `/get_work`) instead of the volunteer picking at startup. Along the way, this
  also closed real feature gaps the per-OS split had let drift (Windows-only leaderboard
  generation, Linux never checking for Intel GPUs, a cruder flat-16GB AMD guess) so all platforms
  now get identical coverage. Old scripts preserved in `archive/`.
- **Servers merged.** `pipeline_crunching/server.py` absorbed `finetune/server_finetune.py`'s
  campaign — one process, one `CURRENT_MODE` switchable live via `POST /admin/mode`, with RAG and
  fine-tune state (locks/stats/hashes/output) kept fully separate. Fixed a real pre-existing bug
  while merging: the RAG server's backup logic passed an absolute path into `os.path.join()`,
  which silently discards prior path components — every "backup" was really the file copied onto
  itself.
- **Versioning & auto-update.** A `client_version` gate (`HTTP 426`) rejects outdated clients
  cleanly; an update check runs every crunching cycle (not just at startup); updates apply via a
  silent `os.execv` restart or an interactive y/n prompt depending on a persisted first-boot
  choice; `CURRENT_MODE` persists across server restarts with an "unfinished campaign" flag if the
  last run didn't shut down cleanly. Also fixed a real **auto-update infinite loop**: a stale CDN
  cache could serve old content that "installed" as a no-op and re-triggered the same version
  mismatch forever — fixed by verifying the downloaded file's own `VERSION` line before installing.
- **Port conflict resolved:** `webapp/chat_server.py` and `pipeline_crunching/server.py` used to
  share port 7000 (run one at a time). `chat_server.py` was moved to port 7001 so the live AI chat
  website and a distributed campaign can now run concurrently.
- **Known, not-yet-fixed:** none of `/admin/mode`, `/submit_work`, or the volunteer `user_id`
  scheme have authentication — needs a real design decision, not fixed yet.

#### Dual-lane crunching & hardware detection

- **GPU+CPU concurrent lanes.** On a machine with a real GPU and spare RAM, `CUBYZ_FOLDING.py` runs
  a GPU lane and a second CPU-only lane (`num_gpu=0`) at once, roughly doubling throughput, with a
  shared `DualStatusBoard` and a live pause-menu toggle. Building this surfaced a real
  **server concurrency bug**: FastAPI's threaded synchronous handlers let two concurrent requests
  interleave read-modify-write cycles on `lock_state.json`, causing duplicate assignments and once
  corrupting the lock file outright — fixed with a single `campaign_state_lock` around every
  read-modify-write endpoint. Also fixed: chunks that failed validation 3 times had no terminal
  state and looped forever between nodes; the server now tracks give-up counts and marks a chunk
  permanently done after 3 independent give-ups.
- **Real hardware readings instead of guesses.** Every hardcoded VRAM guess (AMD/Intel/Nvidia,
  Windows/Linux) was replaced with a real reading (Linux: amdgpu sysfs directly, bypassing ROCm
  tooling that misses older cards; Windows: WMI's `AdapterRAM`) or an honest "unknown" (`0.0`)
  rather than a fabricated number. On top of that, the client now **benchmarks real throughput**
  once per machine at first boot (a representative schema-constrained call, not a trivial toy
  prompt that can pass while still hanging on real work) and picks the lane by capability, not raw
  speed, since a fast lane stuck on the smallest model tier is excluded from fine-tune work
  server-side. CPU-only lane model choice also now scales with system RAM instead of a fixed floor.

#### Campaign completion & the benchmark regression saga

Both distributed campaigns finished: **RAG 3,247/3,247 chunks** (verified clean — 0 malformed, 0
duplicate IDs, 0 empty fields), **fine-tune 2,193/2,193 chunks** → 3,742 training pairs. Rebuilding
the stale `knowledge_base/` from the finished RAG campaign, then re-running the 96-question hybrid
benchmark against the *unchanged* Prototype 4 adapter, surfaced a real regression: **89% → 71.9%**.

Root-causing this took several passes, and the initial diagnosis (context dilution from more
retrieved chunks) turned out to be wrong. Re-testing at `temperature=0.0` showed the correct chunk
was retrieved 100% of the time, yet answers still flipped run-to-run — greedy decoding wasn't
actually reproducible, so part of the "regression" was noise. Digging into the flips found the real
causes and fixed each at the source:

1. **The Prototype 3 fact-loss bug ("topic mentioned, value never stated") was still live** in
   several chunks despite being marked fixed — e.g. a FAQ chunk said it "covers healing mechanics"
   instead of stating there's no way to heal. Hand-corrected against raw source, and a new
   mechanical validator, `check_wiki_faq_grounding()`, now catches missing negation-style facts in
   WIKI-type chunks before they ship.
2. **Retrieved context was ordered worst-to-best**, so the most relevant chunk sat furthest from
   the question in a 10-14 chunk prompt (the "lost in the middle" effect). `local_rag_chat.py` now
   orders worst-first/best-last and uses an explicit seed for reproducibility.

That brought the benchmark to 81.3%, then a full root-cause pass on every remaining wrong answer
(more fact-loss instances, a "respectively"-style keybinding list that reliably caused
position-miscounting until converted to bullet points, and a duplicated fact across two chunks
destabilizing both) reached **97.9% (94/96)**. Real user thumbs-down feedback from the live webapp
was then replayed against the fixed pipeline and mostly resolved as a side effect, surfacing one
more fresh instance of the fact-loss bug (wood recipes) fixed the same way.

The benchmark was then **expanded to 144 questions** to cover previously-untested corpus areas,
which immediately exposed the same bug class at a larger scale (whole policy documents compressed
to one topic-listing sentence) — proof that a benchmark "PASS" only validates the facts it actually
probes. After fixing those, the **final combined result is 138/144 (95.8%)**. The 5 remaining wrong
answers are a distinct, smaller issue — a topically-similar-but-wrong chunk winning attention over
the correct one — confirmed as a retrieval-reranking limitation via retrieval logs, not a data gap,
and left as a known residual rather than chased with prompt tweaks that risked destabilizing
already-fixed behavior.

**Lessons carried into future crunching:** dense reference facts (keybindings, per-slot mappings)
should be crunched as bullet lists, not prose enumeration; multi-topic/long source docs need extra
scrutiny against over-compression; raw PR diff/comment text should be retained alongside crunched
review summaries so a future grounding audit has something to check against.

**In parallel, a new QLoRA training round** (`Qwen2.5-Coder-7B-Instruct`, 7,110 train / 374 val
examples after 1:1 general-data mixing) targeted the 95.8%/144 RAG-side figure once merged. As of
the current stage, the merged GGUF is built but not yet re-benchmarked — see
[Current stage](#current-stage) above.

#### Distributed audit mode

Every fix in the regression saga above was found and applied by hand. A third campaign mode,
**`audit`** (alongside `rag`/`finetune`, same infrastructure), automates that process going
forward: one volunteer's LLM checks a published `knowledge_base/*.md` chunk against its real source
and proposes a fix if it finds the fact-loss pattern; a different volunteer's LLM independently
reviews it (diagnosis, fix correctness, regression check) and can approve/reject/request-revision,
capped at 3 rounds before escalating to a human. Model assignment is server-managed and tiered by
hardware capability, spanning multiple model vendors so concurrent reviews aren't all blind spots
of the same model.

The first live 3-machine test surfaced a real problem: the weakest roster model turned out to be an
unreliable reviewer (56% of its reviews ended on chunks that never converged, including literally
self-contradictory feedback across rounds on the same chunk). Fixed by gating review/revise work to
medium+ hardware tier, and requiring 2 independent approvals (not 1) before a fix lands on `docs`
chunks specifically, since that's the most user-facing content and where every severe bug in this
saga was found. Post-fix, the escalation rate dropped from 30% to under 3% with zero leakage from
the gated-out weak reviewer — confirmed against live campaign data, not just in theory.

The `audit` campaign then ran to completion once: **3,247/3,247 chunks**, 2,255 fixes applied, 168
escalated to human review. A full review pass followed the plan agreed earlier (verify against raw
source, never trust a chunk's or reviewer's own claim): a mechanical sweep across the whole
`knowledge_base/` for known bug patterns came back clean except one isolated bad generation; all 168
escalations were reviewed (15 "malformed content" ones all traced to the *same* root cause — a
proposer re-generating a whole wrapped document instead of just prose — and a structural guard
correctly blocked every one, zero corruption); and a sample of ~35 applied fixes across all four
collections found and fixed 3 real fabrication errors — an isolated failure pattern, not a new
systemic bug class.

This surfaced two real pipeline gaps, both fixed at the root:

- **Fine-tune training data never actually benefited from any audit fix.** `finetune_initialize_chunks()`
  sourced content from the raw, one-time crunch output, completely separate from the
  `knowledge_base/*.md` files audit mode actually edits. Fixed by re-deriving finetune's source
  content live from `knowledge_base/*.md` instead, so every past and future audit fix flows into
  the next training run automatically. A related landmine (`build_knowledge_base.py` silently
  overwriting audit-corrected chunks back to their original content) was fixed to permanently skip
  any chunk already in `audit_lock_state.json`'s completed set.
- **A completed chunk could never be dispatched or resubmitted again**, even when its combined
  raw+kb content hash genuinely changed since its last audit pass — and fixing that then exposed a
  second, more severe bug: nothing pruned a just-resolved chunk from the in-memory dispatch queue,
  so it was immediately re-offered on the very next poll, a live infinite loop that was the actual
  explanation for "100% complete but every client is still working." Fixed across all three
  campaign modes by pruning a chunk from its queue at the moment it resolves.
- Two new server endpoints, `rename_user` and `merge_user`, properly migrate/combine a volunteer's
  stats, hardware info, and first-seen date server-side, instead of the pause menu's rename option
  only changing what the client remembered locally and orphaning the old identity's history.
  `delete_user` does the thorough opposite: purges every trace of an identity.

The audit campaign has continued running re-passes since (chunks become re-eligible when their
source content changes). See [Current stage](#current-stage) for the live numbers and the two
process bugs found most recently by mining the escalation logs.

#### Parallel workers, hardware guardrails, and a multi-lane terminal UI

Raised by a volunteer's own question ("can Ollama process multiple requests at once on consumer
hardware?"): yes, via `OLLAMA_NUM_PARALLEL`, and the client now can too. `ParallelWorkerPoolController`
spins up extra worker identities (independent `crunch_lane()` calls, same pattern as the existing
dual-lane secondary) that all hit the same local Ollama instance concurrently. Worker count scales
down per hardware tier (bigger models cost more KV-cache per concurrent slot), and — after an
initial version that would happily enable this on hardware that couldn't actually support it — a
real `check_headroom()` pre-flight check now refuses to start if the machine's detected VRAM/RAM
doesn't clear a conservative per-tier estimate, rather than finding out via an OOM or stall.

Also added this round: a GPU architecture compatibility database that checks for a small,
deliberately conservative deny-list of *confirmed*-dead architectures (e.g. `gfx803`/Polaris,
dropped from ROCm since 4.5) *before* spending up to two minutes running a real benchmark that was
always going to fail anyway; a pause-menu redesign with new options to rename, change primary lane,
and delete an identity; and the volunteer name length limit raised from 9 to 12 characters.

Making all this visible without the terminal falling apart took several real iterations
(hand-rolled ANSI redraw hit at least 5 distinct bugs across dual-lane, parallel workers, and the
admin dashboard) before landing on the actual fix: switching to the terminal's *alternate screen
buffer*, the same mechanism `htop`/`vim`/`less` use.

#### Textual TUI migration (v1.3.1) and a follow-up bug audit

The hand-rolled ANSI redraw problems above led to a full migration onto the `textual` library for
both the server's admin console and the client's status display (superseding an intermediate
`rich`-only attempt, `server_rich.py`, kept in `archive/` as a real working step along the way).
This covered: a signal-handling crash fixed by inverting which thread owns `textual` vs. `uvicorn`
(Python's `signal` module requires the main thread); a `Live.update(refresh=True)` bug that froze
the dashboard on one static frame despite real traffic; per-machine lane clustering and a live
"Contribution %" per volunteer; exact GPU/CPU model-name detection; a restored auto-updater; and
numerous panel-width/layout fixes found only by watching it run on a real terminal, not headless
tests alone — several real bugs across this migration were only caught that way.

A follow-up audit of that work (once it was done) found and fixed three further real bugs the hard
way — by actually executing the code, not just reading it: a missing `import atexit` that prevented
the client from starting at all; two silently-duplicated auto-update functions where three separate
"fix" commits were all editing dead, shadowed code while a broken regex in the live copy kept every
real download rejected; and fatal startup errors hanging the TUI forever instead of exiting, since
`sys.exit()` on a background thread doesn't stop the main `textual` event loop. All three are fixed.
The redundant duplicate client file (`CUBYZ_FOLDING_TUI.py`) and the two now-superseded servers
(`server.py`, `server_rich.py`) were archived, leaving one canonical client and server going
forward — see [What's in this repo](#whats-in-this-repo) above.

</details>

---

<details>
<summary><strong>Summary table</strong></summary>

| Prototype | Approach | Outcome |
|---|---|---|
| 1 | Fine-tune only | Lobotomized, unusable |
| 2 | RAG only, single-file KB | Facts good, code examples wrong |
| 3 | Distributed crunching | 1,134/1,134 chunks, bigger KB (introduced a fact-loss bug found later) |
| 4 | Fine-tune + RAG hybrid | 89% on 96-question benchmark, general capability fully intact |
| 5 | Consolidation & cleanup | RAG (3,247) + fine-tune (2,193) campaigns both complete; dual-lane crunching; 89%->71.9% regression found and root-caused (live crunching fact-loss bugs + context ordering/list-format issues, not corpus dilution); systematic RAG-side fixes plus a benchmark expansion to 144 questions brought it to 138/144 (95.8%); distributed `audit` campaign mode now catches this bug class on an ongoing basis; client/server migrated to `textual` and consolidated to one canonical file each; new fine-tune training round built but not yet re-benchmarked |

</details>
