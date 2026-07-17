# [easy/codebase_assets_cubyz_blocks_duckweed.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, blockHealth, drops, allowedToolTags, selectionCapabilities, replaceable, degradable, collide, alwaysViewThrough, absorbedLight, model, rotation, texture0, lodReplacement
**Symbols:** tags, blockHealth, drops, items, allowedToolTags, selectionCapabilities, replaceable, degradable, collide, alwaysViewThrough, absorbedLight, model, rotation, texture0, texture1, texture2, texture3, item, lodReplacement
**Concepts:** block asset configuration, cuttable/sliceable tags, fluid-placeable item, tool-effective selection, replaceable block behavior, texture-based model states

## Summary
Defines the Duckweed block configuration with cuttable/sliceable tags, low health, fluid-placeable item, and texture-based model states.

## Explanation
This chunk declares a single block asset named duckweed. It sets .tags to .{.cuttable, .sliceable}, indicating it can be harvested by cutting or slicing tools. The .blockHealth is 0.1, meaning it breaks instantly on any impact. The .drops entry contains one drop with .items set to .{.auto} and .allowedToolTags restricted to .{.cuttable}, so only cuttable tools yield drops. The block has .selectionCapabilities of .{.toolEffective}, allowing tool-based interaction. It is marked .replaceable = true, meaning it can be placed over other blocks, and .degradable = true, implying it can degrade or be consumed. Collision is disabled (.collide = false), so entities pass through it. The block is always view-through (.alwaysViewThrough = true) with no light absorption (.absorbedLight = 0x000000). Its model references cubyz:plane with four states, and the rotation uses cubyz:texture_pile. Textures are assigned per state (duckweed/0 through duckweed/3), while the item texture is duckweed.png tagged as .fluidPlaceable. The lodReplacement points to cubyz:air for low-detail rendering.

## Related Questions
- What tags are assigned to the duckweed block?
- How does the drop behavior of duckweed differ from other blocks?
- Which tool tags are allowed for dropping items from duckweed?
- Is the duckweed block replaceable and what does that imply?
- Does the duckweed block collide with entities or is it transparent to collision?
- What model reference is used for the duckweed block's rendering?
- How many texture states are defined for the duckweed model?
- Which rotation style is applied to the duckweed block textures?
- What is the LOD replacement target for duckweed when rendering at low detail?
- Is there any light absorption configured for the duckweed block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_duckweed.zig.zon_chunk_0*
