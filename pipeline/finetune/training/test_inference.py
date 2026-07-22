"""
Quick qualitative check of the freshly-trained adapter, run BEFORE merge_adapter.py -- loads
the 4-bit base + LoRA adapter directly (same as training, minus the training-only setup) so
there's no need to wait for a full merge just to get a first read on quality.

Why this matters more than the loss/accuracy numbers: eval_loss and mean_token_accuracy tell
you the model got better at predicting the training distribution, but say nothing about the one
failure mode this whole project was built to avoid -- catastrophic forgetting of general
capability (the "lobotomy" from the prior full-fine-tune attempt). That can only be seen by
actually talking to the model. This script asks a mix of:
  - Cubyz-specific questions pulled from the training domains (docs/codebase/reviews) --
    checks the domain knowledge actually landed.
  - Completely unrelated general questions (Python, general knowledge, math) -- checks general
    capability wasn't damaged.

Read every response yourself. There's no automated pass/fail here -- judging "is this actually
good and not degraded" is exactly the kind of thing that needs a human, not a script.
"""
import datetime
import os
import sys

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from train_qlora import MODEL_ID, OUTPUT_DIR

ADAPTER_DIR = f"{OUTPUT_DIR}/final_adapter"
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "standalone_test_results")


class Tee:
    """Mirrors everything written to stdout into a log file, so the transcript survives past the
    terminal scrollback without needing a manual `| tee` redirect."""

    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)

    def flush(self):
        for stream in self.streams:
            stream.flush()

SYSTEM_PROMPT = (
    "You are the Cubyz Assistant, a technical expert on Cubyz, an open-source voxel sandbox "
    "game written in Zig. Answer directly and precisely, in the voice of a developer who "
    "already knows this codebase -- never mention retrieved context or documentation. Be "
    "concise for factual questions, thorough for mechanics and debugging."
)

# (question, known-correct answer per the source data this project already verified) -- printed
# alongside the model's own answer so grading doesn't rely on remembering the ground truth.
CUBYZ_QUESTIONS = [
    ("What key moves the player forward in Cubyz?",
     "W"),
    ("How does Cubyz store its player position data over the network?",
     "The playerPosition struct sends/receives updates, sent no more than once every 50ms"),
    ("What happens if I place a block ID that doesn't exist in an addon?",
     "Engine doesn't crash -- logs \"Couldn't find block {id}. Replacing it with air...\" and substitutes air"),
    ("Who currently maintains Cubyz, and when was it originally created?",
     "Created Aug 22 2018 by zenith391 and ZaUserA; currently maintained by IntegratedQuantum"),
    ("In a Cubyz code review, what's the difference between when a change should get a debugging-style response vs a design-review response?",
     "Debugging/diagnosis = a bug or 'why doesn't this work' issue; design-review = a design/style/architecture choice, not a bug"),
    ("Which key toggles fullscreen mode in Cubyz?",
     "F11"),
    ("How do you access the creative inventory in Cubyz?",
     "C"),
    ("What is the default multiplayer server port in Cubyz?",
     "47649"),
    ("How many hearts of health does the player start with, and what's the total HP?",
     "8 hearts, 16 total health"),
    ("Can the player heal in Cubyz right now?",
     "No -- there is currently no way to regain health other than dying"),
    ("What tool is used to damage/mine soil blocks in Cubyz?",
     "Shovers (shovels)"),
    ("How far can the Cubyz world extend on each axis?",
     "2 billion blocks on each axis"),
    ("What was Cubyz originally called before its current name?",
     "\"Cubz\""),
    ("Is Cubyz available on Mac? Why or why not?",
     "No -- Mac is not supported because it lacks OpenGL 4.3"),
    ("What does the checkResult function do for Vulkan results in Cubyz's renderer?",
     "Logs a Vulkan error (unknown error code, or the specific error tag name) via std.log.err"),
    ("What is utils.NeverFailingAllocator in Cubyz?",
     "An allocator interface that cannot return error.OutOfMemory"),
    ("How does Cubyz's BinaryWriter manage its buffer as data is written?",
     "A dynamically growing buffer"),
    ("Why might a Cubyz reviewer prefer std.StringHashMap's getOrPut over a separate contains-check plus insert?",
     "getOrPut atomically retrieves-or-inserts in one operation instead of two lookups, reducing redundant memory accesses and complexity"),
    ("What's the default value for an item's food field in Cubyz if I don't set it?",
     "0"),
    ("Why might a biome's custom sky color not show up in-game even though I set it in the Addon Creator?",
     "Format mismatch: the website exports skyColor/fogColor as a 3-component float vector, but the engine reads those fields as a packed u32 integer"),

    # --- Remaining movement/interaction keybindings ---
    ("What key moves the player backward in Cubyz?", "S"),
    ("Which key strafes the player left in Cubyz?", "A"),
    ("Which key strafes the player right in Cubyz?", "D"),
    ("What key makes the player sprint in Cubyz?", "Left control"),
    ("What key makes the player jump in Cubyz?", "Space"),
    ("How do you crouch in Cubyz?", "Left shift"),
    ("What key toggles flying in Cubyz?", "F"),
    ("What key toggles ghost mode in Cubyz?", "G"),
    ("What key activates hyperspeed in Cubyz?", "H"),
    ("What button places a block in Cubyz?", "Right mouse button"),
    ("What button breaks a block in Cubyz?", "Left mouse button"),
    ("How do you pick a block (select it into your hotbar) in Cubyz?", "Middle mouse button"),
    ("What key drops an item in Cubyz?", "Q"),
    ("What key takes a background image/screenshot in Cubyz?", "Print Screen"),
    ("What key opens the regular (non-creative) inventory in Cubyz?", "E"),
    ("How do you open chat in Cubyz?", "T"),
    ("What key or character opens the command line in Cubyz?", "/"),
    ("What key hides the menu in Cubyz?", "F1"),
    ("What key hides the display item in Cubyz?", "F2"),
    ("What key toggles the debug overlay in Cubyz?", "F3"),
    ("What key toggles the performance overlay in Cubyz?", "F4"),
    ("What key toggles the GPU overlay in Cubyz?", "F5"),
    ("What key toggles the network overlay in Cubyz?", "F6"),
    ("What key toggles the advanced network overlay in Cubyz?", "F7"),
    ("What key selects hotbar slot 10 in Cubyz?", "0"),
    ("What key selects hotbar slot 11 in Cubyz?", "- (minus)"),
    ("What key selects hotbar slot 12 in Cubyz?", "= (equals)"),

    # --- History ---
    ("When was the project renamed from Cubz to Cubyz?", "March 17, 2019, suggested by zenith391"),
    ("Why was Cubyz rewritten from Java to Zig?", "Java's garbage collector caused freeze-inducing lag spikes at the memory limit; Zig's cross-compilation support was also a major draw"),
    ("When was Cubyz version 0.0.0 released?", "October 5, 2025"),
    ("What language was Cubyz originally written in before the Zig rewrite?", "Java"),
    ("What alternative languages did the Cubyz maintainer consider before choosing Zig for the rewrite?", "C++20 and Rust"),

    # --- Gameplay mechanics ---
    ("What does the energy/stomach bar do in Cubyz right now?", "Nothing -- it's purely cosmetic, there's currently no way to gain or lose energy"),
    ("How many movement modes does the player have in Cubyz?", "Three: walking, sprinting, and crouching"),
    ("How high can the player jump in Cubyz?", "Enough to cross one whole block"),
    ("How many hotbar slots does Cubyz have by default?", "12"),
    ("How many items can a single inventory or hotbar slot stack in Cubyz?", "120"),
    ("How many slots does the main inventory have in Cubyz?", "20"),
    ("What tool is used to mine stone, metal, and gem blocks in Cubyz?", "Pickaxe"),
    ("What tool is used to mine wooden blocks in Cubyz?", "Axe"),
    ("What tool is used to harvest plants, leaves, and cloth in Cubyz?", "Sickle -- also the only way to actually collect plants/leaves, not possible bare-handed"),
    ("What happens if you use the wrong tool type on a block in Cubyz?", "It deals the same damage as bare hands -- no bonus, no penalty"),

    # --- Install/system ---
    ("What operating systems does Cubyz support?", "Windows and Linux"),
    ("What OpenGL version does the Cubyz installation page list as the GPU requirement?", "OpenGL 4.6 hardware support"),

    # --- Networking/permissions ---
    ("What command grants a player full admin permissions in Cubyz?", "/perm add whitelist @<playerIndex> /"),
    ("What command grants a player access to just the /spawn command in Cubyz?", "/perm add whitelist @<playerIndex> /command/spawn"),
    ("What network protocol does Cubyz's server use for port forwarding?", "UDP"),
    ("In Cubyz's permission system, if a path is both whitelisted and blacklisted, which wins?", "The blacklist takes priority"),
    ("What is the root of Cubyz's permission tree, and what is its only child?", "Root is /, and its only child is command"),

    # --- Addon-creator: blocks ---
    ("What's the one field the Cubyz engine truly requires for a block addon to be valid?", ".tags must be non-empty"),
    ("What rotation mode does a Cubyz block default to if .rotation is omitted?", "\"cubyz:no_rotation\""),
    ("What rotation value must a block have for its ore properties to actually load in Cubyz?", "Exactly \"cubyz:ore\""),
    ("What happens if a Cubyz block has ore properties but the wrong rotation mode?", "The engine logs \"Ore must have rotation mode \\\"cubyz:ore\\\"!\" and silently drops the ore properties"),
    ("What happens if a Cubyz block's tags field ends up empty?", "The engine logs \"Block {id} is missing 'tags' field\" but doesn't fail loading -- the block still exists but may not behave correctly"),
    ("What does Cubyz's blockResistance field default to if omitted?", "0"),

    # --- Addon-creator: items ---
    ("What's the default stack size for a Cubyz item if not specified?", "120"),
    ("What does a Cubyz item's display name fall back to if .name isn't set?", "Its own item id"),
    ("Which four Cubyz item material fields have no soft default and fall back to exactly 0 if missing?", "durability, massDamage, hardnessDamage, and swingSpeed"),
    ("What happens if durability is missing from a Cubyz item's material block?", "It falls back to 0, meaning the item breaks instantly"),
    ("What's the default value for textureRoughness in a Cubyz item's material block?", "1.0 -- the one material field that does have a real default"),

    # --- Addon-creator: biomes ---
    ("What do min/max radius default to for a Cubyz biome if not set?", "256"),
    ("What does a Cubyz biome's music field default to if omitted?", "\"cubyz:totaldemented/cubyz\""),
    ("What music does the Addon Creator website itself default to for biomes, and how does that differ from the engine's default?", "The website defaults to 'cubyz:sunrise', which only matters if you hand-edit and drop the field -- the engine's own default is 'cubyz:totaldemented/cubyz'"),
    ("What's the known bug with the 'valid player spawn' checkbox in the Addon Creator?", "The website exports it as .isValidPlayerSpawn but the engine actually reads .validPlayerSpawn (no 'is' prefix), so the value never gets picked up and falls back to false"),
    ("What tag convention do cave biomes need in Cubyz, and what happens if it's missing?", "A tag ending in _layer -- otherwise the engine logs \"Cave biome {id} is missing a '_layer' tag to assign it to a cave layer.\""),

    # --- Addon-creator: recipes ---
    ("What does the .reversible field do on a Cubyz recipe, and what's its default?", "If true, the engine auto-generates the reverse recipe (output becomes input and vice versa); defaults to false, and the website doesn't expose it"),
    ("What's the limitation on a reversible Cubyz recipe?", "It only works for a recipe with exactly one input and one output -- on a multi-ingredient recipe it fails with error.InvalidReversibleRecipe"),

    # --- Addon-creator: entity models & particles ---
    ("What does a Cubyz entity model's .height field default to if omitted, and how does that differ from the website?", "1, but the Addon Creator website's own form defaults to 2.0 instead -- this only diverges for hand-written files"),
    ("What coordinate system does a Cubyz entity model default to?", ".right_handed_z_up"),
    ("What happens if a Cubyz particle definition is missing its .texture field?", "The engine logs \"Particle texture id was not specified for {id}\" and the particle type fails to register entirely -- unlike most particle fields, this one has no fallback"),
    ("What's the dimension requirement for a Cubyz particle's base texture?", "The texture's height must be an exact multiple of its width, since it's used to slice animation frames"),
    ("What unit are particle rotation velocity fields in on the Addon Creator website versus internally in the engine?", "Degrees on the website; the engine converts to radians internally after loading, so the stored file value still matches what you typed"),

    # --- Codebase / review judgment (reinforcing what the review data actually covers) ---
    ("Why would a Cubyz reviewer push back on using a Hashmap for random indexing into tickable blocks?", "Hashmaps have average O(1) lookups but can degrade to O(n) worst case, and maintaining a list of tickable blocks was already being reconsidered -- adding this now looked like premature optimization"),
    ("Why might a Cubyz reviewer suggest replacing manual string-splitting argument parsing with argparse?", "Manual splitting was brittle -- it assumed exact spacing, required repeated string comparisons, and used a custom Helper struct that had to be manually initialized and deferred"),
    ("Why would a Cubyz reviewer accept a stack-allocator-to-arena-allocator change for asset IDs despite a small memory-leak-on-error risk?", "It simplifies the code and avoids issues with stack allocation, and the arena is reset when leaving the world context, so the rare error-path leak was judged an acceptable tradeoff"),
    ("In Cubyz's Blueprint capture code, what convention does min/max follow architecturally?", "min is inclusive, max is exclusive -- mirroring how size() elsewhere in the codebase adds one and avoids bounds failures"),

    # ============================================================
    # Batch 2 -- expanded corpus coverage: game design principles,
    # contribution guidelines, installation, modding, art guidelines,
    # soil block page, wood recipes, developer judgment, ashframe/
    # server list, multiplayer backups, permission syntax. Moved here
    # from GENERAL_QUESTIONS (2026-07-20) -- these are Cubyz domain
    # facts with known answers, not general-capability sanity checks,
    # and had been silently broken there: GENERAL_QUESTIONS' loop
    # assumes plain question strings, so every (question, expected)
    # tuple below was passed to the model as a literal stringified
    # tuple instead of just its question text, producing garbage
    # input and therefore garbage output that looked like lobotomy
    # but wasn't -- it never actually tested anything until this fix.
    # ============================================================
    # --- Game Design Principles ---
    ("Why doesn't Cubyz use separate dimensions for different areas?",
     "Instead of creating separate dimensions, these places are fit physically into Cubyz's massive world for the player to come across"),
    ("Why doesn't Cubyz have teleportation?",
     "Teleportation makes the game less immersive -- it diminishes the exploring aspect and doesn't let the player get a good sense of the scale of the world"),
    ("Per Cubyz's Game Design Principles, why is automation avoided?",
     "Having quick, infinite resources at the palm of players' hands discourages exploration, since the player will never need to forage or search for blocks they desire"),
    ("Do mobs respawn naturally in Cubyz, per the Game Design Principles?",
     "No -- clearing a dangerous area of its monsters makes it safe to build and explore, and this also prevents mob farming"),
    ("Are there passive animals in Cubyz, per the Game Design Principles?",
     "No -- animals do not want to die, so they either run from an attacking player or attempt to defend themselves"),
    ("Why does Cubyz avoid unbreakable tools, per the Game Design Principles?",
     "If a player gets too attached to an unbreakable tool, they won't want to make other types of tools, and low-tier materials will see less use"),
    ("What is the \"2OP4ME\" balancing principle in Cubyz's Game Design Principles?",
     "Players need to be vulnerable at all times to avoid power imbalances -- armor, tools, accessories, and buffs should aid the player, not let them win outright"),
    ("What's the design difference between big trees and small trees in Cubyz?",
     "Big trees are designed to be built upon or left as decoration, whereas small trees are designed to be chopped down"),

    # --- CONTRIBUTING.md: process and conventions ---
    ("What's the maximum recommended size for a Cubyz pull request?",
     "No more than 200 lines -- the maintainer may refuse to review larger PRs"),
    ("What are Cubyz's four main allocators and their intended lifetimes?",
     "main.globalArena for global lifetime (used until the game ends), main.worldArena for world lifetime (used until the player exits the world), main.stackAllocator for local/scope lifetime, and main.globalAllocator for other lifetimes"),
    ("What naming convention does Cubyz use for variables and functions?",
     "camelCase"),
    ("What naming convention does Cubyz use for types?",
     "CapitalCamelCase (PascalCase)"),
    ("What naming convention does Cubyz use for files and namespaces?",
     "snake_case"),
    ("Does Cubyz enforce a maximum line length for code?",
     "No -- there is no line limit, though contributors should still be reasonable about it"),
    ("What is Cubyz's policy on writing code comments?",
     "Don't write comments unless something non-obvious needs explaining -- prefer readable code with descriptive names, and if you do write a comment, explain the why, not the what or how"),
    ("Why does CONTRIBUTING.md ask contributors not to submit AI-generated pull requests?",
     "Narrow AI is trained to produce code matching its training data rather than being good at programming, likely won't follow the project's conventions, and is unable to learn from mistakes the way a human contributor would"),
    ("Whose optimization philosophy does Cubyz's CONTRIBUTING.md say to follow?",
     "Casey Muratori's non-pessimization philosophy -- not needlessly making things worse"),
    ("When is `catch unreachable` the correct way to handle error.OutOfMemory in Cubyz?",
     "When using the standard allocators (main.globalAllocator and main.stackAllocator), since error.OutOfMemory cannot happen with them"),

    # --- Installation ---
    ("What are the three key files needed to run a downloaded Cubyz release?",
     "Cubyz (or Cubyz.exe), launchConfig.zon, and assets"),
    ("What's the minimum recommended RAM to play Cubyz?",
     "At least 4 GB"),
    ("What example GPUs does the Cubyz installation page list as minimum spec?",
     "Radeon Vega 8, Intel HD Graphics 530, or NVIDIA GTX 750"),
    ("What script builds Cubyz from source on Linux?",
     "run_linux.sh"),
    ("What script builds Cubyz from source on Windows?",
     "run_windows.bat"),

    # --- Modding ---
    ("Is Cubyz's official compile-time modding API finished?",
     "No -- it has not been finished; its progress is tracked in GitHub issue #1528"),
    ("Name an unofficial Cubyz modding fork mentioned in the documentation.",
     "Examples include Web Assembly (wasm) modding, compile-time modding by KewaiiGamer, and a Lua integration by LinaPlusPlus"),

    # --- Content Suggestions / art guidelines ---
    ("What texture resolution does Cubyz require for new textures?",
     "16 x 16"),
    ("What lighting direction should Cubyz item and block textures use?",
     "Top-left"),
    ("Who made the majority of the art for Cubyz?",
     "careeoki"),

    # --- Soil block page ---
    ("How much health does a Cubyz soil block have?",
     "6.5"),
    ("What rotation mode does the Cubyz soil block use?",
     "stairs"),
    ("According to its wiki page, how is soil obtained in Cubyz?",
     "Found in temperate biomes as grass blocks or ground patches -- breaking temperate grass drops soil blocks"),

    # --- Wood recipes (codebase) ---
    ("How do you craft a workbench in Cubyz?",
     "4 planks of any wood type"),
    ("How many planks does crafting one log produce in Cubyz?",
     "4 planks (of the same wood type)"),
    ("How many branches does crafting one log produce in Cubyz?",
     "2 branches (of the same wood type)"),
    ("What's needed to craft a chest in Cubyz?",
     "4 planks of the same wood type"),
    ("What ingredients craft a regular torch in Cubyz?",
     "Planks (any mod's, any type) plus coal ore, producing 8 torches"),

    # --- Developer judgment (additional facts) ---
    ("Why does Cubyz prefer explicit code over generic or clever solutions in review?",
     "This project strongly prefers explicit, predictable, allocator-conscious code over clever/generic/automatic solutions, even when the generic solution is more DRY -- \"magic\" is treated as a mild pejorative"),
    ("Is eager or lazy allocation preferred in Cubyz code review?",
     "It's a judgment call, not a fixed rule -- lazy/path-based loading is preferred for large or rarely-touched data, but eager initialization is preferred when correctness or synchronization ordering demands it"),
    ("Why is placing a `defer` far from its matching `init` flagged in Cubyz review, even if technically correct?",
     "Because it's fragile to future edits"),

    # --- Ashframe / server list ---
    ("Who runs Ashframe?",
     "iNiKKo"),
    ("What does the 'enabled' field control in the Cubyz Server List's config.json?",
     "true broadcasts the server's information to the Cubyz Server List (servers.ashframe.net); false disables server list integration entirely"),

    # --- Multiplayer backups ---
    ("Where is a Cubyz world save located by default on Linux, for backup purposes?",
     "/home/USERNAME/.cubyz/saves/WORLD_NAME"),
    ("Where is a Cubyz world save located by default on Windows, for backup purposes?",
     "C:\\Users\\USERNAME\\Saved Games\\Cubyz\\saves\\WORLD_NAME"),

    # --- Permission layer (engine syntax) ---
    ("What is the full engine command syntax for managing permissions in Cubyz?",
     "/perm <add/remove> <whitelist/blacklist> @<playerIndex> <permissionPath>"),

    # --- Installation troubleshooting / misc CONTRIBUTING guidance ---
    ("What should you do if Cubyz runs poorly or doesn't start, per the installation guide?",
     "Reach out on the Cubyz Discord"),
    ("What does CONTRIBUTING.md say about writing long comments instead of readable code?",
     "Prefer readable code with descriptive names instead of long comments, since comments naturally degrade over time as the surrounding code changes; any comment written should explain the why, not the what or how"),
    ("What data-structure guidance does CONTRIBUTING.md give when a collection's size is known upfront?",
     "Use the simplest data structure for the job -- e.g. use a slice instead of a List if you know the size upfront"),
    ("What's the recommended sweet-spot file size (in lines) for a Cubyz source file, per CONTRIBUTING.md?",
     "Very roughly 1000 lines"),
]

# Genuinely unrelated to Cubyz -- general knowledge, math, and basic reasoning. This is the ONLY
# real check for the "lobotomy" failure mode (catastrophic forgetting of general capability) this
# whole project was built to avoid; everything above tests domain recall, not general capability.
# Kept deliberately small and varied rather than large -- a handful of clearly-graded questions
# across different capability types (factual recall, arithmetic, basic logic, simple code) is
# enough to catch gross degradation; it's not trying to be a full general-capability benchmark.
GENERAL_QUESTIONS = [
    "What is the capital of France?",
    "What's 17 * 24?",
    "What's the boiling point of water in Celsius at sea level?",
    "If a train travels 60 miles in 90 minutes, what's its average speed in mph?",
    "Write a Python one-liner that reverses a string.",
    "Which planet in our solar system is closest to the sun?",
    "What's the difference between a list and a tuple in Python?",
    "If all cats are mammals and all mammals are animals, are all cats animals?",
]


def ask(model, tokenizer, question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=False,  # deterministic -- easier to judge quality without sampling noise
            pad_token_id=tokenizer.pad_token_id,
        )
    generated = output[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True).strip()


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(RESULTS_DIR, f"standalone_{timestamp}.txt")
    log_file = open(log_path, "w")
    sys.stdout = Tee(sys.__stdout__, log_file)

    print(f"[~] Loading 4-bit base model: {MODEL_ID}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map={"": 0},
        dtype=torch.bfloat16,
    )

    print(f"[~] Loading LoRA adapter from {ADAPTER_DIR}")
    model = PeftModel.from_pretrained(model, ADAPTER_DIR)
    model.eval()

    print("\n" + "=" * 70)
    print("CUBYZ-SPECIFIC QUESTIONS (checking domain knowledge landed)")
    print("=" * 70)
    for q, expected in CUBYZ_QUESTIONS:
        print(f"\nQ: {q}")
        print(f"A: {ask(model, tokenizer, q)}")
        print(f"   [expected: {expected}]")

    print("\n\n" + "=" * 70)
    print("GENERAL QUESTIONS (checking general capability wasn't damaged)")
    print("=" * 70)
    for q in GENERAL_QUESTIONS:
        print(f"\nQ: {q}")
        print(f"A: {ask(model, tokenizer, q)}")

    print("\n\n[~] Done. Read every answer above -- specifically check the general questions")
    print("    for anything degraded, repetitive, incoherent, or off-topic. That's the")
    print("    'lobotomy' failure mode this whole pipeline was built to avoid.")
    print(f"[~] Transcript saved to {log_path}")

    sys.stdout = sys.__stdout__
    log_file.close()


if __name__ == "__main__":
    main()
