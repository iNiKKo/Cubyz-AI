# [easy/codebase_assets_cubyz_blocks_marigold.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, health, drops, selection capabilities, replaceable, degradability, view-through, absorbed light, collision, model, texture, item, LOD replacement, update function
**Symbols:** Marigold
**Concepts:** block configuration, properties, behavior

## Summary
Marigold block configuration.

## Explanation
This chunk defines the Marigold block's properties and behaviors in detail. It includes the following specific values:
- Tags: `.cuttable`, `.sliceable`
- Health: `blockHealth = 0.2`
- Drops: `{ .items = {.auto}, .allowedToolTags = { .cuttable } }
- Selection capabilities: `.toolEffective`
- Replaceability: `replaceable = true`
- Degradability: `degradable = true`
- View-through property: `viewThrough = true`
- Absorbed light level: `absorbedLight = 0x121012`
- Collision behavior: `collide = false`
- Model: `model = "cubyz:cross"`
- Texture: `texture = "cubyz:marigold"`
- Item appearance: `{ .texture = "marigold.png" }`
- LOD replacement: `lodReplacement = "cubyz:air"`
- Update function type: `.check_support_blocks`

## Related Questions
- What are the tags associated with the Marigold block?
- How is the Marigold block's health defined?
- What items can be dropped when breaking the Marigold block?
- Which tools can effectively select the Marigold block?
- Is the Marigold block replaceable?
- Can the Marigold block degrade over time?
- Does the Marigold block allow players to see through it?
- What is the absorbed light level of the Marigold block?
- Does the Marigold block collide with other blocks?
- What model is used for rendering the Marigold block?
- What texture is applied to the Marigold block in-game?
- What item appears when holding a Marigold block in the inventory?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_marigold.zig.zon_chunk_0*
