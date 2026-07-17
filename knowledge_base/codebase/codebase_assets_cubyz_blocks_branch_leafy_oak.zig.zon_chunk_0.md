# [easy/codebase_assets_cubyz_blocks_branch_leafy_oak.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** decay, drops, branch, leaves, cuttable, texture, lodReplacement, opaqueVariant
**Symbols:** .onUpdate, .drops, .texture, .texture6, .texture7, .texture8, .texture9, .texture10, .texture11, .lodReplacement, .opaqueVariant
**Concepts:** block configuration, decay event, item drops, tool tag constraints, texture variants, LOD replacement, opaque variant

## Summary
Defines the leafy oak block configuration with decay behavior, drop items (branch and leaves), multiple texture variants for LOD replacement, and an opaque variant.

## Explanation
This chunk declares a single object representing the leafy oak block. Its .onUpdate field specifies a decay event that drops cubyz:branch/oak. The .drops array contains two entries: one dropping only cubyz:branch/oak, and another dropping cubyz:leaves/oak with an allowedToolTags constraint of cuttable. Texture fields map to cubyz:leaves/oak (base), cubyz:branch/oak/dot, cubyz:branch/oak/half_line, cubyz:branch/oak/line, cubyz:branch/oak/bend, cubyz:branch/oak/intersection, and cubyz:branch/oak/cross. The lodReplacement and opaqueVariant both reference cubyz:leaves/opaque/oak.

## Related Questions
- What items does the leafy oak block drop when it decays?
- Which texture is used as the base for the leafy oak block?
- What tool tag is required to harvest cubyz:leaves/oak from the leafy oak block?
- Where is the opaque variant of the leafy oak leaves defined in this configuration?
- How many distinct texture variants are specified for the branch side of the leafy oak block?
- Does the decay event drop any items other than cubyz:branch/oak?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_leafy_oak.zig.zon_chunk_0*
