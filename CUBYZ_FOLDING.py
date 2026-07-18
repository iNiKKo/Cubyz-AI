import os
import re
import sys
import json
import ssl
import time
import platform
import subprocess
import shutil
import urllib.request
import urllib.error
import urllib.parse
import threading

if sys.platform.startswith("linux"):
    PLATFORM = "linux"
elif sys.platform == "darwin":
    PLATFORM = "darwin"
elif sys.platform.startswith("win32"):
    PLATFORM = "win32"
else:
    print(f"[X] Unsupported operating system: {sys.platform}")
    sys.exit(1)

if PLATFORM == "win32":
    os.system('color')

# ============================================================
# TERMINAL COLOR -- disabled automatically when stdout isn't a real terminal (piped/redirected
# to a file) or when the standard NO_COLOR env var is set, so logs/redirected output never end
# up full of raw escape codes. All Colors.* attributes become empty strings in that case, so
# every f-string that uses them degrades to plain text for free -- no separate no-color branch
# needed anywhere else in the file.
# ============================================================

def _supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    try:
        return sys.stdout.isatty()
    except Exception:
        return False

_COLOR_ON = _supports_color()

class Colors:
    RESET = "\033[0m" if _COLOR_ON else ""
    BOLD = "\033[1m" if _COLOR_ON else ""
    DIM = "\033[2m" if _COLOR_ON else ""
    RED = "\033[91m" if _COLOR_ON else ""
    GREEN = "\033[92m" if _COLOR_ON else ""
    YELLOW = "\033[93m" if _COLOR_ON else ""
    BLUE = "\033[94m" if _COLOR_ON else ""
    MAGENTA = "\033[95m" if _COLOR_ON else ""
    CYAN = "\033[96m" if _COLOR_ON else ""
    GRAY = "\033[90m" if _COLOR_ON else ""

# One color per campaign mode -- ties the live status box, its mode-activation banner, and the
# progress bar fill together visually so RAG and FINETUNE are never confusable at a glance.
MODE_COLORS = {"rag": Colors.CYAN, "finetune": Colors.MAGENTA, "idle": Colors.GRAY}

def mode_color(mode: str) -> str:
    return MODE_COLORS.get(mode, Colors.BLUE)

# ============================================================
# SERVER PROTOCOL (current + planned)
# ------------------------------------------------------------
# This client no longer lets the volunteer choose which campaign to work on -- that choice
# now belongs entirely to the server. GET /get_work?user_id=...&hardware_tier=...&model=...
# is expected to return a top-level "mode" field telling the client what to do:
#   "idle"      -> no campaign currently active; client shows "server online, no tasks
#                  available" and polls again later.
#   "rag"       -> RAG knowledge-extraction campaign is active; "status"/"task"/
#                  "total_chunks"/"completed_chunks" behave exactly like today's
#                  pipeline_crunching/server.py ("task" is RAG-shaped: file_name,
#                  relative_path, directory_context, chunk_index, chunk_id, raw_content).
#   "finetune"  -> fine-tune pair-generation campaign is active; same status/task/progress
#                  fields, but "task" is finetune-shaped: chunk_id, source_type, record.
#
# pipeline_crunching/server.py now IS this unified server -- it merged in finetune/
# server_finetune.py's campaign (archived at archive/server_finetune.py) and emits "mode" on
# every /get_work response, switchable live via POST /admin/mode?mode=idle|rag|finetune without
# restarting. This client still defaults an absent "mode" field to "rag" as a defensive
# fallback, not because that's expected in normal operation anymore.
#
# hardware_tier is also how the unified server gates finetune-mode work away from low-VRAM
# ("easy" tier, qwen2.5-coder:3b) clients: get_vram_and_choose_model()'s tiers below 6GB VRAM
# don't meet finetune generation's higher instruction-following floor (see choose_model's
# docstring below), so finetune tasks are only ever routed to "medium"/"hard" tier clients --
# the same tiers whose chosen model already happens to satisfy finetune's 7b-class floor, so no
# separate model selection is needed client-side.
#
# /leaderboard's shape still depends on CURRENT_MODE server-side (RAG mode: total_chunks_in_codebase
# / lines_crunched; finetune mode: total_chunks_in_campaign / pairs_generated) since the two
# campaigns' underlying stats were never made to fully agree -- this client reads both field
# name variants defensively so it doesn't crash regardless of which mode is currently active.
# ============================================================

SERVER_URL = "http://ashframe.net:7000"

# Guards stdout when a second (dual-lane) crunch_lane() is running in a background thread
# alongside the primary one in the main thread -- see run_dual_lane_if_capable(). Only ever
# contended on machines with both a real GPU and enough spare RAM to run a second lane; a
# solo-lane client never touches it under contention.
print_lock = threading.Lock()
OLLAMA_URL = "http://localhost:11434/api/generate"
CONFIG_FILE = os.path.expanduser("~/.cubyz_node_config.json")
DIAGNOSTICS_FILE = os.path.expanduser("~/.cubyz_node_diagnostics.jsonl")

# Bump this whenever the protocol this client speaks changes in a way the server needs to know
# about (new required fields, new modes, etc.) -- the server rejects anything below its own
# MIN_CLIENT_VERSION with an "update required" error rather than silently mishandling it.
VERSION = "1.1.17"

def _parse_version(v: str) -> tuple:
    try:
        return tuple(int(p) for p in v.strip().split("."))
    except Exception:
        return (0,)

def check_for_update():
    """Returns (status, info) where status is 'current', 'update_available', 'must_update', or
    'check_failed'. info is the /version response dict, or None on check_failed."""
    try:
        info = make_request(f"{SERVER_URL}/version", timeout=10)
    except Exception:
        return "check_failed", None

    min_v = info.get("min_client_version", "0.0.0")
    latest_v = info.get("latest_client_version", VERSION)
    if _parse_version(VERSION) < _parse_version(min_v):
        return "must_update", info
    if _parse_version(VERSION) < _parse_version(latest_v):
        return "update_available", info
    return "current", info

def _https_context() -> ssl.SSLContext:
    """Best-effort SSL context for the GitHub update download. python.org's macOS installer
    doesn't wire the interpreter up to the system trust store the way Homebrew/Linux Python does,
    so the stdlib's plain default context can fail with "certificate verify failed: unable to get
    local issuer certificate" even on a machine whose certificates are otherwise completely fine.
    Tries certifi's bundle first (if installed), then a couple of common system cert-file
    locations, before falling back to the plain default that would have failed in the first place."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    for candidate in ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt"):
        if os.path.exists(candidate):
            return ssl.create_default_context(cafile=candidate)
    return ssl.create_default_context()

def download_update(download_url: str, expected_version: str) -> bool:
    try:
        with urllib.request.urlopen(download_url, timeout=30, context=_https_context()) as res:
            new_content = res.read()
    except Exception as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e).upper():
            print(
                f"{Colors.RED}[X] Update download failed: couldn't verify the update server's certificate.{Colors.RESET}\n"
                f"{Colors.YELLOW}    Common on macOS with a python.org install -- it isn't wired up to your\n"
                f"    system's root certificates by default. Fix it with one of:\n"
                f"      pip3 install --upgrade certifi\n"
                f"      open \"/Applications/Python {sys.version_info.major}.{sys.version_info.minor}/Install Certificates.command\"\n"
                f"    then restart this client.{Colors.RESET}"
            )
        else:
            print(f"{Colors.RED}[X] Update download failed: {e}{Colors.RESET}")
        return False

    # Confirm the downloaded content actually IS the version being advertised before installing
    # it. raw.githubusercontent.com's CDN can keep serving a stale cached copy for a few minutes
    # right after a push -- without this check, a client polling in exactly that window would
    # "successfully" overwrite itself with content reporting the SAME old version, restart,
    # immediately see the identical "update available" mismatch again, and loop forever
    # (confirmed live: a node stuck re-downloading and restarting on repeat, never actually
    # advancing past the version it already had).
    match = re.search(rb'^VERSION\s*=\s*["\']([\d.]+)["\']', new_content, re.MULTILINE)
    downloaded_version = match.group(1).decode() if match else None
    if downloaded_version != expected_version:
        print(
            f"{Colors.YELLOW}[!] Downloaded update reports v{downloaded_version or '?'}, not the "
            f"expected v{expected_version} -- likely a CDN caching delay right after a release. "
            f"Skipping this restart; will check again next cycle.{Colors.RESET}"
        )
        return False

    this_file = os.path.abspath(__file__)
    try:
        with open(this_file, "wb") as f:
            f.write(new_content)
    except Exception as e:
        print(f"{Colors.RED}[X] Could not write update to {this_file}: {e}{Colors.RESET}")
        return False

    print(f"{Colors.GREEN}[✓] Update downloaded and saved to {this_file}.{Colors.RESET}")
    return True

def offer_update(status: str, info: dict, mandatory: bool):
    latest_v = info.get("latest_client_version", "?")
    download_url = info.get("download_url", "")
    if mandatory:
        print(f"\n{Colors.RED}{Colors.BOLD}[X] This client (v{VERSION}) is no longer accepted by the server -- you must update to continue.{Colors.RESET}")
        print(f"{Colors.RED}    Latest version: v{latest_v}{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}[i] Update available: v{latest_v} (you have v{VERSION}). Not required to keep working, but recommended.{Colors.RESET}")

    if load_auto_update_preference():
        print(f"    {Colors.CYAN}[~] Auto-update is enabled -- downloading and restarting automatically...{Colors.RESET}")
        choice = 'y'
    else:
        choice = input(f"    {Colors.YELLOW}Download the update now? (y/n): {Colors.RESET}").strip().lower()
    if choice != 'y':
        if mandatory:
            sys.exit(f"{Colors.RED}[X] Cannot continue on an unsupported client version. Re-run and accept the update, or update manually: {download_url}{Colors.RESET}")
        return

    if download_update(download_url, latest_v):
        # Overwriting this file on disk doesn't change what's already loaded in this process --
        # os.execv replaces the running process image outright, so the new code actually takes
        # over immediately instead of leaving the volunteer to notice a message and restart it
        # themselves by hand.
        print(f"{Colors.GREEN}[✓] Update installed. Restarting automatically with the new version...{Colors.RESET}")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    elif mandatory:
        sys.exit(f"{Colors.RED}[X] Could not auto-update. Please update manually: {download_url}{Colors.RESET}")

USER_ID_PATTERN = re.compile(r"^[a-zA-Z]+$")

def is_valid_user_id(user_id: str) -> bool:
    return bool(user_id) and 3 <= len(user_id) <= 9 and bool(USER_ID_PATTERN.fullmatch(user_id))

# ============================================================
# RAG MODE -- schema, prompts (from pipeline_crunching/RAG_FOLDING.py)
# ============================================================

RAG_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "A concise 1-2 sentence overview of the chunk's primary purpose."
        },
        "comprehensive_explanation": {
            "type": "string",
            "description": "Dense, explicit technical explanation of only what is present: logic, flow, architecture, algorithms, state changes, interactions, memory ownership, serialization, networking, validation, or gameplay mechanics."
        },
        "symbols": {
            "type": "array",
            "description": "Important identifiers explicitly declared or referenced in the chunk.",
            "items": {"type": "string"}
        },
        "concepts": {
            "type": "array",
            "description": "High-level engine or gameplay concepts represented by the chunk.",
            "items": {"type": "string"}
        },
        "keywords": {
            "type": "array",
            "description": "Short searchable technical keywords for retrieval.",
            "items": {"type": "string"},
            "minItems": 5,
            "maxItems": 15
        },
        "chunk_type": {
            "type": "string",
            "enum": [
                "implementation", "algorithm", "api", "serialization", "networking", "world_generation",
                "configuration", "documentation", "review", "ui", "asset", "gameplay", "other"
            ]
        },
        "code_example": {
            "type": ["string", "null"],
            "description": "Minimal code snippet illustrating the core implementation. Null if none exists."
        },
        "synthetic_queries": {
            "type": "array",
            "description": "Natural developer questions likely to retrieve this chunk.",
            "items": {"type": "string"},
            "minItems": 6,
            "maxItems": 12
        }
    },
    "required": [
        "summary",
        "comprehensive_explanation",
        "symbols",
        "concepts",
        "keywords",
        "chunk_type",
        "code_example",
        "synthetic_queries"
    ],
    "additionalProperties": False
}

RAG_PROMPTS = {
    "CODEBASE": """You are a deterministic data-extraction compiler documenting the Cubyz voxel engine codebase.
Your task is to parse raw content and emit strict JSON describing only the technical realities explicitly present in the source.

Source role: FUNCTIONAL_CODEBASE_LOGIC (.zig, .zon) -- architecture, execution flow, data structures, APIs, engine behavior.

Constraints:
- ZERO EXTRAPOLATION: do not infer or assume anything not explicit; preserve identifiers exactly.
- LANGUAGE ADAPTATION:
    - .zig: extract executable logic; preserve function names and signatures where visible.
    - .zon: treat as configuration/data; extract exact structure; do not invent wrappers.
- DENSE FACTS: each sentence must convey concrete technical information; no introductions or opinions; avoid repetition.
- SUMMARY: 1-2 sentences; state primary chunk responsibility only.
- COMPREHENSIVE_EXPLANATION: describe only information found in the chunk; focus on execution flow, function responsibilities, state transitions, algorithms, dependencies, data structures, error handling, concurrency, memory ownership, serialization, file I/O, networking, and inter-component interactions; do not repeat the summary.
- SYMBOLS: each entry is a bare NAME only -- never a full statement, never containing `(`, `)`, `{`, `;`, or `=`. Include a name only if this chunk itself declares it via `const NAME = struct`, `const NAME = enum`, `const NAME = union`, `fn NAME(`, `pub fn NAME(`, a struct field `NAME:`, or `pub const NAME = @import(...)` (a PUBLIC re-export -- this file is choosing to expose NAME as part of its own API, so it counts as declared here even though the value comes from another file). Exclude anything that is only a local variable inside a function body, only the target of a function call, only a builtin (`@memcpy`, `@import`, ...), or a PRIVATE (non-`pub`) `const NAME = @import(...)` alias used just for internal convenience. If a `fn` or field is declared inside another struct's body, qualify it as `Parent.name`; top-level declarations stay bare.
  - CORRECT pattern: a chunk defining `pub const SomeStruct = struct { fieldName: SomeType, pub fn someMethod(...) T {...} }` has symbols `SomeStruct`, `SomeStruct.fieldName`, `SomeStruct.someMethod` -- names copied from THIS chunk's own declarations, never from an example.
  - CORRECT pattern: a chunk that is only `pub const SomeName = @import("other_file.zig");` (no `struct`/`fn` anywhere) has symbols `SomeName`, because it's a `pub const` re-export -- this file's entire declared surface.
  - INCORRECT: including an imported type used only as a field's type annotation (not declared here); including a whole statement instead of a bare name; or including `someLocalVar.someMethod()` (a call inside a function body, not a declaration).
- CONCEPTS: name the high-level engine/gameplay concepts the chunk implements (e.g. chunk meshing, entity ECS, world generation, networking protocol).
- KEYWORDS: 5-15 short (1-3 word) technical terms a developer would search for -- domain nouns and mechanism names (e.g. "reference counting", "binary serialization", "mutex locking"). Never a raw code expression, dotted call, or anything containing `(`, `)`, or `.` taken verbatim from the source.
- CHUNK_TYPE: pick exactly one enum value by what the chunk's code DOES, not its file location: "serialization" = binary/text encode-decode, read/write formats; "networking" = sockets, packets, protocol messages; "algorithm" = a self-contained computational procedure (pathing, compression, hashing); "api" = a public interface surface meant for other modules to call; "world_generation" = terrain/structure/biome generation; "configuration" = static settings/config data with no executable logic; "gameplay" = player-facing mechanics (combat, inventory, movement rules); "implementation" = general engine logic not covered by the above; use "other" only if truly none apply.
- CODE_EXAMPLE: mechanical procedure, follow it exactly: (1) find every function/method body in the chunk; (2) count the raw lines between each one's opening `{` and matching closing `}`; (3) copy the one with the FEWEST lines VERBATIM, character-for-character, from THIS chunk's own raw content, including every line of its body -- ignore how "important" or "illustrative" it looks, line count is the only criterion. This must be a fresh copy of text that is actually present in the raw content you were given for THIS chunk -- never reuse, recall, or adapt a snippet from any other file or from these instructions themselves. Never omit or replace any part of the body with "..." -- if that impulse comes up, you picked the wrong (too long) function; go back to step 3 and pick the next-shortest one instead. Set null ONLY if the chunk truly has no function bodies or struct/enum definitions at all (e.g. pure imports or comments).
  - CORRECT: the chunk's own shortest complete function or struct/enum body, copied character-for-character from the raw content above -- e.g. if the chunk has a 3-line getter and a 40-line initializer, extract the getter's full 3 lines verbatim, nothing more and nothing paraphrased.
  - INCORRECT: a truncated body with "..." in place of real lines; a function signature with no body at all; or ANY code that does not appear verbatim in this specific chunk's raw content, no matter how plausible it looks.
- SYNTHETIC_QUERIES: generate as many retrieval questions as this chunk's actual content genuinely supports (architecture, implementation, debugging, API lookup, symbol lookup, execution flow, dependency lookup), minimum 6, maximum 12. The minimum of 6 is a legitimate, common outcome for a small or simple chunk -- do NOT stretch toward 12 by inventing speculative questions about "best practices," "potential issues," "future considerations," "how this might affect other code," or any other topic the chunk itself does not address. Every question must be answerable using only what is explicitly in this chunk. Fewer real questions is always better than more invented ones.

OUTPUT: valid JSON conforming to the schema. No markdown, no commentary.
""",
    "WIKI": """You are a deterministic data-extraction compiler documenting Cubyz voxel engine documentation.
Parse documentation and emit strict JSON describing only explicitly documented information.

Source role: DEFINITIVE_WIKI_DOCUMENTATION (.md, .txt, .html)

Constraints:
- ZERO EXTRAPOLATION: rely exclusively on explicitly mentioned game concepts, features, specs, and config properties.
- DENSE FACTS: each sentence must convey concrete technical information; no introductions or opinions; avoid repetition.
- SUMMARY: 1-2 sentences.
- COMPREHENSIVE_EXPLANATION: capture mechanics, gameplay systems, configuration, terminology, limitations, workflows, design intent, requirements, examples; no undocumented behavior.
- VERBATIM FACT PRESERVATION: if the source states a specific number, exact command/config syntax, named value, or a direct question-and-answer pair (e.g. an FAQ entry), COMPREHENSIVE_EXPLANATION must state that value or answer explicitly and completely -- never replace it with a description of its topic or existence. Failure example: writing "covers healing mechanics" when the source literally says "there is no way to heal" is a failure; the actual answer must appear. For FAQ-style, table, or list-structured content specifically, restate each individual entry's actual content one by one, not just an overview of what the list covers as a whole.
- SYMBOLS: explicitly documented commands, configuration keys, block/item/biome/API/entity names.
- CONCEPTS: name the high-level gameplay or documentation topics the chunk covers.
- KEYWORDS: generate 5-15 concise technical keywords present in the chunk.
- CHUNK_TYPE: classify using exactly one enum value that best matches the chunk's role.
- CODE_EXAMPLE: literal code/config examples; otherwise null.
- SYNTHETIC_QUERIES: generate 6-12 retrieval questions (gameplay, mechanics, configuration, terminology, troubleshooting).

OUTPUT: schema-compliant JSON only.
""",
    "GITHUB_REVIEWS": """You are a deterministic data-extraction compiler documenting Cubyz development history.

Source role: GITHUB_REVIEWS (.json, review comments, diffs)

Constraints:
- ZERO EXTRAPOLATION: rely exclusively on explicit statements in the review/diff; never invent motive.
- SUMMARY: summarize the change in 1-2 sentences.
- COMPREHENSIVE_EXPLANATION: focus on bug cause, reviewer concerns, architectural reasoning, regression prevention, refactor motivation, performance, correctness.
- SYMBOLS: extract functions, files, classes, structs, modules, APIs mentioned.
- CONCEPTS: name the high-level engineering concepts at stake (e.g. thread safety, backwards compatibility, memory leak).
- KEYWORDS: generate 5-15 concise technical keywords present in the chunk.
- CHUNK_TYPE: classify using exactly one enum value that best matches the chunk's role (typically "review").
- CODE_EXAMPLE: smallest modified diff portion (<=60 lines); otherwise null.
- SYNTHETIC_QUERIES: generate 6-12 debugging-oriented retrieval questions.

OUTPUT: valid JSON.
""",
    "ADDON_STUDIO": """You are a deterministic data-extraction compiler documenting the Cubyz Addon Creator workspace.

Source role: ADDON_STUDIO_BLUEPRINTS (.js, .html)

Constraints:
- ZERO EXTRAPOLATION: describe only explicit bindings.
- SUMMARY: UI component responsibility in 1-2 sentences.
- COMPREHENSIVE_EXPLANATION: extract UI controls, event handlers, validation, defaults, templates, bindings, engine mappings, configuration generation.
- SYMBOLS: classes, functions, exported objects, UI components, IDs, event handlers.
- CONCEPTS: name the high-level editor/UI concepts the chunk implements (e.g. data-binding, form validation, live preview).
- KEYWORDS: generate 5-15 concise UI/editor keywords.
- CHUNK_TYPE: classify using exactly one enum value that best matches the chunk's role (typically "ui").
- CODE_EXAMPLE: smallest binding/config snippet (<=60 lines); otherwise null.
- SYNTHETIC_QUERIES: generate 6-12 questions about UI behavior, bindings, validation, templates, addon creation, configuration.

OUTPUT: valid JSON.
"""
}

LOW_VRAM_REASONING_RULE = """
Additional constraint for constrained hardware: work in a single deterministic pass. Do not restate these instructions and do not add caveats or meta-commentary. Keep every field as short as the schema allows while remaining accurate, and always fill every required field -- never omit one.
"""

# ============================================================
# FINETUNE MODE -- schema, prompts (from finetune/scripts/FINETUNE_FOLDING.py)
# ============================================================

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
FINETUNE_RESTYLE_PROMPT = """You are creating fine-tuning training data for a Cubyz voxel-engine assistant. You are given an already-validated, fact-checked knowledge record. Treat every field in the input as ground truth -- your job is ONLY to restyle this content into natural instruction/response training pairs, never to add new facts.

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
# JUDGMENT, not facts, so grounding discipline matters even more here.
FINETUNE_REVIEWS_PROMPT = """You are creating fine-tuning training data for a Cubyz assistant, teaching it the judgment shown in a real code review. comprehensive_explanation is the ground-truth extracted account of that real diff and review comment -- treat it as reliable, not as something to be suspicious of. Do not invent additional context, a different bug, or advice beyond what it describes.

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

# ============================================================
# HARDWARE DETECTION -- unchanged from RAG_FOLDING.py. Reused for both modes: finetune's model
# tiers (30b/14b/7b at 20/12/6 GB) are identical to RAG's at those same three tiers, the only
# difference being RAG also has a lower 3b/CPU tier that finetune generation isn't strong enough
# for. A client whose hardware lands it on RAG's 3b tier simply isn't finetune-capable -- see the
# protocol note above on hardware_tier gating finetune work away from "easy" tier clients.
# ============================================================

def get_linux_distro() -> str:
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"')
    except Exception: pass
    return "unknown"

def _run_powershell(command: str) -> str:
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
            capture_output=True, text=True, timeout=15
        )
        return result.stdout.strip()
    except Exception:
        return ""

def get_system_ram_gb() -> float:
    if PLATFORM == "darwin":
        try:
            out = subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True, check=True).stdout.strip()
            return int(out) / (1024.0 ** 3)
        except Exception:
            return 8.0

    if PLATFORM == "win32":
        out = _run_powershell("(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory")
        if out.isdigit():
            return int(out) / (1024.0 ** 3)
        try:
            result = subprocess.run(
                ["wmic", "ComputerSystem", "get", "TotalPhysicalMemory", "/value"],
                capture_output=True, text=True, timeout=15
            )
            for line in result.stdout.split("\n"):
                if "TotalPhysicalMemory" in line and "=" in line:
                    return int(line.split("=")[1].strip()) / (1024.0 ** 3)
        except Exception:
            pass
        return 8.0

    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1]) / (1024.0 * 1024.0)
    except Exception: pass
    return 8.0

def is_apple_silicon() -> bool:
    return platform.machine() == "arm64"

def check_apple_silicon_gpu() -> tuple:
    if not is_apple_silicon():
        return False, 0.0
    ram_gb = get_system_ram_gb()
    # Apple Silicon has unified memory -- there's no separate VRAM pool, so this estimates how
    # much of total RAM is safe to hand to a model. A flat 75% (the old behavior) left only ~2GB
    # for macOS itself on an 8GB M1 -- not enough for the OS to function once a 7B model (the tier
    # that boundary picks) is loaded, causing heavy swap thrashing under sustained crunching load
    # that presented as thermal throttling / full system crashes after 5-10 minutes.
    # min() of a fixed OS-overhead subtraction and the old percentage: for RAM >= 14GB the
    # percentage is the tighter (smaller) bound, so this is a no-op there -- 16GB+ Apple Silicon
    # machines pick exactly the same model as before. Only the 8GB tier (the one actually
    # reported broken) gets a meaningfully smaller, safer budget.
    return True, min(ram_gb - 3.5, ram_gb * 0.75)

def check_intel_mac_dgpu() -> tuple:
    if is_apple_silicon():
        return False, 0.0
    try:
        res = subprocess.run(["system_profiler", "SPDisplaysDataType"], capture_output=True, text=True, timeout=10)
        output = res.stdout
    except Exception:
        return False, 0.0

    for block in re.split(r'\n\s*\n', output):
        if "Bus: PCIe" not in block:
            continue
        match = re.search(r'VRAM[^:\n]*:\s*([\d.]+)\s*(GB|MB)', block)
        if match:
            value, unit = float(match.group(1)), match.group(2)
            return True, (value / 1024.0 if unit == "MB" else value)
        # A discrete GPU block exists but system_profiler didn't report a parseable VRAM figure --
        # detected-but-unknown-size (0.0) rather than a fabricated number. See check_nvidia_gpu's
        # comment for how "unknown" is handled downstream (smallest safe model tier, then the
        # real benchmark decides usability).
        return True, 0.0
    return False, 0.0

def _windows_adapter_vram_gb(adapter_ram) -> float:
    """AdapterRAM from WMI's Win32_VideoController is a real reading when it works, but it's a
    known-unreliable field on some Windows systems: certain drivers report it clamped to exactly
    the 32-bit-unsigned ceiling (4294967295 bytes, "-1" reinterpreted as unsigned) instead of the
    true value once real VRAM exceeds ~4 GB. That's a narrow, specific pattern to reject -- NOT
    "any large value": most real cards legitimately report well above 4 GB and a naive "reject
    anything near or above 4 GB" check would wrongly discard the correct reading for nearly every
    modern GPU (an earlier version of this function did exactly that; caught before it shipped).
    A negative value is the same overflow, just interpreted as signed. 0.0 (detected-but-unknown-
    size) is returned for both that sentinel and anything otherwise unparseable, never a
    fabricated number."""
    try:
        val = int(adapter_ram)
    except (TypeError, ValueError):
        return 0.0
    if val <= 0 or val in (4294967295, 4294967296):
        return 0.0
    return val / (1024.0 ** 3)

def _normalize_gpu_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'\((r|tm|c)\)|[®™©]', '', name)
    return re.sub(r'\s+', ' ', name).strip()

def get_windows_gpus() -> list:
    out = _run_powershell("Get-CimInstance Win32_VideoController | Select-Object Name,AdapterRAM | ConvertTo-Json -Compress")
    gpus = []
    if out:
        try:
            data = json.loads(out)
            if isinstance(data, dict):
                data = [data]
            for entry in data:
                gpus.append({"Name": entry.get("Name") or "", "AdapterRAM": entry.get("AdapterRAM")})
            if gpus:
                return gpus
        except Exception:
            pass
    try:
        result = subprocess.run(
            ["wmic", "path", "win32_VideoController", "get", "Name,AdapterRAM", "/value"],
            capture_output=True, text=True, timeout=15
        )
        current_gpu = {}
        for line in result.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            if "=" in line:
                key, val = line.split("=", 1)
                current_gpu[key.strip()] = val.strip()
                if len(current_gpu) == 2:
                    gpus.append(current_gpu)
                    current_gpu = {}
    except Exception:
        pass
    return gpus

def check_nvidia_gpu() -> tuple:
    try:
        res = subprocess.run(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,nounits,noheader'], capture_output=True, text=True, check=True, timeout=15)
        vram = int(res.stdout.strip().split('\n')[0]) / 1024.0
        return True, vram
    except Exception:
        pass

    # nvidia-smi failing on a real Nvidia card (driver/PATH issue, etc.) still leaves the GPU
    # detectable by name -- but with no real VRAM reading available, report it as detected with
    # an unknown size (0.0) rather than fabricating a number. get_vram_and_choose_model() treats
    # unknown VRAM as "pick the smallest safe model," and the benchmark (see benchmark_lane() in
    # main()) is what actually decides whether this GPU is worth using at all -- not a guess here.
    if PLATFORM == "win32":
        for gpu in get_windows_gpus():
            name = _normalize_gpu_name(str(gpu.get("Name", "")))
            if "nvidia" in name or "geforce" in name or "quadro" in name or "rtx" in name:
                return True, _windows_adapter_vram_gb(gpu.get("AdapterRAM"))
    else:
        try:
            pci = subprocess.run(['lspci'], capture_output=True, text=True).stdout
            if "nvidia" in pci.lower():
                return True, 0.0
        except Exception: pass
    return False, 0.0

def _amd_vram_from_sysfs() -> float:
    """Reads real VRAM size straight from the amdgpu kernel driver's sysfs interface -- exposed
    for essentially every AMD GPU the amdgpu driver supports, including older consumer cards
    (e.g. Polaris/RX 500-series) that amd-smi/rocm-smi frequently don't recognize at all, with no
    extra tooling required. Returns 0.0 if nothing readable is found (not on Linux, driver not
    loaded, permissions, etc.) so callers can fall through to their next-best option."""
    try:
        import glob
        for vendor_path in glob.glob('/sys/class/drm/card*/device/vendor'):
            with open(vendor_path) as f:
                if f.read().strip() != '0x1002':  # AMD's PCI vendor ID
                    continue
            vram_path = vendor_path.replace('/vendor', '/mem_info_vram_total')
            if os.path.exists(vram_path):
                with open(vram_path) as f:
                    vram_bytes = int(f.read().strip())
                if vram_bytes > 0:
                    return vram_bytes / (1024.0 ** 3)
    except Exception:
        pass
    return 0.0

def check_amd_gpu() -> tuple:
    if PLATFORM == "win32":
        for gpu in get_windows_gpus():
            name = _normalize_gpu_name(str(gpu.get("Name", "")))
            if "amd" not in name and "radeon" not in name:
                continue
            # No universally-installed real-VRAM tool for AMD on Windows (amd-smi/rocm-smi are
            # Linux-first and rarely present here) -- AdapterRAM if it's a sane reading, otherwise
            # detected-but-unknown-size (0.0) rather than a fabricated number. See
            # _windows_adapter_vram_gb's comment and get_vram_and_choose_model()/benchmark_lane()
            # for how "unknown" gets handled downstream (smallest safe model, then measured).
            return True, _windows_adapter_vram_gb(gpu.get("AdapterRAM"))
        return False, 0.0

    for cmd in [['amd-smi', 'metric', '--json'], ['rocm-smi', '--showmeminfo', 'vram']]:
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0 or "vram" not in res.stdout.lower():
                continue
            if cmd[0] == 'rocm-smi':
                match = re.search(r'VRAM Total Memory \(B\):\s*(\d+)', res.stdout)
                if match:
                    return True, int(match.group(1)) / (1024.0 ** 3)
            break
        except Exception: continue
    try:
        pci = subprocess.run(['lspci'], capture_output=True, text=True).stdout.lower()
        if "amd" in pci or "radeon" in pci:
            # amd-smi/rocm-smi either aren't installed or don't recognize this card (common for
            # older consumer GPUs, e.g. Polaris/RX 500-series, which ROCm's compute tooling was
            # never targeted at) -- sysfs is the actual real reading, not a guess, and needs
            # nothing beyond the kernel driver that's already loaded for the card to work at all.
            # If even sysfs has nothing, report detected-but-unknown-size (0.0) rather than
            # fabricating a number -- see check_nvidia_gpu's comment for how that's handled
            # downstream (smallest safe model tier, then the real benchmark decides usability).
            return True, _amd_vram_from_sysfs()
    except Exception: pass
    return False, 0.0

def check_intel_gpu() -> tuple:
    if PLATFORM == "win32":
        for gpu in get_windows_gpus():
            name = _normalize_gpu_name(str(gpu.get("Name", "")))
            if "intel" not in name:
                continue
            return True, _windows_adapter_vram_gb(gpu.get("AdapterRAM"))
        return False, 0.0

    try:
        pci = subprocess.run(['lspci'], capture_output=True, text=True).stdout.lower()
        if "intel" in pci and any(x in pci for x in ["arc", "graphics", "dg2", "dg3"]):
            # No reliable real-VRAM reading attempted here (Intel's discrete-GPU sysfs layout is
            # less consistent/verified across kernel driver generations than amdgpu's) -- rather
            # than guess a wrong path or a wrong number, report detected-but-unknown-size and let
            # the benchmark decide, same as everywhere else in this file.
            return True, 0.0
    except Exception: pass
    return False, 0.0

def get_vram_and_choose_model() -> tuple:
    gpu_type, total_vram_gb = "cpu", 0.0
    ram_gb = get_system_ram_gb()

    if PLATFORM == "darwin":
        has_apple_gpu, apple_vram = check_apple_silicon_gpu()
        if has_apple_gpu:
            gpu_type, total_vram_gb = "apple_silicon", apple_vram
        else:
            has_dgpu, dgpu_vram = check_intel_mac_dgpu()
            if has_dgpu:
                gpu_type, total_vram_gb = "intel_dgpu", dgpu_vram
    else:
        has_nv, nv_vram = check_nvidia_gpu()
        if has_nv:
            gpu_type, total_vram_gb = "nvidia", nv_vram
        else:
            has_amd, amd_vram = check_amd_gpu()
            if has_amd:
                gpu_type, total_vram_gb = "amd", amd_vram
            else:
                has_intel, intel_vram = check_intel_gpu()
                if has_intel:
                    gpu_type, total_vram_gb = "intel", intel_vram

    low_tier_ram_threshold = 8.0 if PLATFORM == "darwin" else 11.0

    if total_vram_gb >= 20.0:
        model = "qwen3-coder:30b"
    elif total_vram_gb >= 12.0:
        model = "qwen2.5-coder:14b"
    elif total_vram_gb >= 6.0:
        model = "qwen2.5-coder:7b"
    elif total_vram_gb >= 3.5 or ram_gb >= low_tier_ram_threshold:
        model = "qwen2.5-coder:3b"
    else:
        sys.exit(f"\n[X] Hardware Restriction: Insufficient resources ({total_vram_gb:.1f}G VRAM / {ram_gb:.1f}G RAM).")

    return model, gpu_type, total_vram_gb

def log_diagnostic(event: dict):
    """Appends one line to the LOCAL diagnostic log (this machine only -- see
    submit_diagnostic_to_server() for the subset that also goes to the operator). Best-effort: a
    failure to write a diagnostic line should never interrupt real crunching. Covers every
    retry/failure, not just the final outcome, so if the process dies mid-task (crash, OOM,
    thermal shutdown) the log still shows which chunk was in-flight when it happened."""
    event["timestamp"] = time.time()
    try:
        with open(DIAGNOSTICS_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception:
        pass

def submit_diagnostic_to_server(event: dict):
    """Sends a diagnostic event to the operator's server (POST /diagnostics), in addition to the
    always-local log_diagnostic() write above -- this is what lets the operator see every
    volunteer's stuck/cancelled chunks in one place instead of only ever seeing their own
    machine's local file. Deliberately called only for a task's terminal outcome (gave up after
    all retries, or cancelled mid-task), not every individual retry attempt, so a chunk that needs
    a couple of retries before succeeding doesn't spam the server. Best-effort and silent: a
    diagnostic never being allowed to interrupt or slow down real crunching applies just as much
    to network calls as to local disk writes -- if the server's unreachable, the event is simply
    lost server-side (it's still in the local log either way)."""
    try:
        make_request(f"{SERVER_URL}/diagnostics", event, timeout=10)
    except Exception:
        pass

def load_config() -> dict:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception: pass
    return {}

def save_config(config: dict):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)
    except Exception: pass

def load_saved_user() -> str:
    return load_config().get("user_id", "")

def save_user(user_id: str):
    # Loads-then-merges rather than overwriting the whole file -- this config also holds the
    # auto_update preference, and a plain overwrite here would silently wipe that out.
    config = load_config()
    config["user_id"] = user_id
    save_config(config)

def load_auto_update_preference():
    """True/False once configured; None means never asked yet (first boot)."""
    return load_config().get("auto_update", None)

def save_auto_update_preference(enabled: bool):
    config = load_config()
    config["auto_update"] = enabled
    save_config(config)

def load_benchmark_result() -> dict:
    """{} if never benchmarked (first boot) or the cached result no longer matches this
    machine's current hardware fingerprint (see save_benchmark_result)."""
    return load_config().get("benchmark_result", {})

def save_benchmark_result(result: dict):
    config = load_config()
    config["benchmark_result"] = result
    save_config(config)

# ============================================================
# OLLAMA SETUP -- unchanged from RAG_FOLDING.py.
# ============================================================

def fix_docker_permissions():
    try:
        if subprocess.run(["docker", "ps"], capture_output=True).returncode == 0: return
    except Exception: pass
    print(f"{Colors.YELLOW}[!] Docker Permission Gate Triggered: Account requires validation elevation.{Colors.RESET}")
    try:
        subprocess.run("sudo groupadd -f docker && sudo usermod -aG docker $USER", shell=True, check=True)
        os.execvp("sg", ["sg", "docker", "-c", f"{sys.executable} {' '.join(sys.argv)}"])
    except Exception: sys.exit("[X] Refused to elevate permissions. Execution halted.")

def install_docker():
    distro = get_linux_distro()
    try:
        if distro in ["ubuntu", "debian", "pop", "mint"]:
            subprocess.run("sudo apt-get update && sudo apt-get install -y docker.io", shell=True, capture_output=True, check=True)
        elif distro in ["fedora", "rhel", "centos"]:
            subprocess.run("sudo dnf install -y docker", shell=True, capture_output=True, check=True)
        elif distro in ["arch", "manjaro"]:
            subprocess.run("sudo pacman -S --noconfirm docker", shell=True, capture_output=True, check=True)
        else:
            subprocess.run("curl -fsSL https://get.docker.com | sh", shell=True, capture_output=True, check=True)
        subprocess.run("sudo systemctl enable --now docker", shell=True, capture_output=True, check=True)
    except KeyboardInterrupt:
        sys.exit(f"\n{Colors.CYAN}[X] Docker installation cancelled by user.{Colors.RESET}")
    except subprocess.CalledProcessError as e:
        if e.returncode in (130, -2):
            sys.exit(f"\n{Colors.CYAN}[X] Docker installation cancelled by user.{Colors.RESET}")
        sys.exit(f"{Colors.RED}[X] Docker installation failed: {e}{Colors.RESET}")
    except Exception as e:
        sys.exit(f"{Colors.RED}[X] Docker installation failed: {e}{Colors.RESET}")

def install_ollama_container(gpu_type: str):
    gpu_flags, image_name = "", "ollama/ollama"
    distro = get_linux_distro()

    if gpu_type == "nvidia":
        try:
            if distro in ["ubuntu", "debian", "pop"]:
                subprocess.run("curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg", shell=True, capture_output=True, check=True)
                subprocess.run(". /etc/os-release; curl -s -L https://nvidia.github.io/libnvidia-container/$ID$VERSION_ID/libnvidia-container.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list", shell=True, capture_output=True, check=True)
                subprocess.run("sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit", shell=True, capture_output=True, check=True)
            elif distro in ["arch", "manjaro"]:
                subprocess.run("sudo pacman -S --noconfirm nvidia-container-toolkit", shell=True, capture_output=True, check=True)
            elif distro in ["fedora"]:
                subprocess.run("sudo dnf config-manager --add-repo=https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo && sudo dnf install -y nvidia-container-toolkit", shell=True, capture_output=True, check=True)
            subprocess.run("sudo systemctl restart docker", shell=True, capture_output=True, check=True)
            gpu_flags = "--gpus all"
        except Exception: pass
    elif gpu_type == "amd":
        gpu_flags, image_name = "--device /dev/kfd --device /dev/dri", "ollama/ollama:rocm"
    elif gpu_type == "intel":
        gpu_flags = "--device /dev/dri"

    try:
        subprocess.run(f"sudo docker run -d {gpu_flags} -v ollama:/root/.ollama -p 11434:11434 --name ollama {image_name}", shell=True, capture_output=True, check=True)
    except KeyboardInterrupt:
        sys.exit(f"\n{Colors.CYAN}[X] Container deployment cancelled by user.{Colors.RESET}")
    except subprocess.CalledProcessError as e:
        if e.returncode in (130, -2):
            sys.exit(f"\n{Colors.CYAN}[X] Container deployment cancelled by user.{Colors.RESET}")
        sys.exit(f"{Colors.RED}[X] Failed to deploy container: {e}{Colors.RESET}")
    except Exception as e:
        sys.exit(f"{Colors.RED}[X] Failed to deploy container: {e}{Colors.RESET}")

def ensure_ollama_installed(gpu_type: str = None):
    if PLATFORM == "linux":
        has_docker = bool(shutil.which("docker"))
        if shutil.which("ollama") or (has_docker and "ollama" in subprocess.run(["docker", "ps", "-a", "--format", "{{.Names}}"], capture_output=True, text=True).stdout):
            return

        print(f"{Colors.CYAN}[~] Ollama framework absent. Initializing setup...{Colors.RESET}")
        if input("Would you like to run Ollama inside a Docker container? (y/n): ").strip().lower() == 'y':
            if not has_docker: install_docker()
            fix_docker_permissions()
            install_ollama_container(gpu_type)
        else:
            try:
                subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, capture_output=True, check=True)
            except KeyboardInterrupt:
                sys.exit(f"\n{Colors.CYAN}[X] Installation cancelled by user.{Colors.RESET}")
            except subprocess.CalledProcessError as e:
                if e.returncode in (130, -2):
                    sys.exit(f"\n{Colors.CYAN}[X] Installation cancelled by user.{Colors.RESET}")
                sys.exit(f"{Colors.RED}[X] Installation script failed: {e}{Colors.RESET}")
            except Exception as e:
                sys.exit(f"{Colors.RED}[X] Installation script failed: {e}{Colors.RESET}")
        return

    if shutil.which("ollama"):
        return

    print(f"{Colors.CYAN}[~] Ollama framework absent. Initializing setup...{Colors.RESET}")

    if PLATFORM == "darwin":
        if shutil.which("brew"):
            try:
                subprocess.run(["brew", "install", "ollama"], check=True)
                return
            except Exception as e:
                print(f"{Colors.YELLOW}[!] Homebrew installation failed: {e}{Colors.RESET}")
        sys.exit(
            f"{Colors.RED}[X] Could not install Ollama automatically.\n"
            "    Install Homebrew (https://brew.sh) and re-run this script, or install Ollama\n"
            f"    manually from https://ollama.com/download/mac, then re-run this script.{Colors.RESET}"
        )

    if PLATFORM == "win32":
        if shutil.which("winget"):
            try:
                subprocess.run(
                    ["winget", "install", "--id", "Ollama.Ollama", "-e", "--silent",
                     "--accept-package-agreements", "--accept-source-agreements"],
                    check=True, timeout=300
                )
                if shutil.which("ollama"):
                    return
            except Exception as e:
                print(f"{Colors.YELLOW}[!] winget installation failed: {e}{Colors.RESET}")

        print(f"\n{Colors.YELLOW}[!] Ollama is not installed or could not be located on your system.{Colors.RESET}")
        print(f"{Colors.CYAN}[~] Open your web browser and install Ollama for Windows from: https://ollama.com/download/windows{Colors.RESET}")
        input("[?] Once you have completed the installation, press [ENTER] to continue... ")

        if not shutil.which("ollama"):
            sys.exit("[X] Still could not locate 'ollama' in system PATH. Please restart this terminal and run the script again.")

def ensure_ollama_running_and_model_pulled(model_name):
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=3)
    except Exception:
        if PLATFORM == "linux":
            if shutil.which("ollama"):
                subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                fix_docker_permissions(); subprocess.run(["docker", "start", "ollama"], capture_output=True, check=True)
        elif PLATFORM == "win32":
            subprocess.Popen(
                ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
        else:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)

    if PLATFORM == "linux":
        is_dc = bool(shutil.which("docker") and not shutil.which("ollama"))
        if is_dc: fix_docker_permissions()
        cmd = ["docker", "exec", "-it", "ollama", "ollama", "pull", model_name] if is_dc else ["ollama", "pull", model_name]
    else:
        cmd = ["ollama", "pull", model_name]

    try:
        subprocess.run(cmd, capture_output=True, check=True)
    except KeyboardInterrupt:
        sys.exit(f"\n{Colors.CYAN}[X] Model download cancelled by user.{Colors.RESET}")
    except subprocess.CalledProcessError as e:
        # Ctrl+C during a long `ollama pull` almost always surfaces here, not as a
        # KeyboardInterrupt -- the child (docker exec / ollama) dies from SIGINT and reports exit
        # 130 (128 + SIGINT) or is killed outright (-2) before the interpreter's own signal check
        # runs, so subprocess.run() raises CalledProcessError instead. Without this check that
        # read as "[X] Model setup failed: ...returned non-zero exit status 130", which looks like
        # a real bug report for what was actually a deliberate cancel.
        if e.returncode in (130, -2):
            sys.exit(f"\n{Colors.CYAN}[X] Model download cancelled by user.{Colors.RESET}")
        sys.exit(f"{Colors.RED}[X] Model setup failed: {e}{Colors.RESET}")
    except Exception as e:
        sys.exit(f"{Colors.RED}[X] Model setup failed: {e}{Colors.RESET}")

def make_request(url, payload=None, timeout=180):
    data = json.dumps(payload).encode('utf-8') if payload else None
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'} if data else {})
    # Default 180s (not RAG_FOLDING's original 120s) -- finetune generation prompts run longer
    # than RAG extraction, and this function serves both the Cubyz server calls and the local
    # Ollama call. Callers doing a quick status poll (version/get_work/leaderboard) pass a much
    # shorter timeout explicitly -- a 180s default there meant a genuinely unreachable server (as
    # opposed to a fast "connection refused") could leave the client silently hung for up to 3
    # minutes with nothing on screen and no way out short of Ctrl+C.
    with urllib.request.urlopen(req, timeout=timeout) as res: return json.loads(res.read().decode('utf-8'))

# Bounded generously, but a lane that can't finish a trivial 40-token generation within this long
# isn't worth using at all -- treated the same as an outright failure, not just "slow."
BENCHMARK_TIMEOUT = 45.0

def benchmark_lane(model: str, force_cpu: bool):
    """Times a small, fixed-size real Ollama generation to measure actual throughput -- run once
    per machine (see main()'s use of load_benchmark_result()/save_benchmark_result()) to decide
    which of CPU/GPU actually performs better HERE, rather than guessing from declared hardware
    specs. VRAM detection in particular has repeatedly proven unreliable across GPU vendors and
    driver/tooling states (see check_amd_gpu()'s history in this file) -- and even when the VRAM
    number is accurate, a technically-present GPU can still be too weak, or too poorly supported
    by whatever backend Ollama uses for it, to actually be worth using at all. Measuring real
    throughput sidesteps needing to trust either signal.

    Returns elapsed seconds (lower is better), or None if the lane failed outright or didn't
    finish within BENCHMARK_TIMEOUT.
    """
    payload = {
        "model": model,
        "prompt": "Write a one-sentence description of what a stack data structure is.",
        "stream": False,
        "think": False,
        "options": {"num_predict": 40, **({"num_gpu": 0} if force_cpu else {})},
    }
    start = time.time()
    try:
        make_request(OLLAMA_URL, payload, timeout=BENCHMARK_TIMEOUT)
    except Exception:
        return None
    return time.time() - start

# ============================================================
# RAG MODE -- task processing (from pipeline_crunching/RAG_FOLDING.py)
# ============================================================

def format_chunk_descriptor(task: dict) -> str:
    # GITHUB_REVIEWS tasks don't have a real sequential chunk_index -- each review comment stands
    # alone with no natural position within the file it touches, so the source dataset reuses
    # chunk_index to carry the comment's own (huge, unique) numeric ID instead. Displayed as
    # "Chunk 3295308100" that looks like a bug rather than what it actually is. Issue-discussion
    # chunks (from extract_issues.py) reuse the same GITHUB_REVIEWS category with chunk_index set
    # to the actual issue number, so they get their own equally-readable case.
    match = re.match(r'github_pr_(\d+)_comment_\d+', task.get("chunk_id", ""))
    if match:
        return f"PR #{match.group(1)} review diff"
    match = re.match(r'github_issue_(\d+)_discussion', task.get("chunk_id", ""))
    if match:
        return f"Issue #{match.group(1)} discussion"
    return f"Chunk {task['chunk_index']}"

def format_current_task_line(task: dict) -> str:
    # raw_content for a GITHUB_REVIEWS task is a git diff plus its reviewer comment, pulled from a
    # real PR -- relative_path only names the diff's target file, it is NOT that file's own source
    # being processed. A filename-first line reads exactly like "processing this file's code",
    # which is wrong, so lead with the diff/PR framing instead to make the distinction obvious.
    # Issue-discussion chunks have no target file at all (relative_path is a synthetic
    # issues/issue_N.md path), so they get their own framing rather than the misleading
    # "touching issues/issue_N.md" phrasing that would otherwise result.
    match = re.match(r'github_pr_(\d+)_comment_\d+', task.get("chunk_id", ""))
    if match:
        return f"GitHub PR #{match.group(1)} review diff, touching {task['relative_path']} ({task['lines']} lines)"
    match = re.match(r'github_issue_(\d+)_discussion', task.get("chunk_id", ""))
    if match:
        return f"GitHub Issue #{match.group(1)} discussion ({task['lines']} lines)"
    return f"{task['relative_path']} ({format_chunk_descriptor(task)} • {task['lines']} lines)"

def format_finetune_task_line(task: dict) -> str:
    record = task.get("record") or {}
    title = record.get("title")
    label = f'"{title}"' if title else task.get("chunk_id", "?")
    return f"[{task.get('source_type', '?')}] {label}"

def _find_anchor_index(line: str, raw_content: str):
    line = line.strip()
    if not line:
        return None
    tokens = line.split()
    if not tokens:
        return None
    pattern = r'\s+'.join(re.escape(t) for t in tokens)
    match = re.search(pattern, raw_content)
    return match.start() if match else None

def _skip_balanced(raw_content: str, open_pos: int, open_char: str, close_char: str):
    depth = 0
    i = open_pos
    while i < len(raw_content):
        if raw_content[i] == open_char:
            depth += 1
        elif raw_content[i] == close_char:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None

def _find_declaration_body_brace(raw_content: str, decl_start: int):
    paren_pos = raw_content.find('(', decl_start)
    brace_pos = raw_content.find('{', decl_start)
    if paren_pos != -1 and (brace_pos == -1 or paren_pos < brace_pos):
        after_params = _skip_balanced(raw_content, paren_pos, '(', ')')
        if after_params is None:
            return None
        tail = raw_content[after_params:]
        error_set = re.match(r'[^{;]*?error\s*\{[^{}]*\}', tail)
        search_from = after_params + error_set.end() if error_set else after_params
        return raw_content.find('{', search_from)
    return brace_pos if brace_pos != -1 else None

def repair_code_example(candidate_code, raw_content):
    if not isinstance(candidate_code, str) or not candidate_code.strip():
        return None

    lines = [l for l in candidate_code.splitlines() if l.strip()]
    if not lines:
        return None
    first_line = lines[0]

    anchor_idx = _find_anchor_index(first_line, raw_content)

    if anchor_idx is None:
        name_match = re.search(r'\b(?:fn|struct|enum|union)\s+(\w+)', first_line)
        if name_match:
            name = name_match.group(1)
            decl_match = re.search(rf'\b(?:pub\s+)?(?:fn|const)\s+{re.escape(name)}\b', raw_content)
            if decl_match:
                anchor_idx = decl_match.start()

    if anchor_idx is None:
        return None

    brace_start = _find_declaration_body_brace(raw_content, anchor_idx)
    if brace_start is None or brace_start == -1:
        return None

    # If the model's anchor text isn't actually a declaration signature (e.g. it picked a bare
    # statement instead of a function/struct/enum), the brace found above could belong to a
    # completely unrelated, later block. A genuine signature never contains a statement
    # terminator before its own opening brace, so treat one as a sign this anchor can't be
    # repaired this way -- find_shortest_declaration() is the fallback for that case instead.
    if ';' in raw_content[anchor_idx:brace_start]:
        return None

    depth = 0
    for i in range(brace_start, len(raw_content)):
        if raw_content[i] == '{':
            depth += 1
        elif raw_content[i] == '}':
            depth -= 1
            if depth == 0:
                return raw_content[anchor_idx:i + 1]
    return None

def find_shortest_declaration(raw_content: str):
    # Mirrors the prompt's own "shortest complete function/struct/enum/union, fewest lines wins"
    # procedure, but run deterministically in code as a fallback for when the model's own
    # code_example wasn't declaration-shaped at all (e.g. it picked a bare local-variable
    # statement) and so can't be anchored/repaired from. Correctly returns None -- not a wrong
    # guess -- when no declaration in this specific chunk has a complete body within it (e.g. a
    # long function whose body is cut off by the chunk boundary).
    candidates = []
    pattern = r'\b(?:pub\s+)?(?:fn\s+\w+\s*\(|(?:const|var)\s+\w+\s*(?::[^=;{}]*)?=\s*(?:struct|enum|union)\b)'
    for match in re.finditer(pattern, raw_content):
        brace_start = _find_declaration_body_brace(raw_content, match.start())
        if brace_start is None or brace_start == -1:
            continue
        depth = 0
        end = None
        for i in range(brace_start, len(raw_content)):
            if raw_content[i] == '{':
                depth += 1
            elif raw_content[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is not None:
            candidates.append(raw_content[match.start():end])
    if not candidates:
        return None
    return min(candidates, key=lambda c: c.count('\n'))

def sanitize_extraction(data: dict, raw_content: str, p_key: str = "CODEBASE") -> dict:
    code_example = data.get("code_example")
    if isinstance(code_example, str) and code_example.strip():
        normalized_raw = re.sub(r'\s+', ' ', raw_content)
        normalized_example = re.sub(r'\s+', ' ', code_example)
        has_ellipsis = "..." in code_example or "…" in code_example
        is_verbatim = normalized_example in normalized_raw
        looks_like_declaration = bool(re.search(r'\b(fn|struct|enum|union)\b', code_example))
        balanced_braces = code_example.count('{') == code_example.count('}')

        needs_repair = has_ellipsis or not is_verbatim
        if p_key == "CODEBASE":
            needs_repair = needs_repair or not looks_like_declaration or not balanced_braces

        if needs_repair:
            repaired = repair_code_example(code_example, raw_content)
            if repaired is None and p_key == "CODEBASE":
                repaired = find_shortest_declaration(raw_content)
            data["code_example"] = repaired

    if isinstance(data.get("symbols"), list):
        private_imports = set(re.findall(r'(?m)^[ \t]*const\s+(\w+)\s*=\s*@import\(', raw_content))
        data["symbols"] = [s for s in data["symbols"] if s not in private_imports]

        public_reexports = re.findall(r'(?m)^[ \t]*pub\s+const\s+(\w+)\s*=\s*@import\(', raw_content)
        for name in public_reexports:
            if name not in data["symbols"]:
                data["symbols"].append(name)

    for list_field in ("symbols", "concepts", "keywords", "synthetic_queries"):
        if isinstance(data.get(list_field), list):
            data[list_field] = list(dict.fromkeys(data[list_field]))

    if len(raw_content) < 400 and isinstance(data.get("synthetic_queries"), list):
        data["synthetic_queries"] = data["synthetic_queries"][:6]

    return data

def validate_extraction(data: dict, raw_content: str, p_key: str) -> tuple:

    code_example = data.get("code_example")
    if isinstance(code_example, str) and code_example.strip():
        normalized_raw = re.sub(r'\s+', ' ', raw_content)
        normalized_example = re.sub(r'\s+', ' ', code_example)
        if normalized_example not in normalized_raw:
            return False, "code_example is not a verbatim substring of raw_content"
        if p_key == "CODEBASE":
            if not re.search(r'\b(fn|struct|enum|union)\b', code_example):
                return False, "code_example doesn't look like a function/struct/enum body"
            if code_example.count('{') != code_example.count('}'):
                return False, "code_example has unbalanced braces (likely an incomplete snippet)"

    symbols = data.get("symbols")
    if isinstance(symbols, list) and symbols and p_key == "CODEBASE":
        symbol_set = set(symbols)
        # "." shows up in plenty of non-qualification text too (version numbers like "OpenGL
        # 4.3", decimals, etc.) -- a real Zig Parent.child reference is always a single
        # contiguous identifier with no spaces, so require that to avoid false positives. Also
        # require every dot-separated segment to actually look like a Zig identifier (starts with
        # a letter/underscore, no leading digit or "@" -- "@" is reserved for real builtins like
        # @import, never a user identifier). Without this, something like "@lod0.5Distance" --
        # the model mashing together a value ("lod0"), a number ("0.5"), and a field name
        # ("Distance") into one garbled string -- gets treated as a genuine qualified reference
        # and then rejected as an unfounded "call-chain," when it was never a real symbol at all.
        qualified = [
            s for s in symbols
            if "." in s and " " not in s
            and all(re.match(r'^[A-Za-z_]\w*$', part) for part in s.split("."))
        ]
        if qualified:
            # A qualified symbol's root being absent from the model's own reported symbol list
            # doesn't mean it's fabricated -- orchestration/entry-point code (main.zig's entry
            # point, in particular) is naturally full of calls into imported modules
            # (heap.allocators.deinit, std.log.err) whose root is an import alias the chunk
            # uses, not something the chunk itself declares. Requiring "the root is ALSO in
            # symbol_set" made every genuinely call-heavy chunk fail every single attempt
            # forever (confirmed live: codebase_src_main.zig_chunk_3 hit this 191 times across
            # the diagnostic log before ever being traced to this check). What actually matters
            # is grounding -- does the root token appear anywhere in the chunk's real source at
            # all? A genuinely fabricated dotted reference wouldn't.
            orphaned = [
                s for s in qualified
                if s.split(".")[0] not in symbol_set
                and not re.search(r'\b' + re.escape(s.split(".")[0]) + r'\b', raw_content)
            ]
            if len(orphaned) / len(qualified) > 0.5:
                return False, f"most qualified symbols look like call-chains, not declarations (e.g. {orphaned[0]!r})"

    text_fields = " ".join([
        data.get("summary", "") or "",
        data.get("comprehensive_explanation", "") or "",
        " ".join(data.get("synthetic_queries", []) or []),
    ])
    for name in set(re.findall(r'`([A-Za-z_][A-Za-z0-9_]*)`', text_fields)):
        if not re.search(r'\b' + re.escape(name) + r'\b', raw_content):
            return False, f"'{name}' is quoted as an identifier but doesn't appear in raw_content"

    if not data.get("summary") or not data.get("comprehensive_explanation"):
        return False, "summary or comprehensive_explanation is empty"

    return True, ""

def generate_rag_analysis(task: dict, chosen_model: str, max_threads, status_cb, force_cpu: bool = False) -> tuple:
    raw_content = task.get("raw_content", "")
    ctx_upper = task.get("directory_context", "").upper()
    if "DEFINITIVE_WIKI_DOCUMENTATION" in ctx_upper or "WIKI" in ctx_upper:
        p_key, temp = "WIKI", 0.30
    elif "GITHUB_REVIEWS" in ctx_upper or "REVIEW" in ctx_upper:
        p_key, temp = "GITHUB_REVIEWS", 0.20
    elif "ADDON_STUDIO" in ctx_upper or "ADDON" in ctx_upper:
        p_key, temp = "ADDON_STUDIO", 0.20
    else:
        p_key, temp = "CODEBASE", 0.15

    payload = {
        "model": chosen_model,
        "prompt": f"Context Source File: {task['file_name']}\nRelative Path: {task['relative_path']}\nDirectory Module context: {task['directory_context']}\nChunk Index: {task['chunk_index']}\nRaw Content:\n```\n{raw_content}\n```\n",
        "system": RAG_PROMPTS[p_key] + (LOW_VRAM_REASONING_RULE if chosen_model in ["qwen2.5-coder:3b"] else ""),
        "think": False,
        "stream": False, "format": RAG_JSON_SCHEMA, "options": {
            "temperature": temp,
            **({"num_thread": max_threads} if max_threads else {}),
            # num_gpu=0 tells Ollama to keep every layer on the CPU for this request specifically,
            # regardless of what a concurrent GPU-backed request from the other lane is doing --
            # this is what lets one machine run a GPU lane and a CPU lane against the same Ollama
            # server at once (see run_dual_lane_if_capable()) without them fighting over VRAM.
            **({"num_gpu": 0} if force_cpu else {}),
        }
    }

    # Diagnostic logging here is deliberately scoped to retries/failures only -- a chunk that
    # succeeds on attempt 1 (the normal case) logs nothing at all. The point is "why did this
    # chunk need to be redone," not a full audit trail of routine work.
    #
    # `extra` carries whatever's actually available at each failure point -- the raw unparsed
    # model output on a JSON parse error, or the parsed-but-rejected candidate dict on a
    # self-check failure -- so a later investigation doesn't have to re-simulate the exact
    # request just to see what the model actually produced (this gap is exactly what made
    # diagnosing the "code_example doesn't look like a function/struct/enum body" failures slow
    # to trace live). Capped in size since some raw model output can be large.
    def _log_retry(attempt_num, reason, extra=None):
        event = {
            "event": "task_retry", "mode": "rag", "chunk_id": task.get("chunk_id"),
            "attempt": attempt_num + 1, "reason": reason,
        }
        if extra:
            event.update({k: (v[:2000] if isinstance(v, str) else v) for k, v in extra.items()})
        log_diagnostic(event)

    parsed_data = None
    last_failure_reason = "no attempts made"
    for attempt in range(3):
        if attempt > 0:
            time.sleep(5)

        payload["options"]["temperature"] = temp + (attempt * 0.15)

        try:
            res = make_request(OLLAMA_URL, payload)
            json_string = res.get("response", "").strip()
        except Exception as e:
            last_failure_reason = f"{type(e).__name__}: {e}"
            status_cb(f"⚠ Attempt {attempt+1} failed: {last_failure_reason}")
            _log_retry(attempt, last_failure_reason)
            continue

        if not json_string:
            last_failure_reason = "Ollama returned HTTP 200 with an empty 'response' field"
            status_cb(f"⚠ Attempt {attempt+1}: model returned empty output. Retrying...")
            _log_retry(attempt, last_failure_reason)
            continue

        if json_string.startswith("```"):
            lines = json_string.splitlines()
            if lines and lines[0].startswith("```"): lines = lines[1:]
            if lines and lines[-1].startswith("```"): lines = lines[:-1]
            json_string = "\n".join(lines).strip()
        try:
            candidate = json.loads(json_string[json_string.find("{"):json_string.rfind("}")+1] if "{" in json_string else json_string)
        except Exception as e:
            last_failure_reason = f"JSON parse error: {e}"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
            _log_retry(attempt, last_failure_reason, {"raw_response": json_string})
            continue

        candidate = sanitize_extraction(candidate, raw_content, p_key)

        is_valid, validation_reason = validate_extraction(candidate, raw_content, p_key)
        if is_valid:
            parsed_data = candidate
            break
        last_failure_reason = f"Self-check failed: {validation_reason}"
        status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
        _log_retry(attempt, last_failure_reason, {"candidate": candidate})

    if parsed_data is None:
        gave_up_event = {
            "event": "task_gave_up", "mode": "rag", "chunk_id": task.get("chunk_id"),
            "final_reason": last_failure_reason,
        }
        log_diagnostic(gave_up_event)
        submit_diagnostic_to_server(gave_up_event)

    return parsed_data, last_failure_reason

# ============================================================
# FINETUNE MODE -- task processing (from finetune/scripts/FINETUNE_FOLDING.py)
# ============================================================

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
    symbols_text = " ".join(record.get("symbols") or [])
    return f"{record.get('summary', '')} {record.get('comprehensive_explanation', '')} {record.get('code_example') or ''} {symbols_text}"

def validate_pairs(pairs, grounding_text: str) -> tuple:
    if not isinstance(pairs, list):
        return False, "pairs is not a list"
    for pair in pairs:
        if not isinstance(pair, dict) or "instruction" not in pair or "response" not in pair:
            return False, "malformed pair"
        for name in set(re.findall(r'`([A-Za-z_][A-Za-z0-9_]*)`', pair["response"])):
            if not re.search(r'\b' + re.escape(name) + r'\b', grounding_text):
                return False, f"'{name}' quoted in response but not found in source grounding text"
    return True, ""

def generate_finetune_pairs(task: dict, chosen_model: str, status_cb, force_cpu: bool = False) -> tuple:
    source_type = task["source_type"]
    prompt_text = FINETUNE_RESTYLE_PROMPT if source_type in ("docs", "codebase") else FINETUNE_REVIEWS_PROMPT
    payload = {
        "model": chosen_model,
        "prompt": build_prompt_input(task),
        "system": prompt_text,
        "think": False,
        "stream": False,
        "format": FINETUNE_SCHEMA,
        "options": {"temperature": 0.3, **({"num_gpu": 0} if force_cpu else {})},
    }

    # Same scoping as generate_rag_analysis's _log_retry -- only retries/failures get logged, a
    # clean first-attempt success logs nothing. `extra` captures whatever's actually available at
    # each failure point (see generate_rag_analysis's _log_retry for the full reasoning).
    def _log_retry(attempt_num, reason, extra=None):
        event = {
            "event": "task_retry", "mode": "finetune", "chunk_id": task.get("chunk_id"),
            "attempt": attempt_num + 1, "reason": reason,
        }
        if extra:
            event.update({k: (v[:2000] if isinstance(v, str) else v) for k, v in extra.items()})
        log_diagnostic(event)

    grounding_text = grounding_text_for(task)
    parsed = None
    last_failure = "no attempts made"
    for attempt in range(3):
        if attempt > 0:
            time.sleep(3)
        try:
            res = make_request(OLLAMA_URL, payload)
            raw = res.get("response", "").strip()
        except Exception as e:
            last_failure = f"{type(e).__name__}: {e}"
            status_cb(f"⚠ Attempt {attempt+1} failed: {last_failure}")
            _log_retry(attempt, last_failure)
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
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure}. Retrying...")
            _log_retry(attempt, last_failure, {"raw_response": raw})
            continue

        ok, reason = validate_pairs(candidate.get("pairs", []), grounding_text)
        if ok:
            parsed = candidate
            break
        last_failure = f"Self-check failed: {reason}"
        status_cb(f"⚠ Attempt {attempt+1}: {last_failure}. Retrying...")
        _log_retry(attempt, last_failure, {"candidate": candidate})

    if parsed is None:
        gave_up_event = {
            "event": "task_gave_up", "mode": "finetune", "chunk_id": task.get("chunk_id"),
            "final_reason": last_failure,
        }
        log_diagnostic(gave_up_event)
        submit_diagnostic_to_server(gave_up_event)

    return parsed, last_failure

# ============================================================
# SHARED: leaderboard / roster / interrupt menu (from RAG_FOLDING.py, made defensive about
# field-name differences between the current RAG and finetune servers' /leaderboard responses --
# see the protocol note near the top of this file).
# ============================================================

def format_count(n) -> str:
    """1234 -> '1.2k', 1500000 -> '1.5M' -- keeps chunk/line counts readable once a campaign or a
    single user's lifetime total crosses four digits, instead of a wall of undifferentiated digits."""
    n = float(n)
    tiers = [(1_000_000_000, "B"), (1_000_000, "M"), (1_000, "k")]
    for idx, (div, suffix) in enumerate(tiers):
        if abs(n) >= div:
            value = n / div
            if round(value, 1) >= 1000 and idx > 0:
                # e.g. 999950 rounds to "1000.0k" at this tier -- bump to the next one up instead.
                bigger_div, bigger_suffix = tiers[idx - 1]
                return f"{n / bigger_div:.1f}{bigger_suffix}"
            return f"{value:.1f}{suffix}"
    return str(int(n))

def format_eta(seconds) -> str:
    """None/negative -> 'calculating...' (not enough recent completions yet for the server to
    trust a rate); otherwise the largest two units that matter, e.g. '2h 14m' or '38m'."""
    if seconds is None or seconds < 0:
        return "calculating..."
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    days, rem = divmod(seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, _ = divmod(rem, 60)
    if days:
        return f"{days}d {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"

def generate_local_leaderboard_html(stats: dict):
    """Generates a styled, read-only HTML file next to the client script."""
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leaderboard.html")

    total = stats.get("total_chunks_in_codebase") or stats.get("total_chunks_in_campaign") or 1
    completed = stats.get("total_chunks_completed", 0)
    global_pct = stats.get("global_percentage", 0.0)

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Cubyz Folding Leaderboard</title>
    <meta http-equiv="refresh" content="30"> <!-- Auto refreshes every 30 seconds -->
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #121214; color: #e1e1e6; margin: 40px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: #1a1a1e; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        h1 {{ color: #50fa7b; border-bottom: 2px solid #2a2a30; padding-bottom: 10px; margin-top: 0; }}
        .progress-bar {{ background: #2a2a30; border-radius: 8px; height: 24px; width: 100%; overflow: hidden; margin: 20px 0; position: relative; }}
        .progress-fill {{ background: #50fa7b; height: 100%; width: {global_pct}%; transition: width 0.5s ease; }}
        .progress-text {{ position: absolute; width: 100%; text-align: center; top: 2px; font-weight: bold; color: #000; font-size: 14px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #2a2a30; }}
        th {{ background: #202024; color: #ff79c6; }}
        tr:hover {{ background: #202024; }}
        .rank {{ font-weight: bold; color: #8be9fd; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Cubyz Distributed Folding Leaderboard</h1>
        <p><strong>Global Base Progress:</strong> {completed} / {total} Chunks Analyzed ({global_pct}%)</p>
        <div class="progress-bar">
            <div class="progress-fill"></div>
            <div class="progress-text">{global_pct}%</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>User ID</th>
                    <th>Chunks</th>
                    <th>Lines Crunched</th>
                    <th>Share</th>
                </tr>
            </thead>
            <tbody>
    """

    for user in stats.get("rankings", []):
        lines_crunched = user.get("lines_crunched", user.get("pairs_generated", 0))
        share = user.get("contribution_percentage", "")
        html_content += f"""
                <tr>
                    <td class="rank">#{user.get('rank', '?')}</td>
                    <td>{user.get('user_id', '?')}</td>
                    <td>{user.get('chunks_completed', 0)}</td>
                    <td>{lines_crunched}</td>
                    <td>{share}%</td>
                </tr>"""

    html_content += """
            </tbody>
        </table>
    </div>
</body>
</html>
"""
    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
    except Exception:
        pass

def fetch_and_show_leaderboard():
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard", timeout=10)
    except Exception as e:
        print(f"{Colors.RED}[X] Could not sync ledger metrics: {e}{Colors.RESET}")
        return

    generate_local_leaderboard_html(stats)

    tot = stats.get("total_chunks_in_codebase") or stats.get("total_chunks_in_campaign") or 1
    comp = stats.get("total_chunks_completed", 0)
    pct = stats.get("global_percentage", 0.0)
    bar_len = 20
    # Clamped -- comp can legitimately exceed tot (e.g. cumulative lifetime user stats vs. a
    # freshly-requeued, smaller current campaign), and an unclamped fill_len there turns into a
    # multi-thousand-character bar that floods the terminal instead of just looking "full."
    fill_len = max(0, min(bar_len, int(round(bar_len * comp / float(tot))))) if tot else 0
    p_bar = '█' * fill_len + '░' * (bar_len - fill_len)

    print(f"{Colors.YELLOW}─── [ CUBYZ DISTRIBUTED LEADERBOARD ] ──────────────────────────────────{Colors.RESET}")
    print(f"  Global Progress: [{Colors.GREEN}{p_bar}{Colors.RESET}] {format_count(comp)}/{format_count(tot)} ({pct:.2f}%)")
    print(f"  Est. Time Left : {format_eta(stats.get('eta_seconds'))} (from combined speed of all active nodes)")
    rankings = stats.get("rankings", [])
    if not rankings:
        print(f"  {'Rankings':<13}: No contributions recorded yet.")
    for u in rankings:
        rank = u.get('rank', '?')
        label = f"Rank #{rank}"
        # Gold for #1, everything else plain -- keeps the highlight meaningful instead of every
        # row competing for attention.
        row_color = f"{Colors.YELLOW}{Colors.BOLD}" if rank == 1 else ""
        row_reset = Colors.RESET if rank == 1 else ""
        lines_crunched = u.get("lines_crunched", u.get("pairs_generated", 0))
        share = u.get("contribution_percentage")
        share_text = f" • {share:.1f}% share" if isinstance(share, (int, float)) else ""
        print(f"  {row_color}{label:<13}: {u.get('user_id','?')} • {format_count(u.get('chunks_completed',0))} chunks • {format_count(lines_crunched)} lines{share_text}{row_reset}")
    print(f"  {'Local View':<13}: also written to leaderboard.html next to this script")
    print(f"{Colors.YELLOW}────────────────────────────────────────────────────────────────────────{Colors.RESET}")

def fetch_and_show_userlist():
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard", timeout=10)
    except Exception as e:
        print(f"{Colors.RED}[X] Could not sync node roster: {e}{Colors.RESET}")
        return

    users = stats.get("rankings", [])
    online = [u for u in users if "ONLINE" in u.get("status", "")]
    offline = [u for u in users if "ONLINE" not in u.get("status", "")]

    print(f"{Colors.CYAN}─── [ CUBYZ ACTIVE NODE ROSTER ] ────────────────────────────────────────{Colors.RESET}")
    print(f"  Node Summary : {Colors.GREEN}{len(online)} online{Colors.RESET} • {Colors.GRAY}{len(offline)} offline{Colors.RESET} • {len(users)} known nodes total")
    if not users:
        print(f"  {'Nodes':<13}: No nodes have connected yet.")
    for u in online + offline:
        is_online = "ONLINE" in u.get("status", "")
        status_color = Colors.GREEN if is_online else Colors.GRAY
        label = u.get("status", "?")
        lines_crunched = u.get("lines_crunched", u.get("pairs_generated", 0))
        print(f"  {status_color}{label:<13}{Colors.RESET}: {u.get('user_id','?')} • {format_count(u.get('chunks_completed',0))} chunks • {format_count(lines_crunched)} lines")
    print(f"{Colors.CYAN}────────────────────────────────────────────────────────────────────────{Colors.RESET}")

def handle_interrupt_menu(dual_controller: "DualLaneController | None" = None):
    print(f"\n\n{Colors.YELLOW}{Colors.BOLD}[||] Node Execution Paused via User Action.{Colors.RESET}")
    while True:
        auto_status_color = Colors.GREEN if load_auto_update_preference() else Colors.GRAY
        auto_status = f"{auto_status_color}{'ON' if load_auto_update_preference() else 'OFF'}{Colors.RESET}"
        # dual_controller only exists at all on a machine that was actually dual-capable at
        # startup (see main()) -- its mere presence is what gates this option ever showing up in
        # the prompt, so a non-capable machine's menu looks completely unchanged.
        dual_option = ""
        if dual_controller is not None:
            dual_status_color = Colors.GREEN if dual_controller.active else Colors.GRAY
            dual_status = f"{dual_status_color}{'ON' if dual_controller.active else 'OFF'}{Colors.RESET}"
            dual_option = f", [D] to toggle the secondary CPU lane (currently {dual_status})"
        choice = input(f"Enter [R] to resume, [L] to view the leaderboard, [U] to view active users, [A] to toggle auto-update (currently {auto_status}){dual_option}, or [Q] to safely exit: ").strip().lower()
        if choice == 'r': return
        elif choice == 'l': fetch_and_show_leaderboard()
        elif choice == 'u': fetch_and_show_userlist()
        elif choice == 'a':
            new_value = not load_auto_update_preference()
            save_auto_update_preference(new_value)
            state_color = Colors.GREEN if new_value else Colors.GRAY
            print(f"{state_color}[✓] Auto-update is now {'ENABLED' if new_value else 'DISABLED'}.{Colors.RESET}")
        elif choice == 'd' and dual_controller is not None:
            if dual_controller.active:
                dual_controller.stop()
                print(f"{Colors.GRAY}[✓] Secondary CPU lane DISABLED -- back to a single GPU lane.{Colors.RESET}")
            else:
                dual_controller.start()
                print(f"{Colors.GREEN}[✓] Secondary CPU lane ENABLED -- crunching with GPU + CPU lanes again.{Colors.RESET}")
        elif choice == 'q': sys.exit(f"{Colors.CYAN}[X] Disconnecting safely. Thank you for your computational contributions!{Colors.RESET}")

def interruptible_sleep(seconds, dual_controller: "DualLaneController | None" = None):
    """time.sleep() wrapped for the retry/cooldown waits inside the main loop's except blocks.
    A Ctrl+C during a plain time.sleep() there escapes uncaught -- it's a new KeyboardInterrupt
    raised while already handling another exception, so the loop's own `except KeyboardInterrupt`
    (which only guards the `try`) never sees it and the process dies instead of opening the pause
    menu."""
    try:
        time.sleep(seconds)
    except KeyboardInterrupt:
        handle_interrupt_menu(dual_controller)

# ============================================================
# MAIN
# ============================================================

MODE_BANNERS = {
    "rag": f"{Colors.CYAN}{Colors.BOLD}★ RAG MODE ACTIVATED -- receiving knowledge-extraction tasks{Colors.RESET}",
    "finetune": f"{Colors.MAGENTA}{Colors.BOLD}★ FINETUNE MODE ACTIVATED -- receiving training-pair generation tasks{Colors.RESET}",
}

# Minimum spare system RAM (beyond what the GPU lane's own host-side overhead needs) required
# before a second, CPU-only lane is worth running alongside the GPU lane. Matches the existing
# solo-CPU-node thresholds elsewhere in this file (8-11 GB) plus headroom, since this RAM has to
# cover a full qwen2.5-coder:3b run *while* the GPU lane's own process is also live.
DUAL_LANE_MIN_RAM_GB = 12.0

# Minimum GPU VRAM required before dual-lane is even offered -- not about system RAM at all, but
# whether the GPU itself has headroom to spare. Below this (matching the same 6.0 threshold the
# 7b model tier already uses elsewhere as "a GPU that can comfortably run its own model"), the
# GPU is already fully committed just running its OWN (lowest-tier, 3b) model; a second lane's
# concurrent request to the same Ollama server -- even one forced off-GPU via num_gpu=0 -- still
# has to share that server's scheduling, and confirmed live, on a 2-4 GB card this contention
# stalled BOTH lanes (the GPU lane stuck at "Generating analysis..." indefinitely, the CPU lane
# completing exactly one task and then nothing). Plenty of system RAM doesn't fix a GPU that's
# already maxed out on its own.
DUAL_LANE_MIN_VRAM_GB = 6.0

class DualStatusBoard:
    """One shared, redrawing status window covering BOTH lanes at once, used instead of each
    lane's own independent box in dual-lane mode. A single lane's box (print_terminal_status
    inside crunch_lane) assumes it's the only thing touching the terminal -- true for a solo
    lane, but with two lanes running, whichever one drew last would tear/stack over the other's
    box the moment the other lane printed anything in between (confirmed live). Routing both
    lanes' updates through this one object means there's only ever one piece of code doing
    cursor math, so it can always know exactly how many lines it drew last time.
    """

    def __init__(self, gpu_label: str, cpu_label: str):
        self.labels = {"GPU": gpu_label, "CPU": cpu_label}
        self.state = {
            "GPU": {"task": "(waiting for a task...)", "status": "Starting...", "speed": "calculating..."},
            "CPU": {"task": "(waiting for a task...)", "status": "Starting...", "speed": "calculating..."},
        }
        self.comp = 0
        self.tot = 0
        self.eta = None
        self.rendered_once = False
        self.last_line_count = 0
        self.last_announced_mode = None

    def should_announce_mode(self, mode: str) -> bool:
        """The campaign mode (rag/finetune/idle) is server-global, not per-lane -- both lanes'
        own `current_mode != mode` checks fire independently, typically within moments of each
        other at startup (both transitioning from their own initial None), which without this
        would print the "MODE ACTIVATED" banner twice and force two redundant full-box reprints
        in a row (confirmed live). Only the first lane to notice a given transition actually
        announces it; the other just updates its own current_mode silently."""
        with print_lock:
            if mode == self.last_announced_mode:
                return False
            self.last_announced_mode = mode
            return True

    def _status_color(self, step_msg: str) -> str:
        if step_msg.startswith("✓"):
            return Colors.GREEN
        if step_msg.startswith("⚠"):
            return Colors.YELLOW
        if step_msg.startswith("✗"):
            return Colors.RED
        return ""

    def _build_lines(self) -> list:
        pct = (self.comp / self.tot * 100) if self.tot else 0.0
        bar_len = 20
        fill_len = max(0, min(bar_len, int(round(bar_len * self.comp / float(self.tot))))) if self.tot else 0
        p_bar = '█' * fill_len + '░' * (bar_len - fill_len)

        lines = [f"{Colors.BOLD}─── [ DUAL-LANE CRUNCHING ] ─────────────────────────────────────────{Colors.RESET}"]
        for tag, color in (("GPU", Colors.CYAN), ("CPU", Colors.MAGENTA)):
            s = self.state[tag]
            lines.append(f" {color}{tag}{Colors.RESET} │ {self.labels[tag]}")
            lines.append(f"     │ Task  : {s['task']}")
            lines.append(f"     │ Status: {self._status_color(s['status'])}{s['status']}{Colors.RESET}")
            lines.append(f"     │ Speed : {s['speed']}")
            lines.append(f"{color}─────┴─────────────────────────────────────────────────────────────{Colors.RESET}")
        lines.append(f"  Global Progress: [{Colors.CYAN}{p_bar}{Colors.RESET}] {format_count(self.comp)}/{format_count(self.tot)} ({pct:.2f}%)")
        lines.append(f"  Est. Time Left : {format_eta(self.eta)}")
        lines.append(f"{Colors.BOLD}───────────────────────────────────────────────────────────────────────{Colors.RESET}")
        return lines

    def _render_locked(self):
        lines = self._build_lines()
        if self.rendered_once:
            sys.stdout.write("\033[F\033[K" * self.last_line_count)
        for line in lines:
            print(line)
        sys.stdout.flush()
        self.last_line_count = len(lines)
        self.rendered_once = True

    def update(self, lane_tag: str, task_desc: str, step_msg: str, comp: int, tot: int, eta, speed: str):
        with print_lock:
            self.state[lane_tag] = {"task": task_desc, "status": step_msg, "speed": speed}
            self.comp, self.tot, self.eta = comp, tot, eta
            self._render_locked()

    def note(self, msg: str):
        """A scrolling one-off line (mode changed, idle, an error) from either lane -- printed
        above the board, which then redraws fresh underneath on the next update() instead of
        trying to clear over top of what was just printed."""
        with print_lock:
            print(msg)
            self.rendered_once = False

class DualLaneController:
    """Lets a dual-capable machine's secondary CPU lane be started and stopped at runtime from
    the pause menu (see handle_interrupt_menu()'s "secret" [D] option, which only ever shows up
    at all when a DualLaneController exists -- i.e. the machine was dual-capable at startup),
    instead of the lane count being fixed for the whole process's life. The GPU/primary lane
    (running in the main thread) is given this controller directly and checks `.active` on every
    single status update to decide whether to report into the shared board or its own solo box;
    the CPU lane itself never receives it; it just gets stopped via `stop_event` and, if
    re-enabled later, a fresh thread with a fresh stop_event is spawned from scratch.
    """

    def __init__(self, board: "DualStatusBoard", cpu_lane_kwargs: dict):
        self.board = board
        self.cpu_lane_kwargs = cpu_lane_kwargs
        # One shared pause_event across the whole controller's life (not recreated per start()) --
        # it's how the primary lane's Ctrl+C handling tells a *currently running* CPU lane to stop
        # polling for new work while the interrupt menu is open, same as before this toggle
        # existed; start()/stop() themselves are a separate, independent on/off switch.
        self.pause_event = threading.Event()
        self.active = False
        self._thread = None
        self._stop_event = None

    def start(self):
        if self.active:
            return
        self._stop_event = threading.Event()
        kwargs = dict(self.cpu_lane_kwargs, board=self.board, pause_event=self.pause_event, stop_event=self._stop_event)
        self._thread = threading.Thread(target=_background_lane, kwargs=kwargs, daemon=True)
        self._thread.start()
        self.active = True
        # Whatever's currently on screen (the solo box, or nothing yet) isn't a stale copy of the
        # board -- the next render must print fresh rather than try to clear lines that aren't
        # actually there.
        self.board.rendered_once = False

    def stop(self):
        if not self.active:
            return
        self._stop_event.set()
        self.active = False
        # Same reasoning as start() -- the primary lane's next report() switches back to its own
        # solo box, which has no idea how many lines the board last drew.
        self.board.rendered_once = False

def crunch_lane(lane_tag: str, user_id: str, hardware_tier: str, chosen_model: str, max_threads,
                 cooldown: float, mode_desc: str, hardware_label: str, force_cpu: bool = False,
                 fancy_ui: bool = True, pause_event: "threading.Event | None" = None,
                 board: "DualStatusBoard | None" = None, stop_event: "threading.Event | None" = None,
                 dual_controller: "DualLaneController | None" = None):
    """Runs the poll -> crunch -> submit cycle forever for one lane. A "lane" is one independent
    identity polling /get_work and calling Ollama on its own -- there's normally just one (the
    whole client, as before dual-lane support existed), but a machine with both a real GPU and
    enough spare RAM (see run_dual_lane_if_capable()) runs two: this function unmodified in the
    main thread for the GPU lane (Ctrl+C/the interrupt menu behave exactly as they always have),
    and a second call in a background thread for the CPU lane (force_cpu=True routes that lane's
    Ollama calls through num_gpu=0 so it never competes with the GPU lane for VRAM).

    fancy_ui (this lane's own independent redrawing box) is only ever used for a genuinely solo
    lane. In dual-lane mode both lanes instead report into a single shared `board`
    (DualStatusBoard) -- one lane's own box assumes it's the only thing touching the terminal,
    which a second lane drawing its own box (or even just printing plain lines) would break no
    matter how the printing itself is locked, since a lock only stops characters from
    interleaving, not the cursor math from landing in the wrong place. `board` is None for solo
    runs, in which case fancy_ui's own box is used exactly as before dual-lane support existed.

    pause_event coordinates the two lanes without needing the background thread to handle Ctrl+C
    itself (Python only ever delivers SIGINT/KeyboardInterrupt to the main thread, so a background
    lane can't catch it directly regardless). The lane running in the main thread sets it right
    before opening the interrupt menu and clears it on resume; both lanes check it at the top of
    every cycle and idle without polling for new work while it's set. Solo (non-dual) runs never
    pass an event here at all, so this is a no-op and behavior is identical to before dual-lane
    support existed.

    stop_event, when set, makes this call return (ending the thread it's running in) at the top
    of the next cycle -- only ever given to a CPU lane spawned by DualLaneController, letting the
    pause menu's "toggle dual-lane" option actually stop and later restart it, rather than the
    lane count being fixed for the whole process lifetime.

    dual_controller is only ever given to the GPU/primary lane (the one running in the main
    thread) -- it's how that lane finds out, on every single report()/banner() call, whether
    dual-lane is *currently* active (which can change at runtime via the pause menu) and which
    board to report into if so. Solo lanes and the CPU lane itself never receive it.
    """

    def safe_print(msg):
        with print_lock:
            print(msg)

    def current_board():
        if dual_controller is not None and dual_controller.active:
            return dual_controller.board
        return board

    # Rolling window of this lane's own last few *successful* task times (dispatch -> confirmed
    # submitted) -- retried/abandoned attempts don't count, they'd skew this toward "how slow is
    # a bad chunk" instead of "how fast is this lane" (what the number's actually for).
    task_durations = []
    MAX_DURATION_SAMPLES = 10

    def record_duration(seconds):
        task_durations.append(seconds)
        del task_durations[:-MAX_DURATION_SAMPLES]

    def speed_str():
        if not task_durations:
            return "calculating..."
        avg = sum(task_durations) / len(task_durations)
        return f"{avg:.1f}s/chunk avg (last {len(task_durations)})"

    def print_terminal_status(task_desc, step_msg, is_first, comp, tot, eta=None):
        pct = (comp / tot * 100) if tot else 0.0
        bar_len = 20
        fill_len = max(0, min(bar_len, int(round(bar_len * comp / float(tot))))) if tot else 0
        p_bar = '█' * fill_len + '░' * (bar_len - fill_len)

        box_color = mode_color(current_mode)
        if step_msg.startswith("✓"):
            status_color = Colors.GREEN
        elif step_msg.startswith("⚠"):
            status_color = Colors.YELLOW
        elif step_msg.startswith("✗"):
            status_color = Colors.RED
        else:
            status_color = ""

        with print_lock:
            if not is_first:
                sys.stdout.write("\033[F\033[K" * 8)
            print(f"{box_color}─── [ {hardware_label} ] ──────────────────────────────────────────{Colors.RESET}")
            print(f"  Current Task : {task_desc}")
            print(f"  Configuration: Model: {chosen_model} • Profile: {mode_desc.split(' (')[0]}")
            print(f"  Node Status  : {status_color}{step_msg}{Colors.RESET}")
            print(f"  Lane Speed   : {speed_str()}")
            print(f"  Global Progress: [{box_color}{p_bar}{Colors.RESET}] {format_count(comp)}/{format_count(tot)} ({pct:.2f}%)")
            print(f"  Est. Time Left : {format_eta(eta)}")
            print(f"{box_color}────────────────────────────────────────────────────────────────────────{Colors.RESET}")
            sys.stdout.flush()

    def report(task_desc, step_msg, is_first, comp, tot, eta):
        b = current_board()
        if b is not None:
            b.update(lane_tag, task_desc, step_msg, comp, tot, eta, speed_str())
        elif fancy_ui:
            print_terminal_status(task_desc, step_msg, is_first, comp, tot, eta)
        else:
            suffix = f" ({speed_str()})" if step_msg.startswith("✓") else ""
            safe_print(f"{Colors.GRAY}[{lane_tag}]{Colors.RESET} {task_desc}: {step_msg}{suffix}")

    def banner(msg):
        """A one-off scrolling line (mode changed, idle, an error) rather than an ongoing task
        status -- goes through the shared board's note() in dual-lane mode so it scrolls above
        the board instead of getting silently clobbered by the next redraw, or straight to
        safe_print otherwise."""
        b = current_board()
        if b is not None:
            b.note(msg)
        else:
            safe_print(msg)

    current_mode = None
    first_stat_print = True
    # Set right before a task's heavy generation call, cleared right after -- lets the
    # KeyboardInterrupt handler below know whether a task was actually in-flight when the
    # interrupt landed, so a Ctrl+C mid-crunch can be reported as a cancelled task (chunk_id and
    # all) instead of silently vanishing with no record anywhere of what was abandoned.
    current_task_chunk_id = None
    while True:
        try:
            if stop_event is not None and stop_event.is_set():
                return

            if pause_event is not None and pause_event.is_set():
                time.sleep(1)
                continue

            # Checked every cycle, not just at startup -- a new version can land while this
            # client is mid-campaign. With auto-update ON, offer_update() below downloads and
            # os.execv()'s immediately with no prompt (restarting re-enters main() from the top,
            # which naturally resumes polling/crunching once it reaches this loop again). With
            # auto-update OFF, it prints the notice and blocks on a real y/n prompt -- crunching
            # is effectively stopped right here until answered, then resumes if declined
            # (unless mandatory, which exits instead). Only the fancy_ui (main-thread) lane checks
            # this -- a background lane restarting the whole process out from under the primary
            # lane would be worse than just missing an update check on that one thread.
            if fancy_ui:
                update_status, update_info = check_for_update()
                if update_status == "must_update":
                    offer_update(update_status, update_info, mandatory=True)
                elif update_status == "update_available":
                    offer_update(update_status, update_info, mandatory=False)

            work_package = make_request(f"{SERVER_URL}/get_work?user_id={user_id}&hardware_tier={hardware_tier}&model={urllib.parse.quote(chosen_model)}&client_version={VERSION}", timeout=10)

            mode = work_package.get("mode", "rag")

            if mode != current_mode:
                first_stat_print = True
                # In dual-lane mode this transition is shared server-global state, not a
                # lane-specific event -- only the first lane to notice it announces it (see
                # should_announce_mode's comment). No active board (solo, or dual-lane currently
                # toggled off) means this is always True and behavior is unchanged.
                announce_board = current_board()
                if announce_board is None or announce_board.should_announce_mode(mode):
                    if mode == "idle":
                        banner(f"{Colors.GRAY}[{lane_tag}] Server online -- no tasks available (idle mode).{Colors.RESET}")
                    else:
                        banner(f"\n[{lane_tag}] [{MODE_BANNERS.get(mode, mode.upper() + ' MODE ACTIVATED')}]\n")
                current_mode = mode

            if mode == "idle":
                time.sleep(30)
                continue

            if mode not in ("rag", "finetune"):
                banner(f"{Colors.YELLOW}[{lane_tag}] [!] Unrecognized mode '{mode}' from server -- skipping this cycle.{Colors.RESET}")
                time.sleep(5)
                continue

            total_chunks, completed_chunks = work_package.get("total_chunks", 0), work_package.get("completed_chunks", 0)
            eta_seconds = work_package.get("eta_seconds")

            if work_package.get("status") == "done":
                # Doesn't exit -- the server can switch this client into a different mode (or back
                # to idle) later, and it should just keep following along rather than requiring a
                # manual restart every time one campaign's queue empties out.
                banner(f"\n{mode_color(mode)}{Colors.BOLD}[{lane_tag}] [★] {mode.upper()} campaign complete -- all chunks processed. Waiting for the next campaign...{Colors.RESET}")
                time.sleep(30)
                continue
            if work_package.get("status") == "waiting":
                banner(f"{Colors.GRAY}[{lane_tag}] [~] Server online -- no matched tasks left for hardware tier '{hardware_tier}'. Sleeping...{Colors.RESET}")
                time.sleep(30); continue

            task = work_package["task"]
            task_start_time = time.time()

            if mode == "rag":
                task["lines"] = len(task.get('raw_content', '').splitlines())
                task_desc = format_current_task_line(task)
                report(task_desc, "Generating analysis...", first_stat_print, completed_chunks, total_chunks, eta_seconds)

                current_task_chunk_id = task["chunk_id"]
                parsed_data, last_failure_reason = generate_rag_analysis(
                    task, chosen_model, max_threads,
                    lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                    force_cpu,
                )
                current_task_chunk_id = None

                if parsed_data is None:
                    report(task_desc, f"✗ Skipped after 3 failed attempts ({last_failure_reason}). Releasing chunk for another node.", False, completed_chunks, total_chunks, eta_seconds)
                    time.sleep(cooldown if cooldown > 0 else 1)
                    continue

                parsed_data.update({
                    "chunk_id": task["chunk_id"],
                    "title": f"[{task['relative_path']}] - {format_chunk_descriptor(task)}",
                    "user_id": user_id,
                    "lines_crunched": task["lines"],
                    "mode": "rag",
                    "client_version": VERSION,
                })
                report(task_desc, "Submitting analysis to master server...", False, completed_chunks, total_chunks, eta_seconds)
                make_request(f"{SERVER_URL}/submit_work", parsed_data)

                record_duration(time.time() - task_start_time)
                report(task_desc, "✓ Analysis uploaded successfully!", False, completed_chunks + 1, total_chunks, eta_seconds)

            else:  # mode == "finetune"
                task_desc = format_finetune_task_line(task)
                report(task_desc, "Generating training pairs...", first_stat_print, completed_chunks, total_chunks, eta_seconds)

                current_task_chunk_id = task["chunk_id"]
                parsed, last_failure = generate_finetune_pairs(
                    task, chosen_model,
                    lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                    force_cpu,
                )
                current_task_chunk_id = None

                if parsed is None:
                    # Submit a 0-pairs result instead of just skipping past it: without this, the
                    # chunk is never reported to the server, so its lock just expires and it gets
                    # handed back out again -- forever, if the failure is deterministic.
                    report(task_desc, f"✗ Skipped after 3 failed attempts ({last_failure}). Marking as done with 0 pairs.", False, completed_chunks, total_chunks, eta_seconds)
                    try:
                        make_request(f"{SERVER_URL}/submit_work", {
                            "chunk_id": task["chunk_id"],
                            "source_type": task["source_type"],
                            "pairs": [],
                            "user_id": user_id,
                            "lines_crunched": 0,
                            "mode": "finetune",
                            "client_version": VERSION,
                        })
                    except Exception:
                        pass
                    time.sleep(1)
                    continue

                pairs_generated = len(parsed["pairs"])
                submission = {
                    "chunk_id": task["chunk_id"],
                    "source_type": task["source_type"],
                    "pairs": parsed["pairs"],
                    "user_id": user_id,
                    "lines_crunched": pairs_generated,
                    "mode": "finetune",
                    "client_version": VERSION,
                }
                report(task_desc, "Submitting pairs to master server...", False, completed_chunks, total_chunks, eta_seconds)
                make_request(f"{SERVER_URL}/submit_work", submission)

                record_duration(time.time() - task_start_time)
                report(task_desc, f"✓ Submitted {pairs_generated} training pairs!", False, completed_chunks + 1, total_chunks, eta_seconds)

            first_stat_print = False
            if cooldown > 0: time.sleep(cooldown)

        except KeyboardInterrupt:
            # Only the main-thread (fancy_ui) lane ever actually lands here -- Python only
            # delivers SIGINT/KeyboardInterrupt to the main thread, so a background lane's own
            # `try` never sees one regardless of what's happening in it at the time.
            first_stat_print = True
            if pause_event is not None:
                pause_event.set()
            if current_task_chunk_id is not None:
                # A task was genuinely in-flight (mid-Ollama-call) when the interrupt landed, not
                # just idle-polling or between tasks -- report it as cancelled so it isn't just
                # silently abandoned with zero record of what got interrupted. The chunk itself
                # isn't lost (its server-side lock just expires and it goes back in the pool for
                # another pickup); this is purely about not losing visibility into why it didn't
                # complete this time.
                cancelled_event = {
                    "event": "task_cancelled", "mode": current_mode, "chunk_id": current_task_chunk_id,
                }
                log_diagnostic(cancelled_event)
                submit_diagnostic_to_server(cancelled_event)
                current_task_chunk_id = None
            handle_interrupt_menu(dual_controller)
            if pause_event is not None:
                pause_event.clear()
        except urllib.error.HTTPError as he:
            first_stat_print = True
            if he.code == 426:
                # The server raised its MIN_CLIENT_VERSION while this session was already
                # running -- re-check /version for the real current requirement and prompt the
                # same way the startup check does, rather than just retrying forever.
                status, info = check_for_update()
                if info is not None:
                    offer_update(status, info, mandatory=True)
                else:
                    try:
                        detail = json.loads(he.read().decode('utf-8'))
                    except Exception:
                        detail = he.reason
                    sys.exit(f"\n{Colors.RED}[X] Server rejected this client as outdated (HTTP 426): {detail}{Colors.RESET}")
            if he.code == 403:
                sys.exit(f"\n{Colors.RED}[X] Username '{user_id}' already exists on the network.{Colors.RESET}")
            elif he.code in (400, 422):
                try:
                    detail = json.loads(he.read().decode('utf-8'))
                except Exception:
                    detail = he.reason
                sys.exit(
                    f"\n{Colors.RED}[X] Server rejected the request as invalid (HTTP {he.code}): {detail}\n"
                    f"    This is a data/config problem, not a network hiccup -- retrying won't fix it.\n"
                    f"    Check your volunteer ID and, if this persists, report it as a bug.{Colors.RESET}"
                )
            banner(f"\n{Colors.YELLOW}[{lane_tag}] [Warning] Server error {he.code}. Retrying in 15 seconds...{Colors.RESET}"); interruptible_sleep(15, dual_controller)
        except urllib.error.URLError:
            current_mode = None
            first_stat_print = True
            banner(f"\n{Colors.RED}[{lane_tag}] [X] Server offline -- no tasks available. Retrying in 15 seconds...{Colors.RESET}"); interruptible_sleep(15, dual_controller)
        except Exception as e:
            first_stat_print = True
            banner(f"\n{Colors.RED}[{lane_tag}] [Error] Failure path encounter: {e}. Retrying in 5 seconds...{Colors.RESET}"); interruptible_sleep(5, dual_controller)

def _background_lane(**kwargs):
    """Thread target for the secondary (CPU) lane. sys.exit() from a fatal, unrecoverable error
    (e.g. HTTP 403/400/422 in crunch_lane's HTTPError handler) only kills the thread it's raised
    in, not the whole process -- fine for the primary lane (that's the existing, unchanged
    behavior), but left uncaught here it'd print a raw, alarming-looking traceback for what's
    really just "the secondary lane stopped." Reported cleanly instead; the primary lane and the
    process as a whole keep running either way.
    """
    try:
        crunch_lane(**kwargs)
    except SystemExit as se:
        with print_lock:
            print(f"\n{Colors.YELLOW}[{kwargs.get('lane_tag', 'CPU')}] Secondary lane stopped: {se}{Colors.RESET}")

def main():
    print(f"{Colors.BOLD}=== CAFS -- Cubyz AI Folding System ==={Colors.RESET}")

    user_id = load_saved_user()
    if user_id and is_valid_user_id(user_id):
        print(f"{Colors.GREEN}[✓] Auto-logged in as remembered user: {user_id}{Colors.RESET}")
    else:
        if user_id and not is_valid_user_id(user_id):
            print(f"{Colors.YELLOW}[!] Saved user ID '{user_id}' is no longer valid (3-9 ASCII letters only). Please re-enter.{Colors.RESET}")
        user_id = ""
        while not is_valid_user_id(user_id):
            user_id = input("Enter your unique volunteer ID (3-9 letters only): ").strip()
        save_user(user_id)

    # First boot only -- once configured, this is never asked again (change it from the pause
    # menu with [A] instead). Deliberately asked right after login, not before it: this is a
    # one-time onboarding question tied to "you as a volunteer," not a startup check.
    if load_auto_update_preference() is None:
        print(f"\n{Colors.CYAN}{Colors.BOLD}[i] THIS CLIENT HAS AN AUTO-UPDATE FEATURE. Would you like to enable it?{Colors.RESET}")
        print(f"{Colors.CYAN}    If enabled, updates will download automatically and the client will stop and")
        print(f"    reinstall itself the moment one is available -- no prompts.")
        print(f"    If you select no, you'll be prompted to update manually each time instead.{Colors.RESET}")
        enable_choice = input("Enable auto-update? (y/n): ").strip().lower()
        save_auto_update_preference(enable_choice == 'y')
        state_color = Colors.GREEN if enable_choice == 'y' else Colors.GRAY
        print(f"{state_color}[✓] Auto-update {'enabled' if enable_choice == 'y' else 'disabled'}. Change this anytime from the pause menu ([A]).{Colors.RESET}")

    update_status, update_info = check_for_update()
    if update_status == "must_update":
        offer_update(update_status, update_info, mandatory=True)
    elif update_status == "update_available":
        offer_update(update_status, update_info, mandatory=False)
    elif update_status == "check_failed":
        print(f"{Colors.GRAY}[~] Could not reach server to check for updates -- continuing with the current version.{Colors.RESET}")

    print(f"{Colors.CYAN}[~] Syncing stats and checking environment profiles...{Colors.RESET}")
    server_reachable = True
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard", timeout=10)
        generate_local_leaderboard_html(stats)
    except Exception:
        server_reachable = False

    chosen_model, gpu_type, total_vram_gb = get_vram_and_choose_model()
    system_ram_gb = get_system_ram_gb()

    ensure_ollama_installed(gpu_type)
    ensure_ollama_running_and_model_pulled(chosen_model)
    if gpu_type != "cpu" and chosen_model != "qwen2.5-coder:3b":
        # Needed for the CPU side of the benchmark below (and later, the dual-lane CPU lane
        # itself) regardless of what tier this GPU's own VRAM picked.
        ensure_ollama_running_and_model_pulled("qwen2.5-coder:3b")

    # Declared hardware specs (VRAM detection especially -- see check_amd_gpu()'s history in this
    # file) have repeatedly proven unreliable, and even an accurately-detected GPU can be too
    # weak, or too poorly supported by whatever backend Ollama uses for it, to actually be worth
    # using. So rather than assuming "any non-CPU gpu_type" means the GPU should be used,
    # benchmark real throughput once per machine (cached in CONFIG_FILE, keyed on a hardware
    # fingerprint so a real hardware change re-triggers it) and let the measured result decide.
    primary_is_gpu = gpu_type != "cpu"
    gpu_time = cpu_time = None
    if gpu_type != "cpu":
        fingerprint = f"{gpu_type}:{round(total_vram_gb, 1)}:{os.cpu_count()}:{chosen_model}"
        cached = load_benchmark_result()
        if cached.get("fingerprint") == fingerprint:
            primary_is_gpu = cached["primary_is_gpu"]
            gpu_time, cpu_time = cached.get("gpu_time"), cached.get("cpu_time")
        else:
            print(f"{Colors.CYAN}[~] First-time hardware benchmark: measuring real CPU vs. GPU throughput on this machine (one-time, well under a minute)...{Colors.RESET}")
            gpu_time = benchmark_lane(chosen_model, force_cpu=False)
            cpu_time = benchmark_lane("qwen2.5-coder:3b", force_cpu=True)
            if gpu_time is None:
                primary_is_gpu = False
                print(f"{Colors.YELLOW}[!] GPU benchmark failed or timed out -- this GPU doesn't appear usable for inference here. Falling back to CPU.{Colors.RESET}")
            elif cpu_time is not None and cpu_time < gpu_time:
                primary_is_gpu = False
                print(f"{Colors.YELLOW}[i] Benchmark: CPU ({cpu_time:.1f}s) outperformed GPU ({gpu_time:.1f}s) on this machine -- using CPU as the primary lane instead.{Colors.RESET}")
            else:
                primary_is_gpu = True
                print(f"{Colors.GREEN}[✓] Benchmark: GPU ({gpu_time:.1f}s) vs. CPU ({f'{cpu_time:.1f}s' if cpu_time is not None else 'failed'}) -- using GPU as the primary lane.{Colors.RESET}")
            save_benchmark_result({
                "fingerprint": fingerprint, "primary_is_gpu": primary_is_gpu,
                "gpu_time": gpu_time, "cpu_time": cpu_time,
            })

    if not primary_is_gpu:
        # Whether because there was never a GPU at all, it benchmarked unusable, or the CPU
        # simply won -- the primary lane runs on CPU with the same model/tier a solo CPU-only
        # volunteer would already be using.
        chosen_model = "qwen2.5-coder:3b"
        hardware_tier = "easy"
        mode_desc = "Eco Profile (Automated: CPU processing" + (", GPU benchmarked slower or unusable here" if gpu_type != "cpu" else " infrastructure fallback") + ")"
        cooldown, max_threads = 4.0, 2
        primary_hardware_label = f"CPU Engine ({system_ram_gb:.1f} GB RAM)"
    else:
        hardware_tier = "easy" if total_vram_gb <= 4.5 else ("medium" if total_vram_gb <= 8.5 else "hard")
        if total_vram_gb > 8.0:
            mode_desc = "Performance Profile (Automated: High-memory Apple Silicon or discrete GPU detected)" if PLATFORM == "darwin" else "Performance Profile (Automated: High VRAM GPU detected)"
            cooldown, max_threads = 0.0, None
        else:
            mode_desc = "Balanced Profile (Automated: Standard Apple Silicon or discrete GPU detected)" if PLATFORM == "darwin" else "Balanced Profile (Automated: Standard GPU detected)"
            cooldown, max_threads = 1.5, 4
        if gpu_type == "apple_silicon":
            primary_hardware_label = f"Apple Silicon ({total_vram_gb:.1f} GB effective unified memory)"
        elif gpu_type == "intel_dgpu":
            primary_hardware_label = f"Intel Mac + Discrete GPU ({total_vram_gb:.1f} GB VRAM)"
        else:
            primary_hardware_label = f"{gpu_type.upper()} ({total_vram_gb:.1f} GB VRAM)"

    # Dual-lane needs the GPU to actually BE the primary lane (a benchmark-rejected or CPU-beaten
    # GPU has nothing independent left to add -- see primary_is_gpu above), the CPU side of the
    # same benchmark to have also succeeded (confirms it's independently viable, not just
    # "unmeasured"), and both the RAM/VRAM headroom checks (see DUAL_LANE_MIN_RAM_GB/
    # DUAL_LANE_MIN_VRAM_GB's comments -- system RAM alone doesn't help if the GPU itself is
    # already maxed out).
    dual_capable = (
        primary_is_gpu
        and cpu_time is not None
        and system_ram_gb >= DUAL_LANE_MIN_RAM_GB
        and total_vram_gb >= DUAL_LANE_MIN_VRAM_GB
    )

    log_diagnostic({
        "event": "session_start", "platform": PLATFORM, "gpu_type": gpu_type,
        "total_vram_gb": round(total_vram_gb, 2), "system_ram_gb": round(system_ram_gb, 2),
        "chosen_model": chosen_model, "hardware_tier": hardware_tier, "client_version": VERSION,
        "dual_lane": dual_capable, "primary_is_gpu": primary_is_gpu,
        "benchmark_gpu_time": gpu_time, "benchmark_cpu_time": cpu_time,
    })

    if server_reachable:
        print(f"{Colors.GREEN}[✓] Cluster connectivity established. Entering processing pipeline...{Colors.RESET}\n")
    else:
        print(f"{Colors.YELLOW}[!] Server unreachable -- entering offline-retry mode. Will connect once it's back.{Colors.RESET}\n")

    dual_controller = None
    if dual_capable:
        # Reserve a couple of logical threads for the GPU lane's own overhead and the OS, give
        # the rest to the CPU lane's Ollama call. Hardcoding the same "2" the solo Eco Profile
        # uses here was wrong -- that value is deliberately conservative for a genuinely weak
        # CPU-only volunteer, not for a real multi-core CPU running a *second*, dedicated lane
        # alongside a GPU lane (confirmed live: a 6-core/12-thread Ryzen 5 9600X sat at ~35% CPU
        # utilization capped at "2" -- 2 threads on a 12-thread part).
        cpu_lane_threads = max(2, (os.cpu_count() or 4) - 2)
        cpu_hardware_label = f"{cpu_lane_threads} threads, {system_ram_gb:.1f} GB RAM"
        print(f"{Colors.CYAN}[✓] Dual-lane mode: GPU ({primary_hardware_label}) + a secondary CPU lane (qwen2.5-coder:3b, {cpu_hardware_label}) will crunch two tasks at once. Toggle it off/on anytime from the pause menu.{Colors.RESET}\n")
        board = DualStatusBoard(gpu_label=primary_hardware_label, cpu_label=cpu_hardware_label)
        # user_id is 3-9 alpha chars (enforced at login); truncating to 8 and appending "c" always
        # differs from the primary lane's own id (even at the 9-char ceiling, where a bare
        # suffix would otherwise just silently reproduce the original id) while staying within
        # that same 3-9 range the server itself validates against.
        cpu_user_id = user_id[:8] + "c"
        dual_controller = DualLaneController(board=board, cpu_lane_kwargs=dict(
            lane_tag="CPU", user_id=cpu_user_id, hardware_tier="easy", chosen_model="qwen2.5-coder:3b",
            max_threads=cpu_lane_threads, cooldown=1.0, mode_desc="Eco Profile (Automated: Secondary CPU lane, running alongside the primary GPU lane)",
            hardware_label=cpu_hardware_label, force_cpu=True, fancy_ui=False,
        ))
        dual_controller.start()  # on by default, same as before this toggle existed -- just now reversible

    crunch_lane(
        # fancy_ui is always True here, even on a dual-capable machine -- it means "fall back to
        # my own solo box whenever current_board() has nothing to report into," which is true
        # both for a genuinely solo machine AND a dual-capable one that's toggled the CPU lane
        # off via the pause menu's [D] option. Fixing this at "not dual_capable" (a one-time
        # startup snapshot) meant a dual-capable machine's fancy_ui was permanently False, so
        # toggling dual mode off left it with no fallback at all -- board (via current_board())
        # correctly went away, but so did the box, leaving nothing but plain text.
        lane_tag="GPU" if dual_capable else "MAIN", user_id=user_id, hardware_tier=hardware_tier,
        chosen_model=chosen_model, max_threads=max_threads, cooldown=cooldown, mode_desc=mode_desc,
        hardware_label=primary_hardware_label, force_cpu=not primary_is_gpu, fancy_ui=True,
        pause_event=dual_controller.pause_event if dual_controller is not None else None,
        dual_controller=dual_controller,
    )

if __name__ == "__main__":
    main()
