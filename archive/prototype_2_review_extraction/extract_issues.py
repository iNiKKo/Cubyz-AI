"""
Extracts GitHub Issue discussions (not PRs) from PixelGuys/Cubyz for the same purpose as
extract_reviews.py -- behavioral/judgment training material -- but a different slice of it.
PR reviews teach "is this code change good and why" (code-quality judgment). Issues teach
"here's a reported problem, diagnose it" -- symptom -> hypothesis -> root cause -> resolution,
the same shape as the "Debugging help" behavior already called out in webapp/local_rag_chat.py's
system prompt. Complementary source, not a duplicate of the review extractor.

Different content shape than reviews, so this is its own script rather than a flag on
extract_reviews.py: issues have no diff hunks to anchor against, and the valuable part is the
comment THREAD (symptom -> maintainer diagnosis -> resolution), not any single comment in
isolation the way a self-contained PR review comment is. So this produces one chunk per
qualifying ISSUE (title + body + filtered discussion), not one per comment.

Output slots into the RAG pipeline via the same GITHUB_REVIEWS category reviews already use --
pipeline_crunching/server.py's rag_initialize_chunks() treats ANY .json file in a tier folder as
a pre-chunked review-shaped array (see its `file.lower().endswith('.json')` check), and the
crunching prompt's GITHUB_REVIEWS role already covers "bug cause" reasoning explicitly. No
pipeline changes needed -- just drop the output where organized_cubyz_dataset/ can see it.

Usage:
    export GITHUB_TOKEN=...   # strongly recommended -- issue+comment fetching is call-heavy
    python3 extract_issues.py
"""
import json
import os
import time
import requests


# ============================================================
# CONFIGURATION
# ============================================================

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

REPO_OWNER = "PixelGuys"
REPO_NAME = "Cubyz"

OUTPUT_FILE = "cubyz_issues_dataset.json"
# Closed issues only -- a closed issue's discussion is final. Open issues are NOT tracked here
# and get re-scanned every run instead, same reasoning as extract_reviews.py's open-PR handling:
# their threads can still grow, and comment-level dedup within create_issue_chunk keeps re-scans
# cheap and safe.
STATE_FILE = "processed_issues.txt"

MAX_ISSUES = 3000
PER_PAGE = 100

# Below this many substantive (post-filter) comments, an issue's discussion isn't a real
# diagnosis thread -- just a report that got closed with no real back-and-forth.
MIN_SUBSTANTIVE_COMMENTS = 1

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Cubyz-Dataset-Extractor"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

SESSION = requests.Session()
SESSION.headers.update(HEADERS)


# ============================================================
# GITHUB API HANDLER (identical to extract_reviews.py)
# ============================================================

def github_request(url):
    while True:
        try:
            response = SESSION.get(url, timeout=30)

            if response.status_code == 403:
                remaining = response.headers.get("X-RateLimit-Remaining")
                reset = response.headers.get("X-RateLimit-Reset")
                if remaining == "0" and reset:
                    wait_time = int(reset) - int(time.time()) + 5
                    print(f"[!] Rate limit reached. Sleeping {wait_time}s...")
                    time.sleep(max(wait_time, 5))
                    continue

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print("[!] Timeout. Retrying...")
            time.sleep(5)

        except requests.exceptions.RequestException as e:
            print(f"[X] GitHub request failed: {e}")
            time.sleep(10)


# ============================================================
# DATA STORAGE (identical pattern to extract_reviews.py)
# ============================================================

def load_processed_issues():
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE, "r", encoding="utf-8") as file:
        return {int(line.strip()) for line in file if line.strip().isdigit()}


def save_processed_issues(issue_numbers):
    if not issue_numbers:
        return
    with open(STATE_FILE, "a", encoding="utf-8") as file:
        for num in issue_numbers:
            file.write(f"{num}\n")


def load_dataset():
    if not os.path.exists(OUTPUT_FILE):
        return []
    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("[!] Dataset corrupted. Starting empty.")
        return []


# ============================================================
# COMMENT FILTERING
# ============================================================

# GitHub's author_association field on issues/comments -- these mean the commenter has real
# authority on the project, so their diagnosis carries the judgment/voice this dataset wants.
MAINTAINER_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}

LOW_VALUE_PHRASES = [
    "+1",
    "same here",
    "same issue",
    "any updates",
    "any update?",
    "closing as stale",
    "closing this",
    "duplicate of",
    "me too",
    "bump",
    "still happening",
    "still an issue",
    "can confirm",
    "thanks!",
    "thank you!",
]


def is_substantive_comment(comment):
    """A comment worth keeping in the discussion thread -- real diagnostic content, not noise."""
    body = (comment.get("body") or "").strip()
    if not body:
        return False

    body_lower = body.lower()
    if any(phrase in body_lower for phrase in LOW_VALUE_PHRASES):
        return False

    words = body.split()
    is_maintainer = comment.get("author_association") in MAINTAINER_ASSOCIATIONS

    # Maintainer comments get a lower bar -- a short "it's X, fixed in Y" from a maintainer is
    # exactly the judgment/diagnosis signal this is collecting. Non-maintainer comments need more
    # length to be worth keeping (a real bug report/repro, not a one-line reaction).
    min_words = 6 if is_maintainer else 15
    return len(words) >= min_words


# ============================================================
# GITHUB ISSUE FETCHING
# ============================================================

def get_issues(state, limit):
    """Retrieves issues (not PRs) in the given state, newest-updated first."""
    page = 1
    fetched = 0

    while fetched < limit:
        url = (
            f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
            f"?state={state}&sort=updated&direction=desc&per_page={PER_PAGE}&page={page}"
        )
        items = github_request(url)
        if not items:
            break

        for item in items:
            # The /issues endpoint returns PRs too (GitHub treats every PR as an issue under the
            # hood) -- skip anything that's actually a PR, extract_reviews.py already covers those.
            if "pull_request" in item:
                continue
            yield item
            fetched += 1
            if fetched >= limit:
                break

        page += 1


def get_closed_issues():
    return get_issues("closed", MAX_ISSUES)


def get_open_issues():
    return get_issues("open", MAX_ISSUES)


def get_issue_comments(issue_number):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments"
    return github_request(url) or []


# ============================================================
# DATASET CHUNK CREATION
# ============================================================

def create_issue_chunk(issue, substantive_comments):
    number = issue["number"]
    title = issue.get("title", "")
    body = (issue.get("body") or "").strip()

    discussion_parts = []
    for c in substantive_comments:
        role = "MAINTAINER" if c.get("author_association") in MAINTAINER_ASSOCIATIONS else "USER"
        discussion_parts.append(f"[{role} COMMENT]\n{c.get('body', '').strip()}")

    raw_content = (
        f"// ISSUE TITLE: {title}\n"
        f"// ISSUE REPORT:\n{body}\n\n"
        f"// DISCUSSION:\n" + "\n\n".join(discussion_parts)
    )

    return {
        "file_name": f"issue_{number}.md",
        "relative_path": f"issues/issue_{number}.md",
        "directory_context": "GITHUB_REVIEWS",
        "chunk_id": f"github_issue_{number}_discussion",
        "chunk_index": number,
        "raw_content": raw_content,
    }


def process_issue(issue):
    number = issue["number"]
    print(f"[~] Scanning Issue #{number}: {issue.get('title', '')}")

    comments = get_issue_comments(number)
    substantive = [c for c in comments if is_substantive_comment(c)]

    if len(substantive) < MIN_SUBSTANTIVE_COMMENTS:
        return None

    return create_issue_chunk(issue, substantive)


# ============================================================
# MAIN EXECUTION
# ============================================================

def _scan_issues(issues, existing_chunk_ids, processed_issues, track_processed):
    new_chunks = []
    completed = []
    scanned = 0
    skipped = 0

    for issue in issues:
        number = issue["number"]

        if track_processed and number in processed_issues:
            skipped += 1
            continue

        scanned += 1
        chunk = process_issue(issue)

        if chunk is not None and chunk["chunk_id"] not in existing_chunk_ids:
            existing_chunk_ids.add(chunk["chunk_id"])
            new_chunks.append(chunk)
            print(f"[✓] Issue #{number} added (real discussion found)")
        else:
            print(f"[~] Issue #{number} skipped (no substantive discussion)")

        if track_processed:
            completed.append(number)

    return new_chunks, scanned, skipped, completed


def main():
    print(f"[~] Starting issue-discussion extraction for {REPO_OWNER}/{REPO_NAME} "
          f"(closed issues, permanently tracked, + open issues, re-scanned every run)")

    processed_issues = load_processed_issues()
    dataset = load_dataset()
    existing_chunk_ids = {item.get("chunk_id") for item in dataset if "chunk_id" in item}

    closed_chunks, closed_scanned, closed_skipped, closed_completed = _scan_issues(
        get_closed_issues(), existing_chunk_ids, processed_issues, track_processed=True
    )
    open_chunks, open_scanned, open_skipped, _ = _scan_issues(
        get_open_issues(), existing_chunk_ids, processed_issues, track_processed=False
    )

    new_chunks = closed_chunks + open_chunks
    scanned = closed_scanned + open_scanned
    skipped = closed_skipped + open_skipped

    if not scanned:
        print("[✓] No new issues to process.")
        return

    save_processed_issues(closed_completed)
    dataset.extend(new_chunks)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(dataset, file, indent=4, ensure_ascii=False)

    print("\n========== COMPLETE ==========")
    print(f"Issues scanned: {scanned} ({closed_scanned} closed, {open_scanned} open)")
    print(f"Issues skipped: {skipped} ({closed_skipped} closed, already processed)")
    print(f"New issue-discussion chunks: {len(new_chunks)}")
    print(f"Total dataset size: {len(dataset)}")


if __name__ == "__main__":
    main()
