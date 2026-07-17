# [easy/codebase_assets_cubyz_blocks_dandelions.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, auto drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, LODReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, collide, alwaysViewThrough, absorbedLight, model, rotation, onUpdate, texture, item, lodReplacement
**Concepts:** block asset definition, cuttable tags, auto drops, tool effective selection, replaceable blocks, degradable materials, view-through rendering, light absorption, LOD replacement

## Summary
Defines the dandelion block asset with cuttable/sliceable tags, low health (0.2), drops auto items when cut by a .cuttable tool, supports toolEffective selection, is replaceable and degradable, does not collide, always view-through, absorbs light color 0x121012, uses plane model/carpet rotation, updates via check_support_blocks logic, and references dandelions texture with an air LOD replacement.

## Explanation
This chunk is a .zon configuration file declaring the dandelion block asset. It sets tags to cuttable and sliceable, which implies the block can be harvested by cutting tools. Block health is explicitly set to 0.2, indicating low durability. Drops are defined as an auto item when allowedToolTags includes cuttable, meaning any tool with the cuttable tag will drop the item automatically without requiring a specific tier. Selection capabilities restrict interaction to .toolEffective, so only tools marked effective can select this block. The replaceable flag is true, allowing other blocks to be placed on top of it during world generation or editing. Degradable is true, suggesting the block may degrade over time or under certain conditions (e.g., weather). Collide is false, meaning entities pass through without collision response. AlwaysViewThrough is true, indicating transparency for rendering purposes. AbsorbedLight is set to 0x121012, a specific color value used for lighting attenuation. Model references cubyz:plane and rotation references cubyz:carpet, defining the visual representation. onUpdate specifies .check_support_blocks as its update logic, implying runtime checks for structural support (e.g., whether it is floating). Texture points to cubyz:dandelions, while item texture is dandelions.png, used when dropped or selected. LODReplacement uses cubyz:air, indicating that at lower detail levels the block becomes invisible/transparent.

## Related Questions
- What tags are assigned to the dandelion block asset?
- How is the health of the dandelion block defined in this configuration?
- Under what conditions does the dandelion block drop items automatically?
- Which selection capability restricts interaction with the dandelion block?
- Is the dandelion block replaceable by other blocks during world generation?
- Does the dandelion block collide with entities or projectiles?
- What visual model and rotation are used for rendering the dandelion block?
- How is light absorption handled for the dandelion block texture?
- What update logic runs each frame for the dandelion block?
- Which texture file is referenced for the dandelion block's appearance?
- What item texture is used when the dandelion block is dropped or selected?
- How does LOD replacement affect the visibility of the dandelion block at low detail levels?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_dandelions.zig.zon_chunk_0*
