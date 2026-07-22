"""
Combines the two independent 144-question RAG benchmark sets (rag_batch_test.py's
CUBYZ_QUESTIONS and rag_batch_test_v2.py's CUBYZ_QUESTIONS_V2) into a single 288-question run.

Imported rather than duplicated, so editing either source list automatically stays in sync here --
there is only ever one place to update a given question.

Usage:
    python3 rag_batch_test_combined.py           # all 288 questions
    python3 rag_batch_test_combined.py 10        # first 10 only, for a quick smoke check
"""
import datetime
import os
import sys

from local_rag_chat import ANSWER_MODEL, ask, load_index
from rag_batch_test import CUBYZ_QUESTIONS
from rag_batch_test_v2 import CUBYZ_QUESTIONS_V2

CUBYZ_QUESTIONS_COMBINED = CUBYZ_QUESTIONS + CUBYZ_QUESTIONS_V2
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rag_test_results")


class Tee:
    """Mirrors everything written to stdout into a log file, so the transcript survives past the
    terminal scroll-back without needing a manual `| tee` redirect."""

    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def main():
    limit = None
    for a in sys.argv[1:]:
        if a.isdigit():
            limit = int(a)
    questions = CUBYZ_QUESTIONS_COMBINED[:limit] if limit else CUBYZ_QUESTIONS_COMBINED

    os.makedirs(RESULTS_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(RESULTS_DIR, f"rag_{ANSWER_MODEL}_{timestamp}.txt")
    log_file = open(log_path, "w")
    sys.stdout = Tee(sys.__stdout__, log_file)

    index = load_index()

    for i, (q, expected) in enumerate(questions, 1):
        print(f"\n{'=' * 70}\n[{i}/{len(questions)}] Q: {q}\n{'=' * 70}")
        answer = ask(q, index, verbose=True)
        print(f"A: {answer}")
        print(f"   [expected: {expected}]")

    print(f"\n\n[~] Done -- {len(questions)} questions "
          f"({len(CUBYZ_QUESTIONS)} from set 1 + {len(CUBYZ_QUESTIONS_V2)} from set 2, combined).")
    print(f"[~] Transcript saved to {log_path}")

    sys.stdout = sys.__stdout__
    log_file.close()


if __name__ == "__main__":
    main()
