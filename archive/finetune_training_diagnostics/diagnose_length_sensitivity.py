"""
Isolated test: does a genuinely long (near MAX_SEQ_LENGTH) real training example trigger NaN
under the EXACT training config (LoRA + gradient checkpointing, use_reentrant=False) that a fresh
Qwen3-4B-Instruct-2507 run diverged on?

Why this exists: the earlier diagnose_base_loss.py check used the first (short) training example
and only did a plain forward pass (no LoRA, no checkpointing) -- it came back completely clean,
which ruled out a model-loading/dtype problem but didn't test the actual combination that
diverged. A later attempt to disable gradient checkpointing to isolate a suspected double-
checkpointing interaction (trl's SFTTrainer chunks cross-entropy with its own internal
torch.utils.checkpoint call) just OOM'd instead, so that theory is still untested, not disproven.
This script tests the real combination directly: LoRA + checkpointing + backward, on the longest
real example in the training set, to check for a length-dependent bf16 numerical issue.
"""
import json

import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

from train_qlora import (
    LORA_ALPHA, LORA_DROPOUT, LORA_R, LORA_TARGET_MODULES, MAX_SEQ_LENGTH, MODEL_ID, TRAIN_FILE,
)

print(f"[~] Loading tokenizer: {MODEL_ID}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print("[~] Scanning train.jsonl for the longest example (by token count)...")
longest_text, longest_len = None, 0
with open(TRAIN_FILE) as f:
    for line in f:
        ex = json.loads(line)
        text = tokenizer.apply_chat_template(ex["messages"], tokenize=False, add_generation_prompt=False)
        n = len(tokenizer(text, truncation=True, max_length=MAX_SEQ_LENGTH)["input_ids"])
        if n > longest_len:
            longest_len, longest_text = n, text
print(f"[OK] Longest example: {longest_len} tokens (MAX_SEQ_LENGTH={MAX_SEQ_LENGTH})")

print(f"\n[~] Loading base model in bf16: {MODEL_ID}")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, device_map={"": 0}, dtype=torch.bfloat16, attn_implementation="sdpa",
)
model.enable_input_require_grads()

lora_config = LoraConfig(
    r=LORA_R, lora_alpha=LORA_ALPHA, lora_dropout=LORA_DROPOUT,
    target_modules=LORA_TARGET_MODULES, bias="none", task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)
model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
model.train()
print("[OK] LoRA + gradient checkpointing (use_reentrant=False) enabled -- matches train_qlora.py exactly.")

inputs = tokenizer(
    longest_text, return_tensors="pt", truncation=True, max_length=MAX_SEQ_LENGTH,
).to(model.device)

print(f"\n[~] Running forward+backward on the {longest_len}-token example...")
outputs = model(**inputs, labels=inputs["input_ids"])
loss = outputs.loss
print(f"[~] Loss: {loss.item()}  |  finite? {torch.isfinite(loss).item()}")

loss.backward()
grad_norms = [p.grad.norm().item() for p in model.parameters() if p.requires_grad and p.grad is not None]
any_nan = any(torch.isnan(torch.tensor(g)) for g in grad_norms)
print(f"[~] {len(grad_norms)} adapter tensors got gradients; any NaN grad norm? {any_nan}")
if grad_norms:
    print(f"[~] grad norm range: min={min(grad_norms):.4f}, max={max(grad_norms):.4f}")

print("\n" + "=" * 55)
if torch.isfinite(loss).item() and not any_nan:
    print("RESULT: clean on the longest real example -- length alone doesn't explain the NaN.")
    print("Next suspect: the double-checkpointing interaction with trl's SFTTrainer specifically")
    print("(this script uses a plain model.backward(), not trl's chunked-CE path).")
else:
    print("RESULT: reproduced the NaN in isolation on a long sequence -- this IS a length-")
    print("dependent numerical issue with LoRA+checkpointing+bf16 on this model/hardware.")
