"""
Hand-authored, densely-covered fine-tuning pairs for narrow, enumerable Cubyz facts that the
distributed generation campaign under-covered -- written directly from the same raw doc source
already fully read and verified during the docs audit earlier in this project, not through the
campaign.

Why this exists: test_inference.py against the first trained adapter showed a clear pattern --
judgment/reasoning-style answers (code review shape, allocator concepts) held up well because
they were reinforced across hundreds of similar review pairs, while narrow specific facts
(exact keybindings, exact numbers, exact names) mostly did NOT stick, because each one only had
a single training pair (or none) generated for it -- the campaign's "scale pairs to distinct
content" prompt logic naturally caps how many pairs come out of one chunk, which badly
undercounts a chunk like the full keybinding table (~40 individual facts) that could support far
more dedicated pairs than the 3-6 the campaign produced for it as a whole. This file adds direct,
often multiply-phrased coverage for exactly the facts that failed in that test, plus full
coverage of every keybinding rather than a sampled handful, so repetition during training
actually reinforces them.

Every claim below is traceable to a specific raw source chunk already read verbatim during this
project's docs audit (gameplay_controls.md, development_history.md, gameplay_game_mechanics.md,
installation.md, README.md, development_multiplayer.md, addon reference docs) -- nothing here is
new extraction, just much denser restyling of facts already confirmed true.
"""
import json
import os

# Same reasoning as generate_addon_pairs.py: deliberately NOT inside finetune/pairs/, which is
# server_finetune.py's own managed output and gets wiped on a hard reset.
OUTPUT_FILE = "pipeline/finetune/handwritten_pairs/core_facts_pairs.jsonl"

PAIRS = [
    # --- Movement keybindings (docs_docs_gameplay_controls.md) ---
    {"instruction": "What key do I press to move forward in Cubyz?", "response": "W."},
    {"instruction": "What key moves the player backward?", "response": "S."},
    {"instruction": "Which key strafes the player left?", "response": "A."},
    {"instruction": "Which key strafes the player right?", "response": "D."},
    {"instruction": "What key makes the player sprint?", "response": "Left control."},
    {"instruction": "What key makes the player jump?", "response": "Space."},
    {"instruction": "How do you crouch in Cubyz?", "response": "Press left shift."},
    {"instruction": "What key toggles flying in Cubyz?", "response": "F."},
    {"instruction": "What key toggles ghost mode?", "response": "G."},
    {"instruction": "What key activates hyperspeed?", "response": "H."},
    {"instruction": "How do you descend while flying in Cubyz?", "response": "Left shift -- the same key used for crouching and falling while flying."},

    # --- Block interaction keybindings ---
    {"instruction": "What button places a block in Cubyz?", "response": "Right mouse button."},
    {"instruction": "What button breaks a block in Cubyz?", "response": "Left mouse button."},
    {"instruction": "How do you pick a block (select it into your hotbar) in Cubyz?", "response": "Middle mouse button."},
    {"instruction": "What key drops an item in Cubyz?", "response": "Q."},

    # --- Utility keybindings ---
    {"instruction": "What key takes a background image/screenshot in Cubyz?", "response": "Print Screen."},
    {"instruction": "What key toggles fullscreen mode in Cubyz?", "response": "F11."},
    {"instruction": "What key opens the regular inventory in Cubyz?", "response": "E."},
    {"instruction": "What key opens the creative inventory in Cubyz?", "response": "C."},
    {"instruction": "I want to open my creative inventory in Cubyz -- what's the keybind?", "response": "C."},
    {"instruction": "How do you open chat in Cubyz?", "response": "T."},
    {"instruction": "What key or character opens the command line in Cubyz?", "response": "/."},
    {"instruction": "What key hides the menu in Cubyz?", "response": "F1."},
    {"instruction": "What key hides the display item in Cubyz?", "response": "F2."},

    # --- Overlay keybindings ---
    {"instruction": "What key toggles the debug overlay in Cubyz?", "response": "F3."},
    {"instruction": "What key toggles the performance overlay in Cubyz?", "response": "F4."},
    {"instruction": "What key toggles the GPU overlay in Cubyz?", "response": "F5."},
    {"instruction": "What key toggles the network overlay in Cubyz?", "response": "F6."},
    {"instruction": "What key toggles the advanced network overlay in Cubyz?", "response": "F7."},

    # --- Hotbar ---
    {"instruction": "What keys select hotbar slots 1 through 9 in Cubyz?", "response": "The number keys 1 through 9, in order."},
    {"instruction": "What keys select hotbar slots 10, 11, and 12 in Cubyz?", "response": "0 selects slot 10, - selects slot 11, and = selects slot 12."},

    # --- History (docs_docs_development_history.md, docs_README.md) ---
    {"instruction": "Who created Cubyz and when?", "response": "zenith391 and ZaUserA created it on August 22, 2018."},
    {"instruction": "Who currently maintains Cubyz?", "response": "IntegratedQuantum, also known as QuantumDeveloper."},
    {"instruction": "Who are the original creators of Cubyz, as opposed to who maintains it today?", "response": "zenith391 and ZaUserA created it in 2018; today it's maintained by IntegratedQuantum (QuantumDeveloper)."},
    {"instruction": "What was Cubyz originally called before its current name?", "response": "Cubz."},
    {"instruction": "Before it was called Cubyz, what was this game's name?", "response": "Cubz."},
    {"instruction": "When was the project renamed from Cubz to Cubyz?", "response": "March 17, 2019, when zenith391 suggested the new name in Discord."},
    {"instruction": "When did the Zig rewrite of Cubyz begin?", "response": "August 2022."},
    {"instruction": "Why was Cubyz rewritten from Java to Zig?", "response": "Java's garbage collector caused freeze-inducing lag spikes when the memory limit was hit; Zig's built-in cross-compilation support (letting QuantumDeveloper build for Windows and test via Wine) was also a major draw over alternatives like C++20 or Rust."},
    {"instruction": "When was Cubyz version 0.0.0 released?", "response": "October 5, 2025."},

    # --- Gameplay mechanics (docs_docs_gameplay_game_mechanics.md) ---
    {"instruction": "How much health does the player start with in Cubyz?", "response": "8 hearts, for a total of 16 health points."},
    {"instruction": "Can the player heal in Cubyz?", "response": "No -- there is currently no way to regain health other than dying."},
    {"instruction": "Is there any way to regain lost health in Cubyz?", "response": "No -- currently the only way to reset your health is to die."},
    {"instruction": "What does the energy/stomach bar do in Cubyz?", "response": "Currently nothing -- it's purely cosmetic. There's no way to gain or lose energy yet."},
    {"instruction": "How many movement modes does the player have in Cubyz?", "response": "Three: walking, sprinting, and crouching."},
    {"instruction": "How high can the player jump in Cubyz?", "response": "Enough elevation to cross one whole block."},
    {"instruction": "How many hotbar slots does Cubyz have by default?", "response": "12."},
    {"instruction": "How many items can a single hotbar or inventory slot stack in Cubyz?", "response": "120."},
    {"instruction": "How many slots does the main inventory have in Cubyz?", "response": "20."},
    {"instruction": "What tool is used to mine stone, metal, and gem blocks in Cubyz?", "response": "Pickaxe."},
    {"instruction": "What tool is used to damage or mine soil blocks in Cubyz?", "response": "Shover (shovel)."},
    {"instruction": "What tool is used to mine wooden blocks in Cubyz?", "response": "Axe."},
    {"instruction": "What tool is used to harvest plants, leaves, and cloth in Cubyz?", "response": "Sickle -- it's also the only tool that lets you collect plants and leaves at all, which isn't possible bare-handed."},
    {"instruction": "What happens if you use the wrong tool type on a block in Cubyz?", "response": "It deals the same damage as using your bare hands -- no bonus, no penalty."},

    # --- Installation / system requirements (docs_README.md, docs_docs_installation.md) ---
    {"instruction": "Is Cubyz available on Mac? Why or why not?", "response": "No -- Mac is not supported because it lacks OpenGL 4.3."},
    {"instruction": "What operating systems does Cubyz support?", "response": "Windows and Linux."},

    # --- Networking (docs_docs_development_multiplayer.md, and the network.zig review pair) ---
    {"instruction": "How does Cubyz send player position updates over the network?", "response": "Via the playerPosition struct, which handles sending and receiving player position updates and ensures they're sent no more than once every 50 milliseconds."},
    {"instruction": "What is the default multiplayer server port for Cubyz?", "response": "47649."},
    {"instruction": "Which port does a Cubyz server listen on unless I change it?", "response": "47649."},
    {"instruction": "How do I grant a player full admin permissions via the Cubyz permission command?", "response": "/perm add whitelist @<playerIndex> /"},
    {"instruction": "How do I grant a player access to just the /spawn command in Cubyz?", "response": "/perm add whitelist @<playerIndex> /command/spawn"},
    {"instruction": "What network protocol does Cubyz use for its multiplayer port forwarding?", "response": "UDP."},
    {"instruction": "How far can the Cubyz world extend on each axis?", "response": "2 billion blocks on each axis -- not literally infinite, but effectively so for gameplay purposes."},
    {"instruction": "How big is the Cubyz world -- is it truly infinite?", "response": "Not literally infinite, but effectively so for gameplay purposes -- the world extends 2 billion blocks on each axis."},

    # --- Addon/engine facts (reinforcing existing addon_creator_pairs.jsonl coverage) ---
    {"instruction": "What happens if an addon references a block ID that doesn't exist?", "response": "The engine doesn't crash -- it logs \"Couldn't find block {id}. Replacing it with air...\" and silently substitutes air (block index 0) for the missing reference."},
    {"instruction": "Why might a biome's custom sky or fog color not show up in-game even though it's set in the Addon Creator?", "response": "Likely a format mismatch, not a mistake on your end -- the Addon Creator website exports skyColor/fogColor as a 3-component float vector, but the engine's biome loader reads those fields as a single packed u32 integer, which typically fails silently and falls back to the default color."},
]


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, pair in enumerate(PAIRS):
            f.write(json.dumps({
                "chunk_id": f"core_facts_handwritten_{i}",
                "source_type": "docs",
                "pairs": [pair],
                "user_id": "handwritten",
            }) + "\n")
    print(f"[OK] Wrote {len(PAIRS)} core-facts pairs -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
