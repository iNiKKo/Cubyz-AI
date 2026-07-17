import os
import re
import json

USERS_DIR = "users"
OUTPUT_DIR = "openwebui_knowledge"

# One output folder per Open WebUI "Knowledge" collection. Keep these as four separate
# collections (not one merged blob) so a custom Model can attach only the ones relevant to it,
# and so retrieval scoring for e.g. a debugging question isn't diluted by addon-studio UI chunks.
DATASET_TYPES = {
    "codebase.jsonl": "codebase",
    "wiki.jsonl": "docs",
    "addon_studio.jsonl": "addon_creator",
    "github_reviews.jsonl": "reviews",
}

_UNSAFE_CHARS = re.compile(r'[^A-Za-z0-9_.-]+')


def safe_filename(chunk_id: str) -> str:
    return _UNSAFE_CHARS.sub("_", chunk_id).strip("_")[:150] or "chunk"


def format_chunk_as_document(chunk: dict) -> str:
    # Keywords/symbols/concepts are hoisted right under the title, ahead of the prose, so
    # Open WebUI's lexical/BM25 side of hybrid search has exact identifier tokens to match
    # against -- this is what a pasted error message or a "what does X do" question hits on,
    # which pure embedding similarity over prose alone was missing.
    parts = [f"# {chunk.get('title', 'Untitled Chunk')}\n"]

    if chunk.get("chunk_type"):
        parts.append(f"**Type:** {chunk['chunk_type']}")
    if chunk.get("keywords"):
        parts.append(f"**Keywords:** {', '.join(chunk['keywords'])}")
    if chunk.get("symbols"):
        parts.append(f"**Symbols:** {', '.join(chunk['symbols'])}")
    if chunk.get("concepts"):
        parts.append(f"**Concepts:** {', '.join(chunk['concepts'])}")
    parts.append("")

    if chunk.get("summary"):
        parts.append(f"## Summary\n{chunk['summary']}\n")
    if chunk.get("comprehensive_explanation"):
        parts.append(f"## Explanation\n{chunk['comprehensive_explanation']}\n")
    if chunk.get("code_example"):
        parts.append(f"## Code Example\n```zig\n{chunk['code_example']}\n```\n")
    if chunk.get("synthetic_queries"):
        # Embedding these alongside the prose pulls this chunk's vector closer to how a real
        # user is likely to phrase the same question, since these were written as retrieval
        # queries in the first place.
        parts.append("## Related Questions\n" + "\n".join(f"- {q}" for q in chunk["synthetic_queries"]) + "\n")

    # Deliberately omits contributor/user_id -- that's pipeline provenance (who crunched this
    # chunk), not a fact about Cubyz, and including it in the indexed/embedded text caused the
    # model to answer "who made Cubyz" with a volunteer's name pattern-matched from these lines.
    parts.append(f"*Source: {chunk.get('relative_path', 'unknown')} | chunk_id: {chunk.get('chunk_id', 'unknown')}*\n")
    return "\n".join(parts)


def export():
    if not os.path.exists(USERS_DIR):
        print(f"[X] Directory '{USERS_DIR}' not found.")
        return

    for folder in DATASET_TYPES.values():
        os.makedirs(os.path.join(OUTPUT_DIR, folder), exist_ok=True)

    print("[~] Exporting per-chunk documents for Open WebUI Knowledge collections...")

    for filename, out_folder in DATASET_TYPES.items():
        seen_chunk_ids = set()
        written, skipped_dupe, skipped_bad = 0, 0, 0

        for user_folder in sorted(os.listdir(USERS_DIR)):
            user_path = os.path.join(USERS_DIR, user_folder)
            if not os.path.isdir(user_path):
                continue

            dataset_path = os.path.join(user_path, filename)
            if not os.path.exists(dataset_path):
                continue

            with open(dataset_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        chunk = json.loads(line)
                    except Exception:
                        skipped_bad += 1
                        continue

                    chunk_id = chunk.get("chunk_id")
                    if chunk_id:
                        if chunk_id in seen_chunk_ids:
                            skipped_dupe += 1
                            continue
                        seen_chunk_ids.add(chunk_id)
                    else:
                        chunk_id = f"unknown_{written}"

                    doc_text = format_chunk_as_document(chunk)
                    out_path = os.path.join(OUTPUT_DIR, out_folder, safe_filename(chunk_id) + ".md")
                    with open(out_path, "w", encoding="utf-8") as out_f:
                        out_f.write(doc_text)
                    written += 1

        print(f"[✓] {out_folder}: {written} files written"
              f"{f', {skipped_dupe} duplicates skipped' if skipped_dupe else ''}"
              f"{f', {skipped_bad} corrupt lines skipped' if skipped_bad else ''}"
              f" -> {os.path.join(OUTPUT_DIR, out_folder)}/")

    print(f"\n[✓] Done. Upload each folder in '{OUTPUT_DIR}/' as its own Open WebUI Knowledge collection.")


if __name__ == "__main__":
    export()
