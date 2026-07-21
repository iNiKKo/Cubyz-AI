"""
Filters users/*/codebase.jsonl (1,476 chunks) down to the subset worth fine-tuning on:
architectural/conceptual understanding, not exact symbol-level facts that go stale as Cubyz
ships new versions. Everything excluded here stays RAG-only (still fully retrievable, just not
baked into weights).

Filter logic (two factors, both derived from fields the crunching pipeline already validated --
no new LLM calls needed):
  1. chunk_type:
     - Always included: world_generation, algorithm, gameplay, networking -- these are
       inherently "how does this system work" chunks by category.
     - Never included: configuration -- the largest category (857/1476) but almost entirely
       per-asset .zig.zon stat blocks (biome/block/recipe data), not architecture. Also the
       category most likely to go stale as content gets added/tuned.
     - Conditionally included (see #2): implementation, api, serialization -- these are a mix
       of genuine architecture and narrow utility/precise-signature detail.
  2. difficulty tier (embedded in the title field, e.g. "[easy/path] - Chunk N"): for the
     conditional chunk_types, only medium/hard tier chunks qualify. Easy-tier chunks in these
     categories tend to be short utility functions, not systems worth explaining conceptually.

Output: finetune/source_data/codebase_architectural_subset.jsonl
"""
import json
import os
import re

USERS_DIR = "pipeline/users"
OUTPUT_FILE = "pipeline/finetune/source_data/codebase_architectural_subset.jsonl"

ALWAYS_INCLUDE_TYPES = {"world_generation", "algorithm", "gameplay", "networking"}
CONDITIONAL_TYPES = {"implementation", "api", "serialization"}
CONDITIONAL_MIN_TIER = {"medium", "hard"}

TIER_RE = re.compile(r"\[(easy|medium|hard)/")


def load_deduped_codebase_chunks():
    seen = set()
    entries = []
    for user in sorted(os.listdir(USERS_DIR)):
        path = os.path.join(USERS_DIR, user, "codebase.jsonl")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                chunk = json.loads(line)
                if chunk["chunk_id"] in seen:
                    continue
                seen.add(chunk["chunk_id"])
                entries.append(chunk)
    return entries


def tier_of(chunk: dict) -> str:
    m = TIER_RE.search(chunk.get("title", ""))
    return m.group(1) if m else "unknown"


def qualifies(chunk: dict) -> bool:
    chunk_type = chunk.get("chunk_type")
    if chunk_type in ALWAYS_INCLUDE_TYPES:
        return True
    if chunk_type in CONDITIONAL_TYPES:
        return tier_of(chunk) in CONDITIONAL_MIN_TIER
    return False


def main():
    entries = load_deduped_codebase_chunks()
    filtered = [c for c in entries if qualifies(c)]

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for chunk in filtered:
            f.write(json.dumps(chunk) + "\n")

    by_type = {}
    for c in filtered:
        by_type[c["chunk_type"]] = by_type.get(c["chunk_type"], 0) + 1

    print(f"[OK] {len(entries)} total codebase chunks -> {len(filtered)} architectural subset ({len(filtered)/len(entries)*100:.1f}%)")
    print(f"[OK] Written to {OUTPUT_FILE}")
    print("Breakdown by chunk_type:")
    for t, n in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t}: {n}")


if __name__ == "__main__":
    main()
