import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

BASE_MODEL = "Qwen/Qwen2.5-Coder-3B-Instruct"
LORA_PATH = "./cubyz_ai_3b_v0.1"
MERGED_OUTPUT = "./cubyz_ai_3b_merged"

print("Loading base model...")
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.bfloat16,
    device_map="cpu" # CPU is safest to avoid any VRAM hiccups during merge
)

print("Loading adapter and merging...")
model = PeftModel.from_pretrained(base_model, LORA_PATH)
model = model.merge_and_unload() # Fuses the weights permanently

print("Saving merged model...")
model.save_pretrained(MERGED_OUTPUT)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
tokenizer.save_pretrained(MERGED_OUTPUT)

print(f"Done! Merged HuggingFace format saved to {MERGED_OUTPUT}")
