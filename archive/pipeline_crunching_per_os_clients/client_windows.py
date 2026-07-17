import os
import re
import sys
import json
import time
import subprocess
import shutil
import urllib.request
import urllib.error
import urllib.parse

if not sys.platform.startswith("win32"):
    print("[X] This script is explicitly configured for Windows systems only.")
    sys.exit(1)

os.system('color')

SERVER_URL = "http://ashframe.net:7000"
OLLAMA_URL = "http://localhost:11434/api/generate"
CONFIG_FILE = os.path.expanduser("~/.cubyz_node_config.json")

USER_ID_PATTERN = re.compile(r"^[a-zA-Z]+$")

def is_valid_user_id(user_id: str) -> bool:
    return bool(user_id) and 3 <= len(user_id) <= 9 and bool(USER_ID_PATTERN.fullmatch(user_id))

SESSION_CHUNKS_COMPLETED = 0
SESSION_LINES_CRUNCHED = 0

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

PROMPTS = {
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

DISCRETE_AMD_MARKERS = ["radeon rx", "radeon pro", "radeon vii", "instinct"]
DISCRETE_INTEL_MARKERS = ["arc a", "arc b", "dg2", "dg3", "data center gpu", "flex 1", "max 1"]

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
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.total', '--format=csv,nounits,noheader'],
            capture_output=True, text=True, check=True, timeout=15
        )
        return True, int(result.stdout.strip().split('\n')[0]) / 1024.0
    except Exception:
        pass
    for gpu in get_windows_gpus():
        name = _normalize_gpu_name(str(gpu.get("Name", "")))
        if "nvidia" in name or "geforce" in name or "quadro" in name or "rtx" in name:
            return True, 16.0
    return False, 0.0

def check_amd_gpu() -> tuple:
    for gpu in get_windows_gpus():
        name = _normalize_gpu_name(str(gpu.get("Name", "")))
        if "amd" not in name and "radeon" not in name:
            continue
        if any(m in name for m in DISCRETE_AMD_MARKERS):
            return True, 16.0
        return True, get_system_ram_gb() * 0.4
    return False, 0.0

def check_intel_gpu() -> tuple:
    for gpu in get_windows_gpus():
        name = _normalize_gpu_name(str(gpu.get("Name", "")))
        if "intel" not in name:
            continue
        if any(m in name for m in DISCRETE_INTEL_MARKERS):
            return True, 16.0
        return True, get_system_ram_gb() * 0.4
    return False, 0.0

def get_vram_and_choose_model() -> tuple:
    gpu_type, total_vram_gb = "cpu", 0.0
    ram_gb = get_system_ram_gb()

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

    if total_vram_gb >= 20.0:
        model = "qwen3-coder:30b"
    elif total_vram_gb >= 12.0:
        model = "qwen2.5-coder:14b"
    elif total_vram_gb >= 6.0:
        model = "qwen2.5-coder:7b"
    elif total_vram_gb >= 3.5 or ram_gb >= 11.0:
        model = "qwen2.5-coder:3b"
    else:
        sys.exit(f"\n[X] Hardware Restriction: Insufficient resources ({total_vram_gb:.1f}G VRAM / {ram_gb:.1f}G RAM).")

    return model, gpu_type, total_vram_gb

def load_saved_user() -> str:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("user_id", "")
        except Exception: pass
    return ""

def save_user(user_id: str):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump({"user_id": user_id}, f)
    except Exception: pass

def ensure_ollama_installed():
    if shutil.which("ollama"):
        return

    print("[~] Ollama framework absent. Initializing setup...")
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
            print(f"[!] winget installation failed: {e}")

    print("\n[!] Ollama is not installed or could not be located on your system.")
    print("[~] Open your web browser and install Ollama for Windows from: https://ollama.com/download/windows")
    input("[?] Once you have completed the installation, press [ENTER] to continue... ")

    if not shutil.which("ollama"):
        sys.exit("[X] Still could not locate 'ollama' in system PATH. Please restart this terminal and run the script again.")

def ensure_ollama_running_and_model_pulled(model_name):
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=3)
    except Exception:
        subprocess.Popen(
            ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )
        time.sleep(5)

    try: subprocess.run(["ollama", "pull", model_name], capture_output=True, check=True)
    except Exception as e: sys.exit(f"[X] Model setup failed: {e}")

def format_chunk_descriptor(task: dict) -> str:
    match = re.match(r'github_pr_(\d+)_comment_\d+', task.get("chunk_id", ""))
    if match:
        return f"PR #{match.group(1)} review diff"
    return f"Chunk {task['chunk_index']}"

def format_current_task_line(task: dict) -> str:
    match = re.match(r'github_pr_(\d+)_comment_\d+', task.get("chunk_id", ""))
    if match:
        return f"GitHub PR #{match.group(1)} review diff, touching {task['relative_path']} ({task['lines']} lines)"
    return f"{task['relative_path']} ({format_chunk_descriptor(task)} • {task['lines']} lines)"

def make_request(url, payload=None):
    data = json.dumps(payload).encode('utf-8') if payload else None
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'} if data else {})
    with urllib.request.urlopen(req, timeout=120) as res: return json.loads(res.read().decode('utf-8'))

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
        qualified = [s for s in symbols if "." in s and " " not in s]
        if qualified:
            orphaned = [s for s in qualified if s.split(".")[0] not in symbol_set]
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

def generate_local_leaderboard_html(stats: dict):
    """Generates a styled, read-only HTML file next to the client script."""
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leaderboard.html")

    total = stats.get("total_chunks_in_codebase", 1)
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
        html_content += f"""
                <tr>
                    <td class="rank">#{user['rank']}</td>
                    <td>{user['user_id']}</td>
                    <td>{user['chunks_completed']}</td>
                    <td>{user['lines_crunched']}</td>
                    <td>{user['contribution_percentage']}%</td>
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
        stats = make_request(f"{SERVER_URL}/leaderboard")
    except Exception as e:
        print(f"[X] Could not sync ledger metrics: {e}")
        return

    generate_local_leaderboard_html(stats)

    tot, comp = stats.get("total_chunks_in_codebase", 1), stats.get("total_chunks_completed", 0)
    pct = stats.get("global_percentage", 0.0)
    bar_len = 20
    fill_len = int(round(bar_len * comp / float(tot))) if tot else 0
    p_bar = '█' * fill_len + '░' * (bar_len - fill_len)

    print(f"─── [ CUBYZ DISTRIBUTED LEADERBOARD ] ──────────────────────────────────")
    print(f"  Global Progress: [{p_bar}] {comp}/{tot} ({pct:.2f}%)")
    rankings = stats.get("rankings", [])
    if not rankings:
        print(f"  {'Rankings':<13}: No contributions recorded yet.")
    for u in rankings:
        label = f"Rank #{u['rank']}"
        print(f"  {label:<13}: {u['user_id']} • {u['chunks_completed']} chunks • {u['lines_crunched']} lines • {u['contribution_percentage']:.1f}% share")
    print(f"  {'Local View':<13}: also written to leaderboard.html next to this script")
    print(f"────────────────────────────────────────────────────────────────────────")

def fetch_and_show_userlist():
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard")
    except Exception as e:
        print(f"[X] Could not sync node roster: {e}")
        return

    users = stats.get("rankings", [])
    online = [u for u in users if "ONLINE" in u.get("status", "")]
    offline = [u for u in users if "ONLINE" not in u.get("status", "")]

    print(f"─── [ CUBYZ ACTIVE NODE ROSTER ] ────────────────────────────────────────")
    print(f"  Node Summary : {len(online)} online • {len(offline)} offline • {len(users)} known nodes total")
    if not users:
        print(f"  {'Nodes':<13}: No nodes have connected yet.")
    for u in online + offline:
        label = u["status"]
        print(f"  {label:<13}: {u['user_id']} • {u['chunks_completed']} chunks • {u['lines_crunched']} lines")
    print(f"────────────────────────────────────────────────────────────────────────")

def handle_interrupt_menu():
    print("\n\n[||] Node Execution Paused via User Action.")
    while True:
        choice = input("Enter [R] to resume, [L] to view the leaderboard, [U] to view active users, or [Q] to safely exit: ").strip().lower()
        if choice == 'r': return
        elif choice == 'l': fetch_and_show_leaderboard()
        elif choice == 'u': fetch_and_show_userlist()
        elif choice == 'q': sys.exit("[X] Disconnecting safely. Thank you for your computational contributions!")

def main():
    global SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED
    print("=== Cubyz Dataset Distributed Folding Node (Windows Edition) ===")

    user_id = load_saved_user()
    if user_id and is_valid_user_id(user_id):
        print(f"[✓] Auto-logged in as remembered user: {user_id}")
    else:
        if user_id and not is_valid_user_id(user_id):
            print(f"[!] Saved user ID '{user_id}' is no longer valid (3-9 ASCII letters only). Please re-enter.")
        user_id = ""
        while not is_valid_user_id(user_id):
            user_id = input("Enter your unique volunteer ID (3-9 letters only): ").strip()
        save_user(user_id)

    print("[~] Syncing stats and checking environment profiles...")
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard")
        generate_local_leaderboard_html(stats)
        SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED = next(((u["chunks_completed"], u["lines_crunched"]) for u in stats.get("rankings", []) if u["user_id"].lower() == user_id.lower()), (0, 0))
    except Exception: pass

    chosen_model, gpu_type, total_vram_gb = get_vram_and_choose_model()
    hardware_tier = "easy" if gpu_type == "cpu" or total_vram_gb <= 4.5 else ("medium" if total_vram_gb <= 8.5 else "hard")

    if gpu_type != "cpu" and total_vram_gb > 8.0:
        mode_desc = "Performance Profile (Automated: High VRAM GPU detected)"
        cooldown, max_threads = 0.0, None
    elif gpu_type != "cpu" and total_vram_gb <= 8.0:
        mode_desc = "Balanced Profile (Automated: Standard GPU detected)"
        cooldown, max_threads = 1.5, 4
    else:
        mode_desc = "Eco Profile (Automated: CPU processing infrastructure fallback)"
        cooldown, max_threads = 4.0, 2

    ensure_ollama_installed()
    ensure_ollama_running_and_model_pulled(chosen_model)

    print(f"[✓] Cluster connectivity established. Entering processing pipeline...\n")

    def print_terminal_status(task, step_msg, is_first, comp, tot):
        if not is_first:
            sys.stdout.write("\033[F\033[K" * 7)

        pct = (comp / tot * 100) if tot else 0.0
        bar_len = 20
        fill_len = int(round(bar_len * comp / float(tot))) if tot else 0
        p_bar = '█' * fill_len + '░' * (bar_len - fill_len)

        hw_desc = f"{gpu_type.upper()} ({total_vram_gb:.1f} GB VRAM)" if gpu_type != "cpu" else f"CPU Engine ({get_system_ram_gb():.1f} GB RAM)"

        print(f"─── [ {hw_desc} ] ──────────────────────────────────────────")
        print(f"  Current Task : {format_current_task_line(task)}")
        print(f"  Configuration: Model: {chosen_model} • Mode: {mode_desc.split(' (')[0]}")
        print(f"  Node Status  : {step_msg}")
        print(f"  Your Stats   : {SESSION_CHUNKS_COMPLETED} chunks shared • {SESSION_LINES_CRUNCHED} lines crunched")
        print(f"  Global Progress: [{p_bar}] {comp}/{tot} ({pct:.2f}%)")
        print(f"────────────────────────────────────────────────────────────────────────")
        sys.stdout.flush()

    first_stat_print = True
    while True:
        try:
            work_package = make_request(f"{SERVER_URL}/get_work?user_id={user_id}&hardware_tier={hardware_tier}&model={urllib.parse.quote(chosen_model)}")
            total_chunks, completed_chunks = work_package.get("total_chunks", 0), work_package.get("completed_chunks", 0)

            if work_package.get("status") == "done":
                print("\n[★] Codebase complete! All chunks successfully processed. Thank you!")
                break
            if work_package.get("status") == "waiting":
                print(f"[~] No matched tasks left for hardware tier '{hardware_tier}'. Sleeping...")
                time.sleep(30); continue

            task = work_package["task"]
            task["lines"] = len(task.get('raw_content', '').splitlines())

            print_terminal_status(task, "Generating analysis...", first_stat_print, completed_chunks, total_chunks)

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
                "prompt": f"Context Source File: {task['file_name']}\nRelative Path: {task['relative_path']}\nDirectory Module context: {task['directory_context']}\nChunk Index: {task['chunk_index']}\nRaw Content:\n```\n{task.get('raw_content', '')}\n```\n",
                "system": PROMPTS[p_key] + (LOW_VRAM_REASONING_RULE if chosen_model in ["qwen2.5-coder:3b"] else ""),
                "think": False,
                "stream": False, "format": RAG_JSON_SCHEMA, "options": {"temperature": temp, **({"num_thread": max_threads} if max_threads else {})}
            }

            raw_content = task.get("raw_content", "")
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
                    print_terminal_status(task, f"⚠ Attempt {attempt+1} failed: {last_failure_reason}", False, completed_chunks, total_chunks)
                    continue

                if not json_string:
                    last_failure_reason = "Ollama returned HTTP 200 with an empty 'response' field"
                    print_terminal_status(task, f"⚠ Attempt {attempt+1}: model returned empty output. Retrying...", False, completed_chunks, total_chunks)
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
                    print_terminal_status(task, f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...", False, completed_chunks, total_chunks)
                    continue

                candidate = sanitize_extraction(candidate, raw_content, p_key)

                is_valid, validation_reason = validate_extraction(candidate, raw_content, p_key)
                if is_valid:
                    parsed_data = candidate
                    break
                last_failure_reason = f"Self-check failed: {validation_reason}"
                print_terminal_status(task, f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...", False, completed_chunks, total_chunks)

            if parsed_data is None:
                print_terminal_status(task, f"✗ Skipped after 3 failed attempts ({last_failure_reason}). Releasing chunk for another node.", False, completed_chunks, total_chunks)
                time.sleep(cooldown if cooldown > 0 else 1)
                continue

            parsed_data.update({"chunk_id": task["chunk_id"], "title": f"[{task['relative_path']}] - {format_chunk_descriptor(task)}", "user_id": user_id, "lines_crunched": task["lines"]})
            print_terminal_status(task, "Submitting analysis to master server...", False, completed_chunks, total_chunks)
            make_request(f"{SERVER_URL}/submit_work", parsed_data)

            SESSION_CHUNKS_COMPLETED += 1; SESSION_LINES_CRUNCHED += task["lines"]
            print_terminal_status(task, "✓ Analysis uploaded successfully!", False, completed_chunks + 1, total_chunks)

            first_stat_print = False
            if cooldown > 0: time.sleep(cooldown)

        except KeyboardInterrupt:
            first_stat_print = True; handle_interrupt_menu()
        except urllib.error.HTTPError as he:
            first_stat_print = True
            if he.code == 403:
                sys.exit(f"\n[X] Username '{user_id}' already exists on the network.")
            elif he.code in (400, 422):
                try:
                    detail = json.loads(he.read().decode('utf-8'))
                except Exception:
                    detail = he.reason
                sys.exit(
                    f"\n[X] Server rejected the request as invalid (HTTP {he.code}): {detail}\n"
                    f"    This is a data/config problem, not a network hiccup -- retrying won't fix it.\n"
                    f"    Check your volunteer ID and, if this persists, report it as a bug."
                )
            print(f"\n[Warning] Server error {he.code}. Retrying in 15 seconds..."); time.sleep(15)
        except urllib.error.URLError:
            first_stat_print = True
            print("\n[Warning] Master server offline or unreachable. Retrying in 15 seconds..."); time.sleep(15)
        except Exception as e:
            first_stat_print = True
            print(f"\n[Error] Failure path encounter: {e}. Retrying in 5 seconds..."); time.sleep(5)

if __name__ == "__main__":
    main()
