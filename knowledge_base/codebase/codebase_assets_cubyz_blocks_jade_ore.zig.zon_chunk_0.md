# [easy/codebase_assets_cubyz_blocks_jade_ore.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mineable, durability, massDamage, hardnessDamage, encased, precious, textureRoughness, veins, density, auto drops
**Symbols:** tags, blockHealth, blockResistance, item, texture, material, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, colors, modifiers, id, strength, restriction, encased, precious, amount, ore, veins, size, minHeight, density, drops, items, rotation, model
**Concepts:** block configuration, material properties, modifier restrictions, vein generation, auto drops

## Summary
Defines the Jade ore block configuration including mining properties, item texture/material data with durability and modifiers, vein generation parameters, drop behavior, rotation/model identifiers, and texture path.

## Explanation
This chunk is a .zon configuration file declaring a single block entity for jade ore. It sets tags to {.mineable} indicating the block can be mined. Block health is 12 and resistance is 6. The item field contains a texture reference 'jade.png' and a material struct with durability 600, massDamage 0.4, hardnessDamage 7, swingSpeed 5, textureRoughness 0.1, and an array of five color values (0xff487c54, 0xff56926e, 0xff66af71, 0xff82c994, 0xffbceab9). The material also includes a modifiers array with one modifier: id 'durable', strength 1.5, and restriction specifying encased precious tag amount 4. The ore field defines vein count 4, size 4, minHeight 350, density 0.3. Drops are configured as an auto-drops array containing one entry with items set to .auto (default drop behavior). Rotation is 'cubyz:ore' and model is 'cubyz:cube'. Texture path is 'cubyz:jade_ore'.

## Related Questions
- What is the health value of the jade ore block?
- How many veins does the jade ore generate and what is its size parameter?
- What are the color values defined for the jade item texture?
- Which tag restriction applies to the durable modifier on jade ore?
- What is the swing speed configured for the jade item?
- Does the jade ore drop items automatically or require manual configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_jade_ore.zig.zon_chunk_0*
