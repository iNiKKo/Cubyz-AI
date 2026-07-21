"""
Isolated check: does the FROZEN base model alone (no LoRA, no gradient checkpointing, no
chunked-cross-entropy training loop) already produce an absurd loss on real training data?

Why this exists: a fresh Qwen3-4B-Instruct-2507 QLoRA run showed loss=20,980 on its very first
logged step, then permanently collapsed to loss=0/grad_norm=nan/entropy=nan and never recovered
-- reproducible across a fresh restart, not a one-off. Since LoRA adapters start at ~zero effect,
step 1's loss should just reflect the frozen base model's own coherence on this data (should look
like ~2-3, based on every other model tried this session), not 20,980. This isolates whether the
problem is already present in the plain base model (loading/dtype/tokenizer mismatch) before any
LoRA/checkpointing/chunked-ce interaction gets involved.
"""
import json

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from train_qlora import MODEL_ID, TRAIN_FILE

print(f"[~] Loading base model (no LoRA, no quantization): {MODEL_ID}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map={"": 0},
    dtype=torch.bfloat16,
    attn_implementation="sdpa",
)
model.eval()

with open(TRAIN_FILE) as f:
    example = json.loads(f.readline())

prompt = tokenizer.apply_chat_template(example["messages"], tokenize=False, add_generation_prompt=False)
print(f"\n[~] Example (first training row):\n{prompt[:300]}...\n")

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model(**inputs, labels=inputs["input_ids"])

loss = outputs.loss
print(f"[~] Loss on this example (bf16, frozen, eval mode): {loss.item()}")
print(f"[~] Loss finite? {torch.isfinite(loss).item()}")
print(f"[~] Logits stats: min={outputs.logits.min().item():.2f}, max={outputs.logits.max().item():.2f}, "
      f"any nan? {torch.isnan(outputs.logits).any().item()}, any inf? {torch.isinf(outputs.logits).any().item()}")

# Also try fp32 to see if this is a bf16-specific numerical issue on this ROCm build.
print("\n[~] Reloading in fp32 for comparison...")
model_fp32 = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, device_map={"": 0}, dtype=torch.float32, attn_implementation="sdpa",
)
model_fp32.eval()
with torch.no_grad():
    outputs_fp32 = model_fp32(**inputs, labels=inputs["input_ids"])
print(f"[~] Loss in fp32: {outputs_fp32.loss.item()}")
print(f"[~] Loss finite (fp32)? {torch.isfinite(outputs_fp32.loss).item()}")
