# [easy/codebase_assets_cubyz_blocks_branch_leafy_pine.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** decay, drops, cuttable, texture, lodReplacement, opaqueVariant, branch/pine, leaves/pine, tool tags, item drops
**Symbols:** onUpdate, drops, texture, texture6, texture7, texture8, texture9, texture10, texture11, lodReplacement, opaqueVariant
**Concepts:** block configuration, decay mechanics, item drops, tool tags, texture mapping

## Summary
Defines the leafy pine block configuration with decay behavior, drop items, and texture mappings.

## Explanation
This chunk declares a single object representing the leafy pine block. It sets onUpdate.type to .decay indicating the block decays over time; its drops array contains two entries: one dropping cubyz:branch/pine when decayed, and another dropping cubyz:leaves/pine only when hit with a tool tagged as cuttable. Texture fields map various face indices (texture through texture11) to specific pine branch/leaf textures, while lodReplacement and opaqueVariant both reference the opaque leaves texture for LOD handling.

## Related Questions
- What items does the leafy pine block drop when it decays?
- Under what condition does the leaves/pine item drop from the block?
- Which texture is used for the LOD replacement of the leafy pine block?
- How many texture fields are defined in this block configuration?
- What tool tag is required to harvest leaves from the pine branch block?
- Does the decay onUpdate have any additional parameters besides type and drops?
- Are there any other blocks that share the same opaqueVariant texture as leafy pine?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_pine.zig.zon_chunk_0*
