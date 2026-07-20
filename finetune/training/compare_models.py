"""
Side-by-side comparison of two Ollama-hosted models against the exact same question set used
by test_inference.py -- built specifically to check whether round 2's dataset/config changes
(denser core-facts pairs, 1.0x general:domain ratio, 3 epochs) still help at a much smaller
model size (0.6B), or whether that benefit doesn't transfer down from the 7B it was tuned for.

Runs through Ollama rather than loading the base+adapter directly like test_inference.py does,
because the old round-2 7B's raw LoRA adapter files no longer exist on disk (overwritten by this
session's repeated retraining attempts) -- only its merged/GGUF form survives, in Ollama as
`cubyz-assistant-p5-round2`. Querying both models the same way through Ollama is also more
representative of actual usage than test_inference.py's direct transformers/peft load.

No RAG context is injected here, deliberately matching test_inference.py's intent: this measures
each model's OWN standalone fact recall, not what RAG retrieval can paper over.

Usage:
    python3 compare_models.py
    python3 compare_models.py --old cubyz-assistant-p5-round2 --new cubyz-assistant
"""
import argparse
import json
import urllib.request

from test_inference import CUBYZ_QUESTIONS, GENERAL_QUESTIONS, SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434"


def ask_ollama(model, question, timeout=180):
    data = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        "stream": False,
        # Matches test_inference.py's do_sample=False (greedy) -- deterministic, comparable
        # across models rather than noisy from sampling.
        "options": {"temperature": 0.0, "seed": 42},
    }).encode()
    req = urllib.request.Request(f"{OLLAMA_URL}/api/chat", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())["message"]["content"].strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--old", default="SNALE-AI-P5-7B")
    parser.add_argument("--new", default="SNALE-AI-P6-0.6B")
    args = parser.parse_args()

    print("=" * 70)
    print("CUBYZ-SPECIFIC QUESTIONS")
    print("=" * 70)
    for q, expected in CUBYZ_QUESTIONS:
        print(f"\nQ: {q}")
        print(f"  OLD ({args.old}): {ask_ollama(args.old, q)}")
        print(f"  NEW ({args.new}): {ask_ollama(args.new, q)}")
        print(f"  [expected: {expected}]")

    print("\n\n" + "=" * 70)
    print("GENERAL QUESTIONS")
    print("=" * 70)
    for q in GENERAL_QUESTIONS:
        print(f"\nQ: {q}")
        print(f"  OLD ({args.old}): {ask_ollama(args.old, q)}")
        print(f"  NEW ({args.new}): {ask_ollama(args.new, q)}")

    print("\n\n[~] Done.")


if __name__ == "__main__":
    main()
