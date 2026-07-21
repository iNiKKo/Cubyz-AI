"""
QLoRA fine-tune of the Cubyz assistant model.

Switched from QLoRA (4-bit NF4) to plain LoRA in full bf16 on 2026-07-20 after dropping the base
model to Qwen3.5-0.8B for iteration speed (0.6B/0.8B are small enough that quantization was pure
overhead with no benefit). **Switched back to QLoRA on 2026-07-20** for Qwen3-4B-Instruct-2507
after diffing this file against the commit from the working 7B run (6e7ea68): the only real
config differences were quantization (4-bit vs plain bf16), optimizer (`paged_adamw_8bit` vs
`adamw_torch`), and batch size -- LoRA hyperparameters were identical in both. The 7B's fresh
(non-resumed) runs never had a spontaneous unrecoverable NaN collapse mid-training, only transient
huge-but-finite grad_norm spikes that recovered; this 4B run, in plain bf16, spontaneously
diverged to permanent NaN at epoch 1.685 with no resume involved. Since that's the one thing that
changed between "stable" and "spontaneously diverges," reverting to the more battle-tested 4-bit
QLoRA numerical path is the fix, not a further batch-size/checkpointing tweak. Accept the
quant/dequant speed cost in exchange for stability at this size -- this was always the plan (see
the note this replaced): "if this project ever swaps back to a 7B+ model, reintroduce
BitsAndBytesConfig/prepare_model_for_kbit_training/gradient checkpointing/paged_adamw_8bit
together -- they're a matched set for VRAM-constrained training, not independent choices."

Separately, unresolved: resuming from ANY checkpoint on this stack causes near-instant
catastrophic divergence, reproduced now on both `paged_adamw_8bit` (7B) and `adamw_torch` (4B) --
confirms it's not optimizer-specific. Root cause still unknown; the only safe practice for now is
never interrupting a run, since resuming is not a safety net here.

Why LoRA at all (not a full fine-tune): the previous attempt at this project full-fine-tuned
a small model with no general-data mixing and "lobotomized" it -- catastrophic forgetting of
general capability. LoRA only ever updates a small number of injected adapter weights (the
frozen base never changes), which is inherently far less prone to overwriting general knowledge,
and is combined here with the general-data mixing from prepare_training_data.py as a second,
independent layer of protection against the same failure mode. This protection is unrelated to
4-bit vs bf16 -- dropping QLoRA's quantization above does not weaken it.

Run `prepare_training_data.py` first to produce data/train.jsonl and data/val.jsonl.
"""
import argparse
import os

# Must be set before torch initializes its CUDA/HIP allocator -- reduces the fragmentation
# PyTorch's own OOM error message flagged (2.76GB was "reserved but unallocated" on a 15.92GB
# card, i.e. wasted to fragmentation rather than actually available).
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

# Tried PYTORCH_TUNABLEOP_ENABLED=1 (RDNA4 GEMM autotuning, see rocm.blogs.amd.com's TunableOp
# writeup) on 2026-07-20 -- deadlocked partway through its kernel search on this exact
# torch-2.14.0.dev+rocm7.2 nightly (GPU busy% dropped to ~3%, tunableop_results0.csv stopped
# growing, no progress for 3+ minutes). Reverted rather than chase a bleeding-edge-nightly rough
# edge for a modest, unconfirmed speed gain -- not worth risking a multi-hour run over.

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

# Dropped to Qwen3-0.6B (2026-07-20) purely for iteration speed -- the 7B QLoRA run was taking
# ~4hrs/attempt on this card, too slow to iterate on training-data/hyperparameter changes. Tried
# Qwen3.5-0.8B first but it hard-crashed the GPU driver on step 1 ("Memory access fault... Page
# not present", core dump, process aborted) -- Qwen3.5's hybrid linear-attention architecture
# needs flash-linear-attention/causal-conv1d kernels that aren't installed, and the torch
# fallback path for missing kernels is what faulted. Reverted to plain Qwen3-0.6B (standard dense
# transformer, no such dependency) to unblock iteration -- but measured against the 7B on the
# same 152-question benchmark (see finetune/training/compare_models.py), 0.6B only reached 44.6%
# of the 7B's accuracy (16.4% vs 36.8%), concentrated almost entirely in domain fact recall. That
# capacity loss is real, not marginal, so raising the size back up to test whether a 3-4B model
# recovers more of it without the 7B's training-time cost.
#
# Tried Qwen3.5-4B (2026-07-20) -- a standalone smoke test (smoke_test_qwen35.py: one real
# forward+backward pass) survived cleanly, but that was insufficient: the real training run
# hard-crashed the GPU driver on step 1 with the exact same fault signature as the earlier
# Qwen3.5-0.8B crash ("Memory access fault... Page not present", core dump, abort), first under
# non-reentrant gradient checkpointing (which failed differently -- a Python-level "does not
# require grad" error, worked around with model.enable_input_require_grads()) and then again
# under reentrant checkpointing (the actual GPU fault). Two independent crashes from the same
# architecture family (0.8B and 4B), under two different checkpointing modes, is strong evidence
# this is a fundamental incompatibility between Qwen3.5's hybrid-attention torch fallback and this
# ROCm/RDNA4 setup under real backward-pass load -- not a config problem to keep patching.
#
# Switched to Qwen3-4B-Instruct-2507 instead -- same size class, but standard dense-transformer
# attention (same architecture family as the Qwen3-0.6B that already trained cleanly), no
# flash-linear-attention/causal-conv1d dependency at all. This was always the safer fallback;
# worth it now that Qwen3.5 has cost two full GPU-driver crashes this session.
MODEL_ID = "Qwen/Qwen3-4B-Instruct-2507"

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
# Was raised from 2 to 3 epochs specifically because narrow, rarely-repeated facts (exact
# keybindings, exact numbers, exact names) didn't reliably stick at 2 epochs. Dropped BACK to 2
# for Prototype 7 (2026-07-20): that justification no longer applies once assemble_sft_dataset.py
# cut the domain data to reviews-only (fact Q&A removed entirely, RAG's job now) -- and 3 epochs
# on the much smaller resulting set (1,436 domain examples, down from ~3,850) risks overfitting to
# the exact phrasing of this specific set of PR/issue discussions rather than generalizing the
# judgment pattern, which is the opposite of what a purely behavioral fine-tune needs. Judgment/
# reasoning patterns were already reinforcing reliably at 2 epochs even in earlier rounds.
LEARNING_RATE = 1e-4
NUM_EPOCHS = 2
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
# Tried 16/1 after dropping to Qwen3.5-0.8B in plain bf16 -- VRAM headroom supported it fine, but
# Nick saw desktop-level display artifacting during that run on this same RX9070 that already had
# a real RDNA4 MES-firmware hang earlier this session on this nightly ROCm build. This card/driver
# combo is known flaky under sustained load, so dialed back to 8/2 (same effective batch 16, half
# the peak per-step compute/VRAM pressure) rather than chasing max throughput on unstable hardware.
#
# Dropped to 1/16 for Qwen3.5-4B in plain bf16 (even 2/8 OOM'd there), then that whole plain-bf16
# path got reverted in favor of 4-bit QLoRA (see module docstring -- plain bf16 is what's
# suspected in the spontaneous mid-training NaN, not batch size). Restored to 2/8 to match the
# proven 7B recipe exactly, now that 4-bit quantization frees the VRAM plain bf16 didn't have.
PER_DEVICE_BATCH_SIZE = 2
GRADIENT_ACCUMULATION_STEPS = 8  # effective batch size 16 (unchanged from before)


def format_example(example: dict, tokenizer) -> str:
    # enable_thinking=False: Qwen3's chat template supports an optional reasoning ("thinking")
    # mode that wraps generations in <think>...</think> blocks -- irrelevant/unwanted for this
    # direct instruction-following SFT data, so it's explicitly disabled. Non-Qwen3 templates
    # simply ignore this kwarg, so this stays harmless if the model is swapped again later.
    return tokenizer.apply_chat_template(
        example["messages"], tokenize=False, add_generation_prompt=False, enable_thinking=False
    )


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
    # Also calls the equivalent of enable_input_require_grads() internally -- required for
    # gradient checkpointing on a frozen base model, otherwise backward fails with "element 0 of
    # tensors does not require grad and does not have a grad_fn" once the checkpointed segment's
    # input tensor loses its grad_fn at a frozen (non-LoRA) parameter.
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
        # Qwen3-4B-Instruct-2507 reproducibly diverged to NaN on step 1 with trl's default
        # loss_type="chunked_nll" (a memory-saving path that chunks the lm_head projection and
        # does its own internal torch.utils.checkpoint call, nested inside this script's own
        # model-level gradient checkpointing). Isolated via diagnose_length_sensitivity.py: the
        # exact same LoRA+checkpointing+backward combination is completely clean when computing
        # loss the plain way (trl's "nll" option) instead of the chunked path -- confirms the
        # chunked-CE/checkpointing nesting specifically, not length, not checkpointing alone, not
        # the model/tokenizer. trl's own docs note chunked_nll has known PEFT interaction
        # caveats (e.g. unsupported if lm_head itself is PEFT-wrapped), consistent with this.
        loss_type="nll",
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
        # Tried turning this off (2026-07-20) to chase more speed now that the Qwen3.5 crash was
        # root-caused to its kernel fallback rather than memory pressure -- immediately OOM'd
        # instead ("Tried to allocate 40.00 MiB... 15.08 GiB already allocated"). Root cause isn't
        # model size, it's vocab size: Qwen3's 151,936-token vocab makes the logits tensor alone
        # ~5GB at batch 8/seq 2048 in bf16, and without checkpointing every layer's activations
        # stack on top of that across the full backward pass. Reverted -- this card doesn't have
        # margin to drop checkpointing at this batch size regardless of how small the model is.
        # The working config (this: checkpointing on, batch 8/2) already runs at ~1.37s/it
        # (~30min total) -- that's the number to keep, not push further.
        # Re-enabled (2026-07-20) -- disabling this to test the double-checkpointing theory just
        # OOM'd instead ("Tried to allocate 1.45 GiB... 146.00 MiB free"), so that experiment was
        # inconclusive, not a disproof. See diagnose_length_sensitivity.py for the actual isolated
        # test of whether a long (~2048 token) real sequence triggers the NaN under this exact
        # checkpointing config before assuming this setting is safe again.
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        learning_rate=LEARNING_RATE,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        optim="paged_adamw_8bit",  # memory-efficient optimizer, standard pairing with QLoRA
        bf16=True,
        logging_steps=10,
        eval_strategy="steps",
        # Recalibrated from 100 for Prototype 7 (2026-07-20): the reviews-only dataset is much
        # smaller (~1,436 domain examples vs. ~3,850 before), so at 2 epochs the whole run is only
        # ~340 steps -- eval_steps=100 would give just 3 eval checkpoints, too coarse to catch
        # overfitting onset early on a set this size. 25 keeps roughly the same ~13-14 eval
        # checkpoints across the run as the prior (100-step, ~1,371-step) round had.
        eval_steps=25,
        save_strategy="steps",
        save_steps=25,
        save_total_limit=3,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        report_to="none",
        # CPU-side only -- doesn't touch VRAM, so no OOM risk. Default dataloader_num_workers=0
        # means the main process does its own tokenized-batch collation serially, in between GPU
        # steps, instead of overlapping it with GPU compute; a few worker processes prefetch the
        # next batches on CPU cores while the GPU is still busy with the current one. pin_memory
        # speeds up the CPU->GPU transfer for whatever's prefetched. On a multi-core CPU sitting
        # mostly idle during training (the actual bottleneck is the GPU compute itself), this is
        # free throughput.
        dataloader_num_workers=min(8, (os.cpu_count() or 4)),
        dataloader_pin_memory=True,
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
