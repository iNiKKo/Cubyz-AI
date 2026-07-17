# [easy/codebase_assets_cubyz_blocks_cactus_flower.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, absorbedLight, lodReplacement, hurt damage, check_support_blocks, cactus_flower model
**Symbols:** cactus_flower
**Concepts:** block configuration, cuttable tags, spiky damage, support checking, LOD replacement

## Summary
Defines the cactus_flower block with cuttable/sliceable tags, 0.2 health, spiky damage on touch, support-check updates, and LOD replacement to air.

## Explanation
This chunk declares a single block configuration object containing tags (.cuttable, .sliceable), blockHealth (0.2), drops ({items: auto, allowedToolTags: cuttable}), selectionCapabilities (toolEffective), replaceable (true), degradable (true), collide (false), alwaysViewThrough (true), absorbedLight (0x121012), model/rotation/texture references to cubyz:cactus_flower and its top texture, item texture cactus_flower.png, lodReplacement set to cubyz:air, onTouch event of type hurt with dps 0.2 and damageType spiky, and onUpdate event of type check_support_blocks.

## Related Questions
- What tags are assigned to the cactus_flower block?
- How much health does the cactus_flower block have?
- What items drop when the cactus_flower is cuttable?
- Which tool tag is required for the cactus_flower drops?
- Is the cactus_flower replaceable and degradable?
- Does the cactus_flower collide with other blocks?
- Can players always view through the cactus_flower block?
- What absorbedLight value does the cactus_flower use?
- What model reference is used for the cactus_flower block?
- How is the LOD replacement configured for the cactus_flower?
- What happens when a player touches the cactus_flower block?
- Which update event type runs on the cactus_flower block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_cactus_flower.zig.zon_chunk_0*
