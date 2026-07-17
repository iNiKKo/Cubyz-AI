"""
Mixes the Cubyz SFT dataset (finetune/output/cubyz_sft_dataset.jsonl, 2667 examples) with a
sample of general-purpose instruction data, then splits into train/val.

Why this exists: the whole point of QLoRA + data mixing here is to avoid the failure mode from
the previous fine-tuning attempt -- a model trained purely on narrow domain data forgets how to
be a good general assistant (catastrophic forgetting), even with a parameter-efficient method.
Training on ONLY the 2667 Cubyz examples, however clean, still means every gradient step pushes
the model's weights toward "always talk about Cubyz" -- mixing in general instruction data at a
comparable or larger volume keeps general instruction-following behavior in the loss signal
throughout training, not just at initialization.

General data source: a random sample of teknium/OpenHermes-2.5 (~1M row, high-quality, broadly
permissive general instruction-following dataset, commonly used for exactly this anti-forgetting
mixing purpose in domain QLoRA fine-tunes). Requires internet access + `datasets` library to
pull from the HF Hub on first run (cached locally after).

Deliberately does NOT apply the Cubyz system prompt to the general examples -- forcing the
Cubyz-assistant persona onto unrelated general instructions would teach the model to associate
"be a helpful, correct assistant" only with that persona, which undermines the exact general
capability we're trying to preserve. General examples keep their own (or no) system turn.
"""
import argparse
import json
import os
import random

from datasets import load_dataset

# Anchor paths to the repo root (three levels up from this file: training/ -> finetune/ -> repo
# root) rather than the process's cwd -- these scripts get run from both the repo root and from
# inside finetune/training/ depending on habit, and a bare relative path silently resolves
# differently (and wrongly) depending on which.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CUBYZ_DATASET = os.path.join(REPO_ROOT, "finetune/output/cubyz_sft_dataset.jsonl")
OUTPUT_DIR = os.path.join(REPO_ROOT, "finetune/training/data")
GENERAL_DATASET_ID = "teknium/OpenHermes-2.5"

# General:domain ratio -- general data at least matches domain volume so a full training epoch
# doesn't spend the overwhelming majority of gradient steps exclusively reinforcing Cubyz-only
# behavior. Lowered from 1.5 to 1.0 after the first trained adapter reliably learned judgment
# patterns (reinforced across hundreds of similar review pairs) but not narrow specific facts
# (each seen in only 1-2 pairs) -- test_inference.py showed both general sanity-check questions
# answered cleanly with real headroom to spare, so there's room to shift weight toward domain
# data without meaningfully risking general capability. Still a full 1:1 mix, not a domain-only
# set -- this is a rebalancing, not a removal, of the anti-forgetting protection.
DEFAULT_RATIO = 1.0
VAL_FRACTION = 0.05
SEED = 42


def load_cubyz_examples() -> list:
    examples = []
    with open(CUBYZ_DATASET, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                examples.append(json.loads(line))
    return examples


def convert_openhermes_conversation(conversations: list) -> list:
    role_map = {"system": "system", "human": "user", "gpt": "assistant"}
    messages = []
    for turn in conversations:
        role = role_map.get(turn.get("from"))
        content = turn.get("value", "").strip()
        if not role or not content:
            return None  # malformed/unrecognized turn -- skip the whole conversation
        messages.append({"role": role, "content": content})
    # Keep it comparable in shape to the Cubyz examples: single-turn instruction/response only
    # (a system turn is fine if the source provided one, but multi-turn back-and-forth would
    # need different loss-masking assumptions than the rest of this dataset uses).
    non_system = [m for m in messages if m["role"] != "system"]
    if len(non_system) != 2 or non_system[0]["role"] != "user" or non_system[1]["role"] != "assistant":
        return None
    return messages


def load_general_examples(n: int, seed: int) -> list:
    print(f"[~] Pulling {n} general instruction examples from {GENERAL_DATASET_ID} (HF Hub)...")
    ds = load_dataset(GENERAL_DATASET_ID, split="train")
    indices = list(range(len(ds)))
    random.Random(seed).shuffle(indices)

    examples = []
    for idx in indices:
        if len(examples) >= n:
            break
        messages = convert_openhermes_conversation(ds[idx].get("conversations", []))
        if messages is None:
            continue
        examples.append({"messages": messages})
    print(f"[OK] Collected {len(examples)} usable general examples (skipped malformed/multi-turn ones)")
    return examples


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ratio", type=float, default=DEFAULT_RATIO,
                         help="general:domain example ratio (default 1.5 -- 1.5x as much general data as Cubyz data)")
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()

    cubyz_examples = load_cubyz_examples()
    print(f"[OK] Loaded {len(cubyz_examples)} Cubyz domain examples")

    n_general = int(len(cubyz_examples) * args.ratio)
    general_examples = load_general_examples(n_general, args.seed)

    combined = cubyz_examples + general_examples
    random.Random(args.seed).shuffle(combined)

    n_val = max(1, int(len(combined) * VAL_FRACTION))
    val_set = combined[:n_val]
    train_set = combined[n_val:]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    train_path = os.path.join(OUTPUT_DIR, "train.jsonl")
    val_path = os.path.join(OUTPUT_DIR, "val.jsonl")

    with open(train_path, "w", encoding="utf-8") as f:
        for ex in train_set:
            f.write(json.dumps(ex) + "\n")
    with open(val_path, "w", encoding="utf-8") as f:
        for ex in val_set:
            f.write(json.dumps(ex) + "\n")

    print(f"\n[OK] {len(train_set)} train examples -> {train_path}")
    print(f"[OK] {len(val_set)} val examples -> {val_path}")
    print(f"[OK] Composition: {len(cubyz_examples)} Cubyz + {len(general_examples)} general "
          f"({len(general_examples) / max(len(cubyz_examples), 1):.2f}x ratio)")


if __name__ == "__main__":
    main()
