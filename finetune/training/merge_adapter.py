"""
Merges the trained LoRA adapter weights into the base model, producing a standalone model
directory (full-precision merged weights, not 4-bit) ready for normal HF inference or further
conversion (e.g. to GGUF via llama.cpp's converter, for loading back into Ollama).

QLoRA only ever trains the small adapter matrices on top of a 4-bit frozen base -- the adapter
alone isn't a runnable model by itself in most serving stacks, and merging back into a
higher-precision copy of the base is the standard last step before actually using the result.
"""
import argparse

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

from train_qlora import MODEL_ID, OUTPUT_DIR

DEFAULT_ADAPTER_DIR = f"{OUTPUT_DIR}/final_adapter"
DEFAULT_MERGED_DIR = f"{OUTPUT_DIR}/merged"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-model-id", default=MODEL_ID)
    parser.add_argument("--adapter-dir", default=DEFAULT_ADAPTER_DIR)
    parser.add_argument("--output-dir", default=DEFAULT_MERGED_DIR)
    args = parser.parse_args()

    print(f"[~] Loading base model in bf16 (full precision merge target): {args.base_model_id}")
    base_model = AutoModelForCausalLM.from_pretrained(
        args.base_model_id,
        dtype=torch.bfloat16,
        device_map="cpu",  # merging is a one-time CPU-side op; no need to burn GPU memory on it
    )
    tokenizer = AutoTokenizer.from_pretrained(args.base_model_id)

    print(f"[~] Loading LoRA adapter from {args.adapter_dir}")
    model = PeftModel.from_pretrained(base_model, args.adapter_dir)

    print("[~] Merging adapter into base weights...")
    merged = model.merge_and_unload()

    merged.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print(f"[OK] Merged model saved to {args.output_dir}")
    print("[~] To use with Ollama: convert to GGUF via llama.cpp's convert_hf_to_gguf.py, then `ollama create`.")


if __name__ == "__main__":
    main()
