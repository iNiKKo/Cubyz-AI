# [easy/codebase_assets_cubyz_blocks_obsidian.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mineable, blockHealth, drops, durability, massDamage, hardnessDamage, textureRoughness, fragile modifier, stairs rotation, cube model
**Symbols:** .tags, blockHealth, blockResistance, drops, items, item, material, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, colors, modifiers, id, strength, allowOres, rotation, model, texture
**Concepts:** block asset definition, mineable tag, drop configuration, item material properties, color palette, modifier system, stairs rotation variant, cube model reference

## Summary
Defines the Obsidian block asset with its mining properties, drop configuration, item material stats (durability, damage values, texture roughness), color palette, modifiers, and model/texture references.

## Explanation
This chunk declares a single static object containing all metadata for the Obsidian block. The .tags field lists {.mineable} indicating it is mineable. blockHealth is set to 16 and blockResistance to 2. The drops array contains one entry with items set to .auto, meaning the drop behavior is handled automatically by the engine. The item subobject defines material properties: durability of 55, massDamage of 1.7, hardnessDamage of 5.7, swingSpeed of 2.5, and textureRoughness of 0.1. The colors array provides five hex values (0xff0F0811, 0xff19121C, 0xff312436, 0xff69486B, 0xff462F47). A modifiers array includes one modifier with id 'fragile' and strength 0.33. The allowOres flag is true. The rotation is set to the stairs variant ('cubyz:stairs'), while model and texture both reference the cube variant ('cubyz:cube', 'cubyz:obsidian').

## Related Questions
- What is the blockHealth value for Obsidian?
- Which tags are assigned to this block asset?
- How many colors are defined in the material palette?
- What is the durability of the Obsidian item?
- Does this block allow ores to be found within it?
- What rotation variant is used for this block model?
- Which modifier is applied and what is its strength value?
- Is the drop behavior set to auto or manual?
- What texture file path is referenced for Obsidian?
- How does the massDamage property affect gameplay?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_obsidian.zig.zon_chunk_0*
