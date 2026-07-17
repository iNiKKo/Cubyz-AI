import os
import sys
import time
import shutil
import hashlib
import json
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Cubyz Fine-Tune Dataset Coordinator")

# Anchored to this file's own location rather than the process's cwd -- same reasoning as
# webapp/local_rag_chat.py's REPO_ROOT pattern (and finetune/training/*.py's, which this
# mirrors one directory level shallower since this file lives directly in finetune/).
FINETUNE_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(FINETUNE_ROOT)

# Unlike server.py's pipeline, these inputs are already-chunked, already-validated records --
# each one IS a unit of work directly, no re-chunking needed. Reuses server.py's distributed
# coordination mechanics (lock/hash/stats) verbatim in spirit since that logic is generic and
# already proven; only the work-generation and output-routing differ.
DOCS_SOURCE = os.path.join(REPO_ROOT, "users")  # reads wiki.jsonl from every volunteer, same as the RAG pipeline did
CODEBASE_SUBSET_FILE = os.path.join(FINETUNE_ROOT, "source_data", "codebase_architectural_subset.jsonl")
REVIEWS_SOURCE = os.path.join(REPO_ROOT, "users")  # reads github_reviews.jsonl from every volunteer

OUTPUT_DIR = os.path.join(FINETUNE_ROOT, "pairs")
LOCK_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "lock_state.json")
STATS_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "user_stats.json")
HASH_DB_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "file_hashes.json")
BACKUP_DIR = os.path.join(REPO_ROOT, "archive", "finetune_campaign_backups")
TASK_TIMEOUT = 300

chunk_queue = []
online_clients = {}


class FinetunePairsSubmission(BaseModel):
    chunk_id: str
    source_type: str  # docs | codebase | reviews
    pairs: List[dict]  # [{"instruction": ..., "response": ...}, ...]
    user_id: str = Field(..., min_length=3, max_length=9, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0


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


def initialize_empty_state():
    for f_target in (LOCK_FILE, STATS_FILE, HASH_DB_FILE):
        if os.path.exists(f_target):
            os.remove(f_target)
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    write_json_file(LOCK_FILE, {"locked": {}, "completed": []}, "lock state")
    write_json_file(STATS_FILE, {}, "user stats")
    write_json_file(HASH_DB_FILE, {}, "hash db")
    print("\n[OK] Active structures and statistics initialized back to 0.")


def execute_hard_reset():
    print("\n[!] Initializing System Hard Reset & Backup Sequence...")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_backup = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(session_backup, exist_ok=True)

    files_backed_up = 0
    for f_target in (LOCK_FILE, STATS_FILE, HASH_DB_FILE):
        if os.path.exists(f_target):
            shutil.copy2(f_target, os.path.join(session_backup, os.path.basename(f_target)))
            files_backed_up += 1
    if os.path.exists(OUTPUT_DIR) and os.listdir(OUTPUT_DIR):
        shutil.copytree(OUTPUT_DIR, os.path.join(session_backup, "pairs"), dirs_exist_ok=True)
        files_backed_up += 1

    if files_backed_up > 0:
        print(f"[OK] Archived session data to: {session_backup}")
    else:
        print("[~] No historical operational data found to archive.")
    initialize_empty_state()


def server_startup_gate():
    print("\n" + "=" * 55)
    print("     CUBYZ FINE-TUNE DATASET ENGINE COORDINATOR      ")
    print("=" * 55)
    print("  [1] LAUNCH PIPELINE ENGINE (Resume / Start Processing)")
    print("  [2] HARD RESET RUNWAYS      (Wipe Stats & Pairs to 0)")
    print("  [3] SHUTDOWN ENGINE")
    print("=" * 55)
    while True:
        try:
            choice = input("Select command index (1-3): ").strip()
            if choice == "1":
                print("\n[->] Access Authorized. Initializing ingestion cluster...")
                break
            elif choice == "2":
                confirm = input("\n[!] CRITICAL WARNING: Confirm wiping all generated pairs? (y/n): ").strip().lower()
                if confirm == 'y':
                    execute_hard_reset()
                    break
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "3":
                print("[X] Terminating environment.")
                sys.exit(0)
            else:
                print("[!] Parameter outside boundary bounds. Select 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n[X] Forced Close.")
            sys.exit(0)


def load_lock_state() -> dict:
    return read_json_file(LOCK_FILE, {"locked": {}, "completed": []})


def save_lock_state(state: dict):
    write_json_file(LOCK_FILE, state, "lock state")


def load_user_stats() -> dict:
    return read_json_file(STATS_FILE, {})


def save_user_stats(stats: dict):
    write_json_file(STATS_FILE, stats, "user stats")


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


def initialize_chunks():
    if not os.path.exists(CODEBASE_SUBSET_FILE):
        print(f"[X] {CODEBASE_SUBSET_FILE} not found. Run filter_codebase_subset.py first.")
        sys.exit(1)

    lock_state = load_lock_state()
    completed_chunks = set(lock_state.get("completed", []))
    old_hashes = read_json_file(HASH_DB_FILE, {})
    current_hashes = {}

    # docs: every volunteer's wiki.jsonl, deduped
    docs_paths = [os.path.join(DOCS_SOURCE, u, "wiki.jsonl") for u in os.listdir(DOCS_SOURCE)] if os.path.exists(DOCS_SOURCE) else []
    docs_entries = load_deduped_jsonl(docs_paths)

    # reviews: every volunteer's github_reviews.jsonl, deduped
    review_paths = [os.path.join(REVIEWS_SOURCE, u, "github_reviews.jsonl") for u in os.listdir(REVIEWS_SOURCE)] if os.path.exists(REVIEWS_SOURCE) else []
    review_entries = load_deduped_jsonl(review_paths)

    # codebase architectural subset: single pre-filtered file
    codebase_entries = load_deduped_jsonl([CODEBASE_SUBSET_FILE])

    skipped_unchanged = 0
    for source_type, entries in (("docs", docs_entries), ("codebase", codebase_entries), ("reviews", review_entries)):
        for entry in entries:
            content_hash = calculate_content_hash(entry)
            current_hashes[entry["chunk_id"]] = content_hash

            if (entry["chunk_id"] in completed_chunks and
                    old_hashes.get(entry["chunk_id"]) == content_hash):
                skipped_unchanged += 1
                continue

            chunk_queue.append({
                "chunk_id": entry["chunk_id"],
                "source_type": source_type,
                "record": entry,
            })

    write_json_file(HASH_DB_FILE, current_hashes, "hash db")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n" + "-" * 55)
    print("            FINE-TUNE PIPELINE METRICS                ")
    print("-" * 55)
    print(f" Docs candidates:       {len(docs_entries)}")
    print(f" Codebase candidates:   {len(codebase_entries)}")
    print(f" Review candidates:     {len(review_entries)}")
    print(f" Bypassed (unchanged):  {skipped_unchanged}")
    print(f" Active task targets:   {len(chunk_queue)}")
    print("-" * 55 + "\n")


def prune_stale_locks(state: dict) -> bool:
    now = time.time()
    stale_keys = [cid for cid, info in state["locked"].items() if now - info["timestamp"] > TASK_TIMEOUT]
    for key in stale_keys:
        stale_info = state["locked"].pop(key)
        print(f"[!] Task '{key}' timed out from user '{stale_info['user_id']}'. Released back to queue.")
    return bool(stale_keys)


@app.get("/get_work")
def get_work(user_id: str, source_type: str = ""):
    if not user_id.isalpha() or not (3 <= len(user_id) <= 9):
        raise HTTPException(status_code=400, detail="Invalid ID layout.")

    online_clients[user_id.lower()] = {"timestamp": time.time(), "source_type": source_type}

    state = load_lock_state()
    state_modified = prune_stale_locks(state)

    available_tasks = [
        t for t in chunk_queue
        if t["chunk_id"] not in state["completed"] and t["chunk_id"] not in state["locked"]
        and (not source_type or t["source_type"] == source_type)
    ]

    total_chunks = len(chunk_queue)
    completed_count = len(state["completed"])

    if not available_tasks:
        if state_modified:
            save_lock_state(state)
        if state["locked"] or completed_count < total_chunks:
            return {"status": "waiting", "total_chunks": total_chunks, "completed_chunks": completed_count}
        return {"status": "done", "total_chunks": total_chunks, "completed_chunks": completed_count}

    assigned_task = available_tasks[0]
    state["locked"][assigned_task["chunk_id"]] = {"user_id": user_id, "timestamp": time.time()}
    save_lock_state(state)
    print(f"[->] Dispatched ({assigned_task['source_type']}): {assigned_task['chunk_id']} -> '{user_id}'")

    return {
        "status": "active",
        "task": assigned_task,
        "total_chunks": total_chunks,
        "completed_chunks": completed_count,
    }


@app.post("/submit_work")
def submit_work(submission: FinetunePairsSubmission):
    online_clients[submission.user_id.lower()] = {"timestamp": time.time(), "source_type": "reporting"}

    state = load_lock_state()
    if submission.chunk_id in state["completed"]:
        state["locked"].pop(submission.chunk_id, None)
        save_lock_state(state)
        return {"status": "ignored"}

    state["locked"].pop(submission.chunk_id, None)
    state["completed"].append(submission.chunk_id)
    save_lock_state(state)

    user_stats = load_user_stats()
    user_key = submission.user_id.lower()
    if user_key not in user_stats:
        user_stats[user_key] = {"chunks_completed": 0, "pairs_generated": 0}
    user_stats[user_key]["chunks_completed"] += 1
    user_stats[user_key]["pairs_generated"] += len(submission.pairs)
    save_user_stats(user_stats)

    user_folder = os.path.join(OUTPUT_DIR, submission.user_id.lower())
    os.makedirs(user_folder, exist_ok=True)
    target_file = os.path.join(user_folder, f"{submission.source_type}_pairs.jsonl")
    with open(target_file, "a", encoding="utf-8") as out_f:
        out_f.write(json.dumps({
            "chunk_id": submission.chunk_id,
            "source_type": submission.source_type,
            "pairs": submission.pairs,
            "user_id": submission.user_id,
        }) + "\n")

    print(f"OK Logged from '{submission.user_id}': {submission.chunk_id} -> {len(submission.pairs)} pairs")
    return {"status": "success"}


@app.get("/leaderboard")
def get_leaderboard():
    state = load_lock_state()
    user_stats = load_user_stats()
    total_chunks = len(chunk_queue)
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


if __name__ == "__main__":
    import uvicorn
    server_startup_gate()
    initialize_chunks()
    uvicorn.run(app, host="0.0.0.0", port=7000)
