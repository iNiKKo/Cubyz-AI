"""
Validates the QLoRA training environment BEFORE committing to the real run -- the real base
model is a ~28GB download and the real training data requires the HF Hub pull in
prepare_training_data.py, so this checks the whole pipeline (ROCm PyTorch, bitsandbytes 4-bit
quantization, peft LoRA wrapping, a real forward+backward pass) against a tiny same-architecture
stand-in model first. If this fails, the full run will fail the same way, just after a much
longer wait.

The single most likely failure point, called out here specifically: bitsandbytes' ROCm support
is newer and less battle-tested than its CUDA support. A model "loading successfully" in 4-bit
isn't proof it's actually running on GPU -- bitsandbytes has been known to silently fall back to
a slower/incorrect path rather than hard-erroring, which is why this script checks parameter
device placement explicitly rather than just checking for import errors.

Run this after `pip install -r requirements.txt` (with the ROCm PyTorch build installed first,
per the note in that file) and before running train_qlora.py for real.
"""
import sys

# Small enough to download in seconds, but same architecture family as the real target
# (Qwen/Qwen2.5-Coder-7B-Instruct) -- so the LoRA target_modules list and the 4-bit quantization
# codepath are being exercised identically, just at a size that makes iteration fast.
PROXY_MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"

LORA_TARGET_MODULES = [
    "q_proj", "k_proj", "v_proj", "o_proj",
    "gate_proj", "up_proj", "down_proj",
]

results = []  # (stage_name, passed, detail)


def report(stage, passed, detail=""):
    results.append((stage, passed, detail))
    mark = "[OK]" if passed else "[X]"
    print(f"{mark} {stage}{': ' + detail if detail else ''}")


def main():
    print("=== Cubyz QLoRA environment smoke test ===\n")

    # --- Stage 1: torch + GPU visibility ---
    try:
        import torch
        report("torch import", True, f"version {torch.__version__}")
    except Exception as e:
        report("torch import", False, str(e))
        print("\n[X] Can't proceed without torch. Install the ROCm build from pytorch.org first.")
        sys.exit(1)

    is_rocm = getattr(torch.version, "hip", None) is not None
    is_cuda_build = getattr(torch.version, "cuda", None) is not None
    report("build type", True, "ROCm (HIP)" if is_rocm else ("CUDA" if is_cuda_build else "CPU-only (!!)"))
    if not is_rocm and not is_cuda_build:
        print("    -> This looks like a CPU-only torch build. Reinstall using the ROCm selector at "
              "pytorch.org/get-started/locally/ -- QLoRA training on CPU is not practical.")

    gpu_available = torch.cuda.is_available()
    report("GPU visible to torch", gpu_available)
    if not gpu_available:
        print("\n[X] No GPU visible. If you're on ROCm, check `rocm-smi` sees the card and that "
              "your user is in the `render`/`video` groups. Stopping here -- nothing past this "
              "point can meaningfully pass without a visible GPU.")
        sys.exit(1)

    device_name = torch.cuda.get_device_name(0)
    total_vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
    report("GPU detected", True, f"{device_name}, {total_vram_gb:.1f} GB")

    # --- Stage 2: bitsandbytes ---
    try:
        import bitsandbytes as bnb
        report("bitsandbytes import", True, f"version {bnb.__version__}")
    except Exception as e:
        report("bitsandbytes import", False, str(e))
        print("\n[X] bitsandbytes failed to import -- this is the most likely ROCm-specific "
              "failure point. Check you have a ROCm-compatible bitsandbytes build for your "
              "exact ROCm version (may require building from source).")
        sys.exit(1)

    # --- Stage 3: load a real (tiny) model in 4-bit and verify it actually landed on GPU ---
    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        print(f"\n[~] Downloading + loading {PROXY_MODEL_ID} in 4-bit (small, should be quick)...")
        tokenizer = AutoTokenizer.from_pretrained(PROXY_MODEL_ID)
        model = AutoModelForCausalLM.from_pretrained(
            PROXY_MODEL_ID,
            quantization_config=bnb_config,
            device_map="auto",
            dtype=torch.bfloat16,
        )
        report("4-bit model load", True)

        # The actual proof this is running on GPU, not silently on CPU: check where the
        # quantized weights actually live.
        first_param_device = next(model.parameters()).device
        on_gpu = first_param_device.type == "cuda"
        report("quantized weights on GPU", on_gpu, str(first_param_device))
        if not on_gpu:
            print("    -> Model loaded but landed on CPU. 4-bit quantization is likely not "
                  "using the GPU backend correctly -- training would silently run (extremely "
                  "slowly) on CPU instead of failing loudly.")
    except Exception as e:
        report("4-bit model load", False, str(e))
        print("\n[X] Can't proceed to LoRA/forward-pass checks without a loaded model.")
        sys.exit(1)

    # --- Stage 4: LoRA wrapping ---
    try:
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

        model = prepare_model_for_kbit_training(
            model, use_gradient_checkpointing=True,
            gradient_checkpointing_kwargs={"use_reentrant": False},
        )
        lora_config = LoraConfig(
            r=16, lora_alpha=32, lora_dropout=0.05,
            target_modules=LORA_TARGET_MODULES,
            bias="none", task_type="CAUSAL_LM",
        )
        model = get_peft_model(model, lora_config)
        trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
        total = sum(p.numel() for p in model.parameters())
        report("LoRA wrapping", True, f"{trainable:,}/{total:,} trainable ({100*trainable/total:.3f}%)")
    except Exception as e:
        report("LoRA wrapping", False, str(e))
        sys.exit(1)

    # --- Stage 5: real forward + backward pass, verify gradients only touch adapter weights ---
    try:
        model.train()
        inputs = tokenizer("Testing the Cubyz QLoRA training pipeline.", return_tensors="pt").to(model.device)
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
        loss_is_finite = torch.isfinite(loss).item()
        report("forward pass", loss_is_finite, f"loss={loss.item():.4f}")

        loss.backward()
        base_params_with_grad = [
            n for n, p in model.named_parameters()
            if p.requires_grad is False and p.grad is not None
        ]
        adapter_params_with_grad = [
            n for n, p in model.named_parameters()
            if p.requires_grad is True and p.grad is not None
        ]
        report("backward pass", len(adapter_params_with_grad) > 0,
               f"{len(adapter_params_with_grad)} adapter tensors got gradients")
        report("frozen base stayed frozen", len(base_params_with_grad) == 0,
               f"{len(base_params_with_grad)} frozen tensors unexpectedly got gradients" if base_params_with_grad else "")
    except Exception as e:
        report("forward/backward pass", False, str(e))

    # --- Stage 6: trl import (not running a full SFTTrainer here -- covered above) ---
    try:
        import trl
        report("trl import", True, f"version {trl.__version__}")
    except Exception as e:
        report("trl import", False, str(e))

    try:
        import datasets
        report("datasets import", True, f"version {datasets.__version__}")
    except Exception as e:
        report("datasets import", False, str(e))

    # --- Summary ---
    print("\n" + "=" * 55)
    failed = [r for r in results if not r[1]]
    if failed:
        print(f"RESULT: {len(failed)} check(s) failed -- fix these before running train_qlora.py:")
        for stage, _, detail in failed:
            print(f"  - {stage}: {detail}")
        sys.exit(1)
    else:
        print("RESULT: all checks passed. Environment looks ready for the real QLoRA run.")


if __name__ == "__main__":
    main()
