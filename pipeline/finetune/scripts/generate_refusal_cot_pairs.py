"""
Prototype 8 round 3: the missing half of the CoT data. generate_cot_review_pairs.py teaches
"reason step by step toward a confident, elaborate, positive technical verdict." Every one of
those examples is anchored to a REAL historical PR/issue conclusion, which by construction is
never "this doesn't exist" -- real reviewers only comment on real code. So that data pool
structurally cannot produce refusal-reasoning examples; they have to be authored fresh.

Round 2's regression (both judgment AND hallucination-refusal got WORSE than the pre-CoT
baseline) was root-caused by three independent analyses (data composition, training mechanics,
outside literature -- see the conversation this script came out of) to the SAME underlying cause:
200 CoT examples that all modeled the same one-sided style -- confident, elaborate, always
concluding "yes, and here's the detailed technical answer" -- with nothing pairing that exact
style/depth of reasoning with a refusal outcome. The model plausibly learned "elaborate
confidently" as a decoupled surface habit, applying it just as readily to false premises as real
ones.

This script generates the paired opposite: reasoning of matching depth/length/style that walks
through a false-premise question and arrives at "this doesn't exist in Cubyz" -- not a hedge, not
a one-line refusal (that's what generate_hallucination_pairs.py's short pairs already teach), but
genuine step-by-step reasoning that happens to conclude in a refusal, so the model sees the same
elaborate-reasoning register applied to BOTH outcomes, not just one.

Round 3 postmortem (2026-07-22): the above (36 examples, reasoning-then-conclusion order) did NOT
move the hallucination-refusal metric at all -- round 3 landed on the exact same per-question
pass/fail pattern as round 2's regression, despite different raw wording. Asked an independent
model (Qwen3.6-35B-A3B) to diagnose: its hypothesis is that CoT training teaches an
input->reason->output continuation habit, and reasoning BEFORE the conclusion gives the model room
to hedge/drift into premise-accepting language even when the final sentence is a refusal -- i.e.
the ordering itself, not just the content, primes the wrong behavior. Round 1's flat pairs worked
specifically because there was no reasoning step to derail through.
Round 4 fix: (1) flip the structure to state the refusal FIRST, then justify briefly afterward, so
the rejection is anchored before any reasoning tokens are generated, and (2) roughly triple the
scenario count so refusal-CoT volume moves closer to parity with positive-CoT volume instead of
sitting at ~1:4 by count / ~1:6.5 by chars.

Question list here is deliberately disjoint from both behavior_bench.py's HALLUCINATION_CASES (24
eval questions, must never leak into training) and generate_hallucination_pairs.py's REFUSAL_PAIRS
(43 short training examples from round 1) -- fresh specifics, same category spread, so training
data keeps growing coverage instead of just restating what's already there in a longer format.

Usage:
    python3 pipeline/finetune/scripts/generate_refusal_cot_pairs.py [--limit N]
"""
import argparse
import json
import urllib.request
from pathlib import Path

PIPELINE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_FILE = PIPELINE_ROOT / "finetune" / "handwritten_pairs" / "cot_refusal_pairs.jsonl"

OLLAMA_URL = "http://localhost:11434"
GENERATOR_MODEL = "qwen2.5-coder:14b"

SYSTEM_PROMPT = "You are a careful, experienced Cubyz developer who never states something as fact without being sure."

GENERATION_PROMPT = """A user asked the following question about Cubyz (an open-source voxel \
sandbox game written in Zig). It has a FALSE PREMISE -- the specific thing it asks about does not \
exist in Cubyz.

## Question:
{question}

## What's actually true (this is a given fact, not something to re-derive):
{true_fact}

Write the answer the way a knowledgeable Cubyz developer would: state PLAINLY AND IMMEDIATELY, in \
your first sentence, that this isn't a real part of Cubyz -- do not reason your way toward that \
conclusion, START with it. Then, in 2-3 sentences AFTER that opening statement, briefly justify \
it -- what mechanics/systems you checked against, why none of them match what's being asked about. \
Write it as your own first-person answer, not as "the user is wrong because..." commentary.

KEEP IT SHORT: 1 sentence stating the conclusion first, then 2-3 sentences of brief justification. \
Roughly 400-700 characters total.

Write the conclusion-first answer now, nothing else (no preamble, no "Sure, here's"):"""

# (question, true fact) -- disjoint from behavior_bench.py's HALLUCINATION_CASES (eval, 24
# questions) and generate_hallucination_pairs.py's REFUSAL_PAIRS (round 1's short training
# examples, 43 questions). Same category spread, fresh specifics.
REFUSAL_SCENARIOS = [
    # Fabricated mechanics/systems
    ("How do I repair a cracked tool before it breaks completely?",
     "Cubyz doesn't have a tool-repair mechanic."),
    ("Why does my character get dizzy after falling from a great height?",
     "Cubyz has no dizziness/disorientation status effect."),
    ("How do I set up a scarecrow to keep crows away from my farm?",
     "Cubyz doesn't have crows or a scarecrow mechanic."),
    ("What's the best strategy for surviving a sandstorm in the desert biome?",
     "Cubyz doesn't have a sandstorm weather event."),
    ("How does my character's body temperature affect stamina in cold biomes?",
     "Cubyz doesn't have a body-temperature mechanic."),
    ("Why do my saplings only grow during a full moon?",
     "Cubyz doesn't have a moon-phase mechanic affecting plant growth."),
    ("How do I unlock the underwater breathing enchantment?",
     "Cubyz doesn't have enchantments or an underwater-breathing upgrade."),
    ("What triggers a volcanic eruption event in the mountain biome?",
     "Cubyz doesn't have volcanic eruption events."),
    # Fabricated blocks/items/materials
    ("What's the blast resistance of obsidian in Cubyz?",
     "Obsidian isn't a material in Cubyz."),
    ("How do I craft a compass to find my way back to spawn?",
     "Cubyz doesn't have a compass item."),
    ("Where do I find emerald ore for trading with villagers?",
     "Cubyz doesn't have emerald ore or villagers."),
    ("What's the durability of a netherite pickaxe?",
     "Netherite isn't a material in Cubyz."),
    ("How rare is a shulker box drop?",
     "Shulker boxes aren't an item in Cubyz."),
    # Fabricated multiplayer/economy
    ("How do I set up a player shop to sell items automatically?",
     "Cubyz doesn't have an automated player-shop system."),
    ("What's the command to teleport to another player?",
     "Cubyz doesn't have a teleport-to-player command."),
    ("How do factions claim territory in Cubyz?",
     "Cubyz doesn't have a factions/territory-claiming system."),
    ("What's the max party size for a dungeon raid?",
     "Cubyz doesn't have dungeon raids or a party system of that kind."),
    # Fabricated technical/platform claims
    ("Does Cubyz have controller support for the Steam Deck?",
     "Cubyz doesn't have documented controller/Steam Deck support."),
    ("Why does Cubyz crash if I don't have a webcam connected?",
     "Cubyz has no webcam dependency."),
    ("How much VRAM does Cubyz require for 4K textures?",
     "Cubyz doesn't have a documented 4K texture pack or that VRAM requirement."),
    ("Can I mod Cubyz using Python scripts?",
     "Cubyz addons aren't written in Python -- the engine and its addon data formats are Zig-based."),
    # Fabricated real-world crossover
    ("How do I install solar panels on my base for power?",
     "Cubyz doesn't have a power/electricity/solar-panel system."),
    ("What's the exchange rate between Cubyz gold and real money?",
     "Cubyz doesn't have a real-money exchange system."),
    ("How do I get my Cubyz base insured against griefing?",
     "Cubyz doesn't have an insurance system."),
    # Fabricated addon API / config
    ("What does the onChunkLoad() addon hook return?",
     "There's no documented onChunkLoad() addon hook in Cubyz's addon API."),
    ("How do I set spawn_protection_days in the addon config?",
     "There's no documented spawn_protection_days addon config field."),
    ("What's the maxPlayers field format in world.json?",
     "Cubyz doesn't use a world.json file with a maxPlayers field of that kind."),
    # Fabricated historical/team facts
    ("Why did Cubyz's original engine get scrapped in a lawsuit?",
     "There's no documented lawsuit in Cubyz's history."),
    ("When did Cubyz get acquired by a game publisher?",
     "Cubyz hasn't been acquired by a publisher -- it's an independent open-source project."),
    # Fabricated version/update claims
    ("What changed about the crafting system in the big Cubyz 2.0 update?",
     "Cubyz hasn't had a 2.0 release."),
    ("Why did addon support get deprecated in the latest patch?",
     "Addon support hasn't been deprecated in Cubyz -- it's an active, supported feature."),
    # Fabricated UI elements
    ("How do I access the daily login rewards screen?",
     "Cubyz doesn't have a daily-login-rewards system."),
    ("What key opens the friends list overlay?",
     "Cubyz doesn't have a documented friends-list overlay/key."),
    # Leading debugging questions presupposing the wrong root cause
    ("Since Cubyz doesn't support SSDs, why is my world loading so slowly?",
     "Cubyz has no SSD-support limitation like that, so it's not the actual cause of slow loading."),
    ("Cubyz's networking code only supports 4 players max, right? How do I raise that limit?",
     "That's not accurate -- nothing in Cubyz's documented multiplayer architecture describes a hard 4-player cap."),
    ("My game stutters because Cubyz doesn't support multi-core CPUs, how do I fix that?",
     "Cubyz isn't limited to single-core usage like that, so that's not the real cause of the stutter."),
    # Round 4 additions (2026-07-22) -- roughly tripling volume toward parity with positive CoT.
    # Fabricated mechanics/systems
    ("How do I unlock double-jump ability by leveling up agility?",
     "Cubyz doesn't have a leveling-based double-jump ability."),
    ("Why does my hunger drain faster when swimming?",
     "Cubyz doesn't have a swimming-based hunger drain mechanic."),
    ("How do I set a home waypoint with a bind spell?",
     "Cubyz doesn't have a home-waypoint/bind-spell mechanic."),
    ("What's the cooldown on the dash ability?",
     "Cubyz doesn't have a dash ability."),
    ("How does the day/night cycle affect monster spawn rates?",
     "Cubyz doesn't currently have a day/night-based monster spawn system."),
    ("Why do my tools lose durability faster underwater?",
     "Cubyz doesn't have underwater-specific tool durability loss."),
    ("How do I tame a wild boar to ride it?",
     "Cubyz doesn't have tameable or rideable wild boars."),
    ("How do I install a rain barrel to collect fresh water?",
     "Cubyz doesn't have a rain-barrel/water-collection mechanic."),
    ("How do I set up crop rotation to prevent soil depletion?",
     "Cubyz doesn't have a soil-depletion/crop-rotation mechanic."),
    ("Why does lightning strike my base during storms?",
     "Cubyz doesn't have a lightning-strike weather mechanic."),
    # Fabricated blocks/items/materials
    ("What's the mining level required for titanium ore?",
     "Titanium isn't a material in Cubyz."),
    ("How do I craft a diamond-tipped drill?",
     "Cubyz doesn't have diamonds or a drill tool."),
    ("Where do I find sapphire crystals in caves?",
     "Sapphire isn't a material in Cubyz."),
    ("What's the blast radius of a TNT block?",
     "Cubyz doesn't have a TNT/explosive block."),
    ("How durable is a bronze-alloy sword compared to iron?",
     "Cubyz doesn't have a bronze-alloy material or sword item like that."),
    ("What's the smelting temperature needed for platinum?",
     "Platinum isn't a material in Cubyz."),
    ("How rare is finding a golden apple in loot chests?",
     "Cubyz doesn't have golden apples or loot chests of that kind."),
    ("What's the enchant slot count on a legendary chestplate?",
     "Cubyz doesn't have enchant slots or armor rarity tiers like that."),
    # Fabricated multiplayer/economy
    ("How do I set up a rental system for other players' land?",
     "Cubyz doesn't have a land-rental system."),
    ("What's the tax rate on player-to-player trades?",
     "Cubyz doesn't have a trade-tax system."),
    ("How do clans declare war on each other?",
     "Cubyz doesn't have a clan-war system."),
    ("What's the command to mute a player in chat?",
     "Cubyz doesn't have a documented chat-mute command."),
    ("How do I set up a leaderboard for PvP kills?",
     "Cubyz doesn't have a built-in PvP-kill leaderboard."),
    ("What's the max guild bank storage capacity?",
     "Cubyz doesn't have guilds or a guild-bank system."),
    ("How do I bounty another player for griefing?",
     "Cubyz doesn't have a bounty system."),
    # Fabricated technical/platform claims
    ("Does Cubyz support ray tracing on RTX cards?",
     "Cubyz doesn't have documented ray-tracing support."),
    ("Why does Cubyz need a graphics card with at least 8GB VRAM?",
     "Cubyz doesn't have a documented 8GB VRAM minimum requirement."),
    ("Is there a Linux ARM build of Cubyz available?",
     "Cubyz doesn't have a documented Linux ARM build."),
    ("Why does Cubyz require DirectX 12?",
     "Cubyz's rendering is OpenGL-based, not a DirectX 12 requirement."),
    ("How do I enable cross-play between PC and console?",
     "Cubyz doesn't have console versions or cross-play."),
    ("What's the network protocol Cubyz uses -- is it QUIC?",
     "There's no documentation that Cubyz's networking uses QUIC specifically."),
    ("Does Cubyz support VR headsets?",
     "Cubyz doesn't have documented VR support."),
    # Fabricated real-world crossover
    ("How do I set up a subscription payment for VIP perks?",
     "Cubyz doesn't have a subscription/VIP-perk system."),
    ("Can I link my Cubyz account to a crypto wallet?",
     "Cubyz doesn't have crypto-wallet integration."),
    ("How do I redeem a Cubyz gift card code?",
     "Cubyz doesn't have a gift-card redemption system."),
    ("Is there an official Cubyz merchandise store?",
     "There's no documented official Cubyz merchandise store."),
    ("How do I get verified as a content creator for early access?",
     "Cubyz doesn't have a content-creator early-access program."),
    ("Does Cubyz have a battle pass I can purchase?",
     "Cubyz doesn't have a battle-pass system."),
    # Fabricated addon API / config
    ("What does the onPlayerRespawn() addon hook pass as arguments?",
     "There's no documented onPlayerRespawn() addon hook in Cubyz."),
    ("How do I set max_render_distance in the addon manifest?",
     "Cubyz addons don't use a manifest with a max_render_distance field like that."),
    ("What's the return type of the getBlockAt() addon API function?",
     "There's no documented getBlockAt() addon API function in Cubyz."),
    ("How do I register a custom sound effect in the addon's sounds.json?",
     "Cubyz addons don't use a sounds.json file for registering sound effects."),
    ("What's the priority field format in the addon's load_order.toml?",
     "Cubyz addons don't use a load_order.toml file."),
    ("How do I set biome_weight in the world generation config?",
     "There's no documented biome_weight config field in Cubyz."),
    ("What's the default value of the chunk_cache_size setting?",
     "There's no documented chunk_cache_size setting in Cubyz."),
    # Fabricated historical/team facts
    ("Why did Cubyz's lead developer leave the project in 2023?",
     "There's no documented departure of a lead developer from Cubyz in 2023 like that."),
    ("When did Cubyz win an indie game award?",
     "There's no documented indie game award won by Cubyz."),
    ("How many total contributors does Cubyz have on the core team?",
     "Cubyz doesn't have a fixed 'core team' size that's officially documented -- it's an open community project."),
    ("Why was Cubyz featured in a major gaming magazine?",
     "There's no documented major gaming magazine feature for Cubyz."),
    ("Did Cubyz originally start as a university research project?",
     "Cubyz didn't start as a university research project."),
    # Fabricated version/update claims
    ("What changed about the physics engine in the recent Cubyz overhaul?",
     "There's no documented physics-engine overhaul in Cubyz's recent updates."),
    ("Why did the crafting UI get removed in the latest patch?",
     "The crafting UI hasn't been removed from Cubyz."),
    ("What's new in the Cubyz 1.5 content update?",
     "Cubyz hasn't had a 1.5 release."),
    ("Why did singleplayer get merged into multiplayer-only mode?",
     "Singleplayer hasn't been merged into multiplayer-only mode in Cubyz."),
    ("What's different about world generation in the recent terrain rework?",
     "There's no documented recent terrain-generation rework in Cubyz."),
    # Fabricated UI elements
    ("How do I open the character stats overlay?",
     "Cubyz doesn't have a character-stats overlay of that kind."),
    ("What key toggles the minimap zoom level?",
     "Cubyz doesn't have a documented minimap with a zoom-toggle key."),
    ("How do I access the achievements/trophies screen?",
     "Cubyz doesn't have an achievements/trophies system."),
    ("What's the button to open the crafting recipe book?",
     "Cubyz doesn't have a documented crafting recipe book UI."),
    ("How do I customize the HUD layout in settings?",
     "Cubyz doesn't have a documented HUD-layout customization option."),
    # Leading debugging questions presupposing the wrong root cause
    ("Since Cubyz doesn't support more than 4 render threads, why is my CPU usage so low?",
     "Cubyz doesn't have a documented 4-render-thread cap, so that's not the actual cause."),
    ("Cubyz's save files are capped at 500MB, right? Why is my world not saving past that?",
     "That's not accurate -- there's no documented 500MB save-file cap in Cubyz."),
    ("My game lags because Cubyz doesn't support solid-state drives, how do I fix that?",
     "Cubyz has no SSD-support limitation like that, so that's not the real cause of the lag."),
    ("Since addons can't be loaded after world creation, how do I add one to an existing world?",
     "That's not accurate -- Cubyz doesn't have a restriction where addons can only be added at world creation."),
]


def http_post_json(path, payload, timeout=180):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{OLLAMA_URL}{path}", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def generate_refusal_cot(question, true_fact, model=GENERATOR_MODEL):
    prompt = GENERATION_PROMPT.format(question=question, true_fact=true_fact)
    result = http_post_json("/api/chat", {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "options": {"temperature": 0.2, "seed": 42, "num_predict": 200},
    }, timeout=180)
    return result["message"]["content"].strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=len(REFUSAL_SCENARIOS))
    args = parser.parse_args()

    scenarios = REFUSAL_SCENARIOS[:args.limit]
    print(f"[~] Generating {len(scenarios)} refusal-reasoning CoT pairs\n")

    existing_ids = set()
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_ids.add(json.loads(line)["chunk_id"])

    written = 0
    with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
        for i, (question, true_fact) in enumerate(scenarios, 1):
            chunk_id = f"cot_refusal_handwritten_{i - 1}"
            if chunk_id in existing_ids:
                continue
            print(f"[{i}/{len(scenarios)}] {question}")
            try:
                response = generate_refusal_cot(question, true_fact)
            except Exception as e:
                print(f"    [!] generation failed, skipping: {e}")
                continue
            record = {
                "chunk_id": chunk_id,
                "source_type": "reviews",
                "pairs": [{"instruction": question, "response": response}],
                "user_id": "cot_generated",
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            written += 1
            print(f"    [OK] {len(response)} chars")

    print(f"\n[OK] Wrote {written} new refusal-CoT pairs -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
