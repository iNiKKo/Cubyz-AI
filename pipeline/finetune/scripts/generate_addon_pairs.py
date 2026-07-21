"""
Hand-authored fine-tuning pairs for the addon_creator domain, written directly from
FIELD_REFERENCE.md and ENGINE_VALIDATION_REFERENCE.md rather than routed through the
distributed generation campaign -- this domain is small and bounded (2 reference docs, fully
read and verified against actual source), so direct authoring is both cheaper and higher
quality than a smaller crunching model summarizing fragments.

Every claim in every pair below is traceable to a specific row in one of those two docs.
Output matches the same record schema server_finetune.py's clients produce, so it drops
straight into finetune/pairs/ and flows through assemble_sft_dataset.py with no special-casing.
"""
import json
import os

# Deliberately NOT inside finetune/pairs/ -- that directory is server_finetune.py's own managed
# output, and a hard reset of the generation campaign wipes it entirely (it does get backed up
# first, but there's no reason to rely on digging through a backup folder to recover hand-authored
# data that was never part of the distributed campaign in the first place).
OUTPUT_FILE = "pipeline/finetune/handwritten_pairs/addon_creator_pairs.jsonl"

PAIRS = [
    {
        "instruction": "How do I create a minimal Cubyz block addon?",
        "response": (
            "At minimum you need a `.zig.zon` file under `blocks/` in your addon folder, named "
            "after the block's id. The engine only truly requires `.tags` to be non-empty "
            "(everything else has a fallback default, though `.rotation` defaults to "
            "`\"cubyz:no_rotation\"` if omitted). A minimal example:\n\n"
            "```\n.{\n"
            "    .tags = .{.pickaxe},\n"
            "    .rotation = \"cubyz:no_rotation\",\n"
            "    .blockHealth = 1.0,\n"
            "    .blockResistance = 0.0,\n"
            "    .texture = \"yourname:your_block\",\n"
            "}\n```\n\n"
            "If you're using the Addon Creator Studio website instead of hand-writing this, the "
            "Block panel's \"Base Texture\" and Block ID fields are the only two required to save."
        ),
    },
    {
        "instruction": "What does the 'Blast Resistance' field in the Addon Creator's block panel actually export as?",
        "response": "It maps directly to `.blockResistance` in the exported `.zig.zon` file, and the engine defaults it to `0` if the field is ever omitted.",
    },
    {
        "instruction": "I made an ore block in the Addon Creator but the ore properties (veins, size) don't seem to be applying. What's going on?",
        "response": (
            "Check the block's `.rotation` field -- the engine only loads `.ore` properties "
            "when `.rotation` is exactly `\"cubyz:ore\"`. If it's set to anything else but an "
            "`.ore` block is present, the engine logs \"Ore must have rotation mode "
            "\\\"cubyz:ore\\\"!\" and silently drops the ore properties entirely rather than "
            "erroring out. The Addon Creator website sets rotation correctly when you pick the "
            "ore option in its dropdown, so this usually only happens with hand-edited files."
        ),
    },
    {
        "instruction": "My custom block doesn't seem to be interactable at all and I'm not seeing an error in-game -- any idea why?",
        "response": (
            "First check your `.tags` field -- if it ends up empty, the engine logs \"Block "
            "{id} is missing 'tags' field\" but doesn't fail loading, so the block still exists, "
            "it just may not behave the way you expect since a lot of block behavior (including "
            "structure-building-block child detection) is driven by tags. Every block should "
            "have at least one tag."
        ),
    },
    {
        "instruction": "What's a minimal item definition for Cubyz?",
        "response": (
            "```\n.{\n    .texture = \"your_item.png\",\n}\n```\n\n"
            "That's genuinely the minimum -- `.stackSize` defaults to 120, `.food` defaults to "
            "0, and the item's display name falls back to its own id if you don't set `.name` "
            "explicitly (which the Addon Creator website never sets, so website-exported items "
            "always display their raw id as the tooltip name unless you hand-add `.name`)."
        ),
    },
    {
        "instruction": "I gave my item a .material block but durability/mass damage/hardness damage/swing speed are all coming out as 0 in-game. Why?",
        "response": (
            "Those four material fields (`durability`, `massDamage`, `hardnessDamage`, "
            "`swingSpeed`) have no soft default in the engine -- if any of them is missing from "
            "the `.material` object, it logs `\"Couldn't find material attribute 'X'\"` and "
            "falls back to exactly `0`, not a sensible placeholder. For durability specifically "
            "that means the item breaks instantly. Double-check all four are actually present; "
            "`textureRoughness` is the one exception in that block that does have a real "
            "default (`1.0`) if omitted."
        ),
    },
    {
        "instruction": "How do I make a minimal biome for Cubyz?",
        "response": (
            "```\n.{\n    .chance = 1.0,\n    .ground_structure = .{\"cubyz:grass\", \"0 to 3 cubyz:dirt\"},\n"
            "    .stoneBlock = \"cubyz:stone\",\n}\n```\n\n"
            "Almost everything else has an engine-side default: min/max radius default to 256, "
            "roughness/hills/mountains default to 0, `.music` defaults to "
            "`\"cubyz:totaldemented/cubyz\"` if omitted (note: the Addon Creator website's own "
            "default is `'cubyz:sunrise'` instead, which only matters if you hand-edit and drop "
            "the field)."
        ),
    },
    {
        "instruction": "I checked \"valid player spawn\" for my biome in the Addon Creator, but new players still aren't spawning there. Is this a known issue?",
        "response": (
            "Yes -- this looks like a real bug in the Addon Creator website, not something "
            "you're doing wrong. The website exports that checkbox as `.isValidPlayerSpawn`, "
            "but the engine's biome loader actually reads a field named `.validPlayerSpawn` "
            "(no \"is\" prefix). Since the names don't match, the engine never sees your value "
            "and falls back to its own default of `false`. If you need this to work right now, "
            "hand-edit the exported `.zig.zon` file and rename the field to `.validPlayerSpawn`."
        ),
    },
    {
        "instruction": "I set a custom sky color and fog color for my biome through the Addon Creator, but in-game it still shows the default blue sky. What's wrong?",
        "response": (
            "This is likely a format mismatch between the website and the engine, not a mistake "
            "on your end. The Addon Creator exports `.skyColor`/`.fogColor` as a 3-component "
            "float vector (`.{r, g, b}`), but the engine's biome loader reads those fields as a "
            "single packed `u32` integer (its own fallback default is literally `0xffbfe2ff`). "
            "A vector literal being read through an integer parser is very likely to fail "
            "silently and fall back to the default color. I'd flag this as a bug to verify "
            "in-game -- worth testing whether a hand-written packed-hex value (e.g. `.skyColor "
            "= 0xff75b2ff`) actually takes effect where the website's vector format doesn't."
        ),
    },
    {
        "instruction": "Do cave biomes need anything special compared to regular biomes?",
        "response": (
            "Yes -- a cave biome (`.isCave = true`) needs at least one tag ending in `_layer`, "
            "or the engine logs \"Cave biome {id} is missing a '_layer' tag to assign it to a "
            "cave layer.\" The Addon Creator's generic tag-pill UI doesn't prompt for this "
            "specifically, so it's easy to miss if you're building a cave biome by hand or "
            "through the website without knowing this convention."
        ),
    },
    {
        "instruction": "How does the reversible field work for Cubyz recipes?",
        "response": (
            "`.reversible` is a boolean (default `false`) you can add to a recipe entry by hand "
            "-- the Addon Creator website doesn't expose it. If set to `true`, the engine "
            "automatically generates the reverse recipe (output becomes an input and vice "
            "versa) alongside the one you defined. It only works for a recipe with exactly one "
            "input and one output total -- if you try it on a multi-ingredient recipe, parsing "
            "fails with `error.InvalidReversibleRecipe`."
        ),
    },
    {
        "instruction": "What's the minimal entity model definition?",
        "response": (
            "```\n.{\n    .model = \"yourname:your_model\",\n    .defaultTexture = \"yourname:your_texture\",\n}\n```\n\n"
            "`.height` defaults to `1` if omitted (note: the Addon Creator website's form "
            "defaults to `2.0` instead, so this only diverges for hand-written files), and "
            "`.coordinateSystem` defaults to `.right_handed_z_up`. Neither `.model` nor "
            "`.defaultTexture` being missing causes an error at load time -- the model or "
            "texture path just ends up empty, and the failure only surfaces later when "
            "something actually tries to render it."
        ),
    },
    {
        "instruction": "My particle addon isn't showing up at all, not even a placeholder texture. What could cause a hard failure like that?",
        "response": (
            "Check whether `.texture` is present -- unlike almost every other field in the "
            "particle system, this one has no fallback. If it's missing, the engine logs "
            "\"Particle texture id was not specified for {id}\" and the particle type fails to "
            "register entirely, so it never shows up at all rather than falling back to a "
            "default look. Also double check your texture's actual pixel dimensions: the "
            "engine requires the base texture's height to be an exact multiple of its width "
            "(used to slice animation frames), or you'll get a dimensions error instead."
        ),
    },
    {
        "instruction": "Why does my particle's rotation velocity in the exported file look different from what I typed in the Addon Creator?",
        "response": (
            "That's expected -- the Addon Creator's rotation velocity fields are in degrees, "
            "and the engine converts them to radians internally after loading. The value "
            "stored in the `.zig.zon` file itself matches what you typed (degrees); the "
            "conversion only happens in memory at runtime, so there's nothing to fix."
        ),
    },
    {
        "instruction": "Is there a difference between what the Addon Creator website lets me configure and what the actual Cubyz engine supports?",
        "response": (
            "Yes, in both directions. Some fields the engine reads have no UI in the website at "
            "all -- e.g. a block's `.selectionCapabilities`, a biome's `.parentBiomes` / "
            "`.transitionBiomes` sub-biome system, an item's full procedural-item parameter "
            "system (as opposed to the simple item form), and a particle's `.loopTime`. These "
            "are only reachable by hand-editing the exported `.zig.zon` files. Conversely, when "
            "the website and engine disagree on a field name or format (like the biome spawn-flag "
            "and sky-color cases), the engine's behavior is what actually matters in-game -- "
            "always trust what the engine parses over what the website happens to produce."
        ),
    },
    {
        "instruction": "How do addons actually get turned from the Addon Creator's UI into a file the game reads?",
        "response": (
            "Filling out a panel (Blocks, Items, Biomes, etc.) and clicking \"Save to Project\" "
            "reads the form fields by their HTML element id and stores them as a plain object in "
            "the browser's in-memory project data. Clicking \"Export Full Addon\" then walks that "
            "project data and writes each object out as a `.zig.zon` file via string "
            "concatenation, organized into the standard Cubyz addon folder layout (`blocks/`, "
            "`items/`, `biomes/`, `entityModels/`, `particles/`, `recipes/`). Importing an "
            "existing addon does the reverse: it regex-parses the `.zig.zon` text back into the "
            "same field names to repopulate the form. Cross-references between objects (a "
            "block's drop item, a biome's surface block) get auto-prefixed with your addon's "
            "namespace if they match something already in your project, or `cubyz:` otherwise."
        ),
    },
    {
        "instruction": "If I reference a block ID that doesn't exist anywhere -- in an item's block field, or a recipe -- what happens?",
        "response": (
            "The engine doesn't crash. Its block-lookup function logs \"Couldn't find block "
            "{id}. Replacing it with air...\" and silently substitutes air (block index 0) for "
            "the missing reference. So a typo'd or misspelled block reference won't error out "
            "loudly -- it'll just behave like whatever consumed that reference is actually "
            "pointing at air, which can look like a confusing, hard-to-spot bug rather than an "
            "obvious failure. Check your logs for that exact message if something's acting like "
            "it references nothing."
        ),
    },
]


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, pair in enumerate(PAIRS):
            f.write(json.dumps({
                "chunk_id": f"addon_reference_handwritten_{i}",
                "source_type": "addon_reference",
                "pairs": [pair],
                "user_id": "handwritten",
            }) + "\n")
    print(f"[OK] Wrote {len(PAIRS)} addon_creator pairs -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
