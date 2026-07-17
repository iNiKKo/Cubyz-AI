"""
Merges the distributed fine-tune-generation campaign's output (finetune/pairs/{user}/{source_type}_pairs.jsonl)
into a single training-ready SFT dataset in the standard {"messages": [...]} chat format
(compatible with Axolotl, Unsloth, and HF TRL's SFTTrainer out of the box).

Run this after a generation campaign (server_finetune.py + client_finetune_linux.py) has produced
output, or any time to re-assemble after partial progress.
"""
import os
import re
import json
from collections import Counter

PAIRS_DIR = "finetune/pairs"  # server_finetune.py's own managed output -- wiped on hard reset
HANDWRITTEN_DIR = "finetune/handwritten_pairs"  # never touched by the campaign's reset logic
OUTPUT_FILE = "finetune/output/cubyz_sft_dataset.jsonl"

# Catches a real failure mode found in early generation output: the client would ask itself a
# question it couldn't actually answer from the grounding it was given, and instead of dropping
# that pair (as instructed), it kept the pair with a hedge like "is not specified in the given
# information". The client prompts were fixed to stop producing these going forward, but this
# filter also cleans up anything already generated before that fix, and catches the rare case
# that slips through despite the prompt. A hedge in training data teaches the model to give
# unhelpful non-answers, which is worse than just having one fewer example.
HEDGE_PATTERNS = [
    # Broadened after finding "are not provided" slip through the original "is not provided"
    # -only pattern -- any verb tense/form of the same hedge is just as bad. The "(?:\w+\s+)?"
    # allows for an inserted adverb ("is not EXPLICITLY detailed") which otherwise slips past a
    # pattern that only allows whitespace between "not" and the hedge verb.
    r"\b(?:is|are|was|were)\s+not\s+(?:\w+\s+)?(?:specified|provided|detailed|mentioned|covered|available|given|clear|stated|described|indicated|explained)\b",
    r"\bnot\s+(?:\w+\s+)?(?:specified|provided|detailed|mentioned|covered|stated|described)\s+in\s+(?:the|this)\s+(?:given|provided|available)?\s*(?:information|documentation|source|context|data)\b",
    r"\bno\s+(?:specific\s+)?(?:details|information|examples)\s+(?:is|are|were)\s+(?:provided|given|available)\b",
    r"\bthe\s+exact\s+.*(?:is|are)\s+not\s+(?:provided|specified|given)\b",
]
HEDGE_RE = re.compile("|".join(HEDGE_PATTERNS), re.IGNORECASE)


def strip_quoted_spans(text: str) -> str:
    """
    A hedge phrase only counts if it's in the model's own voice -- a legitimately quoted
    literal string (e.g. citing a real engine error message like "was not specified for {id}")
    can innocently contain the same words without being a hedge at all. Strip anything inside
    double quotes or backticks before hedge-checking so quoted evidence doesn't get mistaken
    for the model dodging its own question.
    """
    text = re.sub(r'"[^"]*"', "", text)
    text = re.sub(r'`[^`]*`', "", text)
    return text


def find_boilerplate_sentence_indices(pairs: list) -> set:
    """
    Catches a second failure mode: the model padding a thin, weakly-grounded answer by
    appending the SAME salient-but-unrelated sentence from elsewhere in the source onto
    multiple different pairs within one chunk (e.g. "the project also discourages
    AI-written PRs" tacked onto three unrelated questions). A sentence that verbatim-repeats
    across 2+ answers in the same chunk is a sign at least one of those pairs isn't really
    being answered on its own merits. Returns the set of pair indices to drop (keeps the
    first occurrence of a repeated sentence, drops the rest).
    """
    sentence_first_seen = {}
    drop_indices = set()
    for i, pair in enumerate(pairs):
        sentences = re.split(r'(?<=[.!?])\s+', pair.get("response", "").strip())
        for sentence in sentences:
            normalized = re.sub(r'\s+', ' ', sentence.strip().lower())
            if len(normalized) < 40:  # short sentences repeating isn't meaningful signal
                continue
            if normalized in sentence_first_seen and sentence_first_seen[normalized] != i:
                drop_indices.add(i)
            else:
                sentence_first_seen.setdefault(normalized, i)
    return drop_indices

# Deliberately short -- the goal of fine-tuning is that the substance (facts, judgment, voice)
# is now IN the weights, not re-explained every request the way the RAG system prompt had to.
# This just sets persona/tone consistently between training and inference.
SYSTEM_PROMPT = (
    "You are the Cubyz Assistant, a technical expert on Cubyz, an open-source voxel sandbox "
    "game written in Zig. Answer directly and precisely, in the voice of a developer who "
    "already knows this codebase -- never mention retrieved context or documentation. Be "
    "concise for factual questions, thorough for mechanics and debugging."
)


def collect_jsonl_files() -> list:
    files = []
    if os.path.exists(PAIRS_DIR):
        for user_folder in sorted(os.listdir(PAIRS_DIR)):
            user_path = os.path.join(PAIRS_DIR, user_folder)
            if not os.path.isdir(user_path):
                continue
            for fname in sorted(os.listdir(user_path)):
                if fname.endswith(".jsonl"):
                    files.append(os.path.join(user_path, fname))
    if os.path.exists(HANDWRITTEN_DIR):
        for fname in sorted(os.listdir(HANDWRITTEN_DIR)):
            if fname.endswith(".jsonl"):
                files.append(os.path.join(HANDWRITTEN_DIR, fname))
    return files


def main():
    jsonl_files = collect_jsonl_files()
    if not jsonl_files:
        print(f"[X] No pairs found in {PAIRS_DIR} or {HANDWRITTEN_DIR} -- run the generation campaign or generate_addon_pairs.py first.")
        return

    seen_chunk_ids = set()
    examples = []
    counts = Counter()
    skipped_dupe = 0
    skipped_hedge = 0
    skipped_boilerplate = 0

    for filepath in jsonl_files:
            with open(filepath, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        record = json.loads(line)
                    except Exception:
                        continue

                    chunk_id = record.get("chunk_id")
                    if chunk_id:
                        if chunk_id in seen_chunk_ids:
                            skipped_dupe += 1
                            continue
                        seen_chunk_ids.add(chunk_id)

                    source_type = record.get("source_type", "unknown")
                    pairs = record.get("pairs", [])
                    boilerplate_indices = find_boilerplate_sentence_indices(pairs)

                    for i, pair in enumerate(pairs):
                        instruction = pair.get("instruction", "").strip()
                        response = pair.get("response", "").strip()
                        if not instruction or not response:
                            continue
                        if HEDGE_RE.search(strip_quoted_spans(response)):
                            skipped_hedge += 1
                            continue
                        if i in boilerplate_indices:
                            skipped_boilerplate += 1
                            continue
                        examples.append({
                            "messages": [
                                {"role": "system", "content": SYSTEM_PROMPT},
                                {"role": "user", "content": instruction},
                                {"role": "assistant", "content": response},
                            ]
                        })
                        counts[source_type] += 1

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for ex in examples:
            f.write(json.dumps(ex) + "\n")

    print(f"[OK] Assembled {len(examples)} training examples -> {OUTPUT_FILE}")
    print(f"[OK] {skipped_dupe} duplicate chunk_ids skipped")
    print(f"[OK] {skipped_hedge} hedge/non-answer pairs filtered out")
    print(f"[OK] {skipped_boilerplate} boilerplate-stuffed pairs filtered out")
    print("Breakdown by source type:")
    for t, n in counts.most_common():
        print(f"  {t}: {n} pairs")


if __name__ == "__main__":
    main()
