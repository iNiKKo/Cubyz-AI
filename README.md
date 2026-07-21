# ASH AI

A local AI assistant that knows the [Cubyz](https://github.com/PixelGuys/Cubyz) codebase and
community — engine internals, keybindings, addon-creator tooling, PR review history — without
losing general competence. RAG retrieval + a QLoRA fine-tune, fed by a distributed,
volunteer-powered crunching pipeline.

---

## What's in this repo

### Client — `pipeline_crunching/client.py`
Donates spare compute to whichever campaign is active.
- Connects to the server, crunches assigned work with local Ollama, submits results
- Auto-detects hardware and picks a model that fits; auto-updates itself
- Runs multiple lanes at once when hardware allows (GPU + CPU, or parallel workers)

### Server — `pipeline_crunching/server.py`
The coordinator.
- Scans source material, chunks it, hands out work, tracks stats/leaderboard
- Switches between RAG / Finetune / Audit campaigns live, no restart needed
- **Data Sync** panel: one-click buttons to pull the latest Cubyz codebase, PR reviews/issues,
  publish crunched output to the knowledge base, and pull an audit report

---

## Current stage

- **RAG:** complete, 3,318 chunks, live on the webapp.
- **Fine-tune:** `ASH-P7-4B` (`Qwen3-4B-Instruct-2507`) — 22.9% standalone, **99.0-99.3% served
  with RAG** across two independent 144-question sets. Fine-tune data is `reviews`-only
  (judgment/voice, not facts) since Prototype 7 — RAG carries all fact recall.
- **Audit:** complete (3,247/3,247), re-runs automatically as chunks change.
- **Infra:** one client, one server — `pipeline_crunching/` holds just those two files. Old/dup
  versions and superseded scripts archived, not deleted.

**Open items:** RAG retrieval efficiency (fewer chunks pulled before landing on the right one);
client/server auto-wiring for new fine-tune rounds; `/disconnect`'s missing auth (known).

**[Live model leaderboard](https://claude.ai/code/artifact/4def066b-3b7d-4ef2-97ac-779689b6d7a4)**
— ranked domain-fact accuracy for every fine-tuned model.

---

## History

One line per round — full narrative/lessons-learned for each lives in git history and `archive/`.

| Prototype | Approach | Outcome |
|---|---|---|
| 1 | Fine-tune only | Lobotomized, unusable (catastrophic forgetting) |
| 2 | RAG only, single-file KB | Facts good, code examples wrong |
| 3 | Distributed crunching | 1,134 chunks, bigger KB (fact-loss bug found later) |
| 4 | Fine-tune + RAG hybrid | 89% on a 96-question benchmark |
| 5 | Consolidation, regression hunt, TUI rewrite | 95.8% on expanded 144Q benchmark; audit mode added |
| 6 | Model-size experiments | Qwen3.5 GPU-crashed (ROCm-incompatible); `P6-4B` reached 91.7% deployed |
| 7 | Behavior-only fine-tune + RAG chunking fixes | `P7-4B` reached 99.0-99.3% deployed on 63% less training data |

