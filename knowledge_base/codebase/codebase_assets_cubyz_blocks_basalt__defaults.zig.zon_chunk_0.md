# [easy/codebase_assets_cubyz_blocks_basalt__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, modifier, encased, precious, auto drop
**Symbols:** .tags, .blockHealth, .blockResistance, .drops, .items, .auto, .item, .material, .durability, .massDamage, .hardnessDamage, .swingSpeed, .textureRoughness, .colors, .modifiers, .id, .strength, .tag, .restriction, .encased, .precious, .amount
**Concepts:** block configuration, item properties, material modifiers, color palettes, drop mechanics

## Summary
Defines the default configuration for basalt blocks and their associated item properties within the Cubyz voxel engine.

## Explanation
This chunk declares a single top-level struct literal containing all static data for the basalt block. The struct includes tags (.stone, .mineable, .basalt), health (30), resistance (1), drop configuration (auto item), and detailed item material properties: durability (75), massDamage (2.0), hardnessDamage (4.0), swingSpeed (2.9), textureRoughness (5.0), a palette of five hex color values, and modifiers defining the 'good_at' ability with 0.5 strength restricted to the 'encased' precious tag requiring amount 2.

## Related Questions
- What are the default tags assigned to basalt blocks?
- How much health does a basalt block have by default?
- What is the resistance value for basalt blocks?
- Which item type drops when a basalt block is mined with auto configuration?
- What is the durability of the basalt item material?
- What mass damage does the basalt item inflict?
- What hardness damage does the basalt item inflict?
- What swing speed is configured for the basalt item?
- How many colors are defined in the basalt material palette?
- What modifier ID is associated with the basalt material?
- Which tag restriction applies to the good_at modifier on basalt items?
- What amount of precious encased blocks does the modifier require?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_basalt__defaults.zig.zon_chunk_0*
