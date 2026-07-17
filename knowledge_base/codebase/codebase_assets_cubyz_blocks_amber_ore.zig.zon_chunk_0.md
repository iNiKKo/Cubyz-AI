# [easy/codebase_assets_cubyz_blocks_amber_ore.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mineable tag, block health, resistance value, item texture, material durability, mass damage, hardness damage, swing speed, texture roughness, color palette, modifier strength, encased restriction, precious tag, vein count, density value
**Symbols:** .tags, .blockHealth, .blockResistance, .item, .texture, .material, .durability, .massDamage, .hardnessDamage, .swingSpeed, .textureRoughness, .colors, .modifiers, .id, .strength, .restriction, .encased, .precious, .amount, .ore, .veins, .size, .maxHeight, .minHeight, .density, .drops, .items, .auto, .rotation, .model
**Concepts:** block asset definition, vein generation parameters, material properties, drop configuration, texture mapping, modifier restrictions

## Summary
Defines the Amber ore block asset with its mining properties, item texture/material stats, vein generation parameters, and drop configuration.

## Explanation
This chunk declares a single top-level struct instance (implicitly named by the root field) containing all static data for the amber ore block. The .tags array lists .mineable as the only tag, indicating this block is mineable but not obtainable via crafting. The .blockHealth scalar sets the health value to 15, and .blockResistance scalar sets resistance to 3. The nested .item struct holds a string field .texture pointing to 'amber.png' and a .material struct with six float fields: .durability = 140, .massDamage = 0.1, .hardnessDamage = 2.3, .swingSpeed = 8.5, .textureRoughness = 0.1, and a .colors array of five hex strings (0xff9b3481b, 0xffd35a1c, 0xffee7023, 0xffff9134, 0xffffc14a). The .material also contains a .modifiers array with one element: an object having .id = 'light', .strength = 0.5, and a nested .restriction struct with .id = .encased, .tag = .precious, and .amount = 4. The top-level block has an .ore struct defining generation parameters: .veins = 3, .size = 3, .maxHeight = -1250, .minHeight = -8000, and .density = 0.15. The .drops array contains one element with a single field .items set to the enum value .auto, meaning drops are handled automatically by the engine. Finally, three string fields specify asset references: .rotation = 'cubyz:ore', .model = 'cubyz:cube', and .texture = 'cubyz:amber_ore'. All fields are literal constants; no executable logic or functions are present.

## Related Questions
- What is the block health of the amber ore?
- Which tags are assigned to this block asset?
- How many veins does the amber ore generate with default settings?
- What is the maximum height for amber ore generation in this configuration?
- What texture file is referenced for the item drop of amber ore?
- Does this block have any modifiers defined, and what are their IDs?
- What restriction tag applies to the light modifier on amber ore?
- How many colors are included in the material palette for amber ore?
- Is the drop configuration set to auto or manual for amber ore?
- Which model is assigned to this block asset by default?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_amber_ore.zig.zon_chunk_0*
