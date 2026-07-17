# [easy/codebase_assets_cubyz_blocks_voidstone__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, modifiers, drops, blockHealth, blockResistance, encased
**Symbols:** .tags, .blockHealth, .drops, .item, .material, .durability, .massDamage, .hardnessDamage, .swingSpeed, .textureRoughness, .colors, .modifiers
**Concepts:** block configuration, item properties, modifier system, drop mechanics, material attributes

## Summary
Defines the Voidstone block configuration including its tags, health, resistance, drops, and item properties such as durability, damage values, texture colors, and modifiers.

## Explanation
This chunk declares a single struct instance representing the Voidstone block. The struct contains a .tags array with stone, mineable, and voidstone identifiers; a .blockHealth scalar set to 60; a .blockResistance scalar set to 5; a .drops array containing one entry that specifies an auto-drop of the associated item; and a nested .item object defining material properties. The material includes a .durability value of 200, a .massDamage float of 3.0, a .hardnessDamage float of 7.0, a .swingSpeed float of 4.7, a .textureRoughness float of 0.2, and a .colors array with five hex color values. The material also includes a .modifiers array containing two modifier objects: the first is an id 'durable' with strength 0.1; the second has id 'good_at', strength 0.5, tag voidstone, and a restriction object specifying id encased, tag precious, and amount 2.

## Related Questions
- What is the durability value of the Voidstone item?
- Which tags are assigned to the Voidstone block?
- How much mass damage does the Voidstone item deal?
- What hardness damage does the Voidstone item inflict?
- Is there a modifier that restricts usage to encased precious blocks, and what is its strength?
- Does the Voidstone drop anything automatically when mined?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_voidstone__defaults.zig.zon_chunk_0*
