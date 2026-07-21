# Cubyz Fine-Tuning Pipeline

Generates a supervised fine-tuning (SFT) dataset that teaches a Cubyz assistant model to
*know* the domain directly (facts, mechanics, developer judgment) rather than retrieving it
every request, then QLoRA fine-tunes a base model on it. Companion to the RAG pipeline in the
project root, which stays the source of truth for precise, fast-changing facts (exact symbol
names, current API shape) that would go stale if baked into frozen weights.

**Status note:** this doc's Pipeline Stages section (below) describes the original distributed
generation campaign (`server_finetune.py` + `client_finetune_*.py`), since archived --
`pipeline/server.py` + `client.py` are the current unified client/server
for both RAG and finetune crunching (see `pipeline/PIPELINE.md`). More importantly, as
of Prototype 7 fine-tune data is **reviews-only** (behavior/judgment pairs) -- stages 1/2's
`docs`/`codebase` pair generation (the `wiki.jsonl`/`codebase_architectural_subset.jsonl` sources
below) is no longer run at all, since every PT6→PT7 benchmark round confirmed RAG alone carries
essentially all real fact-recall accuracy and those ~2,400 pairs were discarded downstream anyway
by `assemble_sft_dataset.py`'s `SOURCE_TYPES = {"reviews"}` filter. Kept below as an accurate
record of how the dataset actually got assembled through Prototype 6.

## Pipeline stages

1. **`scripts/filter_codebase_subset.py`** -- filters `pipeline/users/*/codebase.jsonl` (1,476 RAG
   chunks) down to the 455 that are architectural/conceptual (chunk_type + difficulty tier
   based) rather than precise symbol-level facts. Output: `source_data/codebase_architectural_subset.jsonl`.
   Re-run this any time the upstream RAG crunching campaign adds more codebase chunks.

2. **`server_finetune.py`** (repo root) + **`scripts/client_finetune_{linux,mac,windows}.py`** --
   a distributed generation campaign, structurally mirroring the RAG pipeline's
   `server.py`/`client_*.py` (same lock/hash/stats coordination), but generating natural
   instruction/response training pairs instead of RAG extraction records. Reads from three
   sources:
   - `pipeline/users/*/wiki.jsonl` (docs, 30 chunks)
   - `source_data/codebase_architectural_subset.jsonl` (455 chunks)
   - `pipeline/users/*/github_reviews.jsonl` (behavioral/judgment material, 649 chunks)

   Docs and codebase use a "restyle" prompt (the input record already passed this project's own
   grounding checks during RAG crunching, so this step only rephrases into natural Q&A). Reviews
   use a separate prompt producing either a debugging-diagnosis pair or a code-review pair,
   grounded in `comprehensive_explanation` (the crunched review records never actually carry raw
   diff text -- there's no `raw_content` field, despite earlier code assuming there was; see
   "Bugs found & fixed" below). Server runs on port 7000. Output lands in
   `pairs/{user}/{source_type}_pairs.jsonl`.

3. **`scripts/generate_addon_pairs.py`** -- hand-authored pairs for the addon_creator domain,
   written directly from `raw_cubyz_dataset/addon_creator/FIELD_REFERENCE.md`/
   `ENGINE_VALIDATION_REFERENCE.md` rather than through the distributed campaign, since that
   domain is small and bounded. Output: `handwritten_pairs/addon_creator_pairs.jsonl` (17 pairs).
   This directory is deliberately outside `pairs/` -- a hard reset of the campaign (option 2 in
   `server_finetune.py`'s startup menu) wipes `pairs/` entirely, and hand-authored data should
   never be at risk of that.

3b. **`scripts/generate_core_facts_pairs.py`** -- same pattern, added after the first trained
    adapter's qualitative test showed narrow enumerable facts (exact keybindings, exact numbers,
    exact names) didn't reliably stick even though they existed in the source data, because the
    campaign's "scale pairs to distinct content" logic only produced a handful of pairs per
    chunk -- badly undercounting something like the full keybinding table (~40 individual facts
    in one chunk). Adds direct, often multiply-phrased coverage of exactly the facts that failed.
    Output: `handwritten_pairs/core_facts_pairs.jsonl` (66 pairs).

4. **`scripts/audit_pairs.py`** -- independent second-pass QC over completed campaign output,
   run after generation rather than during it. Re-checks backtick-quoted-identifier grounding,
   hedge phrases, loose numeric-claim grounding, and review shape sanity (0 or 1 pair per
   review chunk), then reports for manual review rather than auto-fixing. This does NOT replace
   manually spot-checking a random sample against real source text -- several real issues in
   this campaign (see below) were fluent, confident, and used no backticks or suspicious
   numbers, so they were invisible to every mechanical check and only caught by direct
   comparison against source.

5. **`scripts/assemble_sft_dataset.py`** -- merges everything in `pairs/**/*.jsonl` +
   `handwritten_pairs/**/*.jsonl` into the final training-ready dataset, standard
   `{"messages": [...]}` chat format. Filters hedge phrases and cross-pair boilerplate
   automatically. Output: `output/cubyz_sft_dataset.jsonl`. Safe to re-run any time.

6. **`training/prepare_training_data.py`** -- mixes the assembled Cubyz dataset with a sample of
   general instruction data (`teknium/OpenHermes-2.5`, default 1.0x the Cubyz volume -- lowered
   from an initial 1.5x once testing showed general capability had headroom to spare) to guard
   against catastrophic forgetting, then splits into `training/data/{train,val}.jsonl`.

7. **`training/train_qlora.py`** -- QLoRA fine-tune (4-bit NF4 base + bf16 LoRA adapters) of
   `Qwen/Qwen2.5-Coder-7B-Instruct`, sized for a 16GB card. See "Why QLoRA" below.

8. **`training/merge_adapter.py`** -- merges the trained adapter back into the base model for
   standalone inference/export (e.g. GGUF conversion for Ollama).

## Why QLoRA, not plain LoRA

Plain LoRA still loads the full frozen base at bf16 -- even at 7B that's ~14GB of weights alone,
too tight on a 16GB card (RX9070) once activations/optimizer state are added. QLoRA quantizes
the frozen base to 4-bit NF4 (~3.7GB at 7B), leaving generous headroom within 16GB.

**Model size note:** originally written for `Qwen/Qwen2.5-Coder-14B-Instruct` (QLoRA'd down to
~7.4GB of weights), but real training runs kept hitting CUDA OOM on this 16GB card even after
cutting `max_length` 4096→2048 and enabling `expandable_segments` -- ~12.4GB allocated at just
2048 tokens, more than weights + adapters should plausibly need. Likely LoRA's extra activation
overhead on the 14B model's large MLP layers, though never fully root-caused after several
rounds of debugging (device_map fixes, swap increases, sequence-length cuts). Dropped to the 7B
variant for a comfortable memory margin rather than continuing to chase it blind.

## Current state -- two training rounds complete, moving to merge + RAG-backed serving

Full generation campaign finished: 30/30 docs, 455/455 codebase, 649/649 reviews (2163 raw
pairs). **Round 1** (Qwen2.5-Coder-7B-Instruct, 2 epochs, 1.5x general ratio): `eval_loss` 0.885,
`eval_mean_token_accuracy` 78.5%. On the first 96-question grounded test
(`training/test_inference.py`): 23 correct (24%), 9 partial/vague (9%), 64 wrong (67%) --
including confident, specific fabrications (an invented `/heal` command contradicting the real
"you can't heal" fact, a fabricated creator name, a fabricated original project name). Critically,
**no catastrophic forgetting** on either round -- every general-capability question (code,
geography, math, hash tables) came back correct and coherent across all testing, confirming the
QLoRA + data-mixing approach met the project's core anti-lobotomy goal.

**Round 2** response to round 1's fact-recall gap: added `generate_core_facts_pairs.py` (66
densely-covered, often multiply-phrased pairs for exactly the facts that failed -- see step 3b
above), dropped the general:domain training ratio from 1.5x to 1.0x, and raised training from 2
to 3 epochs, all to increase how many times each specific fact is actually seen during training.
Assembled dataset grew to **2733 examples** (1938 codebase + 595 reviews + 183 docs + 17
addon_reference). Re-ran the identical 96-question test against the round-2 adapter: **26
correct (27%), 7 partial (7%), 63 wrong (66%)** -- only +3 percentage points net, despite the
targeted intervention. 7 of the previously-wrong facts were genuinely fixed (can't-heal, soil
tool, original name "Cubz", movement modes, missing-durability default, entity coordinate
system, regular-inventory key), but 3 previously-*correct* facts regressed to wrong (network
protocol, reversible-recipe limitation, ore-rotation failure behavior), and several facts given
**two separate dedicated training pairs** (creative-inventory key, server port, the 0.0.0 release
date) still came back wrong -- the 0.0.0 date came back with the exact same wrong value as
round 1, unchanged.

**Decision: stop iterating on standalone fact recall, move to merge + RAG-backed serving.**
Two full rounds of "add more targeted data, more epochs" produced a small net gain with real
regressions mixed in -- evidence this is hitting a genuine capacity/repetition ceiling for
LoRA-based fact injection at this scale (rank 16, ~5.5k examples, 3 epochs) rather than something
a third round reliably fixes. What the fine-tune *did* learn reliably and consistently across
both rounds is voice and judgment (review reasoning, debugging hypotheses) plus rock-solid general
capability -- exactly what a frozen knowledge base like RAG can't provide on its own. Next steps:
run `training/merge_adapter.py` to produce a standalone model, convert to GGUF, load into Ollama,
and point `local_rag_chat.py`'s `ANSWER_MODEL` at it (already updated to expect a model named
`cubyz-assistant`) so the fine-tuned model supplies voice/judgment while RAG's deterministic
retrieval supplies the facts it can't reliably hold on its own.

## Bugs found & fixed during verification (all applied to all 3 platform clients identically)

- **Stub-page hallucination** (docs): 4 near-empty wiki landing pages (e.g. `docs_docs_blocks_index.md`,
  just a title + one sentence) had confidently fabricated content ("dirt and stone," "bricks and
  glass," specific properties) baked into `wiki.jsonl` during the *original* RAG crunching
  campaign, long before this fine-tune pipeline existed -- meaning this was also live and wrong
  in the RAG knowledge base. Hand-corrected all 4 records to state only what's actually present,
  re-exported and re-uploaded to the live Open WebUI knowledge base.
- **`gameplay_controls.md` under-generation**: a legitimately rich source (a full keybinding
  table) was returning 0 pairs. Root cause: the crunched `comprehensive_explanation` described
  the table's existence ("categorizes controls into Movement, Blocks...") without ever stating
  the actual key mappings, so there was nothing for the generation model to ground specific
  answers in. Fixed by rewriting the record to state the actual mappings.
- **`symbols` excluded from grounding checks** (docs/codebase/reviews): `grounding_text_for()`
  never included the `symbols` field, which is itself verified (real identifiers from the
  original crunching, not model output). This caused the self-check to reject legitimate,
  correctly-quoted identifiers that only appeared in `symbols` and not in the prose fields --
  wasting massive compute on false-positive retries and, combined with a second bug (see next),
  causing failed chunks to loop forever instead of completing.
- **Failed chunks retried forever**: when a chunk failed validation 3x, the client just
  `continue`d without telling the server. The chunk's lock would expire (5 min) and it'd be
  handed back out again -- forever, for any deterministically-failing chunk. Fixed: the client
  now submits a 0-pairs result on final failure so the server marks it done.
- **Reviews: `raw_content` field never existed.** `github_reviews.jsonl` records never actually
  carried literal diff/comment text -- only `summary`/`comprehensive_explanation`/`symbols`/etc.
  Every review chunk was fed a prompt claiming "here is the raw diff" followed by an empty code
  block. Combined with an over-cautious "if too fragmentary, output `[]`" instruction, this
  caused 610/649 reviews (94%) to silently produce zero pairs -- including reviews with rich,
  multi-paragraph, clearly generalizable explanations. Fixed by presenting
  `comprehensive_explanation` honestly as the ground truth (not as a derivative of a diff the
  model isn't shown) and recalibrating the prompt's escape hatch to require an explicit,
  narrow trivial-nitpick pattern rather than any hint of uncertainty. Yield after the fix:
  92% (a 40-chunk validation sample went from 0/40 to 20/40 producing valid pairs before the
  full re-run; the full re-run hit 92%).
- **Confident fabrication that evaded every mechanical check** (found only via manual
  source comparison): a codebase pair invented a specific conditional formula
  (`CaveMapFragment.width*map.pos.voxelSize`, `max[0] >= 0`) with no basis in the source, using
  no backticks and no suspicious numbers -- undetectable by the grounding/numeric checks.
  Removed. A handful of review pairs built on `comprehensive_explanation` records that were
  themselves truncated mid-sentence (a pre-existing RAG-crunching bug specifically around Zig's
  `@"identifier"` escape syntax) either quoted the broken fragment verbatim or invented a
  plausible-sounding "why" to fill the gap left by the truncation. Removed (4 chunks affected).
  **Takeaway for future campaigns**: mechanical grounding checks catch quoted-identifier and
  hedge-phrase failures well, but a manual random-sample comparison against real source text is
  still necessary to catch fluent, confident, unquoted fabrication -- budget time for it.
