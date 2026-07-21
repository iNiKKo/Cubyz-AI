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
import sys
import json
import shutil
import time
from collections import defaultdict

# Per-pair correctness/quality issues -- safe to auto-remove, since each is a specific pair that's
# either an explicit non-answer (hedge), a claim not traceable to the source it was generated from
# (grounding/numeric), or structurally broken (malformed). "shape" and "stub-source" are flagged at
# the CHUNK level, not a specific pair, and need a human judgment call (e.g. a review chunk's 2nd
# pair might be a perfectly good, just-redundant answer, not a wrong one) -- left report-only.
REMOVE_CATEGORIES = {"hedge", "grounding", "numeric", "malformed"}

KNOWLEDGE_DIR = "knowledge_base"
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


def _extract_kb_section(text: str, heading: str) -> str:
    match = re.search(rf"## {re.escape(heading)}\n(.*?)(?=\n\n## |\n\n\*Source)", text, re.S)
    return match.group(1).strip() if match else ""


def _parse_kb_md_record(collection: str, chunk_id: str) -> dict:
    """Mirrors pipeline_crunching/server.py's _parse_kb_md_record() -- kept as a separate
    copy here rather than imported, matching this project's existing pattern of standalone scripts
    (see that function's own docstring for why knowledge_base/*.md, not users/*.jsonl, is the
    source of truth: users/*.jsonl is the frozen one-time crunch dump that audit mode's fixes never
    touch, so QC-checking pairs against it means checking grounding against stale, possibly
    already-corrected-elsewhere content -- silently missing real hallucinations that were only
    introduced/left uncorrected in the version actually used to generate these pairs, or flagging a
    fact as ungrounded when an audit fix already added it to the real source)."""
    kb_path = os.path.join(KNOWLEDGE_DIR, collection, f"{chunk_id}.md")
    if not os.path.exists(kb_path):
        return None
    with open(kb_path, encoding="utf-8") as f:
        text = f.read()

    symbols_m = re.search(r"^\*\*Symbols:\*\*\s*(.+)$", text, re.M)
    code_example = _extract_kb_section(text, "Code Example")
    if code_example:
        code_example = re.sub(r"^```\w*\n|\n```$", "", code_example).strip() or None

    return {
        "chunk_id": chunk_id,
        "symbols": [s.strip() for s in symbols_m.group(1).split(",")] if symbols_m else [],
        "summary": _extract_kb_section(text, "Summary"),
        "comprehensive_explanation": _extract_kb_section(text, "Explanation"),
        "code_example": code_example,
    }


def load_source_records():
    """chunk_id -> (source_type, record), read live from knowledge_base/*.md -- the same
    audit-corrected content finetune_initialize_chunks() actually generates pairs from, not the
    frozen pre-audit users/*.jsonl dump this function used to read."""
    by_chunk_id = {}
    for collection in ("docs", "codebase", "reviews"):
        d = os.path.join(KNOWLEDGE_DIR, collection)
        if not os.path.isdir(d):
            continue
        for fname in sorted(os.listdir(d)):
            if not fname.endswith(".md"):
                continue
            chunk_id = fname[:-3]
            rec = _parse_kb_md_record(collection, chunk_id)
            if rec:
                by_chunk_id[chunk_id] = (collection, rec)

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

    if "--apply" in sys.argv:
        apply_removals(flagged)
    else:
        removable = sum(1 for _, _, cat, _, _ in flagged if cat in REMOVE_CATEGORIES)
        if removable:
            print(f"\n[i] {removable} flagged pairs are in auto-removable categories "
                  f"({', '.join(sorted(REMOVE_CATEGORIES))}). Re-run with --apply to strip them "
                  f"from finetune/pairs/**/*.jsonl in place (backs up first).")


def apply_removals(flagged):
    """Strips every flagged pair in REMOVE_CATEGORIES out of finetune/pairs/**/*.jsonl in place.
    Backs up the whole pairs directory first (timestamped, next to it) since this is a real,
    non-trivially-reversible edit to training data -- report-only was this script's original
    design, this is opt-in and explicit."""
    to_remove = defaultdict(set)  # chunk_id -> set of pair indices to drop
    for chunk_id, _src_type, category, _detail, pair_idx in flagged:
        if category in REMOVE_CATEGORIES and pair_idx is not None:
            to_remove[chunk_id].add(pair_idx)

    if not to_remove:
        print("\n[i] Nothing to apply -- no flagged pairs in an auto-removable category.")
        return

    backup_dir = f"{PAIRS_DIR}_backup_{int(time.time())}"
    shutil.copytree(PAIRS_DIR, backup_dir)
    print(f"\n[~] Backed up {PAIRS_DIR} -> {backup_dir}")

    total_removed = 0
    for filepath in collect_pair_files():
        records = load_jsonl(filepath)
        changed = False
        for rec in records:
            chunk_id = rec.get("chunk_id")
            if chunk_id not in to_remove:
                continue
            bad_indices = to_remove[chunk_id]
            kept = [p for i, p in enumerate(rec.get("pairs", [])) if i not in bad_indices]
            removed_here = len(rec.get("pairs", [])) - len(kept)
            if removed_here:
                rec["pairs"] = kept
                total_removed += removed_here
                changed = True
        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                for rec in records:
                    f.write(json.dumps(rec) + "\n")

    print(f"[OK] Removed {total_removed} flagged pairs from {PAIRS_DIR}/**/*.jsonl "
          f"(backup at {backup_dir}).")


if __name__ == "__main__":
    main()
