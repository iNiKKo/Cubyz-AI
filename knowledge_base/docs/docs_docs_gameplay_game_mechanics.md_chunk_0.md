# [easy/docs_docs_gameplay_game_mechanics.md] - Chunk 0

**Type:** gameplay
**Keywords:** health, energy, walking, sprinting, crouching, inventory, hotbar, crafting, building, destruction, tools, damage, resistance
**Symbols:** health, energy, movement, inventory, hotbar, building, destruction
**Concepts:** player mechanics, health system, energy system, movement controls, inventory management, block placement and destruction

## Summary
This page covers player mechanics in Cubyz, including health, energy, movement, inventory management, and building/destruction systems.

## Explanation
Health: the player has a total of 16 health points represented by 8 hearts. Health can be lost from fall damage or hazardous blocks (cacti, lava, magma), but there is currently no way to regain health other than dying. Energy: represented by 8 bars; currently does nothing -- there is no way to gain or lose energy. Movement: the player has 3 means of movement -- walking, sprinting (same as walking but faster), and crouching (slowest, but prevents falling off blocks unless the block is slippery; stepping down from smaller blocks like stairs is still possible while crouching). Crouching also lets the player fit into 1.5-block-tall spaces. The player can also jump, with enough elevation to cross exactly 1 whole block (this is a separate fact from the 1.5-block crouch-space number -- do not confuse the two). Directional control is much weaker while airborne mid-jump. Inventory and hotbar: the hotbar has 12 slots (see the Controls documentation for the exact key bound to each slot). Pressing E (by default) opens the separate inventory screen, which has 20 slots; items there must be left-click-dragged into the hotbar before they can be equipped. Both the hotbar and inventory can each stack up to 120 items per slot. Above the inventory is a crafting button (opens the crafting menu) and a bag slot, which can hold 120 stacks of items. Building and destruction: right-click (by default) places a block, left-click (by default) starts destroying the block on the crosshair. Blocks have health and resistance stats: health is how much damage is needed to destroy the block, and dealt damage is reduced by the block's resistance -- if resistance exceeds the damage you can deal, the block cannot be damaged at all. Tools are specialized per block type: pickaxes deal damage to stone, metal, and gem blocks; shovels (shovers) deal damage to soil blocks; axes deal damage to wooden blocks; sickles damage plants, leaves, and cloth, and are the only way to actually collect plants/leaves (not possible bare-handed). Using a tool on the wrong block type deals the same damage as bare hands -- no bonus, no penalty.

## Related Questions
- How many health points does the player have in Cubyz?
- Can the player regain health in Cubyz?
- What are the three means of movement available to the player?
- How high can the player jump in Cubyz?
- How many block-tall spaces can a crouching player fit into?
- How do you open the inventory screen in Cubyz?
- How many slots are in the hotbar by default?
- What is the maximum number of items each slot in the inventory or hotbar can hold?
- How many stacks can the bag slot hold?
- How does crouching affect the player's ability to fall off blocks?
- What tool is used to mine stone, metal, and gem blocks?
- What tool is used to mine wooden blocks?
- What tool is used to harvest plants, leaves, and cloth?
- What happens if you use the wrong tool type on a block?
- What determines the amount of damage needed to destroy a block?

*Source: unknown | chunk_id: docs_docs_gameplay_game_mechanics.md_chunk_0*
