# [easy/codebase_assets_cubyz_blocks_baobab_top.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** block properties, compile-time configuration, texture mapping, item drops, decay behavior
**Concepts:** block configuration, voxel engine assets

## Summary
Defines properties for the Baobab top block in Cubyz, including tags, health, drops, rotation, model, textures, and decay behavior.

## Explanation
This chunk defines a configuration object for the Baobab top block in the Cubyz voxel engine. It specifies various properties including tags (choppable, wood, log), block health of 8, item drops consisting of baobab logs, rotation behavior defined by 'cubyz:direction', visual model as 'cubyz:cube', texture mappings for different sides ('cubyz:baobab_log' for all sides except the top which uses 'cubyz:baobab_log_top'), and decay prohibition set to true. The configuration is structured using Zig's comptime data structures, ensuring that these properties are known at compile time.

## Related Questions
- What are the tags associated with the Baobab top block?
- How much health does the Baobab top block have?
- What items can be dropped from the Baobab top block?
- How is the rotation behavior of the Baobab top block defined?
- Which model is used for rendering the Baobab top block?
- What textures are applied to different sides of the Baobab top block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_baobab_top.zig.zon_chunk_0*
