"""
QLoRA fine-tune of the Cubyz assistant model.

Why QLoRA specifically (not plain LoRA): even at 7B parameters, bf16 (what plain LoRA trains
against, since only the adapters are updated but the frozen base still loads at full precision)
is ~14GB of weights alone -- too tight on a 16GB card once activations/optimizer state are added.
QLoRA quantizes the frozen base to 4-bit (NF4), dropping it to ~3.7GB, leaving generous headroom
within 16GB. This is a hardware constraint, not a preference.

Note on model size: this was originally written for Qwen2.5-Coder-14B-Instruct, which QLoRA'd
down to ~7.4GB of weights but still hit repeated CUDA OOMs during real training on this 16GB
card (~12.4GB allocated at just 2048 tokens -- more than the weights + adapters should need,
likely LoRA's extra activation overhead on the large MLP layers, though never fully root-caused).
Dropped to the 7B variant for a comfortable memory margin instead of continuing to fight it.

Why LoRA/QLoRA at all (not a full fine-tune): the previous attempt at this project full-fine-tuned
a small model with no general-data mixing and "lobotomized" it -- catastrophic forgetting of
general capability. QLoRA only ever updates a small number of injected adapter weights (the
frozen base never changes), which is inherently far less prone to overwriting general knowledge,
and is combined here with the general-data mixing from prepare_training_data.py as a second,
independent layer of protection against the same failure mode.

Run `prepare_training_data.py` first to produce data/train.jsonl and data/val.jsonl.
"""
import argparse
import os

# Must be set before torch initializes its CUDA/HIP allocator -- reduces the fragmentation
# PyTorch's own OOM error message flagged (2.76GB was "reserved but unallocated" on a 15.92GB
# card, i.e. wasted to fragmentation rather than actually available).
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer

# Anchor paths to the repo root (three levels up: training/ -> finetune/ -> repo root) rather
# than the process's cwd -- these scripts get run from both the repo root and from inside
# finetune/training/ depending on habit, and a bare relative path silently resolves differently
# (and wrongly) depending on which.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Switched from Qwen2.5-Coder-14B-Instruct to the 7B variant after repeated CUDA OOMs during
# real training on a 16GB card (see note above) -- same family/tokenizer/architecture, just
# smaller. Requires its own download (~15GB) the first time this runs; the 14B safetensors
# downloaded earlier are not reused.
MODEL_ID = "Qwen/Qwen2.5-Coder-7B-Instruct"

TRAIN_FILE = os.path.join(REPO_ROOT, "finetune/training/data/train.jsonl")
VAL_FILE = os.path.join(REPO_ROOT, "finetune/training/data/val.jsonl")
OUTPUT_DIR = os.path.join(REPO_ROOT, "finetune/training/output/cubyz-qlora")

# 4096 measured as massive overkill against the actual mixed training data: p99 is ~1245
# tokens and only 17/6334 examples exceed 2048, so 2048 truncates almost nothing while roughly
# halving worst-case activation memory -- the direct cause of the OOM at 4096 on a 16GB card.
MAX_SEQ_LENGTH = 2048

# Rank/alpha kept moderate rather than aggressive -- this is ~5-8k mixed examples, not millions;
# a higher rank risks memorizing training examples rather than generalizing the voice/judgment,
# which is the opposite of what a small, high-quality dataset like this needs.
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
# Standard Qwen2-architecture attention + MLP projections. Covering both (not just attention)
# matters here specifically because a meaningful chunk of what we're teaching is factual
# recall (docs/codebase) as well as behavioral judgment (reviews) -- MLP layers are where a
# transformer stores more of that factual association.
LORA_TARGET_MODULES = [
    "q_proj", "k_proj", "v_proj", "o_proj",
    "gate_proj", "up_proj", "down_proj",
]

# Conservative learning rate -- this project's whole premise is "don't destroy the LLM," and an
# overly aggressive LR is one of the most direct ways a fine-tune degrades general capability
# even with LoRA/QLoRA's inherent protection.
#
# Raised from 2 to 3 epochs after the first trained adapter's test results showed narrow, rarely-
# repeated facts (exact keybindings, exact numbers, exact names) didn't reliably stick, unlike
# judgment/reasoning patterns that got reinforced across hundreds of similar review pairs.
# Combined with generate_core_facts_pairs.py (dense, multiply-phrased coverage of exactly the
# facts that failed) and dropping the general:domain ratio to 1.0 in prepare_training_data.py,
# this meaningfully increases how many times each specific fact is actually seen during training.
LEARNING_RATE = 1e-4
NUM_EPOCHS = 3
# Raised from 1 to 2 after switching to the 7B model freed up substantial VRAM headroom (~3.7GB
# weights vs the 14B model's ~7.4GB) -- gradient accumulation dropped from 16 to 8 in lockstep so
# the EFFECTIVE batch size (16) and therefore the learning rate schedule / training dynamics are
# unchanged. This is a pure throughput change: processing 2 examples per GPU pass instead of 1
# sequential pass at a time cuts wall-clock training time meaningfully, since a training step was
# previously 16 sequential single-example forward/backward passes, each paying the same fixed
# per-call overhead (4-bit dequantization, kernel launch) for very little actual work. Kept at 2
# rather than pushing to 4 -- a worst-case batch could still randomly pair several near-max-length
# (2048 token) examples together, and this card has OOM'd on tighter
# margins than that before. If 2 comfortably fits with headroom to spare, 4 is worth trying next;
# if this still OOMs, drop back to 1/16 (the previously working combination).
PER_DEVICE_BATCH_SIZE = 2
GRADIENT_ACCUMULATION_STEPS = 8  # effective batch size 16 (unchanged from before)


def format_example(example: dict, tokenizer) -> str:
    return tokenizer.apply_chat_template(example["messages"], tokenize=False, add_generation_prompt=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", default=MODEL_ID)
    parser.add_argument("--resume-from-checkpoint", default=None)
    args = parser.parse_args()

    if not os.path.exists(TRAIN_FILE):
        raise SystemExit(f"[X] {TRAIN_FILE} not found -- run prepare_training_data.py first.")

    print(f"[~] Loading tokenizer + 4-bit base model: {args.model_id}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        args.model_id,
        quantization_config=bnb_config,
        # Forced onto GPU 0 explicitly rather than "auto" -- a model this size in real 4-bit NF4
        # comfortably fits inside 16GB alone, so there's no legitimate reason for any of it to
        # land on CPU. "auto" asks accelerate to plan device placement using a memory estimate
        # that can be based on the pre-quantization size, which can wrongly decide to offload
        # chunks to system RAM -- that's what caused an OOM kill on a 32GB-RAM machine earlier
        # in this project (with the original, larger model choice).
        device_map={"": 0},
        dtype=torch.bfloat16,
        # Explicit rather than relying on transformers' auto-selection -- SDPA is PyTorch's own
        # built-in optimized attention (no extra package, works on ROCm), and being explicit
        # guards against silently falling back to the much slower "eager" implementation, which
        # some quantized-model loading paths have defaulted to in the past.
        attn_implementation="sdpa",
    )
    model = prepare_model_for_kbit_training(
        model, use_gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
    )

    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=LORA_TARGET_MODULES,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    print("[~] Loading train/val datasets")
    dataset = load_dataset("json", data_files={"train": TRAIN_FILE, "validation": VAL_FILE})

    sft_config = SFTConfig(
        output_dir=OUTPUT_DIR,
        max_length=MAX_SEQ_LENGTH,  # trl 1.8+ renamed this from max_seq_length
        packing=False,  # keep examples separate rather than concatenated -- avoids cross-example
                        # contamination between unrelated Cubyz/general instructions in one window
        # Note: tried group_by_length=True here (batches similarly-lengthed examples together to
        # cut padding waste) but this trl version's SFTConfig doesn't accept it -- same kind of
        # API drift as max_seq_length -> max_length. Dropped rather than guess another field name
        # and cost another failed run; the batch-size increase below is the main speed lever anyway.
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=PER_DEVICE_BATCH_SIZE,
        per_device_eval_batch_size=PER_DEVICE_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        learning_rate=LEARNING_RATE,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        optim="paged_adamw_8bit",  # memory-efficient optimizer, standard pairing with QLoRA
        bf16=True,
        logging_steps=10,
        eval_strategy="steps",
        eval_steps=100,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=3,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        report_to="none",
    )

    trainer = SFTTrainer(
        model=model,
        args=sft_config,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        processing_class=tokenizer,
        formatting_func=lambda ex: format_example(ex, tokenizer),
    )

    print("[~] Starting training")
    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)

    final_dir = os.path.join(OUTPUT_DIR, "final_adapter")
    trainer.save_model(final_dir)
    print(f"[OK] Training complete. LoRA adapter saved to {final_dir}")
    print("[~] Run merge_adapter.py next to produce a standalone merged model for inference/export.")


if __name__ == "__main__":
    main()
