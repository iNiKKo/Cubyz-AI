# [easy/codebase_assets_cubyz_blocks_pyrolite__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** pyrolite, blockHealth, drops, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, modifiers, encased
**Symbols:** .tags, .blockHealth, .blockResistance, .drops, .item, .material.durability, .material.massDamage, .material.hardnessDamage, .material.swingSpeed, .material.textureRoughness, .material.colors, .material.modifiers
**Concepts:** block configuration, asset defaults, drop behavior, item material properties, modifier restrictions

## Summary
Defines default configuration data for the pyrolite block asset, specifying its tags, health, resistance, drop behavior, and item material properties including durability, damage values, texture roughness, color palette, and modifiers.

## Explanation
This chunk contains only static configuration data with no executable logic. It declares a single object with fields: .tags (array of block tags), .blockHealth (integer health value), .blockResistance (float resistance value), .drops (array containing one drop entry with items set to auto-drop), and .item (object describing the dropped item's material properties). The material sub-object includes: .durability (300), .massDamage (4.0), .hardnessDamage (6.0), .swingSpeed (5.0), .textureRoughness (1.0), .colors (array of five hex color values), and .modifiers (array containing one modifier with id 'good_at', strength 0.5, tag 'pyrolite', and a restriction object specifying id 'encased' with tag 'precious' and amount 2). No functions are defined; all values are literal constants.

## Related Questions
- What are the default tags assigned to the pyrolite block?
- How much health does the pyrolite block have by default?
- What is the resistance value of the pyrolite block?
- Does the pyrolite block drop items automatically, and what do they drop?
- What durability value is assigned to the pyrolite item material?
- How much mass damage does the pyrolite item deal?
- How much hardness damage does the pyrolite item deals?
- What swing speed is configured for the pyrolite item?
- What texture roughness is set for the pyrolite item?
- Which colors are defined in the pyrolite material palette, and how many are there?
- What modifier is applied to the pyrolite item, what is its strength, and which tag does it affect?
- Under what restriction condition can the pyrolite modifier be applied, and what amount is required?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_pyrolite__defaults.zig.zon_chunk_0*
