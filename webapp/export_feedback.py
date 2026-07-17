"""
Pulls every disliked (thumbs-down) question+answer pair out of chat_history.db for review --
this is the actual point of collecting feedback in chat_server.py: turning real user-reported
wrong answers into fixes for knowledge_base/, the same way this project's own 96-question
testing found and fixed gaps all session (missing facts, summarization loss, stubborn model
bias). A disliked answer is a lead on exactly one of those same three problem categories.

Usage:
    python3 webapp/export_feedback.py                  # print to stdout
    python3 webapp/export_feedback.py --json out.json  # write structured JSON instead
    python3 webapp/export_feedback.py --likes          # show liked answers too (sanity-check
                                                         # that the good answers are actually good)
"""
import argparse
import json
import sqlite3
from pathlib import Path

import chat_server  # reuse its db() -- same migration-aware connection, no duplicated schema logic

DB_PATH = Path(__file__).parent / "chat_history.db"


def fetch(feedback_value: str) -> list:
    conn = chat_server.db()  # runs the feedback-column migration if this DB predates it
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, session_id, content, created_at, feedback_note
        FROM messages
        WHERE role = 'assistant' AND feedback = ?
        ORDER BY id ASC
        """,
        (feedback_value,),
    ).fetchall()

    results = []
    for row in rows:
        # The question is the nearest preceding user message in the same session -- messages
        # are always inserted user-then-assistant in order, so this is just "highest id below
        # this one, same session, role=user".
        question_row = conn.execute(
            """
            SELECT content FROM messages
            WHERE session_id = ? AND role = 'user' AND id < ?
            ORDER BY id DESC LIMIT 1
            """,
            (row["session_id"], row["id"]),
        ).fetchone()
        results.append({
            "message_id": row["id"],
            "question": question_row["content"] if question_row else "[no preceding question found]",
            "answer": row["content"],
            "note": row["feedback_note"],
            "created_at": row["created_at"],
        })
    conn.close()
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", metavar="FILE", help="write JSON to this file instead of printing")
    parser.add_argument("--likes", action="store_true", help="also show liked answers")
    args = parser.parse_args()

    if not DB_PATH.exists():
        raise SystemExit(f"[X] {DB_PATH} not found -- has anyone chatted with it yet?")

    dislikes = fetch("dislike")
    output = {"dislikes": dislikes}
    if args.likes:
        output["likes"] = fetch("like")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"[OK] Wrote {len(dislikes)} disliked pair(s) to {args.json}")
        return

    print(f"=== {len(dislikes)} disliked answer(s) ===\n")
    for i, pair in enumerate(dislikes, 1):
        print(f"[{i}] ({pair['created_at']})")
        print(f"Q: {pair['question']}")
        print(f"A: {pair['answer']}")
        if pair["note"]:
            print(f"Reported issue: {pair['note']}")
        print()

    if args.likes:
        print(f"\n=== {len(output['likes'])} liked answer(s) ===\n")
        for i, pair in enumerate(output["likes"], 1):
            print(f"[{i}] ({pair['created_at']})")
            print(f"Q: {pair['question']}")
            print(f"A: {pair['answer']}")
            print()


if __name__ == "__main__":
    main()
