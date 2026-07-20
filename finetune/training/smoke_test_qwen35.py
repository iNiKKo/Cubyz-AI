"""
Isolated risk check for Qwen3.5-4B before committing to a full training run on it.

Why this exists: Qwen3.5-0.8B already hard-faulted the GPU driver on this exact card/ROCm
combo during step 1 of real training ("Memory access fault by GPU node-1... Page not present",
GPU core dump, process aborted, required a full PC reboot). Root cause: Qwen3.5's hybrid Gated
DeltaNet attention needs `flash-linear-attention`/`causal-conv1d` kernels; those aren't installed,
transformers falls back to a torch reimplementation of that path, and that fallback is what
faulted. `causal-conv1d` has no official ROCm support for this RDNA4 chip class as of 2026
(upstream GitHub issue open, unassigned) -- this is architecture-inherent, not size-specific, so
Qwen3.5-4B carries the identical risk.

This script does the smallest real exercise of that exact failure path -- one forward pass, one
backward pass, through the real model with LoRA wrapping (matching train_qlora.py's actual code
path) -- and nothing else. If it's going to crash, better to find out here in a few seconds than
partway through a real multi-hour run.

Note: a clean pass here is a good sign but not an absolute guarantee -- a hard driver-level fault
(as opposed to a clean Python exception) can in principle still surface later under sustained
load even if a single step succeeds. Worth watching the first several real training steps closely
even after this passes.
"""
import sys

import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen3.5-4B"

LORA_TARGET_MODULES = [
    "q_proj", "k_proj", "v_proj", "o_proj",
    "gate_proj", "up_proj", "down_proj",
]


def main():
    print(f"=== Qwen3.5-4B hybrid-attention risk check ===\n")
    print(f"[~] Loading {MODEL_ID} in bf16 (no quantization -- keeping this test as close to "
          f"train_qlora.py's actual codepath as practical while staying fast to iterate on)...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map={"": 0},
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
    )
    print("[OK] Model loaded. Watch the line above/below this for the 'fast path is not "
          "available' warning -- that confirms the fallback path (the risky one) is what's "
          "about to get exercised.")

    lora_config = LoraConfig(
        r=16, lora_alpha=32, lora_dropout=0.05,
        target_modules=LORA_TARGET_MODULES,
        bias="none", task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.train()
    print("[OK] LoRA wrapping succeeded.")

    print("\n[~] Running one forward pass...")
    inputs = tokenizer("Testing the Qwen3.5-4B hybrid attention pipeline.", return_tensors="pt").to(model.device)
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    if not torch.isfinite(loss).item():
        print(f"[X] Forward pass produced a non-finite loss ({loss.item()}) -- something is "
              f"already wrong before backward even runs.")
        sys.exit(1)
    print(f"[OK] Forward pass succeeded, loss={loss.item():.4f}")

    print("\n[~] Running one backward pass (this is the step that actually faulted the GPU "
          "last time on the 0.8B model)...")
    loss.backward()
    print("[OK] Backward pass succeeded -- no GPU fault on this single step.")

    print("\n" + "=" * 55)
    print("RESULT: one forward+backward step completed cleanly. This is a good sign, but per "
          "the note at the top of this file, isn't an absolute guarantee against a fault "
          "showing up later under sustained load -- watch the first several real training "
          "steps closely if you proceed to a full run on this model.")


if __name__ == "__main__":
    main()
