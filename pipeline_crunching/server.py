import os
import sys
import json
import time
import shutil
import hashlib
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Cubyz RAG Dataset Coordinator v2")

# Anchored to this script's own directory / the repo root rather than the process's cwd --
# same reasoning as webapp/local_rag_chat.py's REPO_ROOT pattern. organized_cubyz_dataset/ lives
# alongside this script; users/ stays at the repo root since finetune/server_finetune.py reads
# from it too.
PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PIPELINE_ROOT)

SOURCE_DIR = os.path.join(PIPELINE_ROOT, "organized_cubyz_dataset") + os.sep
USERS_DIR = os.path.join(REPO_ROOT, "users")
LOCK_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "lock_state.json")
STATS_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "user_stats.json")
HASH_DB_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "file_hashes.json")
BACKUP_DIR = os.path.join(REPO_ROOT, "archive", "rag_crunching_campaign_backups")
TASK_TIMEOUT = 300

# A chunk this short (same threshold client_linux.py uses to cap synthetic_queries) doesn't carry
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

chunk_queue = []
online_clients = {}

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
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[X] Failed to write {label} to disk: {e}")

def initialize_empty_state():
    for f_target in (LOCK_FILE, STATS_FILE, HASH_DB_FILE):
        if os.path.exists(f_target):
            os.remove(f_target)

    if os.path.exists(USERS_DIR):
        shutil.rmtree(USERS_DIR)
    os.makedirs(USERS_DIR, exist_ok=True)

    write_json_file(LOCK_FILE, {"locked": {}, "completed": []}, "lock state")
    write_json_file(STATS_FILE, {}, "user stats")
    write_json_file(HASH_DB_FILE, {}, "hash db")

    print("\n[✓] Active structures and statistics initialized back to 0.")

def execute_hard_reset():
    print("\n[!] Initializing System Hard Reset & Backup Sequence...")
    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_backup = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(session_backup, exist_ok=True)

    files_backed_up = 0
    for f_target in (LOCK_FILE, STATS_FILE, HASH_DB_FILE):
        if os.path.exists(f_target):
            shutil.copy2(f_target, os.path.join(session_backup, f_target))
            files_backed_up += 1

    if os.path.exists(USERS_DIR) and os.listdir(USERS_DIR):
        shutil.copytree(USERS_DIR, os.path.join(session_backup, USERS_DIR), dirs_exist_ok=True)
        files_backed_up += 1

    if files_backed_up > 0:
        print(f"[✓] Successfully archived session data to: {session_backup}")
    else:
        print("[~] No historical operational data found to archive.")

    initialize_empty_state()

def server_startup_gate():
    print("\n" + "═"*55)
    print("        CUBYZ DISTRIBUTED DATASET ENGINE COORDINATOR      ")
    print("═"*55)
    print("  [1] 🟢 LAUNCH PIPELINE ENGINE (Resume / Start Processing)")
    print("  [2] ⚠️ HARD RESET RUNWAYS      (Wipe Stats & Database to 0)")
    print("  [3] 🛑 SHUTDOWN ENGINE")
    print("═"*55)

    while True:
        try:
            choice = input("Select command index (1-3): ").strip()
            if choice == "1":
                print("\n[➔] Access Authorized. Initializing ingestion cluster...")
                break
            elif choice == "2":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping all contribution stats? (y/n): ").strip().lower()
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

def initialize_chunks():
    chunk_size, overlap = 150, 30
    step = chunk_size - overlap

    if not os.path.exists(SOURCE_DIR):
        print(f"[X] Error: Organized source workspace not found at '{SOURCE_DIR}'!")
        sys.exit(1)

    lock_state = load_lock_state()
    completed_chunks = set(lock_state.get("completed", []))
    old_hashes = read_json_file(HASH_DB_FILE, {})

    current_hashes = {}
    skipped_unchanged_count = 0
    total_scanned_files = 0

    for tier in ["easy", "medium", "hard"]:
        tier_path = os.path.join(SOURCE_DIR, tier)
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

                    chunk_queue.extend(file_chunks)

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

                    chunk_queue.extend(file_chunks)

            except Exception as e:
                print(f"[!] Error parsing file entry {file}: {e}")

    write_json_file(HASH_DB_FILE, current_hashes, "hash db")
    os.makedirs(USERS_DIR, exist_ok=True)

    print("\n" + "─"*55)
    print("               CUBYZ PIPELINE METRICS                 ")
    print("─"*55)
    print(f" 📂 Total Workspace Files Found:  {total_scanned_files}")
    print(f" ⏭️ Bypassed (Fully Completed):   {skipped_unchanged_count}")
    print(f" 🔥 Active Task Targets Queued:   {len(chunk_queue)}")
    print("─"*55 + "\n")

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

# --- API ENDPOINTS ---
@app.get("/get_work")
def get_work(user_id: str, hardware_tier: str = "medium", model: str = ""):
    if not user_id.isalpha() or not (3 <= len(user_id) <= 9):
        raise HTTPException(status_code=400, detail="Invalid ID layout.")

    online_clients[user_id.lower()] = {
        "timestamp": time.time(),
        "tier": hardware_tier
    }

    state = load_lock_state()
    state_modified = prune_stale_locks(state)

    if hardware_tier == "easy":
        allowed = ["easy"]
    elif hardware_tier == "medium":
        allowed = ["easy", "medium"]
    else:
        allowed = ["easy", "medium", "hard"]

    # Unrecognized/unset model names (older clients that don't send this param yet) default to the
    # lowest rank -- they still get every normal chunk, just not the ones flagged as needing a
    # stronger model to avoid fabricated content on thin chunks.
    client_model_rank = MODEL_TIER_RANK.get(model, 1)

    available_tasks = [
        t for t in chunk_queue
        if t["chunk_id"] not in state["completed"]
        and t["chunk_id"] not in state["locked"]
        and t["difficulty"] in allowed
        and (not t.get("requires_strong_model") or client_model_rank >= THIN_CHUNK_MIN_TIER)
    ]

    total_chunks = len(chunk_queue)
    completed_chunks = len(state["completed"])

    if not available_tasks:
        if state_modified:
            save_lock_state(state)
        # "done" must mean the whole project is finished, not just "nothing available for me right
        # now" -- otherwise a swarm of only-3B clients would see thin chunks (which they're
        # deliberately excluded from) as a false "Codebase complete!" the moment their eligible work
        # runs dry, while those chunks sit unprocessed forever waiting for a 14B+ client to show up.
        if state["locked"] or completed_chunks < total_chunks:
            return {
                "status": "waiting",
                "total_chunks": total_chunks,
                "completed_chunks": completed_chunks
            }
        return {
            "status": "done",
            "total_chunks": total_chunks,
            "completed_chunks": completed_chunks
        }

    if "hard" in allowed:
        priority_map = {"hard": 0, "medium": 1, "easy": 2}
        available_tasks.sort(key=lambda t: priority_map.get(t["difficulty"], 3))

    assigned_task = available_tasks[0]
    state["locked"][assigned_task["chunk_id"]] = {
        "user_id": user_id,
        "timestamp": time.time()
    }

    save_lock_state(state)
    print(f"[➔] Queue Dispatched Priority ({assigned_task['difficulty'].upper()}): {assigned_task['chunk_id']} -> '{user_id}'")

    return {
        "status": "active",
        "task": assigned_task,
        "total_chunks": total_chunks,
        "completed_chunks": completed_chunks
    }

@app.post("/submit_work")
def submit_work(node: RAGNode):
    online_clients[node.user_id.lower()] = {
        "timestamp": time.time(),
        "tier": "reporting"
    }

    state = load_lock_state()

    if node.chunk_id in state["completed"]:
        state["locked"].pop(node.chunk_id, None)
        save_lock_state(state)
        return {"status": "ignored"}

    state["locked"].pop(node.chunk_id, None)
    state["completed"].append(node.chunk_id)
    save_lock_state(state)

    user_stats = load_user_stats()
    user_key = node.user_id.lower()
    if user_key not in user_stats:
        user_stats[user_key] = {"chunks_completed": 0, "lines_crunched": 0}

    user_stats[user_key]["chunks_completed"] += 1
    user_stats[user_key]["lines_crunched"] += node.lines_crunched or 0
    save_user_stats(user_stats)

    user_folder = os.path.join(USERS_DIR, node.user_id.lower())
    os.makedirs(user_folder, exist_ok=True)

    # Route by the chunk's own recorded directory_context (set once, authoritatively, at ingestion
    # time in initialize_chunks()) rather than pattern-matching node.title. Title is built
    # client-side from the chunk's relative_path -- for GitHub review chunks that's the path of
    # the file *being reviewed* (e.g. "src/gui/windows/connecting.zig"), which never contains the
    # word "review", so title-based matching silently misfiled every review chunk into
    # codebase.jsonl. chunk_queue is populated once at startup and never has entries removed, so
    # this lookup is always reliable for any chunk_id that really came from get_work.
    original_task = next((t for t in chunk_queue if t["chunk_id"] == node.chunk_id), None)
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

    with open(user_file, "a", encoding="utf-8") as out_f:
        out_f.write(node.model_dump_json(exclude_none=False) + "\n")

    print(f"✓ Node Entry Logged from '{node.user_id}': {node.title} -> {target_file} ({node.lines_crunched} LOC)")
    return {"status": "success"}

@app.get("/leaderboard")
def get_leaderboard():
    state = load_lock_state()
    user_stats = load_user_stats()

    total_chunks = len(chunk_queue)
    completed_chunks = len(state["completed"])
    global_pct = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

    # Union with online_clients, not just user_stats -- a node that has connected but not yet
    # completed a chunk has no stats entry yet, but should still show up as an active user.
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

if __name__ == "__main__":
    import uvicorn
    server_startup_gate()
    initialize_chunks()
    uvicorn.run(app, host="0.0.0.0", port=7000)
