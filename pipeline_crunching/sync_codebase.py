"""
Replaces the manual "clone Cubyz, copy src/mods/assets into raw_cubyz_dataset/codebase by hand"
step with an automated one: clones (or updates) the real PixelGuys/Cubyz repo, mirrors its
src/, mods/, and assets/ folders into raw_cubyz_dataset/codebase/, then runs dataset_sorter.py's
existing easy/medium/hard tiering so the result lands straight in organized_cubyz_dataset/ ready
for the next RAG crunching campaign.

Only touches codebase/ -- docs/, addon_creator/, and reviews/ under raw_cubyz_dataset/ have
other, non-git-clone sources (the repo's own docs/ folder is only part of what's under docs/,
the rest is wiki content and hand-authored material; addon_creator/ comes from a separate repo;
reviews/ comes from the GitHub API, not a clone) and are left exactly as they are.

Usage:
    python3 pipeline_crunching/sync_codebase.py
"""
import os
import shutil
import subprocess
import sys

import dataset_sorter

PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
UPSTREAM_REPO_URL = "https://github.com/PixelGuys/Cubyz.git"
UPSTREAM_CLONE_DIR = os.path.join(PIPELINE_ROOT, "_cubyz_upstream_clone")
CODEBASE_RAW_DIR = os.path.join(dataset_sorter.SOURCE_DIR, "codebase")

# The exact subfolders raw_cubyz_dataset/codebase/ has always mirrored -- confirmed against the
# real repo layout (src/, mods/, assets/ at the repo root) and against what was already there
# from the manual process this replaces.
SYNCED_SUBDIRS = ("src", "mods", "assets")


def _run(cmd, **kwargs):
    print(f"[~] {' '.join(cmd)}")
    subprocess.run(cmd, check=True, **kwargs)


def sync_upstream_clone():
    """Clones PixelGuys/Cubyz on first run, or fast-forwards an existing clone on every run
    after. --depth 1 + a fetch/reset (not a full-history pull) since nothing here ever needs
    Cubyz's own commit history -- only the current state of a few folders."""
    if not os.path.exists(os.path.join(UPSTREAM_CLONE_DIR, ".git")):
        print(f"[~] No local clone yet -- cloning {UPSTREAM_REPO_URL} (shallow)...")
        if os.path.exists(UPSTREAM_CLONE_DIR):
            shutil.rmtree(UPSTREAM_CLONE_DIR)  # leftover partial/non-git directory, if any
        _run(["git", "clone", "--depth", "1", UPSTREAM_REPO_URL, UPSTREAM_CLONE_DIR])
        return

    print(f"[~] Updating existing clone at {UPSTREAM_CLONE_DIR}...")
    _run(["git", "fetch", "--depth", "1", "origin", "main"], cwd=UPSTREAM_CLONE_DIR)
    _run(["git", "reset", "--hard", "origin/main"], cwd=UPSTREAM_CLONE_DIR)


def mirror_codebase_folders():
    """Fully replaces raw_cubyz_dataset/codebase/{src,mods,assets} with what's in the fresh
    clone -- a full wipe+recopy, not an incremental diff, which is safe here specifically because
    nothing ever hand-edits files inside raw_cubyz_dataset/codebase/ (unlike docs/, which mixes
    in wiki/hand-authored content and must never be touched by this script). Renamed/deleted
    upstream files are handled by this wipe on the raw side, and by dataset_sorter.py's own
    stale-cleanup (see its produced/removed tracking) on the organized_cubyz_dataset/ side."""
    for subdir in SYNCED_SUBDIRS:
        src = os.path.join(UPSTREAM_CLONE_DIR, subdir)
        dst = os.path.join(CODEBASE_RAW_DIR, subdir)
        if not os.path.isdir(src):
            print(f"[!] Warning: upstream repo has no '{subdir}/' -- skipping (layout may have changed).")
            continue
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"[OK] Synced {subdir}/ -> {dst}")


def main():
    os.makedirs(CODEBASE_RAW_DIR, exist_ok=True)
    sync_upstream_clone()
    mirror_codebase_folders()
    print()
    dataset_sorter.organize_dataset()


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(f"[X] Git command failed ({e}). Is git installed and is github.com reachable?")
