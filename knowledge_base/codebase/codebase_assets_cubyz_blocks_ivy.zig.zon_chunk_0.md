# [easy/codebase_assets_cubyz_blocks_ivy.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, alwaysViewThrough, absorbedLight, lodReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, collide, alwaysViewThrough, absorbedLight, model, rotation, texture, item, lodReplacement
**Concepts:** block configuration, tag metadata, drop generation, tool interaction, selection rules, light absorption, LOD replacement

## Summary
Defines a configuration block for Ivy with cuttable/sliceable tags, low health, tool-specific drops, and texture/model references.

## Explanation
This chunk declares a single configuration object containing tag metadata (.cuttable, .sliceable), numeric properties (blockHealth = 0.2, absorbedLight = 0x121012), boolean flags (replaceable, degradable, collide, alwaysViewThrough), and string references for model ('cubyz:plane'), rotation ('cubyz:carpet'), texture ('cubyz:ivy'), lodReplacement ('cubyz:air'). The drops field is an array with one entry specifying item type .auto and allowedToolTags restricted to .cuttable. SelectionCapabilities lists .toolEffective, indicating the block can be selected only when a tool is active.

## Related Questions
- What tags are assigned to the Ivy block configuration?
- How is the health of the Ivy block defined in this chunk?
- Which tool tag must be present for drops from Ivy to occur?
- What item type does Ivy drop when harvested with a valid tool?
- Under what condition can the Ivy block be selected by the player?
- Does the Ivy block collide with other entities according to this config?
- Is the Ivy block marked as degradable in this configuration?
- Which model is referenced for rendering the Ivy block?
- What rotation identifier is used for Ivy's visual orientation?
- What texture file path is specified for Ivy's item representation?
- To which LOD replacement does Ivy fall back when not visible?
- What absorbedLight value is set for Ivy and how is it encoded?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_ivy.zig.zon_chunk_0*
