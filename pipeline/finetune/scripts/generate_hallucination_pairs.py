"""
Prototype 8: hand-authored training pairs teaching false-premise refusal -- the behavior gap
behavior_bench.py's baseline measured directly (P7-4B: 29.2% correct-refusal rate, meaning it
fabricated a confident answer to 17/24 leading/false-premise questions). Written as a generator
script rather than a static JSONL file so the category list stays easy to see/extend in one place.

Split into two halves on purpose:
  - REFUSAL_PAIRS: false-premise questions paired with a correct "that's not real" answer, in
    the same confident-developer voice as the rest of the reviews training data.
  - GENUINE_SURPRISING_PAIRS: real, verified Cubyz facts that happen to SOUND like they could be
    made up (oddly specific numbers, a game with a missing feature, etc.) -- included so training
    teaches "check whether it's actually true" rather than "refuse anything that sounds unusual,"
    which would just trade one failure mode for another (reflexive over-refusal).

None of these questions overlap with pipeline/finetune/training/behavior_bench.py's
HALLUCINATION_CASES -- different specific questions, similar categories, so the eval set stays a
genuine held-out test of whether the behavior generalized rather than being memorized verbatim.

source_type is deliberately "reviews" (not "docs") -- assemble_sft_dataset.py's SOURCE_TYPES
filter only keeps "reviews" since Prototype 7 (fine-tuning shapes behavior, not fact memorization)
-- this file is squarely behavior training (recognizing and refusing a false premise), the same
bucket as PR-review judgment, even though it's not literally a PR review.

Usage:
    python3 pipeline/finetune/scripts/generate_hallucination_pairs.py
"""
import json
import os

OUTPUT_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "handwritten_pairs", "hallucination_refusal_pairs.jsonl",
)

# (question, correct refusal response) -- response states plainly that the premise is false,
# same voice as the rest of the training data (confident developer, no hedging about "the
# provided context doesn't mention X" -- that phrasing would get caught by
# assemble_sft_dataset.py's own HEDGE_RE filter anyway, and isn't the point: the model should
# just know it's false, not describe its own uncertainty about a retrieval process it doesn't
# have here).
REFUSAL_PAIRS = [
    # Fabricated mechanics/systems
    ("Why does my torch go out faster when it's raining in Cubyz?",
     "Torches in Cubyz don't have a rain-extinguish mechanic -- that's not a real interaction in the game."),
    ("How do I cure my character of poison sickness over time?",
     "Cubyz doesn't have a poison-sickness/disease system for the player to cure."),
    ("What's the formula for calculating fall damage reduction from boots?",
     "Cubyz doesn't have a boots-based fall damage reduction mechanic."),
    ("How long does it take for my character to age and need a new body?",
     "Cubyz has no character-aging mechanic."),
    ("Why does my crops wilt faster when I plant them near lava?",
     "Cubyz doesn't have a crop-wilting-from-heat mechanic."),
    ("How do I set up a weather forecast system to predict storms?",
     "Cubyz doesn't have a storm/weather-forecasting system."),
    ("What's the max number of pets I can have following me at once?",
     "Cubyz doesn't have a pet-following mechanic with a cap like that."),
    ("How do I reduce fatigue when mining for long periods?",
     "Cubyz doesn't have a mining-fatigue mechanic."),
    ("Why do my tools rust faster near the ocean biome?",
     "Cubyz doesn't have a tool-rusting mechanic tied to biome proximity."),
    ("How does the seasons system affect crop growth speed?",
     "Cubyz doesn't currently have a seasons system."),
    # Fabricated blocks/items/materials
    ("What's the smelting time for adamantium ore in the furnace?",
     "Adamantium isn't a real material in Cubyz."),
    ("Where do I find mythril deposits underground?",
     "Mythril isn't a real material in Cubyz."),
    ("How do I craft an enchantment table?",
     "Cubyz doesn't have enchantment tables or an enchanting system."),
    ("What potion do I brew to gain night vision?",
     "Cubyz doesn't have a potion-brewing system."),
    ("How rare is the legendary phoenix feather drop?",
     "There's no phoenix feather item in Cubyz."),
    # Fabricated multiplayer/economy features
    ("How do I set up an auction house for trading with other players?",
     "Cubyz doesn't have a built-in auction house/trading-post system."),
    ("What's the in-game currency called that I use to buy from NPC shops?",
     "Cubyz doesn't have NPC shops or an in-game currency system."),
    ("How do I create a guild and invite other players?",
     "Cubyz doesn't have a guild/clan system."),
    ("What's the PvP arena queue command?",
     "Cubyz doesn't have a PvP arena/queue system."),
    ("How do I set a spawn protection radius as a server admin?",
     "Cubyz doesn't have a documented spawn-protection-radius setting."),
    # Fabricated technical/platform claims
    ("Does Cubyz support DLSS upscaling on Nvidia cards?",
     "Cubyz doesn't have documented DLSS support."),
    ("Why does Cubyz require a Steam account to launch?",
     "Cubyz doesn't require a Steam account -- it's not distributed as a Steam-locked game."),
    ("How much does the mobile version of Cubyz cost?",
     "There is no mobile version of Cubyz."),
    ("What's the minimum Vulkan version required to run Cubyz?",
     "Cubyz's rendering requirements are OpenGL-based (4.3+), not a Vulkan version requirement."),
    ("Why does Cubyz need an internet connection to play singleplayer?",
     "Cubyz singleplayer doesn't require an internet connection."),
    # Fabricated addon API specifics
    ("What parameters does the onBlockPlace() addon callback take?",
     "There's no documented onBlockPlace() addon callback in Cubyz's addon API."),
    ("How do I register a custom particle effect in my addon's manifest.json?",
     "Cubyz addons don't use a manifest.json file -- addon data is defined per-category in .zig.zon files."),
    ("What's the addon_version field format in the addon config?",
     "There's no documented addon_version field in Cubyz's addon format."),
    ("How do I hook into the onWorldSave() event from an addon?",
     "There's no documented onWorldSave() addon hook in Cubyz."),
    # Fabricated config/commands
    ("What's the /gamemode creative command syntax in Cubyz?",
     "Cubyz doesn't use Minecraft-style /gamemode commands."),
    ("How do I set difficulty=hard in the world config?",
     "Cubyz doesn't have a documented difficulty setting of that kind."),
    ("What's the tickSpeed config option's default value?",
     "There's no documented tickSpeed config option in Cubyz."),
    # Fabricated historical/team facts
    ("Why did the original Cubyz team disband in 2020?",
     "The Cubyz team hasn't disbanded -- it's an actively maintained project."),
    ("When did Cubyz switch from being closed-source to open-source?",
     "Cubyz doesn't have a closed-source-to-open-source transition in its history that's documented."),
    ("How many people are on the paid Cubyz development team?",
     "Cubyz isn't developed by a paid team -- it's an open-source community project."),
    # Fabricated version/update claims
    ("What major feature did Cubyz 1.0 add?",
     "Cubyz hasn't reached a 1.0 release."),
    ("Why was multiplayer removed in the latest Cubyz update?",
     "Multiplayer hasn't been removed from Cubyz -- it's an active, supported feature."),
    # Fabricated UI elements
    ("How do I open the skill tree menu?",
     "Cubyz doesn't have a skill tree system or menu."),
    ("What key opens the world map overview?",
     "Cubyz doesn't have a documented world-map-overview key/menu."),
    ("How do I customize my character's face in the appearance menu?",
     "Cubyz doesn't have a character face-customization menu."),
    # Leading debugging questions presupposing the wrong root cause
    ("My game crashes because Cubyz doesn't support more than 8GB of RAM, how do I fix that?",
     "Cubyz doesn't have an 8GB RAM ceiling like that -- that's not a real limitation, so it's not the actual cause of the crash."),
    ("Since Cubyz caps FPS at 30 by default, how do I unlock higher framerates?",
     "Cubyz doesn't have a default 30 FPS cap."),
    ("Cubyz's chunk loading is single-threaded, right? How do I enable multithreaded loading?",
     "That's not accurate -- nothing in Cubyz's documented architecture describes chunk loading as single-threaded by default with a separate opt-in multithreaded mode."),
]

# Real, verified facts that sound like they could be made up -- included so training doesn't
# teach reflexive suspicion of anything unusual-sounding. Sourced from knowledge_base/docs and
# knowledge_base/reviews content already crunched and verified against raw engine/doc source.
GENUINE_SURPRISING_PAIRS = [
    ("Is it true there's currently no way to heal in Cubyz?",
     "Yes -- there is currently no way to regain health in Cubyz other than dying."),
    ("Does Cubyz's world really extend 2 billion blocks in each direction?",
     "Yes -- the Cubyz world can extend up to 2 billion blocks on each axis."),
    ("If I reference a block ID that doesn't exist in my addon, does the game crash?",
     "No -- the engine doesn't crash. It logs \"Couldn't find block {id}. Replacing it with air...\" and substitutes air."),
    ("Is Cubyz really unsupported on Mac?",
     "Yes -- Mac isn't supported because it lacks OpenGL 4.3."),
    ("Was Cubyz really called something else before its current name?",
     "Yes -- Cubyz was originally called \"Cubz.\""),
    ("Is the default multiplayer port for Cubyz really 47649?",
     "Yes -- that's the default multiplayer server port."),
    ("Does the player really start with only 8 hearts in Cubyz?",
     "Yes -- 8 hearts, 16 total health."),
    ("Would a Cubyz reviewer really prefer getOrPut over a separate contains-check plus insert?",
     "Yes -- getOrPut atomically retrieves-or-inserts in one operation instead of two lookups, reducing redundant memory accesses and complexity."),
    ("Is it true a biome's custom sky color might not show up even if I set it correctly in the Addon Creator?",
     "Yes -- that's a real format mismatch: the website exports skyColor/fogColor as a 3-component float vector, but the engine reads those fields as a packed u32 integer."),
    ("Did Cubyz really get rewritten from one programming language to another?",
     "Yes -- Cubyz was rewritten from Java to Zig, largely due to Java's garbage collector causing lag spikes when the upper memory limit was hit."),
    ("Is there really a NeverFailingAllocator type in Cubyz's codebase?",
     "Yes -- utils.NeverFailingAllocator is an allocator interface that cannot return error.OutOfMemory."),
    ("Is it true tools are used to damage soil blocks specifically, not just any tool?",
     "Yes -- shovels are specifically the tool used to damage/mine soil blocks."),
]


def build_records(pairs, prefix):
    return [
        {
            "chunk_id": f"{prefix}_{i}",
            "source_type": "reviews",
            "pairs": [{"instruction": q, "response": a}],
            "user_id": "handwritten",
        }
        for i, (q, a) in enumerate(pairs)
    ]


def main():
    records = (
        build_records(REFUSAL_PAIRS, "hallucination_refusal_handwritten")
        + build_records(GENUINE_SURPRISING_PAIRS, "hallucination_genuine_handwritten")
    )
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"[OK] Wrote {len(records)} pairs ({len(REFUSAL_PAIRS)} refusal + {len(GENUINE_SURPRISING_PAIRS)} genuine) to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
