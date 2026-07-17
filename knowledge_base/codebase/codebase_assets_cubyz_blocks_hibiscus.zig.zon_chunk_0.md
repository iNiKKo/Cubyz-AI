# [easy/codebase_assets_cubyz_blocks_hibiscus.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collide, model, rotation, texture, lodReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, viewThrough, absorbedLight, collide, model, rotation, texture, texture_top, texture_bottom, item, lodReplacement, onUpdate
**Concepts:** block configuration, cuttable tags, drop generation, tool interaction, replaceability, degradation, view-through rendering, light absorption, collision handling, model referencing, texture mapping, LOD replacement, support block checking

## Summary
Configuration data defining the hibiscus block's properties including cuttable/sliceable tags, health value, drop behavior, selection capabilities, replaceability, degradability, view-through status, lighting absorption (none), collision settings, model and rotation identifiers, texture references for all faces, item representation, LOD replacement target, and an onUpdate hook that checks support blocks.

## Explanation
This chunk is a .zon configuration file containing a single block definition object. The object declares tags (.cuttable, .sliceable) indicating the block can be cut with appropriate tools; blockHealth is set to 0.2 (a float value); drops are defined as an array of one entry where items are auto-generated and only allowed when the tool tag matches .cuttable; selectionCapabilities includes .toolEffective meaning the block responds to tool interactions; replaceable and degradable are both true, allowing replacement by other blocks and degradation over time; viewThrough is true permitting line-of-sight through the block; absorbedLight is 0x000000 (no light absorption); collide is false so entities pass through without collision response; model references cubyz:flower/height_8 for rendering geometry; rotation uses cubyz:planar orientation; texture fields point to cubyz:hibiscus and cubyz:hibiscus_top for side/top/bottom faces; item field defines a placeholder with texture hibiscus.png; lodReplacement sets the low-detail replacement to cubyz:air; onUpdate specifies type .check_support_blocks, indicating runtime logic that verifies whether supporting blocks exist beneath this block.

## Related Questions
- What tags are assigned to the hibiscus block and what do they signify?
- How is the drop behavior configured for this block when cut with a tool?
- Which selection capabilities does the hibiscus block support?
- Is the hibiscus block replaceable by other blocks, and why might that be important?
- What happens to light passing through or being absorbed by this block?
- Does the hibiscus block collide with entities, and what are the implications of collide = false?
- Which model file is used for rendering the hibiscus block geometry?
- How is the rotation of the hibiscus block defined in its configuration?
- What textures are referenced for the side, top, and bottom faces of this block?
- What item representation is provided for the hibiscus block in inventory or drop views?
- To what LOD replacement does the hibiscus block fall back when detail level drops?
- What onUpdate hook type is attached to this block and what operation does it perform?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_hibiscus.zig.zon_chunk_0*
