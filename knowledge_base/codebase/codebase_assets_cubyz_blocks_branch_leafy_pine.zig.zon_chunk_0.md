# [easy/codebase_assets_cubyz_blocks_branch_leafy_pine.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** block properties, texture mapping, LOD replacement, decay effect, item drops
**Concepts:** block configuration, drop behavior, texturing

## Summary
Defines properties for a leafy pine branch block, including its drop behavior, textures, and LOD replacement.

## Explanation
This chunk defines the configuration for a leafy pine branch block in the Cubyz voxel engine. The block's decay effect is defined as `type = .decay`, meaning it will decay over time. When it decays, it drops pine branches (`drops`), which are specified to be of type `cubyz:branch/pine`. Additionally, the block can drop pine leaves (`cubyz:leaves/pine`) when cut with a tool tagged as `.cuttable`. The block has multiple textures assigned to different faces (6-10) and uses specific LOD replacement textures. The opaque variant for rendering purposes is also specified.

## Related Questions
- What is the type of update for the leafy pine branch block?
- What items does the leafy pine branch drop when it decays?
- Which texture is used for the leafy pine branch block?
- How many different textures are assigned to the leafy pine branch block?
- What is the LOD replacement texture for the leafy pine branch block?
- What is the opaque variant of the leafy pine branch block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_pine.zig.zon_chunk_0*
