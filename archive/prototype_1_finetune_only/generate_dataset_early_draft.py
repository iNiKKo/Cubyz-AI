import os
import json
from typing import Generator, Set
import urllib.request

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"

SOURCE_DIR = "/home/nick/Desktop/pyut/Cubyz/assets/cubyz/"
OUTPUT_FILE = "cubyz_training.jsonl"
TARGET_EXTENSIONS = ('.zig', '.zon', '.txt', '.md', '.json', '.glsl')

# Define the strict JSON schema to enforce on the LLM
JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "dataset": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "instruction": {"type": "string"},
                    "input": {"type": "string"},
                    "output": {"type": "string"}
                },
                "required": ["instruction", "input", "output"]
            }
        }
    },
    "required": ["dataset"]
}

SYSTEM_PROMPT = """You are an expert Zig software engineer specializing in the Cubyz voxel engine.
Your task is to analyze the provided source code or configuration files and generate 1 to 3 diverse training examples
useful for teaching another AI about this engine.

CRITICAL RULES FOR GENERATION:
1. NO TRUNCATED CODE: When writing code for the 'input' or 'output' fields, write fully functional, syntactically correct Zig snippets. Never use '...' or truncate critical code logic if it fits.
2. ENGINE SPECIFICITY: Frame your questions specifically around the context of the Cubyz game engine.
"""

def is_target_file(filename: str) -> bool:
    return filename.lower().endswith(TARGET_EXTENSIONS)

def chunk_file(file_path: str, max_lines: int = 150) -> Generator[str, None, None]:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        for i in range(0, len(lines), max_lines):
            yield "".join(lines[i:i + max_lines])
    except Exception as e:
        print(f"Skipping {file_path} due to read error: {e}")
        return

def query_devstral(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "format": JSON_SCHEMA,  # <-- Enforces the JSON schema natively in Ollama!
        "options": {
            "temperature": 0.2
        }
    }

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data.get("response", "")
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return ""

def get_processed_files(output_file_path: str) -> Set[str]:
    """Reads the existing output file and returns a set of file paths that have already been parsed."""
    processed = set()
    if not os.path.exists(output_file_path):
        return processed

    print(f"Analyzing existing '{output_file_path}' to find where we left off...")

    # Pre-build a map of lowercase filenames to their actual absolute paths
    # This keeps lookups incredibly fast without running walk() inside a loop
    all_workspace_files = {}
    for root, dirs, files in os.walk(SOURCE_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if is_target_file(file):
                all_workspace_files[file.lower()] = os.path.join(root, file)

    try:
        with open(output_file_path, 'r', encoding='utf-8') as f:
            for line_idx, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)

                    # 1. Primary check: Use our modern source tracking key
                    if "_source_file" in data:
                        processed.add(data["_source_file"])
                        continue

                    # 2. Smart Fallback: Scan text fields for file names to skip past entries
                    instruction_lower = data.get("instruction", "").lower()
                    input_lower = data.get("input", "").lower()

                    for filename, full_path in all_workspace_files.items():
                        # If the filename (e.g., 'utils.zig') is referenced in the Q&A, skip it
                        if filename in instruction_lower or filename in input_lower:
                            processed.add(full_path)

                except json.JSONDecodeError:
                    continue
    except Exception as e:
        print(f"Warning: Could not read existing dataset cleanly: {e}")

    if processed:
        print(f"Found {len(processed)} files already successfully completed. They will be skipped.")
    return processed

def main():
    print(f"Scanning from root: {os.path.abspath(SOURCE_DIR)}")
    print(f"Outputting to: {OUTPUT_FILE}")

    # Identify files we have already processed
    processed_files = get_processed_files(OUTPUT_FILE)

    # Open in 'a' mode to append data cleanly without erasing anything
    with open(OUTPUT_FILE, "a", encoding="utf-8") as out_f:
        for root, dirs, files in os.walk(SOURCE_DIR):
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if not is_target_file(file):
                    continue
                if file == OUTPUT_FILE:
                    continue

                file_path = os.path.join(root, file)

                # Skip files we have already parsed in a previous run
                if file_path in processed_files:
                    continue

                print(f"\nProcessing: {file_path}")

                for chunk_idx, chunk in enumerate(chunk_file(file_path)):
                    prompt_text = (
                        f"File: {file}\n"
                        f"File Path: {file_path}\n"
                        f"Chunk index: {chunk_idx}\n"
                        f"Content:\n```\n{chunk}\n```\n"
                        f"Analyze this block of Cubyz engine data and generate 1 to 3 diverse JSON training objects."
                    )

                    response_text = query_devstral(prompt_text)
                    if not response_text:
                        print(f"  -> Empty response from LLM for chunk {chunk_idx}")
                        continue

                    try:
                        # Because of JSON_SCHEMA, we can safely trust json.loads directly!
                        response_json = json.loads(response_text)
                        parsed_examples = response_json.get("dataset", [])
                    except json.JSONDecodeError:
                        print(f"  -> Failed to parse JSON response from LLM on chunk {chunk_idx}.")
                        continue

                    saved_count = 0
                    for item in parsed_examples:
                        if all(k in item for k in ("instruction", "input", "output")):
                            # Auto-anchoring enhancement
                            instruction = item["instruction"].strip()
                            if "cubyz" not in instruction.lower():
                                instruction = f"In the Cubyz game engine, {instruction[0].lower()}{instruction[1:]}"

                            cleaned_item = {
                                "instruction": instruction,
                                "input": item["input"].strip(),
                                "output": item["output"].strip(),
                                "_source_file": file_path  # We tag the source file path here to keep track of progress!
                            }

                            if not cleaned_item["instruction"] or not cleaned_item["output"]:
                                continue

                            out_f.write(json.dumps(cleaned_item) + "\n")
                            saved_count += 1

                    out_f.flush()

                    if saved_count > 0:
                        print(f"  -> Generated {saved_count} clean training pairs from chunk {chunk_idx}")

if __name__ == "__main__":
    main()
