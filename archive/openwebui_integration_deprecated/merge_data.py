import os
import json

# Anchored to this script's own directory / the repo root rather than the process's cwd --
# same reasoning as webapp/local_rag_chat.py's REPO_ROOT pattern. users/ stays at the repo root
# since finetune/server_finetune.py reads from it too; merged_datasets/ lives alongside this
# script since only pipeline_crunching uses it.
PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PIPELINE_ROOT)

USERS_DIR = os.path.join(REPO_ROOT, "users")
OUTPUT_DIR = os.path.join(PIPELINE_ROOT, "merged_datasets")

# Each per-user file gets merged into its own standalone document -- these are meant to be
# uploaded as four SEPARATE Open WebUI "Knowledge" collections, each backing a different custom
# Model (e.g. a Docs-scoped assistant, an Addon-Creator-scoped assistant), rather than one
# undifferentiated blob.
DATASET_TYPES = {
    "codebase.jsonl": ("cubyz_codebase_knowledgebase.md", "Cubyz Codebase Knowledge Base"),
    "wiki.jsonl": ("cubyz_docs_knowledgebase.md", "Cubyz Official Documentation Knowledge Base"),
    "addon_studio.jsonl": ("cubyz_addon_creator_knowledgebase.md", "Cubyz Addon Creator Knowledge Base"),
    "github_reviews.jsonl": ("cubyz_reviews_knowledgebase.md", "Cubyz GitHub Review History Knowledge Base"),
}

def format_chunk_as_markdown(chunk: dict) -> str:
    parts = [f"## {chunk.get('title', 'Untitled Chunk')}\n"]
    if chunk.get("chunk_type"):
        parts.append(f"**Type:** {chunk['chunk_type']}\n")
    if chunk.get("summary"):
        parts.append(f"**Summary:** {chunk['summary']}\n")
    if chunk.get("comprehensive_explanation"):
        parts.append(f"**Explanation:**\n{chunk['comprehensive_explanation']}\n")
    if chunk.get("symbols"):
        parts.append(f"**Symbols:** {', '.join(chunk['symbols'])}\n")
    if chunk.get("concepts"):
        parts.append(f"**Concepts:** {', '.join(chunk['concepts'])}\n")
    if chunk.get("keywords"):
        parts.append(f"**Keywords:** {', '.join(chunk['keywords'])}\n")
    if chunk.get("code_example"):
        parts.append(f"**Code Example:**\n```zig\n{chunk['code_example']}\n```\n")
    if chunk.get("synthetic_queries"):
        parts.append("**Related Questions:**\n" + "\n".join(f"- {q}" for q in chunk["synthetic_queries"]) + "\n")
    parts.append(f"*Contributed by: {chunk.get('user_id', 'unknown')}*\n")
    parts.append("\n---\n")
    return "\n".join(parts)

def merge_datasets():
    if not os.path.exists(USERS_DIR):
        print(f"[X] Directory '{USERS_DIR}' not found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("[~] Merging volunteer datasets into per-type Knowledge Base documents...")

    for filename, (output_name, doc_title) in DATASET_TYPES.items():
        seen_chunk_ids = set()
        entries = []

        for user_folder in sorted(os.listdir(USERS_DIR)):
            user_path = os.path.join(USERS_DIR, user_folder)
            if not os.path.isdir(user_path):
                continue

            dataset_path = os.path.join(user_path, filename)
            if not os.path.exists(dataset_path):
                continue

            try:
                with open(dataset_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            chunk = json.loads(line)
                        except Exception:
                            continue

                        # Keep only the first copy of a given chunk_id -- duplicates can occur
                        # legitimately (e.g. a stale lock reassigned the same chunk to a second
                        # node before the first node's submission was recorded).
                        chunk_id = chunk.get("chunk_id")
                        if chunk_id:
                            if chunk_id in seen_chunk_ids:
                                continue
                            seen_chunk_ids.add(chunk_id)

                        entries.append(chunk)
            except Exception as e:
                print(f"[!] Error reading {dataset_path}: {e}")

        if not entries:
            print(f"[~] No entries found for '{filename}' across any user; skipping {output_name}.")
            continue

        output_path = os.path.join(OUTPUT_DIR, output_name)
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write(f"# {doc_title}\n\n")
            for chunk in entries:
                out_f.write(format_chunk_as_markdown(chunk))

        print(f"[✓] Merged {len(entries)} chunks from '{filename}' across all users -> {output_path}")

    print(f"\n[✓] Done. Upload each file in '{OUTPUT_DIR}/' as its own Open WebUI Knowledge collection.")

if __name__ == "__main__":
    merge_datasets()
