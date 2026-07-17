import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

BASE_MODEL_ID = "Qwen/Qwen2.5-Coder-3B-Instruct"
LORA_PATH = "./cubyz_ai_3b_v0.1"

print("Loading base 3B model...")
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

print("Loading and merging your custom Cubyz LoRA weights...")
model = PeftModel.from_pretrained(base_model, LORA_PATH)
tokenizer = AutoTokenizer.from_pretrained(LORA_PATH)

print("\n--- System Ready! ---")
print("Type your prompt below. Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")
    if user_input.strip().lower() == "exit":
        break

    # Format using the exact system prompt you trained it on
    prompt = (
        f"<|im_start|>system\nYou are an expert Zig software engineer specializing in the Cubyz voxel engine.<|im_end|>\n"
        f"<|im_start|>user\n{user_input}\nInput context:\n<|im_end|>\n"
        f"<|im_start|>assistant\n"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            eos_token_id=tokenizer.encode("<|im_end|>")[0]
        )

    # Decode only the newly generated tokens
    generated_tokens = outputs[0][inputs.input_ids.shape[-1]:]
    response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    print(f"\nAssistant: {response}\n" + "-"*40 + "\n")
