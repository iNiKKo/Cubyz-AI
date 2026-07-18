# [easy/codebase_assets_cubyz_blocks_lantern__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mineable, blockHealth, drops, viewThrough, rotation, model, lodReplacement
**Concepts:** block properties, mineable blocks, drop behavior, transparency

## Summary
Defines default properties for the lantern block in Cubyz.

## Explanation
This chunk specifies various attributes of the lantern block, including its mineability, health, drop behavior, transparency, rotation model, and level of detail (LOD) replacement. The `.tags` field marks it as mineable. The `blockHealth` is set to 0.5, indicating moderate durability. The `drops` array specifies that it drops items automatically when mined. The block allows view-through with the `viewThrough` flag. The `rotation` property uses a specific model for orientation. The `model` field defines different textures for its sides, ceiling, and floor. Lastly, the `lodReplacement` is set to 'air', suggesting how it should be rendered at lower levels of detail.

## Related Questions
- What tags are assigned to the lantern block?
- How much health does the lantern block have?
- Does the lantern block drop items when mined?
- Can players see through the lantern block?
- Which model is used for rotating the lantern block?
- What textures are applied to different sides of the lantern block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_lantern__defaults.zig.zon_chunk_0*
