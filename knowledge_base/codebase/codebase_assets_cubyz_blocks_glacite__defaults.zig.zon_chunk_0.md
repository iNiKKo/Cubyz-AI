# [easy/codebase_assets_cubyz_blocks_glacite__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, colors, modifiers, restriction, mineable, glacite
**Symbols:** tags, blockHealth, blockResistance, drops, item, material, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, colors, modifiers, id, strength, tag, restriction
**Concepts:** block configuration, item properties, modifier system, color palette definition, drop table setup

## Summary
Defines the default configuration for the glacite block, specifying its tags, health, resistance, drops, and item properties including durability, damage values, texture roughness, color palette, and modifiers.

## Explanation
This chunk declares a single struct instance with fields: tags (array of .stone, .mineable, .glacite), blockHealth (25), blockResistance (1), drops (array containing one item entry with auto items), and item (struct containing material subfields). The material subfield defines durability (65), massDamage (1.0), hardnessDamage (4.3), swingSpeed (2.6), textureRoughness (2.0), colors (array of five hex values: 0xff6E757F, 0xff86898E, 0xffA4A7AA, 0xffB9BCBF, 0xffCACCCE), and modifiers (array containing one modifier with id 'good_at', strength 0.5, tag .glacite, and restriction object with id .encased, tag .precious, amount 2).

## Related Questions
- What is the durability value assigned to the glacite item?
- Which tags are associated with the glacite block definition?
- How many color values are defined in the glacite material palette?
- What restriction tag and amount are specified for the good_at modifier on glacite?
- Is the glacite block marked as mineable in its default configuration?
- What is the blockHealth value set for the glacite block by default?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_glacite__defaults.zig.zon_chunk_0*
