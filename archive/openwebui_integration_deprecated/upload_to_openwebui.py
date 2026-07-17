"""
Bulk-creates the 4 Cubyz Knowledge collections in Open WebUI and uploads every file
exported by export_for_openwebui.py into them via Open WebUI's REST API.

Why this exists: dragging ~2200 individual files through the browser upload dialog isn't
practical. This automates it.

Setup:
    pip install requests
    Get an API key from your Open WebUI instance: Settings -> Account -> API Keys -> Create.
    export OPEN_WEBUI_URL="http://localhost:3000"
    export OPEN_WEBUI_API_KEY="sk-..."
    python3 upload_to_openwebui.py

Note on API stability: these endpoints (/api/v1/knowledge/*, /api/v1/files/) reflect Open
WebUI's long-standing REST API shape, but this project moves fast. If a call fails, the
script prints the raw HTTP status + response body -- cross-check that against your own
instance's live API docs at {OPEN_WEBUI_URL}/docs before assuming the data is bad.
"""
import os
import sys
import time

import requests

BASE_URL = os.environ.get("OPEN_WEBUI_URL", "http://localhost:3000").rstrip("/")
API_KEY = os.environ.get("OPEN_WEBUI_API_KEY", "")
SOURCE_DIR = "openwebui_knowledge"

COLLECTIONS = {
    "codebase": ("Cubyz Codebase", "Structured extraction of the Cubyz Zig source: architecture, symbols, functions, engine logic."),
    "docs": ("Cubyz Documentation", "Official Cubyz wiki/docs: gameplay, mechanics, history, contributing guidelines."),
    "addon_creator": ("Cubyz Addon Creator", "Addon Creator Studio UI/blueprint knowledge for building blocks, items, biomes, etc."),
    "reviews": ("Cubyz GitHub Reviews", "Real PR review comments and diffs: bug causes, reviewer concerns, refactor motivations."),
}

if not API_KEY:
    sys.exit("[X] Set OPEN_WEBUI_API_KEY (Settings -> Account -> API Keys in Open WebUI) before running.")

HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def api_get(path):
    r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
    if not r.ok:
        print(f"[X] GET {path} -> {r.status_code}: {r.text[:300]}")
    r.raise_for_status()
    return r.json()


def api_post_json(path, payload):
    r = requests.post(f"{BASE_URL}{path}", headers={**HEADERS, "Content-Type": "application/json"}, json=payload, timeout=30)
    if not r.ok:
        print(f"[X] POST {path} -> {r.status_code}: {r.text[:300]}")
    r.raise_for_status()
    return r.json()


def get_or_create_knowledge(name: str, description: str) -> str:
    # GET /api/v1/knowledge/ returns {"items": [...], "total": N}, paginated at 30/page -- fine
    # here since we only ever look for 4 known names among presumably < 30 existing collections.
    existing = api_get("/api/v1/knowledge/")
    for k in existing.get("items", []):
        if k.get("name") == name:
            print(f"[~] Knowledge collection '{name}' already exists, reusing id {k['id']}")
            return k["id"]

    created = api_post_json("/api/v1/knowledge/create", {"name": name, "description": description})
    print(f"[✓] Created knowledge collection '{name}' -> id {created['id']}")
    return created["id"]


def api_delete(path):
    r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
    if not r.ok:
        print(f"[X] DELETE {path} -> {r.status_code}: {r.text[:300]}")
    r.raise_for_status()
    return r.json()


def purge_knowledge_files(knowledge_id: str, display_name: str):
    # Files aren't deduped by filename on upload -- re-running an upload for a collection whose
    # source data changed (e.g. a corrected chunk) would otherwise leave the old, now-stale file
    # sitting alongside the new one instead of being replaced. Deleting the file objects outright
    # (not just detaching them from the collection) also frees the underlying embedding.
    detail = api_get(f"/api/v1/knowledge/{knowledge_id}")
    existing_files = detail.get("files") or []
    if not existing_files:
        return
    print(f"[~] Purging {len(existing_files)} existing files from '{display_name}' before re-upload...")
    for f in existing_files:
        try:
            api_delete(f"/api/v1/files/{f['id']}")
        except Exception as e:
            print(f"    [X] failed to delete {f.get('id')}: {e}")


def upload_file(file_path: str) -> str:
    with open(file_path, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/api/v1/files/",
            headers=HEADERS,
            files={"file": (os.path.basename(file_path), f, "text/markdown")},
            timeout=60,
        )
    if not r.ok:
        raise RuntimeError(f"upload failed {r.status_code}: {r.text[:300]}")
    return r.json()["id"]


def attach_files_batch(knowledge_id: str, file_ids: list) -> list:
    # POST /api/v1/knowledge/{id}/files/batch/add takes a bare JSON array of {"file_id": ...}
    # objects (list[KnowledgeFileIdForm]), and processes/embeds them server-side as one batch --
    # much better than one /file/add call per file for both call count and embedding throughput.
    # This is a long synchronous call (embeds every file in the batch before returning), so give
    # it a generous timeout scaled to batch size.
    r = requests.post(
        f"{BASE_URL}/api/v1/knowledge/{knowledge_id}/files/batch/add",
        headers={**HEADERS, "Content-Type": "application/json"},
        json=[{"file_id": fid} for fid in file_ids],
        timeout=60 + 10 * len(file_ids),
    )
    if not r.ok:
        raise RuntimeError(f"batch attach failed {r.status_code}: {r.text[:300]}")
    body = r.json() or {}
    warnings = body.get("warnings") or {}
    return warnings.get("errors", [])


BATCH_SIZE = 25  # files embedded per batch/add call -- keeps each request's timeout/GPU burst reasonable


def main():
    # Optional CLI args: a collection name restricts the run to one collection (e.g.
    # `python3 upload_to_openwebui.py docs`) instead of re-uploading all ~2200 files -- useful for
    # re-syncing a single collection after a source-data fix without touching the others.
    # `--reset` purges that collection's existing files first, so a re-sync replaces stale content
    # instead of leaving old + corrected versions sitting side by side (uploads aren't deduped by
    # filename).
    args = sys.argv[1:]
    reset = "--reset" in args
    positional = [a for a in args if a != "--reset"]
    only = positional[0] if positional else None
    if only and only not in COLLECTIONS:
        sys.exit(f"[X] Unknown collection '{only}'. Choose from: {', '.join(COLLECTIONS)}")
    collections = {only: COLLECTIONS[only]} if only else COLLECTIONS

    for folder, (display_name, description) in collections.items():
        dir_path = os.path.join(SOURCE_DIR, folder)
        if not os.path.isdir(dir_path):
            print(f"[!] Skipping '{folder}': directory not found. Run export_for_openwebui.py first.")
            continue

        files = sorted(f for f in os.listdir(dir_path) if f.endswith(".md"))
        if not files:
            print(f"[!] Skipping '{folder}': no files to upload.")
            continue

        knowledge_id = get_or_create_knowledge(display_name, description)
        if reset:
            purge_knowledge_files(knowledge_id, display_name)

        print(f"[~] Uploading {len(files)} raw files into '{display_name}'...")
        file_ids, upload_failed = [], 0
        for i, fname in enumerate(files, 1):
            file_path = os.path.join(dir_path, fname)
            try:
                file_ids.append(upload_file(file_path))
            except Exception as e:
                upload_failed += 1
                print(f"    [X] upload {fname}: {e}")

            if i % 100 == 0 or i == len(files):
                print(f"    ... uploaded {i}/{len(files)} ({upload_failed} failed)")
            time.sleep(0.02)

        print(f"[~] Embedding {len(file_ids)} files into '{display_name}' in batches of {BATCH_SIZE}...")
        attach_failed = 0
        for start in range(0, len(file_ids), BATCH_SIZE):
            batch = file_ids[start:start + BATCH_SIZE]
            try:
                errors = attach_files_batch(knowledge_id, batch)
                if errors:
                    attach_failed += len(errors)
                    for err in errors:
                        print(f"    [X] {err}")
            except Exception as e:
                attach_failed += len(batch)
                print(f"    [X] batch {start}-{start + len(batch)}: {e}")

            done = min(start + BATCH_SIZE, len(file_ids))
            print(f"    ... embedded {done}/{len(file_ids)} ({attach_failed} failed so far)")

        print(f"[✓] '{display_name}' done: {len(file_ids) - attach_failed}/{len(files)} usable, "
              f"{upload_failed} upload failures, {attach_failed} embed failures\n")

    print("[✓] All collections processed. Attach the ones you need to a custom Model in Open WebUI.")


if __name__ == "__main__":
    main()
