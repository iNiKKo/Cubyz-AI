# Cubyz-AI — Memory & Technical Documentation

This document maintains key architectural details, historical decisions, server/client protocol specifications, and recent session progress notes for the Cubyz-AI project.

---

## 1. System Architecture Overview

Cubyz-AI is a hybrid local LLM system combining fine-tuning (for developer voice, code reviews, and reasoning) with RAG (Retrieval-Augmented Generation for hard engine facts, keybindings, and specifications).

- **Coordinator Server:** Located in `pipeline_crunching/server_textual.py`. Manages campaign modes (`rag`, `finetune`, `audit`, `idle`), work assignment, lock files, leaderboard stats, and volunteer node tracking. Built with FastAPI and Textual TUI.
- **Volunteer Client:** Located in `CUBYZ_FOLDING.py` and `CUBYZ_FOLDING_TUI.py` (v1.3.0). Runs on volunteer hardware (GPU/CPU) via local Ollama instances. Uses Textual TUI for multi-lane execution (Primary GPU/CPU, Secondary Dual-Lane CPU, and Parallel Worker pool `P1`, `P2`, etc.).

---

## 2. Server/Client Protocol & Endpoints

- `GET /get_work?user_id=...&hardware_tier=...&model=...&client_version=...&available_models=...&avg_task_seconds=...&lane=...`
  - Returns current mode (`rag`, `finetune`, `audit`, `idle`), task payload, total chunks, completed chunks, and ETA.
  - Rejects clients lower than `MIN_CLIENT_VERSION` with HTTP 426.
- `POST /submit_work`
  - Submits completed chunk processing results or audit proposals/reviews.
- `POST /disconnect?user_id=...&lane=...`
  - Instantly zeroes out the node's timestamp in `online_clients` so the server dashboard renders it as offline immediately on graceful client exit.
- `GET /version`
  - Returns `min_client_version`, `latest_client_version`, and `download_url`.
- `POST /rename_user?old_user_id=...&new_user_id=...`
  - Migrates volunteer history, stats, and hardware records to a new identity.
- `POST /delete_user?user_id=...`
  - Purges volunteer stats, hardware info, and releases any held task locks.

---

## 3. Client Capabilities & Multi-Lane Architecture

- **Primary Lane:** Auto-detects hardware (NVIDIA via `nvidia-smi`, AMD via ROCm/sysfs/lspci, Apple Silicon via `sysctl`, or CPU fallback) and queries actual model names (e.g. `AMD Radeon RX 9070/9070 XT`, `AMD Ryzen 5 9600X`).
- **Dual-Lane Mode:** Spawns a secondary CPU lane alongside the GPU lane when system RAM >= 12 GB and VRAM >= 4 GB.
- **Parallel Worker Pool (`P1`, `P2`...):** Runs multiple concurrent requests against Ollama (`OLLAMA_NUM_PARALLEL`). Headroom check (`check_headroom()`) validates:
  - `hard` tier: VRAM floor 8.5 GB + 3.5 GB per worker (2 workers) = 15.5 GB required.
  - `medium` tier: VRAM floor 4.5 GB + 2.0 GB per worker (2 workers).
  - `easy` tier: VRAM floor 0.0 GB + 1.0 GB per worker (3 workers).
- **Auto-Bootstrapper:** Imports `textual` and `rich` inside a `try...except ImportError` block that automatically runs `pip install textual rich` using multiple environment flags (`--user`, `--break-system-packages`) if missing on a new system.
- **Auto-Updater & Version Handling:** Fully integrates `check_for_update()`, `download_update()`, and `offer_update()`. On HTTP 426 or version mismatch, automatically fetches `download_url`, verifies version tag, overwrites local script, and calls `os.execv()` to restart process seamlessly.
- **Docker Ollama Verification:** Checks model availability using HTTP `GET /api/tags` and `POST /api/pull` to avoid CLI `FileNotFoundError` when Ollama is running inside Docker containers.

---

## 4. Recent Progress Notes (v1.3.0 Migration)

1. **Client TUI Rewrite (`CUBYZ_FOLDING_TUI.py` & `CUBYZ_FOLDING.py`):**
   - Converted client to full Textual TUI interface with sidebar navigation, live global status header, lane cards, log viewer, and prompt input box.
   - Auto-detects and displays exact GPU and CPU model names.
   - Restored complete auto-updater pipeline (`check_for_update`, `download_update`, `offer_update`, HTTP 426 exception handler).
   - Fully integrated production processing logic for RAG, FINETUNE, and AUDIT modes.
   - Added `_notify_server_disconnect()` to send `POST /disconnect` on exit for all active lanes.
   - Fixed IDLE mode display to show `No tasks (idle)` on status cards and `N/A` for ETA.
   - Fixed parallel worker VRAM headroom constants to match 15.9 GB GPUs.

2. **Server TUI Updates (`pipeline_crunching/server_textual.py`):**
   - Restored full 4-lane display (`GPU`, `CPU`, `P1`, `P2`) in the connections panel.
   - Added live machine **Contribution %** calculation relative to total network processing throughput.
   - Added `POST /disconnect` route (supporting GET & POST methods).
   - Dynamically calculates audit progress and ETA based on `AUDIT_LOCK_FILE` and action timing logs.
   - Bumped `MIN_CLIENT_VERSION` and `LATEST_CLIENT_VERSION` to `1.3.0` to force auto-update across the volunteer network.
