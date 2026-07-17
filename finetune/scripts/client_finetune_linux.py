import os
import re
import sys
import json
import time
import subprocess
import urllib.request
import urllib.error

if not sys.platform.startswith("linux"):
    print("[X] This script is explicitly configured for Linux systems only.")
    sys.exit(1)

SERVER_URL = "http://ashframe.net:7000"
OLLAMA_URL = "http://localhost:11434/api/generate"
CONFIG_FILE = os.path.expanduser("~/.cubyz_finetune_node_config.json")

USER_ID_PATTERN = re.compile(r"^[a-zA-Z]+$")


def is_valid_user_id(user_id: str) -> bool:
    return bool(user_id) and 3 <= len(user_id) <= 9 and bool(USER_ID_PATTERN.fullmatch(user_id))


FINETUNE_SCHEMA = {
    "type": "object",
    "properties": {
        "pairs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "instruction": {"type": "string"},
                    "response": {"type": "string"},
                },
                "required": ["instruction", "response"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["pairs"],
    "additionalProperties": False,
}

# Shared by docs + codebase: the input record already passed this project's own "zero
# extrapolation" grounding checks during RAG crunching. This prompt's only job is to RESTYLE
# already-validated content into natural training pairs -- a constrained rephrasing task, not a
# fresh-extraction task, which is deliberately safer against hallucination than re-deriving facts
# from raw source a second time.
RESTYLE_PROMPT = """You are creating fine-tuning training data for a Cubyz voxel-engine assistant. You are given an already-validated, fact-checked knowledge record. Treat every field in the input as ground truth -- your job is ONLY to restyle this content into natural instruction/response training pairs, never to add new facts.

For 3 to 6 of the most genuinely distinct synthetic_queries provided (fewer if the chunk doesn't support that many), write a pair:
- "instruction": the question, phrased as a real developer would naturally ask it in conversation. You may lightly rephrase the synthetic_query for naturalness, but must not change its meaning or add specifics not already implied by it.
- "response": a direct, specific, confident answer in the voice of a helpful, precise Cubyz expert who already knows this -- never phrases like "the retrieved context says" or "according to the documentation."
  - Factual/simple questions: 1-3 sentences, no padding.
  - "how does X work" / mechanism questions: explain the mechanism, then include the code_example verbatim if it's relevant and available.
  - Never state a fact, name, number, or claim that is not explicitly present in the summary, comprehensive_explanation, or code_example you were given.
  - Make sure the response actually answers what its own instruction specifically asks -- not just adjacent or generally-related information from the input.
  - Don't pad a thin or generic answer by appending an unrelated fact from elsewhere in the source just because it's salient (e.g. don't tack "the project also discourages AI-written PRs" onto an answer about memory allocation just because both facts appear somewhere in the same chunk). Every sentence in a response must actually belong to answering that response's own instruction.
  - Don't just restate the instruction's own words back as if that were an answer (e.g. instruction "What happens when X is called during Y?" answered with "During Y, X handles Y-related things"). If you can't add genuinely new, specific detail beyond what the question itself already implies, that question isn't well-supported by this chunk -- pick a different synthetic_query instead.

Before including a pair, check whether you're about to write a hedge like "is not specified", "is not provided", "is not detailed", "is not mentioned", or anything similar (in any verb tense/form -- "are not provided" is just as much a hedge as "is not provided"). If so, that question isn't actually answerable from what you were given -- DROP it entirely and pick a different synthetic_query instead of keeping a pair with a hedge in it. A hedge in the training data is worse than one fewer pair; it teaches the model to give unhelpful non-answers instead of either a real answer or honest silence.

If the input record's own content is too thin, short, or stub-like to support ANY genuinely specific question (e.g. it's just a page title or placeholder with no real body text), output {"pairs": []} entirely rather than inventing generic-sounding questions and answers about the general topic.

The number of pairs must scale with how much genuinely distinct, specific content the input actually contains -- this applies even when the input isn't completely empty. A one- or two-sentence summary supports at most one or two real questions, not three to six. Once you've asked everything the input specifically supports, STOP -- do not keep generating pairs by filling gaps with your own general knowledge of voxel games, Minecraft-like mechanics, or what a system "probably" does. If you notice a candidate answer isn't actually traceable to a specific word or fact in the input you were given, that's fabrication, not restyling -- drop it, even if it sounds plausible.

Do not pad with redundant or speculative pairs just to hit 6 -- fewer genuine pairs is better than inventing marginal ones.

Output strict JSON matching the schema. No markdown, no commentary.
"""

# Reviews get a different, higher-stakes prompt: this is the material that teaches developer
# JUDGMENT, not facts, so grounding discipline matters even more here (see project's own
# CUBYZ_DEVELOPER_JUDGMENT.md for why this category is treated as the core fine-tuning target).
REVIEWS_PROMPT = """You are creating fine-tuning training data for a Cubyz assistant, teaching it the judgment shown in a real code review. comprehensive_explanation is the ground-truth extracted account of that real diff and review comment -- treat it as reliable, not as something to be suspicious of. Do not invent additional context, a different bug, or advice beyond what it describes.

Generate exactly ONE training pair, choosing whichever shape genuinely fits:

SHAPE A (debugging/diagnosis) -- if this review is about a bug or a "why doesn't this work" issue:
  "instruction": a natural first-person description of hitting this exact problem, as if a developer pasted their own code/situation and asked for help. Paraphrase the symptom comprehensive_explanation describes -- do not invent a different scenario.
  "response": the diagnosis and reasoning, grounded strictly in what comprehensive_explanation says the actual reviewer identified. Write it as direct advice from you -- never "the reviewer said X."

SHAPE B (code review) -- if this review is about a design/style/architecture choice rather than a bug:
  "instruction": "Can you review this approach: [a natural paraphrase of what the original code attempted]"
  "response": constructive review feedback matching the real concern raised, in the voice of a direct, technically precise maintainer. Explain WHY, not just what to change.

Most reviews in this dataset ARE substantial enough to support a pair -- a multi-sentence comprehensive_explanation describing a real function, struct, refactor, or design concern is exactly the kind of content this task is FOR, even though you only have the explanation and not the raw diff text itself. Only output {"pairs": []} when comprehensive_explanation itself is a single short sentence describing a trivial rename, import path change, or line-shortening tweak with no design/correctness reasoning behind it at all. When in doubt between generating and skipping, and the explanation gives you a real mechanism or concern to explain, generate the pair.

Never state a fact, name, or claim not present in comprehensive_explanation, symbols, or concepts -- if you can't ground a specific detail, ground the response in a more general but still-true statement from what IS there rather than reaching for an unstated specific (e.g. don't guess at a renamed identifier's exact new spelling if it isn't given).

Output strict JSON matching the schema. No markdown, no commentary.
"""


def check_amd_gpu() -> tuple:
    try:
        res = subprocess.run(['rocm-smi', '--showmeminfo', 'vram'], capture_output=True, text=True)
        if res.returncode == 0 and "vram" in res.stdout.lower():
            match = re.search(r'VRAM Total Memory \(B\):\s*(\d+)', res.stdout)
            if match:
                return True, int(match.group(1)) / (1024.0 ** 3)
    except Exception:
        pass
    try:
        pci = subprocess.run(['lspci'], capture_output=True, text=True).stdout.lower()
        if "amd" in pci or "radeon" in pci:
            return True, 16.0
    except Exception:
        pass
    return False, 0.0


def check_nvidia_gpu() -> tuple:
    try:
        res = subprocess.run(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,nounits,noheader'], capture_output=True, text=True, check=True)
        return True, int(res.stdout.strip().split('\n')[0]) / 1024.0
    except Exception:
        return False, 0.0


def choose_model() -> tuple:
    has_nv, nv_vram = check_nvidia_gpu()
    if has_nv:
        vram = nv_vram
    else:
        has_amd, amd_vram = check_amd_gpu()
        vram = amd_vram if has_amd else 0.0

    # This task needs stronger instruction-following than raw extraction did (it's generating
    # natural prose + judging shape A vs B for reviews), so the floor here is higher than the
    # RAG-crunching client's -- no 3b tier.
    if vram >= 20.0:
        return "qwen3-coder:30b", vram
    elif vram >= 12.0:
        return "qwen2.5-coder:14b", vram
    elif vram >= 6.0:
        return "qwen2.5-coder:7b", vram
    else:
        sys.exit(f"\n[X] Insufficient VRAM ({vram:.1f}G) for fine-tune data generation -- needs at least a 7b-class model.")


def load_saved_user() -> str:
    if os.path.exists(CONFIG_FILE):
        try:
            return json.load(open(CONFIG_FILE)).get("user_id", "")
        except Exception:
            pass
    return ""


def save_user(user_id: str):
    try:
        json.dump({"user_id": user_id}, open(CONFIG_FILE, "w"))
    except Exception:
        pass


def make_request(url, payload=None):
    data = json.dumps(payload).encode('utf-8') if payload else None
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'} if data else {})
    with urllib.request.urlopen(req, timeout=180) as res:
        return json.loads(res.read().decode('utf-8'))


def build_prompt_input(task: dict) -> str:
    record = task["record"]
    source_type = task["source_type"]
    if source_type == "reviews":
        # No raw_content field actually exists in the crunched review records (the RAG campaign
        # never preserved the literal diff text) -- presenting a fake empty "raw_content" block
        # here was misleading, so comprehensive_explanation is presented directly as the ground
        # truth instead of implying there's a raw diff backing it that the model isn't seeing.
        return (
            f"comprehensive_explanation (ground truth, extracted from the real diff/review):\n{record.get('comprehensive_explanation', '')}\n\n"
            f"summary: {record.get('summary', '')}\n"
            f"symbols: {record.get('symbols', [])}\n"
            f"concepts: {record.get('concepts', [])}\n"
        )
    return (
        f"title: {record.get('title', '')}\n"
        f"summary: {record.get('summary', '')}\n"
        f"comprehensive_explanation: {record.get('comprehensive_explanation', '')}\n"
        f"code_example: {record.get('code_example') or 'null'}\n"
        f"symbols: {record.get('symbols', [])}\n"
        f"concepts: {record.get('concepts', [])}\n"
        f"synthetic_queries: {record.get('synthetic_queries', [])}\n"
    )


def grounding_text_for(task: dict) -> str:
    record = task["record"]
    if task["source_type"] == "reviews":
        symbols_text = " ".join(record.get("symbols") or [])
        return f"{record.get('comprehensive_explanation', '')} {symbols_text}"
    # `symbols` is itself a verified field (real identifiers pulled straight from the source
    # during the original RAG crunching, not model-generated prose) -- omitting it here was
    # causing the self-check to reject legitimate, correctly-quoted identifiers (e.g.
    # `baseGravity`) just because they only appeared in symbols and not in the prose summary or
    # the one code_example snippet, which doesn't cover every symbol in the chunk.
    symbols_text = " ".join(record.get("symbols") or [])
    return f"{record.get('summary', '')} {record.get('comprehensive_explanation', '')} {record.get('code_example') or ''} {symbols_text}"


def validate_pairs(pairs, grounding_text: str) -> tuple:
    if not isinstance(pairs, list):
        return False, "pairs is not a list"
    for pair in pairs:
        if not isinstance(pair, dict) or "instruction" not in pair or "response" not in pair:
            return False, "malformed pair"
        # Same spirit as the RAG pipeline's own check: any backtick-quoted identifier in the
        # generated response must actually appear in the source grounding text, or it's very
        # likely an invented symbol/name.
        for name in set(re.findall(r'`([A-Za-z_][A-Za-z0-9_]*)`', pair["response"])):
            if not re.search(r'\b' + re.escape(name) + r'\b', grounding_text):
                return False, f"'{name}' quoted in response but not found in source grounding text"
    return True, ""


def main():
    print("=== Cubyz Fine-Tune Dataset Generation Node (Linux Edition) ===")

    user_id = load_saved_user()
    if not is_valid_user_id(user_id):
        user_id = ""
        while not is_valid_user_id(user_id):
            user_id = input("Enter your unique volunteer ID (3-9 letters only): ").strip()
        save_user(user_id)
    print(f"[OK] Logged in as: {user_id}")

    model, vram = choose_model()
    print(f"[~] Selected model: {model} ({vram:.1f}G VRAM)")

    source_type_filter = input("Restrict to one source type (docs/codebase/reviews), or leave blank for any: ").strip().lower()
    if source_type_filter not in ("docs", "codebase", "reviews"):
        source_type_filter = ""

    while True:
        try:
            query = f"{SERVER_URL}/get_work?user_id={user_id}"
            if source_type_filter:
                query += f"&source_type={source_type_filter}"
            work_package = make_request(query)

            if work_package.get("status") == "done":
                print("\n[*] Campaign complete! All chunks processed. Thank you!")
                break
            if work_package.get("status") == "waiting":
                print("[~] No tasks available right now. Sleeping...")
                time.sleep(30)
                continue

            task = work_package["task"]
            source_type = task["source_type"]
            prompt_text = RESTYLE_PROMPT if source_type in ("docs", "codebase") else REVIEWS_PROMPT

            payload = {
                "model": model,
                "prompt": build_prompt_input(task),
                "system": prompt_text,
                "think": False,
                "stream": False,
                "format": FINETUNE_SCHEMA,
                "options": {"temperature": 0.3},
            }

            print(f"[~] Processing {source_type}: {task['chunk_id']}...")

            parsed = None
            last_failure = "no attempts"
            for attempt in range(3):
                if attempt > 0:
                    time.sleep(3)
                try:
                    res = make_request(OLLAMA_URL, payload)
                    raw = res.get("response", "").strip()
                except Exception as e:
                    last_failure = f"{type(e).__name__}: {e}"
                    continue
                if raw.startswith("```"):
                    lines = raw.splitlines()
                    if lines and lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].startswith("```"):
                        lines = lines[:-1]
                    raw = "\n".join(lines).strip()
                try:
                    candidate = json.loads(raw[raw.find("{"):raw.rfind("}") + 1] if "{" in raw else raw)
                except Exception as e:
                    last_failure = f"JSON parse error: {e}"
                    continue

                ok, reason = validate_pairs(candidate.get("pairs", []), grounding_text_for(task))
                if ok:
                    parsed = candidate
                    break
                last_failure = f"Self-check failed: {reason}"

            if parsed is None:
                # Submit a 0-pairs result instead of just `continue`-ing past it: without this,
                # the chunk is never reported to the server, so its lock just expires after
                # TASK_TIMEOUT and it gets handed back out again -- forever, if the failure is
                # deterministic (e.g. a genuinely too-thin/unanswerable chunk). Marking it
                # complete with 0 pairs lets the campaign actually finish instead of looping.
                print(f"    [X] Giving up after 3 failed attempts ({last_failure}). Marking as done with 0 pairs.")
                try:
                    make_request(f"{SERVER_URL}/submit_work", {
                        "chunk_id": task["chunk_id"],
                        "source_type": source_type,
                        "pairs": [],
                        "user_id": user_id,
                        "lines_crunched": 0,
                    })
                except Exception:
                    pass
                time.sleep(1)
                continue

            submission = {
                "chunk_id": task["chunk_id"],
                "source_type": source_type,
                "pairs": parsed["pairs"],
                "user_id": user_id,
                "lines_crunched": len(parsed["pairs"]),
            }
            make_request(f"{SERVER_URL}/submit_work", submission)
            print(f"    [OK] Submitted {len(parsed['pairs'])} pairs.")

        except KeyboardInterrupt:
            print("\n[X] Disconnecting. Thank you for your contributions!")
            break
        except urllib.error.HTTPError as he:
            print(f"\n[Warning] Server error {he.code}. Retrying in 15 seconds...")
            time.sleep(15)
        except Exception as e:
            print(f"\n[Error] {e}. Retrying in 5 seconds...")
            time.sleep(5)


if __name__ == "__main__":
    main()
