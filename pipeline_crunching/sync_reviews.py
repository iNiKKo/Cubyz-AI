"""
One-command PR/issue refresh, the reviews-collection counterpart to sync_codebase.py: runs
extract_reviews.py (PR review comments) and extract_issues.py (issue discussions) to pull
anything new from GitHub, then re-runs dataset_sorter.py's tiering so the result is ready for
the next RAG crunching campaign.

Both extractors are already incremental on their own (closed PRs/issues are tracked in
campaign_state/processed_prs.txt and processed_issues.txt and never re-scanned; open ones are
re-scanned every run since their threads can still grow) -- this script doesn't add its own
incremental logic, it just runs both in sequence and re-tiers.

Usage:
    export GITHUB_TOKEN=...   # strongly recommended, see extract_reviews.py/extract_issues.py
    python3 pipeline_crunching/sync_reviews.py
"""
import os
import sys

import extract_reviews
import extract_issues
import dataset_sorter


def main():
    if not os.environ.get("GITHUB_TOKEN"):
        print("[!] No GITHUB_TOKEN set -- unauthenticated GitHub requests are capped at "
              "60/hour, which a repo this size will burn through fast. Recommended:\n"
              "      export GITHUB_TOKEN=ghp_...\n"
              "    before running this again. Continuing anyway...\n")

    print("=" * 60)
    print("STEP 1/3: PR review comments")
    print("=" * 60)
    extract_reviews.main()

    print("\n" + "=" * 60)
    print("STEP 2/3: Issue discussions")
    print("=" * 60)
    extract_issues.main()

    print("\n" + "=" * 60)
    print("STEP 3/3: Re-tiering into organized_cubyz_dataset/")
    print("=" * 60)
    dataset_sorter.organize_dataset()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n[X] Interrupted -- already-fetched data was saved incrementally, safe to re-run.")
