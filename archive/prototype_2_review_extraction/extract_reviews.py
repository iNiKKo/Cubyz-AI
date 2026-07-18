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

OUTPUT_FILE = "cubyz_reviews_dataset.json"
# Closed PRs only -- a closed PR's review thread is final, so once scanned it never needs
# re-checking. Open PRs are NOT tracked here (see get_open_pull_requests()): their review threads
# are still active and can grow new comments, so every run re-scans all currently-open PRs. This
# is cheap (comment-level chunk_id dedup in main() already skips anything already collected) and
# means a comment only gets picked up once it actually exists, without needing this script to
# separately notice "this open PR grew a new comment since last time."
STATE_FILE = "processed_prs.txt"

# Maximum amount of closed PRs to scan per run
MAX_PULL_REQUESTS = 2000

# GitHub maximum allowed
PER_PAGE = 100


HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Cubyz-Dataset-Extractor"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


# Reuse HTTP connections
SESSION = requests.Session()
SESSION.headers.update(HEADERS)



# ============================================================
# GITHUB API HANDLER
# ============================================================

def github_request(url):
    """
    Sends GitHub API requests with automatic rate limit handling.
    """

    while True:
        try:
            response = SESSION.get(url, timeout=30)

            # Rate limit reached
            if response.status_code == 403:

                remaining = response.headers.get(
                    "X-RateLimit-Remaining"
                )

                reset = response.headers.get(
                    "X-RateLimit-Reset"
                )

                if remaining == "0" and reset:
                    wait_time = int(reset) - int(time.time()) + 5

                    print(
                        f"[!] Rate limit reached. "
                        f"Sleeping {wait_time}s..."
                    )

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
# DATA STORAGE
# ============================================================

def load_processed_prs():
    """
    Loads already completed PR numbers.
    """

    if not os.path.exists(STATE_FILE):
        return set()

    with open(
        STATE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return {
            int(line.strip())
            for line in file
            if line.strip().isdigit()
        }



def save_processed_prs(pr_numbers):
    """
    Saves processed PR numbers in one write operation.
    """

    if not pr_numbers:
        return

    with open(
        STATE_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        for pr in pr_numbers:
            file.write(f"{pr}\n")



def load_dataset():
    """
    Loads existing JSON dataset.
    """

    if not os.path.exists(OUTPUT_FILE):
        return []

    try:
        with open(
            OUTPUT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:
        print(
            "[!] Dataset corrupted. Starting empty."
        )

        return []
# ============================================================
# COMMENT FILTERING
# ============================================================

def is_tier_1_only(comment_body):
    """
    Keeps only high-level architecture/code quality reviews.
    """

    if not comment_body:
        return False


    body = comment_body.lower()


    # Remove low-value comments. "color"/"fog" deliberately removed from here -- as bare words
    # they reject legitimate architectural discussion that happens to mention a rendering/fog
    # system (e.g. a real comment about gpu_performance_measuring for Skybox rendering got
    # rejected purely for containing "fog" nowhere near a rendering context). Kept only as
    # specific dismissive phrases, which is what this list is actually trying to catch.
    blacklist = [
        "sorry",
        "idk",
        "i didn't know",
        "i didnt know",
        "close this",
        "can we close",
        "can i close",
        "does this mean",
        "is this ready",
        "typo",
        "spelling",
        "grammar",
        "just a color",
        "wrong color",
        "look better"
    ]


    if any(word in body for word in blacklist):
        return False



    words = body.split()


    # Architectural reviews normally need explanation
    if len(words) < 12:
        return False



    structural_keywords = [
        "allocator",
        "alloc",
        "memory",
        "leak",
        "deinit",
        "free",
        "struct",
        "pointer",
        "hashmap",
        "array",
        "lifetime",
        "parser",
        "copy",
        "performance",
        "optimization",
        "optimize",
        "redundant",
        "refactor",
        "architecture",
        "design",
        "ownership"
    ]


    has_structure = any(
        key in body
        for key in structural_keywords
    )


    has_suggestion = (
        "```suggestion" in body
        and len(words) > 20
    )


    return has_structure or has_suggestion




# ============================================================
# GITHUB PR FETCHING
# ============================================================

def get_pull_requests(state, limit):
    """
    Retrieves PRs in the given state ("closed" or "open") from newest to oldest.
    """

    page = 1
    fetched = 0


    while fetched < limit:

        url = (
            f"https://api.github.com/repos/"
            f"{REPO_OWNER}/{REPO_NAME}/pulls"
            f"?state={state}"
            f"&sort=updated"
            f"&direction=desc"
            f"&per_page={PER_PAGE}"
            f"&page={page}"
        )


        pull_requests = github_request(url)


        if not pull_requests:
            break



        for pr in pull_requests:

            yield pr

            fetched += 1


            if fetched >= limit:
                break


        page += 1


def get_closed_pull_requests():
    return get_pull_requests("closed", MAX_PULL_REQUESTS)


def get_open_pull_requests():
    # No cap to speak of -- Cubyz's open-PR count is small (low hundreds at most), nowhere near
    # MAX_PULL_REQUESTS, and every one of them gets re-scanned every run anyway (see STATE_FILE
    # comment above), so there's no meaningful "too many to handle" case here.
    return get_pull_requests("open", MAX_PULL_REQUESTS)




# ============================================================
# COMMENT EXTRACTION
# ============================================================

def extract_pr_comments(pr_number):
    """
    Gets review comments attached to changed files.
    """

    url = (
        f"https://api.github.com/repos/"
        f"{REPO_OWNER}/{REPO_NAME}"
        f"/pulls/{pr_number}/comments"
    )


    return github_request(url) or []





# ============================================================
# DATASET CHUNK CREATION
# ============================================================

def create_chunk(pr_number, comment):
    """
    Converts GitHub review comments into training data.
    """

    path = comment.get("path", "")

    directory, filename = os.path.split(path)


    return {
        "file_name": filename,

        "relative_path": path,

        "directory_context": directory,

        "chunk_id":
            f"github_pr_{pr_number}_comment_{comment['id']}",

        "chunk_index":
            comment["id"],

        "raw_content":
            (
                f"// FILE TARGET: {path}\n"
                f"// CODE DIFF CONTEXT:\n"
                f"{comment.get('diff_hunk', '')}\n\n"
                f"// CRITICAL ARCHITECTURAL REVIEW:\n"
                f"{comment.get('body', '')}"
            )
    }





# ============================================================
# PROCESS SINGLE PR
# ============================================================

def process_pull_request(pr):
    """
    Scans one PR and returns valid dataset chunks.
    """

    pr_number = pr["number"]

    print(
        f"[~] Scanning PR #{pr_number}: "
        f"{pr['title']}"
    )


    chunks = []


    comments = extract_pr_comments(
        pr_number
    )


    for comment in comments:

        path = comment.get(
            "path",
            ""
        )


        # Only Zig source files
        if not path.lower().endswith(".zig"):
            continue



        body = comment.get(
            "body",
            ""
        )


        if not is_tier_1_only(body):
            continue



        chunks.append(
            create_chunk(
                pr_number,
                comment
            )
        )


    return chunks

# ============================================================
# MAIN EXECUTION
# ============================================================

def _scan_prs(prs, existing_chunk_ids, processed_prs, track_processed):
    """
    Scans an iterable of PRs, returning (new_chunks, scanned_count, skipped_count,
    newly_completed_pr_numbers). If track_processed is False, every PR is scanned every run
    (used for open PRs, whose review threads can still grow) instead of being skipped once seen.
    """

    new_chunks = []
    completed_prs = []
    scanned = 0
    skipped = 0

    for pr in prs:
        pr_number = pr["number"]

        if track_processed and pr_number in processed_prs:
            skipped += 1
            continue

        scanned += 1
        chunks = process_pull_request(pr)

        added = 0
        for chunk in chunks:
            chunk_id = chunk["chunk_id"]
            if chunk_id in existing_chunk_ids:
                continue
            existing_chunk_ids.add(chunk_id)
            new_chunks.append(chunk)
            added += 1

        if track_processed:
            completed_prs.append(pr_number)

        print(f"[✓] PR #{pr_number} added {added} chunks")

    return new_chunks, scanned, skipped, completed_prs


def main():

    print(
        f"[~] Starting Tier-1 architecture "
        f"dataset extraction for "
        f"{REPO_OWNER}/{REPO_NAME} "
        f"(closed PRs, permanently tracked, + open PRs, re-scanned every run)"
    )

    processed_prs = load_processed_prs()
    dataset = load_dataset()

    # Prevent duplicate chunks
    existing_chunk_ids = {
        item.get("chunk_id")
        for item in dataset
        if "chunk_id" in item
    }

    closed_chunks, closed_scanned, closed_skipped, closed_completed = _scan_prs(
        get_closed_pull_requests(), existing_chunk_ids, processed_prs, track_processed=True
    )
    open_chunks, open_scanned, open_skipped, _ = _scan_prs(
        get_open_pull_requests(), existing_chunk_ids, processed_prs, track_processed=False
    )

    new_chunks = closed_chunks + open_chunks
    scanned = closed_scanned + open_scanned
    skipped = closed_skipped + open_skipped

    if not scanned:
        print(
            "[✓] No new PRs to process."
        )
        return

    # Save processed state -- closed PRs only, open ones are never permanently skipped
    save_processed_prs(
        closed_completed
    )

    # Merge datasets
    dataset.extend(
        new_chunks
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            dataset,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\n========== COMPLETE ==========")

    print(
        f"PRs scanned: {scanned} "
        f"({closed_scanned} closed, {open_scanned} open)"
    )

    print(
        f"PRs skipped: {skipped} "
        f"({closed_skipped} closed, already processed)"
    )

    print(
        f"New architecture chunks: "
        f"{len(new_chunks)}"
    )

    print(
        f"Total dataset size: "
        f"{len(dataset)}"
    )




# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
