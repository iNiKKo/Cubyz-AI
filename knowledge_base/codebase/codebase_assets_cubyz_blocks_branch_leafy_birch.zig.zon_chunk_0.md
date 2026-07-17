# [easy/codebase_assets_cubyz_blocks_branch_leafy_birch.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** decay, drops, cuttable, texture, lodReplacement, opaqueVariant, branch, leaves, toolTag, item
**Symbols:** .onUpdate, .decay, .drops, .items, .allowedToolTags, .cuttable, .texture, .texture6, .texture7, .texture8, .texture9, .texture10, .texture11, .lodReplacement, .opaqueVariant
**Concepts:** block configuration, decay mechanics, item drops, tool tag filtering, texture mapping, LOD replacement

## Summary
Defines the leafy birch block configuration with decay behavior, drop items, and texture mappings.

## Explanation
This chunk declares a block definition for 'leafy_birch' containing an onUpdate callback of type .decay that drops cubyz:branch/birch when decaying. The drops field lists two entries: one dropping cubyz:branch/birch unconditionally, and another dropping cubyz:leaves/birch only when the tool tag is cuttable. Texture fields map to various branch and leaf variants (dot, half_line, line, bend, intersection, cross) plus an opaque variant for LOD replacement.

## Related Questions
- What items does the leafy birch block drop when it decays?
- Under what condition is cubyz:leaves/birch dropped from the leafy birch block?
- Which texture files are referenced for the leafy birch branch variants?
- What is the purpose of the lodReplacement field in this block definition?
- How does the allowedToolTags filter affect item drops on the leafy birch block?
- What opaque variant is used as a fallback for LOD replacement on the leafy birch block?
- Does the decay onUpdate callback include any additional parameters besides type and drops?
- Are there any other texture fields beyond texture through texture11 defined in this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_birch.zig.zon_chunk_0*
