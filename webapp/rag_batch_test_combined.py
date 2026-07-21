"""
Combines the two independent 144-question RAG benchmark sets (rag_batch_test.py's
CUBYZ_QUESTIONS and rag_batch_test_v2.py's CUBYZ_QUESTIONS_V2) into a single 288-question run.

Imported rather than duplicated, so editing either source list automatically stays in sync here --
there is only ever one place to update a given question.

Usage:
    python3 rag_batch_test_combined.py           # all 288 questions
    python3 rag_batch_test_combined.py 10        # first 10 only, for a quick smoke check
"""
import sys

from local_rag_chat import ask, load_index
from rag_batch_test import CUBYZ_QUESTIONS
from rag_batch_test_v2 import CUBYZ_QUESTIONS_V2

CUBYZ_QUESTIONS_COMBINED = CUBYZ_QUESTIONS + CUBYZ_QUESTIONS_V2


def main():
    limit = None
    for a in sys.argv[1:]:
        if a.isdigit():
            limit = int(a)
    questions = CUBYZ_QUESTIONS_COMBINED[:limit] if limit else CUBYZ_QUESTIONS_COMBINED

    index = load_index()

    for i, (q, expected) in enumerate(questions, 1):
        print(f"\n{'=' * 70}\n[{i}/{len(questions)}] Q: {q}\n{'=' * 70}")
        answer = ask(q, index, verbose=True)
        print(f"A: {answer}")
        print(f"   [expected: {expected}]")

    print(f"\n\n[~] Done -- {len(questions)} questions "
          f"({len(CUBYZ_QUESTIONS)} from set 1 + {len(CUBYZ_QUESTIONS_V2)} from set 2, combined).")


if __name__ == "__main__":
    main()
