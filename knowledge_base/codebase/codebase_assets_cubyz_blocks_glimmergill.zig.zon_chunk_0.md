# [easy/codebase_assets_cubyz_blocks_glimmergill.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** health, drops, selection capabilities, replaceable, degradable, view-through, light absorption, emitted light, collision, rotation model, update function, model details, textures, item texture, LOD replacement
**Symbols:** Glimmergill
**Concepts:** block configuration, light management, collision detection, modeling, texture mapping, item representation

## Summary
Glimmergill block configuration

## Explanation
Defines the Glimmergill block's properties including:
- **Tags:** .cuttable, .sliceable, .mushroom
- **Health:** 0.2
- **Drops:** { .items = .{.auto}, .allowedToolTags = .{.cuttable} }
- **Selection Capabilities:** toolEffective
- **Replaceability:** true
- **Degradation:** true
- **View Through:** true
- **Light Absorption:** 0x010101 (RGB: 1, 1, 1)
- **Emission Light:** 0x392862 (RGB: 57, 40, 98)
- **Collision Behavior:** false
- **Rotation Model:** cubyz:torch
- **Update Function:** check_support_blocks
- **Model Details:** base = "cubyz:glimmergill/floor", side = "cubyz:glimmergill/shelf"
- **Textures:** texture = "cubyz:glimmergill_side", texture_top = "cubyz:glimmergill_top", texture_bottom = "cubyz:glimmergill_bottom"
- **Item Texture:** glimmergill.png
- **LOD Replacement:** cubyz:air

## Related Questions
- What are the tags associated with the Glimmergill block?
- How is the health of the Glimmergill block defined?
- What items can be dropped when the Glimmergill block is broken?
- What tools are allowed to interact with the Glimmergill block?
- Is the Glimmergill block replaceable?
- Can the Glimmergill block degrade over time?
- Does the Glimmergill block allow light through it?
- What is the color of the light absorbed by the Glimmergill block?
- What is the color of the light emitted by the Glimmergill block?
- Is the Glimmergill block collidable?
- What rotation model is used for the Glimmergill block?
- What function is called when the Glimmergill block updates its state?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_glimmergill.zig.zon_chunk_0*
