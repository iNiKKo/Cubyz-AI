"""
Independent second-pass QC over a completed generation campaign's output
(finetune/pairs/**/*.jsonl), run AFTER the campaign finishes rather than during generation.

Why this exists as a separate pass from the client's own validate_pairs() self-check: that
check only sees one chunk at a time and only catches ungrounded backtick-quoted identifiers.
This script re-checks the same grounding rule with fresh eyes (independent of whatever bug
might exist in a given client version at generation time), adds a few checks the self-check
doesn't do (loose numeric-claim grounding, review shape sanity, stub-source detection), and
reports everything so a human can do a fast, prioritized manual pass instead of reading
thousands of pairs cold.

This does not modify any files -- it only reports. Fixes/removals are applied by hand based on
the report, same as the docs audit earlier in this project.
"""
import os
import re
import json
from collections import defaultdict

WIKI_GLOB_DIRS = "users"
CODEBASE_SUBSET_FILE = "finetune/source_data/codebase_architectural_subset.jsonl"
REVIEWS_GLOB_DIRS = "users"
PAIRS_DIR = "finetune/pairs"

HEDGE_PATTERNS = [
    r"\b(?:is|are|was|were)\s+not\s+(?:\w+\s+)?(?:specified|provided|detailed|mentioned|covered|available|given|clear|stated|described|indicated|explained)\b",
    r"\bnot\s+(?:\w+\s+)?(?:specified|provided|detailed|mentioned|covered|stated|described)\s+in\s+(?:the|this)\s+(?:given|provided|available)?\s*(?:information|documentation|source|context|data)\b",
    r"\bno\s+(?:specific\s+)?(?:details|information|examples)\s+(?:is|are|were)\s+(?:provided|given|available)\b",
    r"\bthe\s+exact\s+.*(?:is|are)\s+not\s+(?:provided|specified|given)\b",
]
HEDGE_RE = re.compile("|".join(HEDGE_PATTERNS), re.IGNORECASE)

STUB_THRESHOLD_CHARS = 150  # below this, a chunk with non-empty pairs gets flagged for manual review


def strip_quoted_spans(text: str) -> str:
    text = re.sub(r'"[^"]*"', "", text)
    text = re.sub(r'`[^`]*`', "", text)
    return text


def load_jsonl(path):
    records = []
    if not os.path.exists(path):
        return records
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except Exception:
                pass
    return records


def load_source_records():
    """chunk_id -> record, across docs (wiki.jsonl), codebase (subset file), reviews (github_reviews.jsonl)"""
    by_chunk_id = {}

    if os.path.isdir(WIKI_GLOB_DIRS):
        for user in os.listdir(WIKI_GLOB_DIRS):
            path = os.path.join(WIKI_GLOB_DIRS, user, "wiki.jsonl")
            for rec in load_jsonl(path):
                by_chunk_id[rec["chunk_id"]] = ("docs", rec)

    for rec in load_jsonl(CODEBASE_SUBSET_FILE):
        by_chunk_id[rec["chunk_id"]] = ("codebase", rec)

    if os.path.isdir(REVIEWS_GLOB_DIRS):
        for user in os.listdir(REVIEWS_GLOB_DIRS):
            path = os.path.join(REVIEWS_GLOB_DIRS, user, "github_reviews.jsonl")
            for rec in load_jsonl(path):
                by_chunk_id[rec["chunk_id"]] = ("reviews", rec)

    return by_chunk_id


def grounding_text_for(source_type, record):
    # No raw_content field actually exists in the crunched review records -- matches the same
    # fix applied to the client scripts' grounding_text_for.
    symbols_text = " ".join(record.get("symbols") or [])
    if source_type == "reviews":
        return f"{record.get('comprehensive_explanation', '')} {symbols_text}"
    return f"{record.get('summary', '')} {record.get('comprehensive_explanation', '')} {record.get('code_example') or ''} {symbols_text}"


def check_backtick_grounding(response, grounding_text):
    issues = []
    for name in set(re.findall(r'`([A-Za-z_][A-Za-z0-9_]*)`', response)):
        if not re.search(r'\b' + re.escape(name) + r'\b', grounding_text):
            issues.append(f"ungrounded identifier `{name}`")
    return issues


def check_numeric_grounding(response, grounding_text):
    issues = []
    for num in set(re.findall(r'\b\d+(?:\.\d+)?\b', response)):
        if num not in grounding_text:
            issues.append(f"ungrounded number '{num}'")
    return issues


def check_hedge(response):
    return HEDGE_RE.search(strip_quoted_spans(response)) is not None


def collect_pair_files():
    files = []
    if os.path.exists(PAIRS_DIR):
        for user_folder in sorted(os.listdir(PAIRS_DIR)):
            user_path = os.path.join(PAIRS_DIR, user_folder)
            if not os.path.isdir(user_path):
                continue
            for fname in sorted(os.listdir(user_path)):
                if fname.endswith(".jsonl"):
                    files.append(os.path.join(user_path, fname))
    return files


def main():
    sources = load_source_records()
    print(f"[~] Loaded {len(sources)} source records (docs+codebase+reviews)")

    flagged = []
    stats = defaultdict(int)
    missing_source = []

    for filepath in collect_pair_files():
        for rec in load_jsonl(filepath):
            chunk_id = rec.get("chunk_id")
            source_type = rec.get("source_type", "unknown")
            pairs = rec.get("pairs", [])
            stats[f"{source_type}_chunks"] += 1
            stats[f"{source_type}_pairs"] += len(pairs)

            src = sources.get(chunk_id)
            if src is None:
                if pairs:
                    missing_source.append(chunk_id)
                continue
            src_type, record = src
            grounding_text = grounding_text_for(src_type, record)
            core_len = len(f"{record.get('summary','')} {record.get('comprehensive_explanation','')} {record.get('code_example') or ''}".strip()) \
                if src_type != "reviews" else len(record.get("comprehensive_explanation", "").strip())

            # Review shape sanity
            if src_type == "reviews" and len(pairs) > 1:
                flagged.append((chunk_id, src_type, "shape", f"{len(pairs)} pairs (reviews should be 0 or 1)", None))

            # Stub-source flag: non-empty pairs from a very thin source
            if pairs and core_len < STUB_THRESHOLD_CHARS:
                flagged.append((chunk_id, src_type, "stub-source", f"source core content only {core_len} chars but {len(pairs)} pairs generated", None))

            for i, pair in enumerate(pairs):
                response = pair.get("response", "")
                instruction = pair.get("instruction", "")
                if not response or not instruction:
                    flagged.append((chunk_id, src_type, "malformed", "empty instruction/response", i))
                    continue
                bt_issues = check_backtick_grounding(response, grounding_text)
                for issue in bt_issues:
                    flagged.append((chunk_id, src_type, "grounding", issue, i))
                num_issues = check_numeric_grounding(response, grounding_text)
                for issue in num_issues:
                    flagged.append((chunk_id, src_type, "numeric", issue, i))
                if check_hedge(response):
                    flagged.append((chunk_id, src_type, "hedge", "hedge phrase detected", i))

    if missing_source:
        print(f"[!] {len(missing_source)} chunk_ids with pairs have NO matching source record (orphaned): {missing_source[:10]}{'...' if len(missing_source) > 10 else ''}")

    print("\n=== Campaign stats ===")
    for k in sorted(stats):
        print(f"  {k}: {stats[k]}")

    print(f"\n=== Flagged issues: {len(flagged)} ===")
    by_category = defaultdict(list)
    for chunk_id, src_type, category, detail, pair_idx in flagged:
        by_category[category].append((chunk_id, src_type, detail, pair_idx))

    for category in sorted(by_category):
        items = by_category[category]
        print(f"\n--- {category} ({len(items)}) ---")
        for chunk_id, src_type, detail, pair_idx in items:
            idx_str = f" pair#{pair_idx}" if pair_idx is not None else ""
            print(f"  [{src_type}] {chunk_id}{idx_str}: {detail}")

    # Write machine-readable report too, for scripted follow-up
    out = {
        "stats": dict(stats),
        "missing_source": missing_source,
        "flagged": [
            {"chunk_id": c, "source_type": s, "category": cat, "detail": d, "pair_index": pi}
            for c, s, cat, d, pi in flagged
        ],
    }
    os.makedirs("finetune/output", exist_ok=True)
    with open("finetune/output/audit_report.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"\n[OK] Full machine-readable report written to finetune/output/audit_report.json")


if __name__ == "__main__":
    main()
