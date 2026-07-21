import os
import shutil
import sys

# Anchored to this script's own directory rather than the process's cwd -- same reasoning as
# webapp/local_rag_chat.py's REPO_ROOT pattern. raw_cubyz_dataset/ and organized_cubyz_dataset/
# live alongside this script since they're only ever used by the pipeline_crunching scripts.
PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))

SOURCE_DIR = os.path.join(PIPELINE_ROOT, "raw_cubyz_dataset")
OUTPUT_DIR = os.path.join(PIPELINE_ROOT, "organized_cubyz_dataset")

TIERS = ("easy", "medium", "hard")

ACCEPTABLE_EXTENSIONS = ('.txt', '.md', '.zig', '.zon', '.json', '.html', '.js', '.sh')

EASY_MAX_LINES = 150
MEDIUM_MAX_LINES = 450


def count_lines(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return sum(1 for _ in f)


def determine_tier(file: str, top_folder: str, file_path: str) -> str:

    if file.lower().endswith('.json') or top_folder == 'github':
        return "hard"

    line_count = count_lines(file_path)
    if line_count <= EASY_MAX_LINES:
        return "easy"
    elif line_count <= MEDIUM_MAX_LINES:
        return "medium"
    else:
        return "hard"


def build_unique_filename(rel_path: str, file: str) -> str:

    if rel_path == ".":
        return file
    return f"{rel_path.replace(os.sep, '_')}_{file}"


def organize_dataset():
    print("=== Cubyz Dataset Automation Sorter ===")

    if not os.path.exists(SOURCE_DIR):
        print(f"[X] Source directory '{SOURCE_DIR}' not found!")
        print(f"Please create '{SOURCE_DIR}' and place your folders/files inside it.")
        sys.exit(1)

    for tier in TIERS:
        os.makedirs(os.path.join(OUTPUT_DIR, tier), exist_ok=True)

    counters = {"easy": 0, "medium": 0, "hard": 0, "skipped": 0}
    # Every (tier, unique_filename) this run actually produces -- used below to remove anything
    # already sitting in OUTPUT_DIR that this run did NOT produce. Without this, a file renamed
    # or deleted upstream (now automated via sync_codebase.py rather than hand-copied, so this
    # will actually happen routinely) left its old organized copy behind forever: the crunching
    # campaign would keep tracking and re-verifying content for a file that no longer exists.
    # Tracked as (tier, filename) pairs, not just filename, since a file crossing a line-count
    # threshold between runs legitimately moves tiers -- the OLD tier's copy is exactly as stale
    # as one from a deleted file and needs the same cleanup.
    produced = set()

    print(f"[~] Scanning '{SOURCE_DIR}' for valid tracking files...")

    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.lower().endswith(ACCEPTABLE_EXTENSIONS):
                counters["skipped"] += 1
                continue

            file_path = os.path.join(root, file)

            try:
                rel_path = os.path.relpath(root, SOURCE_DIR)
                top_folder = rel_path.split(os.sep)[0].lower() if rel_path != "." else ""

                tier_target = determine_tier(file, top_folder, file_path)
                unique_filename = build_unique_filename(rel_path, file)

                destination_path = os.path.join(OUTPUT_DIR, tier_target, unique_filename)
                shutil.copy2(file_path, destination_path)
                counters[tier_target] += 1
                produced.add((tier_target, unique_filename))

            except Exception as e:
                print(f"[!] Warning: Error reading file {file}: {e}")
                counters["skipped"] += 1

    # Scoped to "codebase_"-prefixed files ONLY -- confirmed live that organized_cubyz_dataset/
    # is NOT entirely derived from raw_cubyz_dataset/: several docs_* files and
    # hard/issues_issues.json exist in the organized output with no corresponding raw source
    # anywhere (hand-added directly at some point, bypassing this script). A blanket "remove
    # anything this run didn't produce" pass deleted those on first test -- codebase/ is the one
    # folder that's fully automated (sync_codebase.py wipes and regenerates it from a git clone
    # every run, nothing hand-edited lives there), so it's the only prefix safe to auto-clean.
    removed = 0
    for tier in TIERS:
        tier_dir = os.path.join(OUTPUT_DIR, tier)
        for existing in os.listdir(tier_dir):
            if existing.startswith("codebase_") and (tier, existing) not in produced:
                os.remove(os.path.join(tier_dir, existing))
                removed += 1

    print("\n[✓] Dataset Sorting Complete!")
    print(f"    🟢 EASY Files (<= {EASY_MAX_LINES} lines):   {counters['easy']}")
    print(f"    🟡 MEDIUM Files ({EASY_MAX_LINES + 1}-{MEDIUM_MAX_LINES} lines): {counters['medium']}")
    print(f"    🔴 HARD Files (> {MEDIUM_MAX_LINES} lines):     {counters['hard']}")
    print(f"    ⚪ SKIPPED Files (other types):  {counters['skipped']}")
    print(f"    🗑️  Removed (no longer in source): {removed}")
    print(f"\nYour sorted dataset folders are located under: '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    organize_dataset()
