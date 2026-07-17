# [easy/codebase_assets_cubyz_blocks_glimmergill.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, mushroom, blockHealth, drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, emittedLight, rotation, check_support_blocks, lodReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, viewThrough, absorbedLight, emittedLight, collide, rotation, onUpdate, model, texture, texture_top, texture_bottom, item, lodReplacement
**Concepts:** block configuration, tag system, drop mechanics, selection capabilities, light emission, model loading, update logic

## Summary
Defines the Glimmergill block configuration with cuttable/sliceable tags, mushroom classification, health value, drop behavior, selection capabilities, replaceability, degradability, light absorption/emission properties, collision settings, rotation reference, update logic for support checking, and model/texture/item definitions.

## Explanation
This chunk declares a single block configuration object containing tag arrays (.cuttable, .sliceable, .mushroom), numeric health (0.2), drop definition with auto items and allowed tool tags, selection capabilities (.toolEffective), replaceable and degradable flags set to true, viewThrough flag true, absorbedLight hex value 0x010101, emittedLight hex value 0x392862, collide false, rotation string referencing cubyz:torch, onUpdate type .check_support_blocks, model base and side strings, texture names for top/bottom/side, item texture reference to glimmergill.png, and lodReplacement set to cubyz:air.

## Related Questions
- What tags are assigned to the Glimmergill block?
- How is the health of the Glimmergill block defined?
- Which items drop when the Glimmergill block is broken and what tool tags allow it?
- Can the Glimmergill block be selected with any tool or only specific ones?
- Is the Glimmergill block replaceable in the world?
- Does the Glimmergill block degrade over time when exposed to elements?
- Can players see through the Glimmergill block?
- What light values does the Glimmergill block absorb and emit?
- Is collision enabled for the Glimmergill block?
- Which rotation reference is used for the Glimmergill block?
- What update logic runs on the Glimmergill block each tick?
- What model files are loaded for the base and side of the Glimmergill block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_glimmergill.zig.zon_chunk_0*
