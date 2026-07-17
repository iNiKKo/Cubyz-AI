# [easy/codebase_assets_cubyz_blocks_vetch.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collide, model, texture, lodReplacement, onUpdate
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, viewThrough, absorbedLight, collide, model, texture, item, lodReplacement, onUpdate
**Concepts:** block configuration, drop mechanics, tool interaction tags, selection capabilities, light absorption, LOD replacement, support block checking

## Summary
Defines the vetch block configuration with cuttable/sliceable tags, health value, drop behavior, selection capabilities, replaceability, degradability, view-through property, absorbed light color, collision setting, model and texture references, item definition, LOD replacement, and an onUpdate hook that checks support blocks.

## Explanation
The chunk declares a single block configuration object containing tags (.cuttable, .sliceable), blockHealth (0.2), drops with auto items allowed only by the cuttable tool tag, selectionCapabilities set to toolEffective, replaceable and degradable both true, viewThrough true, absorbedLight as 0x121012, collide false, model string cubyz:cross, texture string cubyz:vetch, item object with texture vetch.png, lodReplacement string cubyz:air, and an onUpdate hook of type check_support_blocks.

## Related Questions
- What tags are assigned to the vetch block?
- What is the health value of the vetch block?
- How does the drop configuration for vetch work?
- Which tool tag allows selection of the vetch block?
- Is the vetch block replaceable and degradable?
- Does the vetch block allow viewing through it?
- What color is absorbed by the vetch block's light property?
- Does the vetch block collide with entities?
- Which model and texture are used for the vetch block?
- What item representation does the vetch block have?
- What LOD replacement is configured for the vetch block?
- What type of onUpdate hook is attached to the vetch block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_vetch.zig.zon_chunk_0*
