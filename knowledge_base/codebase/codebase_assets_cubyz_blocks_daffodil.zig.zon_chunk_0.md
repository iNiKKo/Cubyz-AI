# [easy/codebase_assets_cubyz_blocks_daffodil.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, auto-drop, allowedToolTags, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collide, model, rotation, texture
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, viewThrough, absorbedLight, collide, model, rotation, texture, texture_top, texture_bottom, item, lodReplacement, onUpdate
**Concepts:** block configuration, cuttable tags, drop behavior, selection capabilities, replaceability, degradability, view-through rendering, light absorption, collision handling, model and rotation identifiers, texture mapping, item representation, LOD replacement, support block checking

## Summary
Defines the daffodil block configuration with cuttable/sliceable tags, health value, drop behavior, selection capabilities, replaceability, degradability, view-through property, lighting absorption (none), collision disabled, model and rotation identifiers, texture mappings for all faces, item representation, LOD replacement to air, and an onUpdate hook that checks support blocks.

## Explanation
The chunk declares a single block configuration object containing tags (.cuttable, .sliceable) indicating the block can be cut or sliced; blockHealth set to 0.2 defining its durability; drops array with one entry specifying auto-drop items and allowedToolTags restricted to .cuttable; selectionCapabilities includes .toolEffective meaning tools are effective on this block; replaceable is true allowing replacement by other blocks; degenerative is true indicating it can degrade over time; viewThrough is true permitting line-of-sight through the block; absorbedLight is 0x000000 (no light absorption); collide is false so entities pass through without collision; model references cubyz:flower/height_8 and rotation uses cubyz:planar; texture fields map to cubyz:daffodil for side faces, cubyz:daffodil_top for top and bottom; item field provides a daffodil.png texture for the dropped item; lodReplacement is set to cubyz:air indicating LOD fallback to air block; onUpdate contains a single hook of type .check_support_blocks which runs each tick to verify support blocks beneath the block.

## Related Questions
- What tags are assigned to the daffodil block and what do they signify?
- How is the health of the daffodil block defined in this configuration?
- Which tool tag is required for the daffodil block to drop items automatically?
- Does the daffodil block allow players to select it with tools, and if so how?
- Is the daffodil block replaceable by other blocks when placed or mined?
- Can the daffodil block degrade over time, and what does that imply for gameplay?
- Does light pass through the daffodil block without absorption, and why is absorbedLight set to zero?
- Is collision enabled on the daffodil block, and how does this affect entity movement?
- What model identifier is used for rendering the daffodil block in the engine?
- How is the rotation of the daffodil block specified, and what does planar mean here?
- Which textures are applied to the side faces versus top/bottom faces of the daffodil block?
- What texture is used for the item representation when the daffodil block drops?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_daffodil.zig.zon_chunk_0*
