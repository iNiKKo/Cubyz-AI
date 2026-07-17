# [easy/codebase_assets_cubyz_blocks_bluebells.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collide, lodReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, viewThrough, absorbedLight, collide, model, texture, item, lodReplacement, onUpdate
**Concepts:** block configuration, cuttable tags, drop generation, tool selection, replaceable blocks, degradable blocks, view through rendering, light absorption, collision disabling, LOD replacement, update actions

## Summary
Defines the Bluebells block with cuttable/sliceable tags, low health (0.2), drops auto-generated items when cut by a cuttable tool, supports tool-effective selection, is replaceable and degradable, allows view-through rendering, absorbs light color 0x121012, has no collision, uses the cubyz:cross model with bluebells texture, item displays bluebells.png, lodReplacement points to air, and onUpdate runs a check_support_blocks action.

## Explanation
The chunk declares a single block configuration object containing tags (cuttable, sliceable), blockHealth set to 0.2, drops defined as an auto-generated item allowed only by cuttable tools, selectionCapabilities limited to toolEffective, replaceable and degradable flags both true, viewThrough true, absorbedLight color 0x121012, collide false, model string cubyz:cross, texture string cubyz:bluebells, item object with texture bluebells.png, lodReplacement string cubyz:air, and an onUpdate action of type check_support_blocks. No executable logic or functions are present; all fields are static configuration values.

## Related Questions
- What tags are assigned to the Bluebells block?
- How much health does the Bluebells block have?
- Which items drop when the Bluebells block is cut?
- What tool tag is required for the drops to occur?
- Can the Bluebells block be selected with any tool?
- Is the Bluebells block replaceable in the world?
- Does the Bluebells block degrade over time?
- Can players see through the Bluebells block model?
- What color does the Bluebells block absorb light as?
- Does the Bluebells block collide with entities?
- Which model is used for rendering the Bluebells block?
- What texture is applied to the Bluebells block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_bluebells.zig.zon_chunk_0*
