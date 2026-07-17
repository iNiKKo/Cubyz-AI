# [easy/codebase_assets_cubyz_blocks_branch_leafy_baobab.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** decay, drops, cuttable, texture, lodReplacement, opaqueVariant, branch, leaves
**Symbols:** onUpdate, drops, texture, texture6, texture7, texture8, texture9, texture10, lodReplacement, opaqueVariant
**Concepts:** block configuration, decay mechanics, item drops, tool restrictions, texture mapping

## Summary
Defines the leafy baobab block configuration including decay behavior, drop items, and texture mappings.

## Explanation
This chunk declares a single block definition with an onUpdate hook set to .decay that drops cubyz:branch/baobab. The drops field contains two entries: one dropping only cubyz:branch/baobab, and another dropping both cubyz:branch/baobab and cubyz:leaves/baobab while restricting the latter to tools tagged as cuttable. Texture fields map six variants (texture through texture10) to specific baobab branch textures including dot, half_line, line, bend, intersection, and cross. The lodReplacement and opaqueVariant both reference cubyz:leaves/opaque/baobab.

## Related Questions
- What items are dropped when the leafy baobab block decays?
- Which texture is assigned to the main face of the leafy baobab block?
- How does the drop configuration differentiate between branch and leaves?
- What tool tag restricts picking up the leaves variant?
- Where are the LOD replacement and opaque variant textures defined for this block?
- List all texture variants referenced in the leafy baobab block definition
- Does the decay onUpdate hook drop any items other than cubyz:branch/baobab?
- What is the purpose of the texture6 field in this block configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_baobab.zig.zon_chunk_0*
