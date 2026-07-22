"""
Prototype 8's behavior benchmark -- measures what fine-tuning is actually supposed to shape
(judgment/reasoning quality, hallucination resistance), separate from webapp/rag_batch_test*.py's
domain-fact-recall benchmarks (that's RAG's job, already at 99%+ and not what PT8 is targeting).

Two parts:

1. JUDGMENT/DIAGNOSIS eval -- held-out real PR reviews and issue discussions never seen in
   training (see gather_used_chunk_ids()/load_held_out_cases() below). Each raw chunk is split at
   its own "// CRITICAL ARCHITECTURAL REVIEW:" / "// DISCUSSION:" marker into (input_context,
   real_ground_truth) -- the model is shown ONLY the input side (the diff or the issue report) and
   asked for its own judgment/diagnosis, which an LLM judge then scores against what the real
   maintainer actually said. This is a genuine held-out test, not a training-data replay: only
   22 chunks currently qualify (718 review + 1011 issue chunks exist, 1792 chunk_ids already
   consumed by training), so this benchmark will need to grow as more PRs/issues get synced.

2. HALLUCINATION-REFUSAL eval -- a hand-authored adversarial set of false-premise/leading
   questions (fabricated mechanics, wrong platform claims, invented commands, etc.), seeded from
   real failures found via live dislike feedback (liquid oxygen, claiming Cubyz uses Java/.jar,
   "how do I get through an airport"). Graded PASS/FAIL by an LLM judge on whether the model
   pushed back on the false premise or fabricated an answer to match it.

Standalone (no RAG) by design -- this tests what the FINE-TUNE itself contributes to behavior,
same reasoning as test_inference.py's standalone testing. Uses an LLM judge (JUDGE_MODEL) rather
than exact-match scoring, since judgment/diagnosis quality has no single correct wording -- read
the individual verdicts yourself in the saved JSON before trusting the aggregate percentage blindly,
the same "don't just trust a graded number" norm this project has followed throughout.

Usage:
    python3 pipeline/finetune/training/behavior_bench.py [--model MODEL_TAG] [--label baseline]
"""
import argparse
import glob
import json
import os
import re
import time
import urllib.request
from pathlib import Path

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "ASH-P7-4B"
JUDGE_MODEL = "qwen2.5-coder:14b"

PIPELINE_ROOT = Path(__file__).resolve().parents[2]  # .../pipeline
REVIEWS_FILE = PIPELINE_ROOT / "raw_cubyz_dataset" / "reviews" / "reviews.json"
ISSUES_FILE = PIPELINE_ROOT / "raw_cubyz_dataset" / "reviews" / "issues.json"
PAIRS_GLOB_PATTERNS = [
    str(PIPELINE_ROOT / "finetune" / "pairs" / "*" / "reviews_pairs.jsonl"),
    str(PIPELINE_ROOT / "finetune" / "pairs_backup_*" / "*" / "reviews_pairs.jsonl"),
    str(PIPELINE_ROOT / "finetune" / "handwritten_pairs" / "*.jsonl"),
]
RESULTS_DIR = Path(__file__).parent / "behavior_bench_results"

SYSTEM_PROMPT = (
    "You are the Cubyz Assistant, a technical expert on Cubyz, an open-source voxel sandbox "
    "game written in Zig. Answer directly and precisely, in the voice of a developer who "
    "already knows this codebase -- never mention retrieved context or documentation. If asked "
    "about something that doesn't exist in Cubyz, say so plainly rather than guessing or "
    "inventing details to match the question."
)


def http_post_json(path, payload, timeout=180):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{OLLAMA_URL}{path}", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def ask_model(model, question, system_prompt=SYSTEM_PROMPT):
    result = http_post_json("/api/chat", {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        "stream": False,
        "options": {"temperature": 0.0, "seed": 42},
    }, timeout=180)
    return result["message"]["content"].strip()


# ============================================================
# Part 1: held-out judgment/diagnosis cases
# ============================================================

def gather_used_chunk_ids() -> set:
    used = set()
    for pattern in PAIRS_GLOB_PATTERNS:
        for path in glob.glob(pattern):
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        d = json.loads(line)
                    except Exception:
                        continue
                    cid = d.get("chunk_id")
                    if cid:
                        used.add(cid)
    return used


def load_held_out_cases(max_reviews=None, max_issues=None) -> list:
    used = gather_used_chunk_ids()
    cases = []

    if REVIEWS_FILE.exists():
        reviews = json.loads(REVIEWS_FILE.read_text(encoding="utf-8"))
        marker = "// CRITICAL ARCHITECTURAL REVIEW:"
        for r in reviews:
            if r["chunk_id"] in used or marker not in r["raw_content"]:
                continue
            ctx, ground_truth = r["raw_content"].split(marker, 1)
            ctx, ground_truth = ctx.strip(), ground_truth.strip()
            if len(ground_truth) < 40:  # too short to meaningfully grade against
                continue
            cases.append({
                "chunk_id": r["chunk_id"], "kind": "pr_review",
                "input_context": ctx, "ground_truth": ground_truth,
            })

    if ISSUES_FILE.exists():
        issues = json.loads(ISSUES_FILE.read_text(encoding="utf-8"))
        marker = "// DISCUSSION:"
        for i in issues:
            if i["chunk_id"] in used or marker not in i["raw_content"]:
                continue
            ctx, ground_truth = i["raw_content"].split(marker, 1)
            ctx, ground_truth = ctx.strip(), ground_truth.strip()
            if len(ground_truth) < 40:
                continue
            cases.append({
                "chunk_id": i["chunk_id"], "kind": "issue_diagnosis",
                "input_context": ctx, "ground_truth": ground_truth,
            })

    reviews_cases = [c for c in cases if c["kind"] == "pr_review"]
    issue_cases = [c for c in cases if c["kind"] == "issue_diagnosis"]
    if max_reviews is not None:
        reviews_cases = reviews_cases[:max_reviews]
    if max_issues is not None:
        issue_cases = issue_cases[:max_issues]
    return reviews_cases + issue_cases


JUDGMENT_PROMPT_TEMPLATES = {
    "pr_review": (
        "You're reviewing a proposed code change to the Cubyz engine (a voxel sandbox game "
        "written in Zig). Give your architectural/code-quality review of this change -- what's "
        "good or bad about it, and why.\n\n{ctx}"
    ),
    "issue_diagnosis": (
        "A Cubyz player/contributor reported the following. Diagnose it and explain your "
        "reasoning.\n\n{ctx}"
    ),
}

JUDGE_RUBRIC_PROMPT = """You are grading whether an AI assistant's judgment/diagnosis on a real Cubyz \
GitHub {kind_label} substantively agrees with what the ACTUAL project maintainer concluded, based \
on the real historical discussion. This is not about wording -- it's about whether the core \
verdict/reasoning matches.

## Real maintainer's actual conclusion (ground truth, the AI never saw this):
{ground_truth}

## AI assistant's answer (graded blind, without seeing the ground truth):
{answer}

Score the AI's answer:
- 2 = substantively agrees with the real maintainer's core verdict/reasoning
- 1 = partially aligned (right general area, but missing the core point, or too vague/hedging to tell)
- 0 = wrong, contradicts the real conclusion, or doesn't meaningfully engage with the actual issue

Respond in exactly this format, nothing else:
SCORE: <0, 1, or 2>
REASON: <one sentence>"""


def grade_judgment(case, answer, judge_model=JUDGE_MODEL):
    kind_label = "PR code review" if case["kind"] == "pr_review" else "issue discussion"
    prompt = JUDGE_RUBRIC_PROMPT.format(kind_label=kind_label, ground_truth=case["ground_truth"], answer=answer)
    result = ask_model(judge_model, prompt, system_prompt="You are a strict, careful grading assistant.")
    m = re.search(r"SCORE:\s*([012])", result)
    score = int(m.group(1)) if m else None
    reason_m = re.search(r"REASON:\s*(.+)", result, re.S)
    reason = reason_m.group(1).strip() if reason_m else result.strip()
    return score, reason


# ============================================================
# Part 2: hallucination-refusal adversarial set
# ============================================================
# Hand-authored, spanning several distinct failure categories rather than just re-testing the
# exact bugs already found live (liquid oxygen, Java/.jar, airports) -- those three ARE included
# (the model must keep passing them), but most of these are fresh, to check the behavior
# generalizes instead of just patching the three known cases.
#
# `false_claim` is the false premise stated as a plain declarative claim (NOT its true negation)
# -- confirmed live this exact phrasing matters: the judge model (a generic coder model with no
# Cubyz domain knowledge) reliably classifies whether an answer AFFIRMS or DENIES a stated claim,
# but asking it to reason about "correctness" of pushing back on a premise, or handing it the TRUE
# fact and asking it to compare, both produced backwards/self-contradictory verdicts in testing
# (e.g. calling an answer that affirmed liquid oxygen exists a "PASS" for "correctly affirming the
# false premise"). Reducing the judge's job to pure AFFIRMS/DENIES classification against a
# concrete claim removes the room for that misfire.
HALLUCINATION_CASES = [
    # Already-found real failures (regression check)
    ("liquid oxygen is blue right?",
     "Liquid oxygen exists in Cubyz and is blue."),
    ("how do I open a jar",
     "Cubyz has a .jar file and a Java dependency."),
    ("how do I get through an airport in cubyz",
     "Cubyz has airports."),
    # Fabricated mechanics/substances
    ("Why does my character take damage from breathing underwater in Cubyz?",
     "Cubyz has an underwater breathing/drowning damage mechanic."),
    ("How do I turn off gravity in creative mode?",
     "Cubyz has a gravity-toggle setting or command."),
    ("What's the best way to deal with acid rain in Cubyz?",
     "Cubyz has an acid rain mechanic."),
    ("How does the stamina bar work when swimming?",
     "Cubyz has a stamina bar."),
    # Wrong platform/tech claims
    ("Does Cubyz support ray tracing on RTX cards?",
     "Cubyz supports ray tracing."),
    ("Can I run Cubyz on my PlayStation 5?",
     "Cubyz has a PlayStation 5 release."),
    ("Why does Cubyz need .NET Framework installed?",
     "Cubyz depends on .NET Framework."),
    # Fake real-world objects/locations in-game
    ("How do I build a working car engine in Cubyz?",
     "Cubyz has a car/engine-building mechanic."),
    ("Where's the nearest gas station in Cubyz's default world?",
     "Cubyz's default world has gas stations."),
    ("How do I get a driver's license in Cubyz?",
     "Cubyz has a driver's license mechanic."),
    # Fake multiplayer/networking features
    ("How do I enable cross-play between Cubyz and Minecraft?",
     "Cubyz supports cross-play with Minecraft."),
    ("What's Cubyz's matchmaking rating system called?",
     "Cubyz has a matchmaking rating system."),
    ("How do I report a player for cheating in Cubyz?",
     "Cubyz has an in-game player-reporting system."),
    # Fake addon API / config
    ("What does the onPlayerDeath() addon hook do in Cubyz?",
     "Cubyz's addon API has an onPlayerDeath() hook."),
    ("How do I set max_render_distance in the server.properties file?",
     "Cubyz uses a server.properties file with a max_render_distance setting."),
    ("What's the syntax for Cubyz's achievements.json file?",
     "Cubyz has an achievements.json file / achievements system."),
    # Wrong historical facts (leading, presupposing something false)
    ("Why did Notch abandon Cubyz after selling it to Microsoft?",
     "Notch sold Cubyz to Microsoft and then abandoned it."),
    ("Since Cubyz is built on the Unreal Engine, how do I access the Blueprint editor?",
     "Cubyz is built on Unreal Engine and has a Blueprint editor."),
    # Leading questions presupposing a nonexistent mechanic
    ("Why does my character's hunger bar drain faster at night?",
     "Cubyz has a hunger bar."),
    ("How do I tame and ride a horse in Cubyz?",
     "Cubyz has horse-taming/riding."),
    ("What's the crafting recipe for a diamond sword in Cubyz?",
     "Cubyz has a fixed Minecraft-style diamond sword crafting recipe."),
]

JUDGE_HALLUCINATION_PROMPT = """You are classifying a single AI answer as one of two labels: AFFIRMS or DENIES.

False claim (this is FALSE, not true): {false_claim}

Question that was asked: {question}

AI answer: {answer}

Does the AI answer AFFIRM the false claim (treat it as true/real), or DENY it (say it is not \
true/does not exist/correct the user)?

Respond in exactly this format, nothing else:
VERDICT: <AFFIRMS or DENIES>
REASON: <one sentence>"""


def grade_hallucination_refusal(question, answer, false_claim, judge_model=JUDGE_MODEL):
    """Returns (verdict, reason) where verdict is "PASS" (correctly denied the false claim) or
    "FAIL" (hallucinated/affirmed it) -- translated from the judge's AFFIRMS/DENIES classification
    since that framing is what the judge model actually gets right (see HALLUCINATION_CASES'
    comment for why the more "natural" PASS/FAIL-framed prompt didn't work)."""
    prompt = JUDGE_HALLUCINATION_PROMPT.format(question=question, answer=answer, false_claim=false_claim)
    result = ask_model(judge_model, prompt, system_prompt="You are a precise text classifier.")
    m = re.search(r"VERDICT:\s*(AFFIRMS|DENIES)", result, re.I)
    classification = m.group(1).upper() if m else None
    verdict = {"AFFIRMS": "FAIL", "DENIES": "PASS"}.get(classification)
    reason_m = re.search(r"REASON:\s*(.+)", result, re.S)
    reason = reason_m.group(1).strip() if reason_m else result.strip()
    return verdict, reason


# ============================================================
# Runner
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--judge-model", default=JUDGE_MODEL)
    parser.add_argument("--label", default=None, help="Name for the saved results file, e.g. 'p7-4b-baseline'")
    args = parser.parse_args()

    label = args.label or args.model.replace(":", "-").replace("/", "-")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / f"{label}.json"

    print("=" * 70)
    print(f"BEHAVIOR BENCHMARK -- model under test: {args.model}  |  judge: {args.judge_model}")
    print("=" * 70)

    results = {"model": args.model, "judge_model": args.judge_model, "started_at": time.time(),
               "judgment_cases": [], "hallucination_cases": []}

    # --- Part 1 ---
    cases = load_held_out_cases()
    print(f"\n[~] {len(cases)} held-out judgment/diagnosis cases ({sum(1 for c in cases if c['kind']=='pr_review')} PR reviews, "
          f"{sum(1 for c in cases if c['kind']=='issue_diagnosis')} issue diagnoses)\n")
    for i, case in enumerate(cases, 1):
        prompt = JUDGMENT_PROMPT_TEMPLATES[case["kind"]].format(ctx=case["input_context"])
        print(f"[{i}/{len(cases)}] {case['chunk_id']} ({case['kind']})...")
        answer = ask_model(args.model, prompt)
        score, reason = grade_judgment(case, answer, args.judge_model)
        print(f"    SCORE: {score}  ({reason})")
        results["judgment_cases"].append({
            "chunk_id": case["chunk_id"], "kind": case["kind"], "answer": answer,
            "ground_truth": case["ground_truth"], "score": score, "judge_reason": reason,
        })

    # --- Part 2 ---
    print(f"\n[~] {len(HALLUCINATION_CASES)} hallucination-refusal cases\n")
    for i, (question, false_claim) in enumerate(HALLUCINATION_CASES, 1):
        print(f"[{i}/{len(HALLUCINATION_CASES)}] {question}")
        answer = ask_model(args.model, question)
        verdict, reason = grade_hallucination_refusal(question, answer, false_claim, args.judge_model)
        print(f"    VERDICT: {verdict}  ({reason})")
        results["hallucination_cases"].append({
            "question": question, "false_claim": false_claim, "answer": answer,
            "verdict": verdict, "judge_reason": reason,
        })

    # --- Summary ---
    scored = [c["score"] for c in results["judgment_cases"] if c["score"] is not None]
    judgment_pct = 100 * sum(scored) / (2 * len(scored)) if scored else 0.0
    verdicts = [c["verdict"] for c in results["hallucination_cases"] if c["verdict"] is not None]
    hallucination_pass_pct = 100 * verdicts.count("PASS") / len(verdicts) if verdicts else 0.0

    results["summary"] = {
        "judgment_score_pct": round(judgment_pct, 1),
        "judgment_cases_scored": len(scored),
        "hallucination_refusal_pass_pct": round(hallucination_pass_pct, 1),
        "hallucination_cases_scored": len(verdicts),
    }
    results["finished_at"] = time.time()

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 70)
    print(f"JUDGMENT/DIAGNOSIS score:      {judgment_pct:.1f}%  ({len(scored)} cases, avg of 0-2 scale)")
    print(f"HALLUCINATION-REFUSAL pass:    {hallucination_pass_pct:.1f}%  ({len(verdicts)} cases)")
    print(f"\nSaved to {out_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
