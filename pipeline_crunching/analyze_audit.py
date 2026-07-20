#!/usr/bin/env python3
"""Summarizes audit_needs_human_review.jsonl / audit_applied_log.jsonl into a readable diagnostic
report -- what's actually failing, how often, and in which collection -- instead of that only
being answerable by hand-writing a one-off script every time someone wants to know. Read-only,
safe to run anytime against a live campaign_state directory.

Usage: python3 pipeline_crunching/analyze_audit.py
"""
import json
import collections
import os
import sys

STATE_DIR = os.path.join(os.path.dirname(__file__), "campaign_state")
APPLIED_LOG = os.path.join(STATE_DIR, "audit_applied_log.jsonl")
NEEDS_HUMAN = os.path.join(STATE_DIR, "audit_needs_human_review.jsonl")


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _same_proposer_repeat_rate(escalations):
    """Of 'disagreed repeatedly' escalations, how many show a single proposer reassigned the
    identical chunk 2+ times in a row -- burning the review-round budget on a no-op instead of a
    genuinely fresh attempt. Was a real, unfixed bug (~35% of that bucket) until the propose-side
    dispatch filter started tracking rejected_proposers -- kept here as a regression check."""
    disagreed = [e for e in escalations if "disagreed" in e.get("reason", "")]
    if not disagreed:
        return 0, 0
    repeats = 0
    for e in disagreed:
        proposers = [h["user_id"] for h in e.get("history", []) if h.get("stage") == "proposed"]
        if len(proposers) >= 2 and len(set(proposers)) == 1:
            repeats += 1
    return repeats, len(disagreed)


def main():
    applied = _read_jsonl(APPLIED_LOG)
    escalations = _read_jsonl(NEEDS_HUMAN)

    print(f"Applied fixes logged:  {len(applied)}")
    print(f"Escalations logged:    {len(escalations)}")
    if applied or escalations:
        total = len(applied) + len(escalations)
        print(f"Escalation rate:       {len(escalations) / total * 100:.1f}%")
    print()

    print("=== Escalation reasons ===")
    reasons = collections.Counter(e.get("reason", "?") for e in escalations)
    for r, c in reasons.most_common():
        print(f"  {c:5d}  {r}")
    print()

    print("=== Escalations by collection ===")
    by_coll = collections.Counter(e.get("collection", "?") for e in escalations)
    for c, n in by_coll.most_common():
        print(f"  {n:5d}  {c}")
    print()

    print("=== Applied-fix attempt distribution (1 = clean first-try approval) ===")
    att = collections.Counter(a.get("attempts", 1) for a in applied)
    for k in sorted(att):
        print(f"  attempts={k}: {att[k]}")
    print()

    repeats, disagreed_total = _same_proposer_repeat_rate(escalations)
    if disagreed_total:
        pct = repeats / disagreed_total * 100
        flag = "  <-- investigate, should be near 0" if pct > 5 else ""
        print(f"=== Same-proposer-reassigned-after-reject rate ===")
        print(f"  {repeats}/{disagreed_total} ({pct:.0f}%) of 'disagreed repeatedly' escalations{flag}")
        print()

    print("=== Proposers most often rejected (signal for a weak/over-eager model) ===")
    rejected_by = collections.Counter()
    for e in escalations:
        for h in e.get("history", []):
            if h.get("stage") == "reviewed" and h.get("verdict") == "reject":
                proposed_before = [x for x in e["history"] if x.get("stage") == "proposed"]
                if proposed_before:
                    rejected_by[proposed_before[-1]["user_id"]] += 1
    for user, n in rejected_by.most_common(10):
        print(f"  {n:5d}  {user}")


if __name__ == "__main__":
    sys.exit(main())
