# [easy/codebase_assets_cubyz_blocks_osier.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, alwaysViewThrough, absorbedLight, texture, lodReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, collide, alwaysViewThrough, absorbedLight, model, rotation, onUpdate, texture, item, lodReplacement
**Concepts:** block configuration, drop mechanics, selection capabilities, light absorption, LOD replacement, update hooks

## Summary
Defines the Osier block configuration with cuttable/sliceable tags, health value, drop behavior, selection capabilities, replaceability, degradability, collision settings, light absorption, model/rotation references, texture and item definitions, LOD replacement, and an onUpdate hook for support checking.

## Explanation
This chunk is a .zon configuration file that declares the Osier block's static properties. It sets tags to cuttable and sliceable, assigns a blockHealth of 0.2, defines drops as auto with allowedToolTags restricted to cuttable, enables toolEffective selection capabilities, marks the block as replaceable and degradable, disables collision (collide = false), sets alwaysViewThrough to true, specifies absorbedLight as 0x121012, references model cubyz:plane and rotation cubyz:carpet, provides texture cubyz:osier, defines item with texture osier.png, sets lodReplacement to cubyz:air, and includes an onUpdate hook of type check_support_blocks.

## Related Questions
- What tags are assigned to the Osier block?
- How is the health of the Osier block defined?
- Which tool tag is required for drops from the Osier block?
- What selection capabilities does the Osier block support?
- Is the Osier block replaceable in the world?
- Does the Osier block collide with other blocks?
- Can players see through the Osier block by default?
- What is the absorbedLight value for the Osier block?
- Which model and rotation are referenced for the Osier block?
- What texture is used for the Osier item?
- What LOD replacement does the Osier block use?
- What type of onUpdate hook is configured for the Osier block?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_osier.zig.zon_chunk_0*
