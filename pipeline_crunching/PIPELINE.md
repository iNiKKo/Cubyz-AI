# Cubyz Data Pipeline -- How To Use

End-to-end guide for taking new raw source material all the way through to "the live website can
answer questions about it," and separately through to "there's a fine-tuned model trained on it."
Written so this whole process can be repeated identically every time, not just remembered.

Two campaigns share this infrastructure -- **RAG** (knowledge extraction, feeds the live website)
and **finetune** (training-pair generation, feeds a QLoRA fine-tune). RAG always runs first.

---

## 1. Where does raw data go?

New source material -- a wiki page, a codebase file, an addon-creator doc -- goes into:

```
pipeline_crunching/organized_cubyz_dataset/{easy|medium|hard}/
```

Pick a tier based on how hard the content is to analyze correctly (`easy` = short/simple docs,
`hard` = dense code or long files) -- this controls which volunteers' hardware get handed the
chunk, not anything about correctness.

**Naming determines how it's classified** (see `_classify_role_context()` in `server_textual.py`):

| Filename starts with... | Treated as |
|---|---|
| `docs` | Wiki/documentation (`DEFINITIVE_WIKI_DOCUMENTATION`) |
| `codebase` | Engine source code (`FUNCTIONAL_CODEBASE_LOGIC`) |
| `addon_creator` | Addon Creator tooling (`ADDON_STUDIO_BLUEPRINTS`) |
| anything else | Falls back to extension: `.md`/`.txt`/`.html` -> wiki-like, everything else -> code-like |

So a new wiki-style doc about, say, a new game mechanic should be named
`docs_<something>.md` and placed in `easy/` (or `medium/` if it's long/dense). See
`docs_ashframe_overview.md` and `docs_automation_not_supported.md` in `easy/` for real examples.

**GitHub PR reviews are a special case** -- they don't go in as raw prose. Run
`archive/prototype_2_review_extraction/extract_reviews.py` (needs a `GITHUB_TOKEN` env var) to
pull PR review comments straight from GitHub into a pre-chunked JSON array
(`cubyz_reviews_dataset.json`), which gets placed as `reviews_reviews.json` in a tier folder
(currently `hard/`). The crunching scanner detects this by filename (`reviews*` or `*.json`) and
skips the normal line-splitting step entirely, since each entry is already one self-contained
review comment + diff.

## 2. Does the data need to be organized/chunked before running RAG folding?

**Only the placement above (tier + filename prefix) -- not the chunking itself.** Drop the whole
raw file in; `rag_initialize_chunks()` (runs automatically every time `server_textual.py` starts) splits
it into 150-line chunks with 30-line overlap and queues them. You never manually pre-split a doc.

The one thing that *does* need to be correct before you drop a file in: it should read like an
actual wiki page (clear, factual prose) -- the crunching prompt has a "zero extrapolation" rule
and will only extract what's explicitly stated, so vague or padded source text produces a
vague/padded chunk.

**The server only re-scans at startup.** If you add a new raw file while the server is already
running, restart it to pick the new file up (or extend `/admin/mode` later if live re-scanning
becomes worth building -- not there today).

## 3. Run RAG folding

1. Start (or restart) `pipeline_crunching/server_textual.py`. It scans `organized_cubyz_dataset/`
   and queues any new/changed chunks automatically. On a real terminal this opens the textual
   admin console directly (no more numbered startup menu) -- pick **RAG** from the sidebar's
   Campaign Mode selector. The header panel shows live progress (`completed/total (pct%)`) so you
   can see how much is left. (Piped/non-interactive output, e.g. systemd, still falls back to the
   old `server_startup_gate()` numbered menu since there's no console to pick a mode with there.)
2. Run `CUBYZ_FOLDING.py` (any volunteer machine, or your own) -- it auto-detects RAG mode from
   the server and starts crunching. Output lands in `users/<user_id>/{wiki,codebase,addon_studio,github_reviews}.jsonl`.
3. Repeat/leave running until the admin console's header progress bar shows the RAG queue fully
   complete (or check `GET /leaderboard`).

## 4. Fine-tune folding only runs after RAG folding is done

This is now enforced, not just a convention to remember:

- Selecting **FINETUNE** from the admin console's sidebar Campaign Mode selector while RAG isn't
  finished refuses the switch and shows the real `X/Y` count as a red hint under the selector,
  reverting the radio button back to the current mode (`on_radio_set_changed` in
  `server_textual.py`, which just calls the same `set_mode()` the HTTP endpoint uses underneath).
- The live `POST /admin/mode?mode=finetune` endpoint returns `409 Conflict` under the same
  condition unless you pass `force=true`.

**Why:** finetune pair generation reads from RAG's own output (`users/*/wiki.jsonl`, the
architectural codebase subset, `users/*/github_reviews.jsonl` -- see `finetune/README.md`), so
running it against a half-finished RAG campaign means training pairs get generated from
incomplete/inconsistent source data.

Once RAG is done, select **FINETUNE** in the sidebar and run `CUBYZ_FOLDING.py` again -- same
client, it follows whatever mode the server is in. Output lands in
`pairs/<user_id>/<source_type>_pairs.jsonl`.

## 5. What's the next step? Publishing crunched RAG output to the live site

This is the piece that was missing until now: crunching a chunk only writes to
`users/*/wiki.jsonl` etc. -- **nothing automatically turns that into what the live website
retrieves from.** After a RAG crunching session (or any time you want to publish what's been
crunched so far, even mid-campaign):

```bash
python3 pipeline_crunching/build_knowledge_base.py
```

This reads every `users/*/{wiki,codebase,addon_studio,github_reviews}.jsonl`, and writes/updates
one `.md` file per chunk into `knowledge_base/{docs,codebase,addon_creator,reviews}/` -- the exact
format `webapp/local_rag_chat.py` embeds and retrieves from. It's safe to re-run any time:
unchanged chunks are left alone, only new or changed ones are written, and it reports
`X new, Y updated, Z unchanged` each run.

**It never deletes.** `users/` empties out on every campaign hard reset (by design -- see
`rag_execute_hard_reset()`), but the knowledge base accumulates permanently across every campaign
run, the same way leaderboard stats do. A chunk missing from `users/` right now because its
campaign was just reset does not mean it should vanish from the live site.

Then, to actually serve the new/updated content:

```bash
cd webapp
python3 local_rag_chat.py --rebuild "test question"    # rebuilds the embedding cache once
```

or just restart `webapp/chat_server.py` -- its own startup already re-checks the cache against
the current file set (an exact content comparison, not just a count) and rebuilds automatically
if anything changed.

## 6. Finetune folding's next steps (training)

Once finetune pairs are generated, the rest of the pipeline is already fully documented in
`finetune/README.md` (stages 4-8: `audit_pairs.py` for QC, `assemble_sft_dataset.py` to merge
everything into the final training set, `prepare_training_data.py` to mix in general instruction
data, `train_qlora.py`, then `merge_adapter.py` + GGUF conversion + `ollama create` to produce the
`cubyz-assistant` model `local_rag_chat.py` actually talks to). That part of the pipeline doesn't
change here -- this guide's job was steps 1-5, which is where the RAG side actually connects to
what's live.

## Full pipeline, start to finish

```
1. Add raw source file -> organized_cubyz_dataset/{tier}/docs_*.md (or codebase_*/addon_creator_*)
2. Restart pipeline_crunching/server_textual.py -> auto-scans, auto-chunks, queues new work
3. Admin console sidebar: select RAG -> run CUBYZ_FOLDING.py until RAG queue is complete
4. python3 pipeline_crunching/build_knowledge_base.py -> publishes to knowledge_base/
5. Restart webapp/chat_server.py (or --rebuild) -> live site now answers from the new content
6. Admin console sidebar: select FINETUNE (blocked/warned if step 3 isn't actually done)
   -> run CUBYZ_FOLDING.py until finetune queue is complete
7. finetune/README.md stages 4-8 -> audit, assemble, mix, train, merge, deploy
```

Steps 1-5 are the RAG loop and can be repeated as often as you like (add more docs, re-publish).
Step 6 only happens once per RAG campaign, after it's actually finished.
