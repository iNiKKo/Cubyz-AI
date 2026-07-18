# [easy/codebase_assets_cubyz_blocks_branch_leafy_oak.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** onUpdate, drops, textures, decay effect, LOD replacement
**Concepts:** block configuration, drop mechanics, texture mapping

## Summary
Defines properties for the leafy oak branch block, including textures and drop items.

## Explanation
This chunk defines configuration settings for a specific type of block in the Cubyz voxel engine. The block is identified as a 'leafy oak branch' and includes several properties:

- **onUpdate**: Specifies behavior when the block updates, with a decay effect that drops an oak branch item.
- **drops**: Lists items that can drop from the block, including oak branches and oak leaves (with a condition that the tool used must be cuttable).
- **texture**: Base texture for the block.
- **texture6 to texture11**: Additional textures for different orientations or states of the branch.
- **lodReplacement**: Texture used for lower detail levels (LOD) when the block is far away.
- **opaqueVariant**: Alternative opaque version of the block for rendering purposes.

## Related Questions
- What is the decay behavior of the leafy oak branch block?
- Which items can drop from the leafy oak branch block?
- What are the different textures associated with the leafy oak branch block?
- How does the leafy oak branch block handle lower detail levels (LOD)?
- What tool tags are allowed to drop oak leaves from the leafy oak branch block?
- Which opaque variant is used for rendering the leafy oak branch block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_oak.zig.zon_chunk_0*
