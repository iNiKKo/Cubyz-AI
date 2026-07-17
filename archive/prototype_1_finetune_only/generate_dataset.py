import os
import json
import time
import urllib.request
from typing import Generator, Set

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "devstral:24b"  # Your high-powered 24B agentic model

SOURCE_DIR = "/home/nick/Desktop/pyut/Cubyz/"
OUTPUT_FILE = "cubyz_rag_dataset.jsonl"
STATE_FILE = ".processed_files.json"
TARGET_EXTENSIONS = ('.zig', '.zon', '.txt', '.md', '.json', '.glsl')

# RAG-Focused JSON Schema
RAG_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "comprehensive_explanation": {"type": "string"},
        "code_example": {"type": ["string", "null"]},
        "synthetic_queries": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 2,
            "maxItems": 4
        }
    },
    "required": ["summary", "comprehensive_explanation", "code_example", "synthetic_queries"]
}

SYSTEM_PROMPT = """You are a strict, literalist Zig software engineer documenting the Cubyz voxel engine.
Your singular goal is to extract facts from the raw file chunk and convert it into a deterministic data node.

STRICT TRUTH, LANGUAGE, AND CODE SYNTHESIS RULES:
1. NO EXTRAPOLATION: Rely ONLY on the explicit syntax, variables, types, and logic present in the provided chunk. Do not assume how external systems or unmentioned Cubyz engine functions work.
2. STRICT ENGLISH: All output fields—including explanations, summaries, and queries—MUST be written entirely in clear, technical English. Never output in other languages.
3. DETAILED CODE SYNTHESIS: In 'code_example', do not just copy-paste massive blocks. Instead, write a simplified, clean, and fully-functional Zig (or GLSL/JSON depending on the file) code snippet demonstrating how to use, call, or configure the logic present in this chunk. If the chunk contains no logical code (e.g. metadata or a text log), set 'code_example' to null.
4. ABSOLUTE CERTAINTY: If you are not 100% sure about a specific implementation detail based solely on this chunk, do not include it in the 'comprehensive_explanation'.
"""

def is_target_file(filename: str) -> bool:
    return filename.lower().endswith(TARGET_EXTENSIONS)

def chunk_file_with_overlap(file_path: str, chunk_size: int = 150, overlap: int = 30) -> Generator[str, None, None]:
    """Chunks the file while keeping a rolling overlap to ensure functions aren't cut in half."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        if len(lines) <= chunk_size:
            yield "".join(lines)
            return

        step = chunk_size - overlap
        for i in range(0, len(lines), step):
            chunk = lines[i:i + chunk_size]
            yield "".join(chunk)
            if i + chunk_size >= len(lines):
                break
    except Exception as e:
        print(f"Skipping {file_path} due to read error: {e}")
        return

def query_generator_llm(prompt: str, temperature: float = 0.1, retries: int = 3) -> str:
    """Queries Ollama with automatic retry logic and exponential backoff to handle GPU/container timeouts."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "format": RAG_JSON_SCHEMA,
        "options": {
            "temperature": temperature
        }
    }

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                return res_data.get("response", "")
        except Exception as e:
            wait_time = (attempt + 1) * 5
            print(f"\n  [Warning] Ollama call failed: {e}. Retrying in {wait_time}s... (Attempt {attempt + 1}/{retries})")
            time.sleep(wait_time)

    return ""

def load_processed_state() -> Set[str]:
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                return set(json.load(f))
        except Exception:
            pass
    return set()

def save_processed_state(processed_set: Set[str]):
    try:
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(list(processed_set), f, indent=2)
    except Exception as e:
        print(f"Error saving tracking state: {e}")

def main():
    print(f"Scanning codebase: {os.path.abspath(SOURCE_DIR)}")
    processed_files = load_processed_state()

    if processed_files:
        print(f"Loaded {len(processed_files)} completed files. Skipping them.")

    with open(OUTPUT_FILE, "a", encoding="utf-8") as out_f:
        for root, dirs, files in os.walk(SOURCE_DIR):
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if not is_target_file(file) or file in (OUTPUT_FILE, STATE_FILE):
                    continue

                file_path = os.path.join(root, file)
                if file_path in processed_files:
                    continue

                # Context enrichment: Grab directory hierarchy to guide the LLM
                relative_path = os.path.relpath(file_path, SOURCE_DIR)
                relative_dir = os.path.dirname(relative_path)

                # Dynamic Temperature Selection
                is_doc = file.lower().endswith(('.md', '.txt'))
                temp = 0.12 if is_doc else 0.02  # Rigid logic for code, slightly smoother for md files

                print(f"\nProcessing: {file_path}")
                file_success = True

                for chunk_idx, chunk in enumerate(chunk_file_with_overlap(file_path)):
                    prompt_text = (
                        f"Context Source File: {file}\n"
                        f"Relative Path: {relative_path}\n"
                        f"Directory Module context: {relative_dir}\n"
                        f"Chunk Index: {chunk_idx}\n"
                        f"Raw Content:\n```\n{chunk}\n```\n"
                    )

                    response_text = query_generator_llm(prompt_text, temperature=temp)
                    if not response_text:
                        file_success = False
                        print(f"  -> Critical: Failed to get response for {file_path} chunk {chunk_idx}")
                        continue

                    try:
                        parsed_node = json.loads(response_text)

                        # Double-check schema integrity
                        required_keys = ["summary", "comprehensive_explanation", "code_example", "synthetic_queries"]
                        if not all(k in parsed_node for k in required_keys):
                            file_success = False
                            continue

                        # ENHANCEMENT: Inject a clean, normalized deterministic title on our side
                        file_label = relative_path.replace("\\", "/")
                        parsed_node["title"] = f"[{file_label}] - Chunk {chunk_idx}"

                        # Clean dataset write
                        out_f.write(json.dumps(parsed_node, ensure_ascii=False) + "\n")
                        out_f.flush()
                        print(f"  -> Generated high-fidelity RAG node for chunk {chunk_idx}")

                    except json.JSONDecodeError:
                        print(f"  -> Failed JSON validation on chunk {chunk_idx}")
                        file_success = False

                if file_success:
                    processed_files.add(file_path)
                    save_processed_state(processed_files)

if __name__ == "__main__":
    main()
