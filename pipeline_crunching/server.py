import os
import sys
import json
import time
import shutil
import hashlib
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

app = FastAPI(title="Cubyz Distributed Dataset Coordinator")

# ============================================================
# This server used to be two separate processes (this file, RAG-only, and
# finetune/server_finetune.py) that happened to both bind port 7000 -- meaning only one could
# ever run at a time anyway. Merged into one process that runs BOTH campaigns' state side by
# side and switches which one is being served via CURRENT_MODE, matching what
# CUBYZ_FOLDING.py (the unified client) expects: a "mode" field on /get_work telling it whether
# to do RAG extraction, fine-tune pair generation, or nothing (idle).
#
# RAG and fine-tune chunk_ids are NOT interchangeable even though they can be equal as strings
# -- a fine-tune chunk_id is literally copied from an already-completed RAG chunk_id, so treating
# them as the same lock/completion namespace would be wrong. Their queues, lock files, stats
# files, and hash databases stay fully separate; only the HTTP surface and the online-clients
# roster are unified.
# ============================================================

PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PIPELINE_ROOT)
FINETUNE_ROOT = os.path.join(REPO_ROOT, "finetune")

# --- RAG campaign paths (unchanged from this file's pre-merge state) ---
RAG_SOURCE_DIR = os.path.join(PIPELINE_ROOT, "organized_cubyz_dataset") + os.sep
USERS_DIR = os.path.join(REPO_ROOT, "users")
RAG_LOCK_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "lock_state.json")
RAG_STATS_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "user_stats.json")
RAG_HASH_DB_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "file_hashes.json")
RAG_BACKUP_DIR = os.path.join(REPO_ROOT, "archive", "rag_crunching_campaign_backups")

# --- Fine-tune campaign paths (unchanged from finetune/server_finetune.py's pre-merge state) ---
FINETUNE_DOCS_SOURCE = USERS_DIR  # reads wiki.jsonl from every volunteer
FINETUNE_CODEBASE_SUBSET_FILE = os.path.join(FINETUNE_ROOT, "source_data", "codebase_architectural_subset.jsonl")
FINETUNE_REVIEWS_SOURCE = USERS_DIR  # reads github_reviews.jsonl from every volunteer
FINETUNE_OUTPUT_DIR = os.path.join(FINETUNE_ROOT, "pairs")
FINETUNE_LOCK_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "lock_state.json")
FINETUNE_STATS_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "user_stats.json")
FINETUNE_HASH_DB_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "file_hashes.json")
FINETUNE_BACKUP_DIR = os.path.join(REPO_ROOT, "archive", "finetune_campaign_backups")

TASK_TIMEOUT = 300

# A chunk this short (same threshold the client uses to cap synthetic_queries) doesn't carry
# enough genuine content for small local models to extract from without fabricating -- verified live
# against qwen2.5-coder:3b/7b/14b: only the 14b tier stayed fully grounded on chunks this thin.
THIN_CONTENT_CHAR_THRESHOLD = 400
MODEL_TIER_RANK = {
    "qwen2.5-coder:3b": 1,
    "qwen2.5-coder:7b": 2,
    "qwen2.5-coder:14b": 3,
    "qwen3-coder:30b": 4,
}
THIN_CHUNK_MIN_TIER = 3  # requires a qwen2.5-coder:14b-or-better client

# ============================================================
# CLIENT VERSIONING -- old clients (the archived per-OS scripts, RAG_FOLDING.py,
# FINETUNE_FOLDING.py) don't send a client_version at all and don't understand the "mode"
# field this server now returns; letting them through would silently misdispatch work to them.
# get_work/submit_work reject anything below MIN_CLIENT_VERSION with HTTP 426 and a message
# telling the operator to update, rather than accepting and mishandling it.
# ============================================================
MIN_CLIENT_VERSION = "1.0.0"
LATEST_CLIENT_VERSION = "1.1.1"
CLIENT_DOWNLOAD_URL = "https://raw.githubusercontent.com/iNiKKo/Cubyz-AI/main/CUBYZ_FOLDING.py"

def _parse_version(v: str) -> tuple:
    try:
        return tuple(int(p) for p in v.strip().split("."))
    except Exception:
        return (0,)

def _version_rejection_message(client_version: str) -> str:
    return (
        f"Your client is out of date (sent version '{client_version or 'none'}', server requires "
        f">= {MIN_CLIENT_VERSION}). You must update to the new version. Download: {CLIENT_DOWNLOAD_URL}"
    )

# "idle": server up, no campaign handing out work. Set at startup via server_startup_gate() and
# switchable afterward without restarting via POST /admin/mode?mode=idle|rag|finetune.
CURRENT_MODE = "idle"
SERVER_STATE_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "server_mode_state.json")

rag_chunk_queue = []
finetune_chunk_queue = []
online_clients = {}  # unified roster -- one client identity now, regardless of which mode it's working in


class RAGNode(BaseModel):
    chunk_id: str
    summary: str
    comprehensive_explanation: str
    symbols: List[str] = []
    concepts: List[str] = []
    keywords: List[str] = []
    chunk_type: Optional[str] = None
    code_example: Optional[str] = None
    synthetic_queries: List[str]
    title: str
    user_id: str = Field(..., min_length=3, max_length=9, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0


class FinetunePairsSubmission(BaseModel):
    chunk_id: str
    source_type: str  # docs | codebase | reviews
    pairs: List[dict]  # [{"instruction": ..., "response": ...}, ...]
    user_id: str = Field(..., min_length=3, max_length=9, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0


class UnifiedSubmission(BaseModel):
    # "mode" defaults to "rag" so an old, not-yet-updated RAG-only client (which never sends this
    # field) still submits correctly as long as the server happens to be in RAG mode -- the same
    # spirit as CUBYZ_FOLDING.py defaulting an absent /get_work "mode" to "rag".
    mode: Literal["rag", "finetune"] = "rag"
    client_version: str = ""  # absent (old client) is treated the same as "0.0.0" -- see _parse_version
    chunk_id: str
    user_id: str = Field(..., min_length=3, max_length=9, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0
    # RAG-mode fields
    summary: Optional[str] = None
    comprehensive_explanation: Optional[str] = None
    symbols: List[str] = []
    concepts: List[str] = []
    keywords: List[str] = []
    chunk_type: Optional[str] = None
    code_example: Optional[str] = None
    synthetic_queries: List[str] = []
    title: Optional[str] = None
    # Fine-tune-mode fields
    source_type: Optional[str] = None
    pairs: List[dict] = []


def read_json_file(path: str, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def write_json_file(path: str, data, label: str = "file"):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[X] Failed to write {label} to disk: {e}")

def load_lock_state(path: str) -> dict:
    return read_json_file(path, {"locked": {}, "completed": []})

def save_lock_state(path: str, state: dict):
    write_json_file(path, state, "lock state")

def load_user_stats(path: str) -> dict:
    return read_json_file(path, {})

def save_user_stats(path: str, stats: dict):
    write_json_file(path, stats, "user stats")

def load_server_mode_state() -> dict:
    return read_json_file(SERVER_STATE_FILE, {"mode": "idle", "clean_shutdown": True})

def save_server_mode_state(mode: str, clean_shutdown: bool):
    write_json_file(SERVER_STATE_FILE, {"mode": mode, "clean_shutdown": clean_shutdown}, "server mode state")

def prune_stale_locks(state: dict) -> bool:
    now = time.time()
    stale_keys = [
        chunk_id for chunk_id, info in state["locked"].items()
        if now - info["timestamp"] > TASK_TIMEOUT
    ]
    for key in stale_keys:
        stale_info = state["locked"].pop(key)
        print(f"[!] Task '{key}' timed out from user '{stale_info['user_id']}'. Released back to queue.")
    return bool(stale_keys)

# ============================================================
# RAG CAMPAIGN -- chunk ingestion, hard reset (unchanged logic from the pre-merge server.py,
# except execute_hard_reset's backup copy now uses os.path.basename()/a literal "users" name
# when joining onto session_backup -- the original passed the source's own ABSOLUTE path as the
# second os.path.join() argument, which Python discards all prior components for, so every
# "backup" copy was actually just the file copied onto itself and never actually landed in
# session_backup at all. finetune/server_finetune.py's equivalent code already used the correct
# pattern; this merge adopts that version for both campaigns.
# ============================================================

def rag_initialize_empty_state():
    # RAG_STATS_FILE (per-user chunks_completed/lines_crunched -- the leaderboard) is deliberately
    # left untouched here: a hard reset clears the campaign so chunks can be redone (e.g. after a
    # crunching-prompt fix), but a volunteer's lifetime contribution total should never drop back
    # to 0 just because the campaign queue was rebuilt.
    for f in (RAG_LOCK_FILE, RAG_HASH_DB_FILE):
        if os.path.exists(f):
            os.remove(f)
    if os.path.exists(USERS_DIR):
        shutil.rmtree(USERS_DIR)
    os.makedirs(USERS_DIR, exist_ok=True)

    save_lock_state(RAG_LOCK_FILE, {"locked": {}, "completed": []})
    write_json_file(RAG_HASH_DB_FILE, {}, "hash db")
    print("\n[✓] RAG campaign structures initialized back to 0 (contribution stats preserved).")

def rag_execute_hard_reset():
    print("\n[!] Initializing RAG System Hard Reset & Backup Sequence...")
    os.makedirs(RAG_BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_backup = os.path.join(RAG_BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(session_backup, exist_ok=True)

    files_backed_up = 0
    for f in (RAG_LOCK_FILE, RAG_STATS_FILE, RAG_HASH_DB_FILE):
        if os.path.exists(f):
            shutil.copy2(f, os.path.join(session_backup, os.path.basename(f)))
            files_backed_up += 1

    if os.path.exists(USERS_DIR) and os.listdir(USERS_DIR):
        shutil.copytree(USERS_DIR, os.path.join(session_backup, "users"), dirs_exist_ok=True)
        files_backed_up += 1

    if files_backed_up > 0:
        print(f"[✓] Successfully archived RAG session data to: {session_backup}")
    else:
        print("[~] No historical RAG operational data found to archive.")

    rag_initialize_empty_state()

def calculate_file_hash(file_path: str) -> str:
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while block := f.read(8192):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception:
        return ""

def _is_chunk_set_unchanged(file_chunks: list, file: str, f_hash: str, old_hashes: dict, completed_chunks: set) -> bool:
    all_completed = len(file_chunks) > 0 and all(c["chunk_id"] in completed_chunks for c in file_chunks)
    return file in old_hashes and old_hashes[file] == f_hash and all_completed

def _classify_role_context(file_lower: str, tier_path: str) -> str:
    if file_lower.startswith("docs"):
        return "DEFINITIVE_WIKI_DOCUMENTATION"
    elif file_lower.startswith("codebase"):
        return "FUNCTIONAL_CODEBASE_LOGIC"
    elif file_lower.startswith("addon_creator") or "addon" in tier_path.lower():
        return "ADDON_STUDIO_BLUEPRINTS"
    else:
        is_wiki_ext = file_lower.endswith(('.md', '.txt', '.html'))
        return "DEFINITIVE_WIKI_DOCUMENTATION" if is_wiki_ext else "FUNCTIONAL_CODEBASE_LOGIC"

def rag_initialize_chunks():
    chunk_size, overlap = 150, 30
    step = chunk_size - overlap

    if not os.path.exists(RAG_SOURCE_DIR):
        print(f"[X] Error: Organized source workspace not found at '{RAG_SOURCE_DIR}'!")
        sys.exit(1)

    lock_state = load_lock_state(RAG_LOCK_FILE)
    completed_chunks = set(lock_state.get("completed", []))
    old_hashes = read_json_file(RAG_HASH_DB_FILE, {})

    current_hashes = {}
    skipped_unchanged_count = 0
    total_scanned_files = 0

    for tier in ["easy", "medium", "hard"]:
        tier_path = os.path.join(RAG_SOURCE_DIR, tier)
        if not os.path.exists(tier_path):
            continue

        for file in os.listdir(tier_path):
            file_path = os.path.join(tier_path, file)
            if not os.path.isfile(file_path):
                continue

            total_scanned_files += 1
            f_hash = calculate_file_hash(file_path)
            current_hashes[file] = f_hash

            try:
                if file.lower().endswith('.json') or file.lower().startswith('reviews'):
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        review_array = json.load(f)

                    file_chunks = []
                    for review_item in review_array:
                        review_raw_content = review_item.get("raw_content", "")
                        file_chunks.append({
                            "chunk_id": review_item.get("chunk_id"),
                            "file_name": review_item.get("file_name", "unknown.zig"),
                            "relative_path": review_item.get("relative_path", "unknown_path"),
                            "directory_context": f"{tier} | GITHUB_REVIEWS",
                            "chunk_index": review_item.get("chunk_index", 0),
                            "difficulty": tier,
                            "raw_content": review_raw_content,
                            "requires_strong_model": len(review_raw_content) < THIN_CONTENT_CHAR_THRESHOLD
                        })

                    if _is_chunk_set_unchanged(file_chunks, file, f_hash, old_hashes, completed_chunks):
                        skipped_unchanged_count += 1
                        continue

                    rag_chunk_queue.extend(file_chunks)

                else:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()

                    isolated_role_context = _classify_role_context(file.lower(), tier_path)

                    file_chunks = []
                    idx = 0
                    for i in range(0, len(lines), step):
                        chunk_lines = lines[i:i + chunk_size]
                        chunk_raw_content = "".join(chunk_lines)
                        file_chunks.append({
                            "chunk_id": f"{file}_chunk_{idx}",
                            "file_name": file,
                            "relative_path": f"{tier}/{file}",
                            "directory_context": f"{tier} | {isolated_role_context}",
                            "chunk_index": idx,
                            "difficulty": tier,
                            "raw_content": chunk_raw_content,
                            "requires_strong_model": len(chunk_raw_content) < THIN_CONTENT_CHAR_THRESHOLD
                        })
                        idx += 1
                        if i + chunk_size >= len(lines):
                            break

                    if _is_chunk_set_unchanged(file_chunks, file, f_hash, old_hashes, completed_chunks):
                        skipped_unchanged_count += 1
                        continue

                    rag_chunk_queue.extend(file_chunks)

            except Exception as e:
                print(f"[!] Error parsing file entry {file}: {e}")

    write_json_file(RAG_HASH_DB_FILE, current_hashes, "hash db")
    os.makedirs(USERS_DIR, exist_ok=True)

    print("\n" + "─"*55)
    print("               RAG PIPELINE METRICS                   ")
    print("─"*55)
    print(f" 📂 Total Workspace Files Found:  {total_scanned_files}")
    print(f" ⏭️ Bypassed (Fully Completed):   {skipped_unchanged_count}")
    print(f" 🔥 Active Task Targets Queued:   {len(rag_chunk_queue)}")
    print("─"*55 + "\n")

# ============================================================
# FINE-TUNE CAMPAIGN -- chunk ingestion, hard reset (unchanged logic from the pre-merge
# finetune/server_finetune.py).
# ============================================================

def finetune_initialize_empty_state():
    # FINETUNE_STATS_FILE (per-user chunks_completed/pairs_generated -- the leaderboard) is
    # deliberately left untouched here, same reasoning as rag_initialize_empty_state(): the
    # campaign queue resets, but lifetime contribution totals never should.
    for f in (FINETUNE_LOCK_FILE, FINETUNE_HASH_DB_FILE):
        if os.path.exists(f):
            os.remove(f)
    if os.path.exists(FINETUNE_OUTPUT_DIR):
        shutil.rmtree(FINETUNE_OUTPUT_DIR)
    os.makedirs(FINETUNE_OUTPUT_DIR, exist_ok=True)

    save_lock_state(FINETUNE_LOCK_FILE, {"locked": {}, "completed": []})
    write_json_file(FINETUNE_HASH_DB_FILE, {}, "hash db")
    print("\n[OK] Fine-tune campaign structures initialized back to 0 (contribution stats preserved).")

def finetune_execute_hard_reset():
    print("\n[!] Initializing Fine-Tune System Hard Reset & Backup Sequence...")
    os.makedirs(FINETUNE_BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_backup = os.path.join(FINETUNE_BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(session_backup, exist_ok=True)

    files_backed_up = 0
    for f in (FINETUNE_LOCK_FILE, FINETUNE_STATS_FILE, FINETUNE_HASH_DB_FILE):
        if os.path.exists(f):
            shutil.copy2(f, os.path.join(session_backup, os.path.basename(f)))
            files_backed_up += 1
    if os.path.exists(FINETUNE_OUTPUT_DIR) and os.listdir(FINETUNE_OUTPUT_DIR):
        shutil.copytree(FINETUNE_OUTPUT_DIR, os.path.join(session_backup, "pairs"), dirs_exist_ok=True)
        files_backed_up += 1

    if files_backed_up > 0:
        print(f"[OK] Archived fine-tune session data to: {session_backup}")
    else:
        print("[~] No historical fine-tune operational data found to archive.")
    finetune_initialize_empty_state()

def calculate_content_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode("utf-8")).hexdigest()

def load_deduped_jsonl(paths):
    seen = set()
    entries = []
    for path in paths:
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                except Exception:
                    continue
                if chunk["chunk_id"] in seen:
                    continue
                seen.add(chunk["chunk_id"])
                entries.append(chunk)
    return entries

def finetune_initialize_chunks():
    if not os.path.exists(FINETUNE_CODEBASE_SUBSET_FILE):
        print(f"[X] {FINETUNE_CODEBASE_SUBSET_FILE} not found. Run filter_codebase_subset.py first.")
        sys.exit(1)

    lock_state = load_lock_state(FINETUNE_LOCK_FILE)
    completed_chunks = set(lock_state.get("completed", []))
    old_hashes = read_json_file(FINETUNE_HASH_DB_FILE, {})
    current_hashes = {}

    docs_paths = [os.path.join(FINETUNE_DOCS_SOURCE, u, "wiki.jsonl") for u in os.listdir(FINETUNE_DOCS_SOURCE)] if os.path.exists(FINETUNE_DOCS_SOURCE) else []
    docs_entries = load_deduped_jsonl(docs_paths)

    review_paths = [os.path.join(FINETUNE_REVIEWS_SOURCE, u, "github_reviews.jsonl") for u in os.listdir(FINETUNE_REVIEWS_SOURCE)] if os.path.exists(FINETUNE_REVIEWS_SOURCE) else []
    review_entries = load_deduped_jsonl(review_paths)

    codebase_entries = load_deduped_jsonl([FINETUNE_CODEBASE_SUBSET_FILE])

    skipped_unchanged = 0
    for source_type, entries in (("docs", docs_entries), ("codebase", codebase_entries), ("reviews", review_entries)):
        for entry in entries:
            content_hash = calculate_content_hash(entry)
            current_hashes[entry["chunk_id"]] = content_hash

            if (entry["chunk_id"] in completed_chunks and
                    old_hashes.get(entry["chunk_id"]) == content_hash):
                skipped_unchanged += 1
                continue

            finetune_chunk_queue.append({
                "chunk_id": entry["chunk_id"],
                "source_type": source_type,
                "record": entry,
            })

    write_json_file(FINETUNE_HASH_DB_FILE, current_hashes, "hash db")
    os.makedirs(FINETUNE_OUTPUT_DIR, exist_ok=True)

    print("\n" + "─"*55)
    print("            FINE-TUNE PIPELINE METRICS                ")
    print("─"*55)
    print(f" Docs candidates:       {len(docs_entries)}")
    print(f" Codebase candidates:   {len(codebase_entries)}")
    print(f" Review candidates:     {len(review_entries)}")
    print(f" Bypassed (unchanged):  {skipped_unchanged}")
    print(f" Active task targets:   {len(finetune_chunk_queue)}")
    print("─"*55 + "\n")

def _rag_campaign_complete() -> bool:
    # An empty queue (RAG source not configured/scanned) counts as "complete" -- nothing to
    # block on. Real incompleteness is completed < total with a nonzero total.
    total = len(rag_chunk_queue)
    if total == 0:
        return True
    state = load_lock_state(RAG_LOCK_FILE)
    return len(state["completed"]) >= total

# ============================================================
# STARTUP GATE -- picks the initial CURRENT_MODE. Both campaigns' chunk queues are always built
# regardless of which mode is chosen, so /admin/mode can switch live without a restart.
# ============================================================

def server_startup_gate():
    global CURRENT_MODE

    # If the last run's mode change was never followed by a clean shutdown (crash, kill -9,
    # power loss -- anything that skipped the finally block in __main__), flag it here instead
    # of silently forgetting what was running. Doesn't auto-resume -- the operator still has to
    # pick it -- just makes it obvious that campaign was mid-run when the server last stopped.
    persisted = load_server_mode_state()
    unfinished_mode = persisted.get("mode") if not persisted.get("clean_shutdown", True) and persisted.get("mode") in ("rag", "finetune") else None
    rag_flag = "  ⚠ was still running when the server last stopped -- resume?" if unfinished_mode == "rag" else ""
    finetune_flag = "  ⚠ was still running when the server last stopped -- resume?" if unfinished_mode == "finetune" else ""

    rag_total = len(rag_chunk_queue)
    rag_done = len(load_lock_state(RAG_LOCK_FILE)["completed"])
    rag_progress = f"  [{rag_done}/{rag_total} chunks]" if rag_total else ""
    finetune_not_ready = "  ⚠ RAG campaign not finished yet -- see note below" if not _rag_campaign_complete() else ""

    print("\n" + "═"*55)
    print("        CUBYZ DISTRIBUTED DATASET ENGINE COORDINATOR      ")
    print("═"*55)
    print(f"  [1] 🟢 LAUNCH IN RAG MODE           (knowledge extraction){rag_flag}{rag_progress}")
    print(f"  [2] 🟢 LAUNCH IN FINETUNE MODE      (training-pair generation){finetune_flag}{finetune_not_ready}")
    print("  [3] 🟢 LAUNCH IN IDLE MODE          (server up, no tasks handed out)")
    print("  [4] ⚠️ HARD RESET RAG CAMPAIGN       (wipe queue & database to 0 -- contribution stats kept)")
    print("  [5] ⚠️ HARD RESET FINETUNE CAMPAIGN  (wipe queue & pairs to 0 -- contribution stats kept)")
    print("  [6] ⚠️ HARD RESET BOTH CAMPAIGNS     (wipe both queues to 0 -- contribution stats kept)")
    print("  [7] 🛑 SHUTDOWN ENGINE")
    print("═"*55)
    print("  Mode can be switched later without restarting: POST /admin/mode?mode=idle|rag|finetune")
    print("═"*55)

    while True:
        try:
            choice = input("Select command index (1-7): ").strip()
            if choice == "1":
                CURRENT_MODE = "rag"
                print("\n[➔] Access Authorized. Launching in RAG mode...")
                break
            elif choice == "2":
                if not _rag_campaign_complete():
                    confirm = input(
                        f"\n⚠️ RAG campaign is not finished yet ({rag_done}/{rag_total} chunks). "
                        f"Fine-tune pair generation is meant to run after RAG extraction is done -- "
                        f"pair quality depends on the RAG knowledge base being complete. Launch in "
                        f"FINETUNE mode anyway? (y/n): "
                    ).strip().lower()
                    if confirm != 'y':
                        print("[~] Staying at menu -- finish the RAG campaign first, or confirm to override.")
                        continue
                CURRENT_MODE = "finetune"
                print("\n[➔] Access Authorized. Launching in FINETUNE mode...")
                break
            elif choice == "3":
                CURRENT_MODE = "idle"
                print("\n[➔] Access Authorized. Launching in IDLE mode...")
                break
            elif choice == "4":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping the RAG queue/database to 0? (leaderboard stats are kept) (y/n): ").strip().lower()
                if confirm == 'y':
                    rag_execute_hard_reset()
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "5":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping all fine-tune generated pairs? (leaderboard stats are kept) (y/n): ").strip().lower()
                if confirm == 'y':
                    finetune_execute_hard_reset()
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "6":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping BOTH campaigns' queues/data to 0? (leaderboard stats are kept) (y/n): ").strip().lower()
                if confirm == 'y':
                    rag_execute_hard_reset()
                    finetune_execute_hard_reset()
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "7":
                print("[X] Terminating environment.")
                sys.exit(0)
            else:
                print("[!] Parameter outside boundary bounds. Select 1-7.")
        except KeyboardInterrupt:
            print("\n[X] Forced Close.")
            sys.exit(0)

# ============================================================
# API ENDPOINTS
# ============================================================

def _get_rag_work(user_id: str, hardware_tier: str, model: str) -> dict:
    state = load_lock_state(RAG_LOCK_FILE)
    state_modified = prune_stale_locks(state)

    if hardware_tier == "easy":
        allowed = ["easy"]
    elif hardware_tier == "medium":
        allowed = ["easy", "medium"]
    else:
        allowed = ["easy", "medium", "hard"]

    # Unrecognized/unset model names default to the lowest rank -- they still get every normal
    # chunk, just not the ones flagged as needing a stronger model to avoid fabricated content on
    # thin chunks.
    client_model_rank = MODEL_TIER_RANK.get(model, 1)

    available_tasks = [
        t for t in rag_chunk_queue
        if t["chunk_id"] not in state["completed"]
        and t["chunk_id"] not in state["locked"]
        and t["difficulty"] in allowed
        and (not t.get("requires_strong_model") or client_model_rank >= THIN_CHUNK_MIN_TIER)
    ]

    total_chunks = len(rag_chunk_queue)
    completed_chunks = len(state["completed"])

    if not available_tasks:
        if state_modified:
            save_lock_state(RAG_LOCK_FILE, state)
        # "done" must mean the whole campaign is finished, not just "nothing available for me
        # right now" -- otherwise a swarm of only-3B clients would see thin chunks (which they're
        # deliberately excluded from) as a false "complete!" the moment their eligible work runs
        # dry, while those chunks sit unprocessed forever waiting for a 14B+ client to show up.
        if state["locked"] or completed_chunks < total_chunks:
            return {"mode": "rag", "status": "waiting", "total_chunks": total_chunks, "completed_chunks": completed_chunks}
        return {"mode": "rag", "status": "done", "total_chunks": total_chunks, "completed_chunks": completed_chunks}

    if "hard" in allowed:
        priority_map = {"hard": 0, "medium": 1, "easy": 2}
        available_tasks.sort(key=lambda t: priority_map.get(t["difficulty"], 3))

    assigned_task = available_tasks[0]
    state["locked"][assigned_task["chunk_id"]] = {"user_id": user_id, "timestamp": time.time()}
    save_lock_state(RAG_LOCK_FILE, state)
    print(f"[RAG ➔ {user_id}] Dispatched Priority ({assigned_task['difficulty'].upper()}): {assigned_task['chunk_id']}")

    return {"mode": "rag", "status": "active", "task": assigned_task, "total_chunks": total_chunks, "completed_chunks": completed_chunks}

def _get_finetune_work(user_id: str, hardware_tier: str) -> dict:
    state = load_lock_state(FINETUNE_LOCK_FILE)
    state_modified = prune_stale_locks(state)

    total_chunks = len(finetune_chunk_queue)
    completed_chunks = len(state["completed"])

    # Fine-tune generation needs stronger instruction-following than RAG extraction (natural
    # prose + judging debugging-vs-review shape for reviews) -- "easy" tier clients are capped at
    # qwen2.5-coder:3b, which isn't reliable enough for this task, so they never get fine-tune
    # work even while the campaign has plenty left to do. See CUBYZ_FOLDING.py's protocol notes.
    if hardware_tier == "easy":
        available_tasks = []
    else:
        available_tasks = [
            t for t in finetune_chunk_queue
            if t["chunk_id"] not in state["completed"] and t["chunk_id"] not in state["locked"]
        ]

    if not available_tasks:
        if state_modified:
            save_lock_state(FINETUNE_LOCK_FILE, state)
        if state["locked"] or completed_chunks < total_chunks:
            return {"mode": "finetune", "status": "waiting", "total_chunks": total_chunks, "completed_chunks": completed_chunks}
        return {"mode": "finetune", "status": "done", "total_chunks": total_chunks, "completed_chunks": completed_chunks}

    assigned_task = available_tasks[0]
    state["locked"][assigned_task["chunk_id"]] = {"user_id": user_id, "timestamp": time.time()}
    save_lock_state(FINETUNE_LOCK_FILE, state)
    print(f"[FINETUNE ➔ {user_id}] Dispatched ({assigned_task['source_type']}): {assigned_task['chunk_id']}")

    return {"mode": "finetune", "status": "active", "task": assigned_task, "total_chunks": total_chunks, "completed_chunks": completed_chunks}

@app.get("/get_work")
def get_work(user_id: str, hardware_tier: str = "medium", model: str = "", client_version: str = ""):
    if not user_id.isalpha() or not (3 <= len(user_id) <= 9):
        raise HTTPException(status_code=400, detail="Invalid ID layout.")

    if _parse_version(client_version) < _parse_version(MIN_CLIENT_VERSION):
        raise HTTPException(status_code=426, detail=_version_rejection_message(client_version))

    online_clients[user_id.lower()] = {"timestamp": time.time(), "tier": hardware_tier}

    if CURRENT_MODE == "rag":
        return _get_rag_work(user_id, hardware_tier, model)
    if CURRENT_MODE == "finetune":
        return _get_finetune_work(user_id, hardware_tier)
    return {"mode": "idle", "status": "idle"}

def _submit_rag_work(submission: UnifiedSubmission) -> dict:
    state = load_lock_state(RAG_LOCK_FILE)

    if submission.chunk_id in state["completed"]:
        state["locked"].pop(submission.chunk_id, None)
        save_lock_state(RAG_LOCK_FILE, state)
        return {"status": "ignored"}

    state["locked"].pop(submission.chunk_id, None)
    state["completed"].append(submission.chunk_id)
    save_lock_state(RAG_LOCK_FILE, state)

    user_stats = load_user_stats(RAG_STATS_FILE)
    user_key = submission.user_id.lower()
    if user_key not in user_stats:
        user_stats[user_key] = {"chunks_completed": 0, "lines_crunched": 0}
    user_stats[user_key]["chunks_completed"] += 1
    user_stats[user_key]["lines_crunched"] += submission.lines_crunched or 0
    save_user_stats(RAG_STATS_FILE, user_stats)

    user_folder = os.path.join(USERS_DIR, submission.user_id.lower())
    os.makedirs(user_folder, exist_ok=True)

    # Route by the chunk's own recorded directory_context (set once, authoritatively, at ingestion
    # time in rag_initialize_chunks()) rather than pattern-matching the submitted title. Title is
    # built client-side from the chunk's relative_path -- for GitHub review chunks that's the path
    # of the file *being reviewed*, which never contains the word "review", so title-based
    # matching would silently misfile every review chunk into codebase.jsonl.
    original_task = next((t for t in rag_chunk_queue if t["chunk_id"] == submission.chunk_id), None)
    directory_context = (original_task or {}).get("directory_context", "").upper()

    if "GITHUB_REVIEWS" in directory_context:
        target_file = "github_reviews.jsonl"
    elif "DEFINITIVE_WIKI_DOCUMENTATION" in directory_context:
        target_file = "wiki.jsonl"
    elif "ADDON_STUDIO" in directory_context:
        target_file = "addon_studio.jsonl"
    else:
        target_file = "codebase.jsonl"

    user_file = os.path.join(user_folder, target_file)
    # Only the RAG-relevant subset of UnifiedSubmission's fields -- not a raw dump of the whole
    # model, which would otherwise pollute this output with always-empty finetune-only fields
    # (source_type, pairs) that downstream consumers of codebase.jsonl/wiki.jsonl don't expect.
    output_record = {
        "chunk_id": submission.chunk_id,
        "summary": submission.summary,
        "comprehensive_explanation": submission.comprehensive_explanation,
        "symbols": submission.symbols,
        "concepts": submission.concepts,
        "keywords": submission.keywords,
        "chunk_type": submission.chunk_type,
        "code_example": submission.code_example,
        "synthetic_queries": submission.synthetic_queries,
        "title": submission.title,
        "user_id": submission.user_id,
        "lines_crunched": submission.lines_crunched,
    }
    with open(user_file, "a", encoding="utf-8") as out_f:
        out_f.write(json.dumps(output_record) + "\n")

    print(f"[RAG ✓] '{submission.user_id}': {submission.title} -> {target_file} ({submission.lines_crunched} LOC)")
    return {"status": "success"}

def _submit_finetune_work(submission: UnifiedSubmission) -> dict:
    state = load_lock_state(FINETUNE_LOCK_FILE)
    if submission.chunk_id in state["completed"]:
        state["locked"].pop(submission.chunk_id, None)
        save_lock_state(FINETUNE_LOCK_FILE, state)
        return {"status": "ignored"}

    state["locked"].pop(submission.chunk_id, None)
    state["completed"].append(submission.chunk_id)
    save_lock_state(FINETUNE_LOCK_FILE, state)

    user_stats = load_user_stats(FINETUNE_STATS_FILE)
    user_key = submission.user_id.lower()
    if user_key not in user_stats:
        user_stats[user_key] = {"chunks_completed": 0, "pairs_generated": 0}
    user_stats[user_key]["chunks_completed"] += 1
    user_stats[user_key]["pairs_generated"] += len(submission.pairs)
    save_user_stats(FINETUNE_STATS_FILE, user_stats)

    user_folder = os.path.join(FINETUNE_OUTPUT_DIR, submission.user_id.lower())
    os.makedirs(user_folder, exist_ok=True)
    target_file = os.path.join(user_folder, f"{submission.source_type}_pairs.jsonl")
    with open(target_file, "a", encoding="utf-8") as out_f:
        out_f.write(json.dumps({
            "chunk_id": submission.chunk_id,
            "source_type": submission.source_type,
            "pairs": submission.pairs,
            "user_id": submission.user_id,
        }) + "\n")

    print(f"[FINETUNE ✓] '{submission.user_id}': {submission.chunk_id} -> {len(submission.pairs)} pairs")
    return {"status": "success"}

@app.post("/submit_work")
def submit_work(submission: UnifiedSubmission):
    if _parse_version(submission.client_version) < _parse_version(MIN_CLIENT_VERSION):
        raise HTTPException(status_code=426, detail=_version_rejection_message(submission.client_version))

    online_clients[submission.user_id.lower()] = {"timestamp": time.time(), "tier": "reporting"}

    if submission.mode == "finetune":
        return _submit_finetune_work(submission)
    return _submit_rag_work(submission)

def _rag_leaderboard() -> dict:
    state = load_lock_state(RAG_LOCK_FILE)
    user_stats = load_user_stats(RAG_STATS_FILE)

    total_chunks = len(rag_chunk_queue)
    completed_chunks = len(state["completed"])
    global_pct = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

    # Union with online_clients, not just user_stats -- a node that has connected but not yet
    # completed a chunk (in this campaign specifically) has no stats entry yet, but should still
    # show up as an active user.
    known_users = set(user_stats.keys()) | set(online_clients.keys())

    rankings = []
    for u_id in known_users:
        data = user_stats.get(u_id, {"chunks_completed": 0, "lines_crunched": 0})
        contribution = (data["chunks_completed"] / completed_chunks * 100) if completed_chunks > 0 else 0.0
        is_online = u_id in online_clients and (time.time() - online_clients[u_id]["timestamp"] < 60)

        rankings.append({
            "user_id": u_id,
            "chunks_completed": data["chunks_completed"],
            "lines_crunched": data["lines_crunched"],
            "contribution_percentage": round(contribution, 2),
            "status": "ONLINE 🟢" if is_online else "OFFLINE 🔴"
        })

    rankings.sort(key=lambda x: (x["chunks_completed"], x["lines_crunched"]), reverse=True)
    for index, entry in enumerate(rankings, 1):
        entry["rank"] = index

    return {
        "total_chunks_in_codebase": total_chunks,
        "total_chunks_completed": completed_chunks,
        "global_percentage": round(global_pct, 2),
        "rankings": rankings
    }

def _finetune_leaderboard() -> dict:
    state = load_lock_state(FINETUNE_LOCK_FILE)
    user_stats = load_user_stats(FINETUNE_STATS_FILE)
    total_chunks = len(finetune_chunk_queue)
    completed_chunks = len(state["completed"])
    global_pct = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

    known_users = set(user_stats.keys()) | set(online_clients.keys())
    rankings = []
    for u_id in known_users:
        data = user_stats.get(u_id, {"chunks_completed": 0, "pairs_generated": 0})
        is_online = u_id in online_clients and (time.time() - online_clients[u_id]["timestamp"] < 60)
        rankings.append({
            "user_id": u_id,
            "chunks_completed": data["chunks_completed"],
            "pairs_generated": data["pairs_generated"],
            "status": "ONLINE" if is_online else "OFFLINE",
        })
    rankings.sort(key=lambda x: (x["chunks_completed"], x["pairs_generated"]), reverse=True)
    for i, entry in enumerate(rankings, 1):
        entry["rank"] = i

    return {
        "total_chunks_in_campaign": total_chunks,
        "total_chunks_completed": completed_chunks,
        "global_percentage": round(global_pct, 2),
        "rankings": rankings,
    }

@app.get("/leaderboard")
def get_leaderboard():
    # Reflects whichever campaign is currently active, same as /get_work -- defaults to the RAG
    # shape while idle (arbitrary but stable) rather than returning nothing.
    result = _finetune_leaderboard() if CURRENT_MODE == "finetune" else _rag_leaderboard()
    result["mode"] = CURRENT_MODE
    return result

@app.get("/admin/mode")
def get_mode():
    return {"mode": CURRENT_MODE}

@app.post("/admin/mode")
def set_mode(mode: str, force: bool = False):
    global CURRENT_MODE
    if mode not in ("idle", "rag", "finetune"):
        raise HTTPException(status_code=400, detail="mode must be one of: idle, rag, finetune")
    if mode == "finetune" and not force and not _rag_campaign_complete():
        total = len(rag_chunk_queue)
        completed = len(load_lock_state(RAG_LOCK_FILE)["completed"])
        raise HTTPException(
            status_code=409,
            detail=f"RAG campaign is not finished ({completed}/{total} chunks) -- fine-tune pair "
                   f"generation is meant to run after RAG extraction completes. Retry with "
                   f"force=true to override."
        )
    CURRENT_MODE = mode
    # Marked dirty (clean_shutdown=False) immediately -- if the process dies before a clean
    # shutdown writes True, the next startup's "unfinished campaign" flag reflects THIS mode,
    # not whatever was persisted before the switch.
    save_server_mode_state(CURRENT_MODE, clean_shutdown=False)
    print(f"[ADMIN] Campaign mode switched to: {mode.upper()}")
    return {"mode": CURRENT_MODE}

@app.get("/version")
def get_version():
    return {
        "min_client_version": MIN_CLIENT_VERSION,
        "latest_client_version": LATEST_CLIENT_VERSION,
        "download_url": CLIENT_DOWNLOAD_URL,
    }

if __name__ == "__main__":
    import uvicorn
    # Scanned before the gate (not after, as before) so the menu can show real RAG/finetune
    # progress and server_startup_gate()'s "finetune after RAG" safeguard has real numbers to
    # check against instead of an empty, not-yet-scanned queue.
    rag_initialize_chunks()
    finetune_initialize_chunks()
    server_startup_gate()
    # Dirty the persisted state the moment we're about to actually start serving -- only the
    # finally block below (a real clean stop) clears it back to True.
    save_server_mode_state(CURRENT_MODE, clean_shutdown=False)
    try:
        uvicorn.run(app, host="0.0.0.0", port=7000)
    except KeyboardInterrupt:
        pass
    finally:
        save_server_mode_state(CURRENT_MODE, clean_shutdown=True)
        print("\n[X] Server shut down cleanly.")
