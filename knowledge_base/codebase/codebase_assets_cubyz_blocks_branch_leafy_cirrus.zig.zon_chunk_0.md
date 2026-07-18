# [easy/codebase_assets_cubyz_blocks_branch_leafy_cirrus.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** block configuration, texture assignment, drop items, LOD replacement, opaque variant
**Concepts:** block properties, texture mapping, item drops

## Summary
Defines properties for a leafy cirrus block, including textures, drop items, and LOD replacement.

## Explanation
This chunk configures the behavior of a specific block type in the Cubyz voxel engine, specifically for a leafy cirrus block. It specifies that the block decays over time and drops 'cubyz:branch/cirrus' items when it does. Additionally, if mined with tools tagged as cuttable (e.g., axes), it can drop 'cubyz:leaves/cirrus'. The block has multiple textures assigned to different faces for rendering: texture6 is 'cubyz:branch/cirrus/dot', texture7 is 'cubyz:branch/cirrus/half_line', texture8 is 'cubyz:branch/cirrus/line', texture9 is 'cubyz:branch/cirrus/bend', texture10 is 'cubyz:branch/cirrus/intersection', and texture11 is 'cubyz:branch/cirrus/cross'. The LOD replacement specifies a simpler version of the block for lower detail levels, which is 'cubyz:leaves/opaque/cirrus', and an opaque variant is provided for solid rendering, also set to 'cubyz:leaves/opaque/cirrus'.

## Related Questions
- What textures are assigned to the leafy cirrus block?
- How does the leafy cirrus block decay?
- What items can be dropped from the leafy cirrus block?
- Which tool tags allow dropping cirrus leaves?
- What is the LOD replacement for the leafy cirrus block?
- What is the opaque variant of the leafy cirrus block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_cirrus.zig.zon_chunk_0*
