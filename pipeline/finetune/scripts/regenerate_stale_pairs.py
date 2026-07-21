#!/usr/bin/env python3
"""Regenerates finetune training pairs for chunks whose underlying knowledge_base/*.md content
has changed (usually via an audit-mode fix) since finetune pairs were last generated for them --
without going through the live distributed campaign server at all.

Why standalone instead of switching the live server to finetune mode: CURRENT_MODE is global --
switching it would redirect every currently-connected volunteer off of whatever campaign they're
actually running (audit, most of the time) just to process what's usually a small backlog. This
script reuses the exact same generation/validation logic as client.py's crunch_lane()
(imported directly, not reimplemented) against a local Ollama instance, and writes results into
their own pairs file under finetune/pairs/<RUNNER_ID>/ -- entirely local, no /get_work, no
/submit_work, no shared campaign state touched.

Usage: python3 finetune/scripts/regenerate_stale_pairs.py [--model MODEL_TAG]
"""
import os
import sys
import json
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

RUNNER_ID = "claudecrunch"
DEFAULT_MODEL = "qwen2.5-coder:7b"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    args = parser.parse_args()

    # Import server FIRST, before client -- the latter monkey-patches builtins.print at import
    # time (routes it into its own TUI log queue instead of real stdout), so anything we still
    # want printed normally has to happen before that, or go through the _orig_print reference
    # it conveniently keeps.
    import server as srv
    srv.finetune_initialize_chunks(verbose=False)
    queue = list(srv.finetune_chunk_queue)
    print(f"[~] {len(queue)} chunk(s) need regeneration (changed since last finetune pass).")
    if not queue:
        return

    import client
    real_print = client._orig_print

    out_dir = os.path.join("pipeline", "finetune", "pairs", RUNNER_ID)
    os.makedirs(out_dir, exist_ok=True)
    by_source_type = {}  # source_type -> list of {"chunk_id", "source_type", "pairs"}

    ok_count = 0
    failed = []
    for i, item in enumerate(queue):
        chunk_id = item["chunk_id"]
        source_type = item["source_type"]
        record = item["record"]
        task = {"chunk_id": chunk_id, "source_type": source_type, "record": record}
        real_print(f"[{i+1}/{len(queue)}] {chunk_id} ({source_type})...")

        parsed, failure_reason = client.generate_finetune_pairs(
            task, args.model, status_cb=lambda m: real_print(f"    {m}"), force_cpu=False,
        )
        if parsed is None:
            real_print(f"    [X] gave up: {failure_reason}")
            failed.append(chunk_id)
            continue

        pairs = parsed.get("pairs", [])
        real_print(f"    [OK] {len(pairs)} pair(s)")
        ok_count += 1
        by_source_type.setdefault(source_type, []).append({
            "chunk_id": chunk_id, "source_type": source_type, "pairs": pairs,
        })

    for source_type, records in by_source_type.items():
        out_path = os.path.join(out_dir, f"{source_type}_pairs.jsonl")
        # Merge with anything already in this file for this runner (append-and-replace by
        # chunk_id, same semantics as a real campaign run resubmitting a chunk) rather than
        # clobbering any prior local run's output for chunks NOT in this batch.
        existing = {}
        if os.path.exists(out_path):
            with open(out_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    existing[rec["chunk_id"]] = rec
        for rec in records:
            existing[rec["chunk_id"]] = rec
        with open(out_path, "w", encoding="utf-8") as f:
            for rec in existing.values():
                f.write(json.dumps(rec) + "\n")
        real_print(f"[OK] wrote {len(records)} record(s) -> {out_path}")

    real_print(f"\n[DONE] {ok_count}/{len(queue)} regenerated, {len(failed)} gave up: {failed}")


if __name__ == "__main__":
    main()
