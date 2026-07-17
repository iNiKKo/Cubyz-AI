import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer, SFTConfig

# Prevent VRAM fragmentation crashes on ROCm/AMD
os.environ["PYTORCH_HIP_ALLOC_CONF"] = "expandable_segments:True"

# 1. Setup paths and configuration
MODEL_ID = "Qwen/Qwen2.5-Coder-3B-Instruct"
DATASET_FILE = "cubyz_training.jsonl"
OUTPUT_DIR = "./cubyz_ai_3b_v0.1"

print("Loading dataset...")
dataset = load_dataset("json", data_files=DATASET_FILE, split="train")

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token

print("Loading 3B model in native BF16 (No quantization, perfectly stable)...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,   # Pure 16-bit
    device_map="auto",
    attn_implementation="sdpa"    # Native PyTorch attention
)

# CRUCIAL: We do NOT run model.gradient_checkpointing_enable() here to prevent ROCm page faults!

# 2. Configure LoRA Parameters (Optimized to keep VRAM low without checkpointing)
lora_config = LoraConfig(
    r=8,                          # Reduced rank from 16 to 8 to save massive memory
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"], # Target key layers only (saves ~4GB VRAM)
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
print("LoRA adapter weights attached successfully.")
model.print_trainable_parameters()

# 3. Define the Prompt Formatting Function
def format_prompts(batch):
    formatted_texts = []
    for i in range(len(batch['instruction'])):
        text = (
            f"<|im_start|>system\nYou are an expert Zig software engineer specializing in the Cubyz voxel engine.<|im_end|>\n"
            f"<|im_start|>user\n{batch['instruction'][i]}\n"
            f"Input context:\n{batch['input'][i]}<|im_end|>\n"
            f"<|im_start|>assistant\n{batch['output'][i]}<|im_end|>"
        )
        formatted_texts.append(text)
    return {"text": formatted_texts}

dataset = dataset.map(format_prompts, batched=True)

# 4. Define Training and SFT Arguments
training_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    dataset_text_field="text",
    max_length=1024,
    per_device_train_batch_size=1,   # Keep batch size at 1 to prevent VRAM spikes
    gradient_accumulation_steps=16,  # 1 x 16 = effective batch size of 16
    learning_rate=2e-4,
    logging_steps=10,
    num_train_epochs=3,
    save_strategy="epoch",
    bf16=True,
    optim="adamw_torch",
    report_to="none",
    gradient_checkpointing=False     # FORCE OFF to prevent AMD driver page faults
)

# 5. Initialize SFTTrainer and Train
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    processing_class=tokenizer,
    args=training_args,
)

print("\nStarting 3B Fine-Tuning Execution...")
trainer.train()

print(f"\nTraining Complete! Saving 3B LoRA adapter weights to: {OUTPUT_DIR}")
trainer.model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
