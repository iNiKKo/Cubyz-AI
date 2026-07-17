"""
Publishes crunched volunteer output (users/*/{wiki,codebase,addon_studio,github_reviews}.jsonl)
into knowledge_base/ -- the one-file-per-chunk format webapp/local_rag_chat.py actually embeds
and retrieves. This is the missing link between "a volunteer's client submitted a chunk" and
"the live website can answer questions from it" -- nothing else in the pipeline does this step.

Safe to re-run any time (idempotent -- unchanged chunks are left alone, only new/changed ones are
written). Never deletes: users/ is expected to empty out on every campaign hard reset (see
pipeline_crunching/server.py's rag_execute_hard_reset/finetune_execute_hard_reset), while the
knowledge base accumulates permanently across every campaign run, the same way contribution stats
do. A chunk_id missing from users/ right now (because its campaign was just reset) does not mean
it should disappear from the live knowledge base.

Usage:
    python3 pipeline_crunching/build_knowledge_base.py

Then restart webapp/chat_server.py (or run `python3 webapp/local_rag_chat.py --rebuild`) to pick
up the changes in the live embedding index -- this script only touches knowledge_base/ on disk,
it does not touch the running webapp's in-memory index.
"""
import os
import json

PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PIPELINE_ROOT)

USERS_DIR = os.path.join(REPO_ROOT, "users")
KNOWLEDGE_DIR = os.path.join(REPO_ROOT, "knowledge_base")

# Same four categories pipeline_crunching/merge_data.py uses -- this script is that script's
# sibling, publishing one file per chunk instead of one merged-blob file per category, since that
# per-chunk shape is what the current retrieval pipeline (local_rag_chat.py) actually needs.
DATASET_TYPES = {
    "wiki.jsonl": "docs",
    "codebase.jsonl": "codebase",
    "addon_studio.jsonl": "addon_creator",
    "github_reviews.jsonl": "reviews",
}


def format_chunk_as_kb_md(chunk: dict) -> str:
    # Mirrors the existing knowledge_base/*.md format exactly (title as H1, then Type/Keywords/
    # Symbols/Concepts, Summary/Explanation/Related Questions sections, Source footer) -- title
    # already contains "[tier/file] - Chunk N" (or "PR #N review diff" for reviews), built
    # client-side in CUBYZ_FOLDING.py at submission time, so no extra lookups are needed here.
    lines = [f"# {chunk.get('title', 'Untitled Chunk')}", ""]
    if chunk.get("chunk_type"):
        lines.append(f"**Type:** {chunk['chunk_type']}")
    if chunk.get("keywords"):
        lines.append(f"**Keywords:** {', '.join(chunk['keywords'])}")
    if chunk.get("symbols"):
        lines.append(f"**Symbols:** {', '.join(chunk['symbols'])}")
    if chunk.get("concepts"):
        lines.append(f"**Concepts:** {', '.join(chunk['concepts'])}")
    lines.append("")
    if chunk.get("summary"):
        lines.append("## Summary")
        lines.append(chunk["summary"])
        lines.append("")
    if chunk.get("comprehensive_explanation"):
        lines.append("## Explanation")
        lines.append(chunk["comprehensive_explanation"])
        lines.append("")
    if chunk.get("code_example"):
        lines.append("## Code Example")
        lines.append(f"```zig\n{chunk['code_example']}\n```")
        lines.append("")
    if chunk.get("synthetic_queries"):
        lines.append("## Related Questions")
        lines.extend(f"- {q}" for q in chunk["synthetic_queries"])
        lines.append("")
    lines.append(f"*Source: unknown | chunk_id: {chunk['chunk_id']}*")
    text = "\n".join(lines) + "\n"
    # Some source content (e.g. a code_example pulled from a GitHub diff) carries embedded \r\n.
    # Writing that raw would leave literal \r\n on disk, but reading it back applies universal
    # newline translation (\r\n -> \n) -- the two would never compare equal, so the file would
    # look "updated" and get rewritten on every single run forever. Normalize once here instead.
    return text.replace("\r\n", "\n").replace("\r", "\n")


def build_knowledge_base():
    if not os.path.exists(USERS_DIR):
        print(f"[X] Directory '{USERS_DIR}' not found.")
        return

    added, updated, unchanged, skipped = 0, 0, 0, 0

    for filename, kb_subdir in DATASET_TYPES.items():
        target_dir = os.path.join(KNOWLEDGE_DIR, kb_subdir)
        os.makedirs(target_dir, exist_ok=True)

        seen_chunk_ids = set()
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

                        chunk_id = chunk.get("chunk_id")
                        if not chunk_id:
                            continue
                        # First submission of a given chunk_id across all users wins, same
                        # tie-break merge_data.py already uses -- duplicates only happen from a
                        # stale-lock race (rare), not normal operation.
                        if chunk_id in seen_chunk_ids:
                            skipped += 1
                            continue
                        seen_chunk_ids.add(chunk_id)

                        out_path = os.path.join(target_dir, f"{chunk_id}.md")
                        new_content = format_chunk_as_kb_md(chunk)

                        if os.path.exists(out_path):
                            with open(out_path, "r", encoding="utf-8") as existing_f:
                                if existing_f.read() == new_content:
                                    unchanged += 1
                                    continue
                            updated += 1
                        else:
                            added += 1

                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(new_content)
            except Exception as e:
                print(f"[!] Error reading {dataset_path}: {e}")

    print(f"[✓] Knowledge base publish complete -- {added} new, {updated} updated, {unchanged} unchanged"
          + (f", {skipped} duplicate chunk_ids skipped" if skipped else "") + ".")
    if added or updated:
        print("[~] Restart webapp/chat_server.py (or run `python3 local_rag_chat.py --rebuild` from")
        print("    webapp/) to pick up the new/changed content in the live embedding index.")


if __name__ == "__main__":
    build_knowledge_base()
