# [easy/codebase_assets_cubyz_biomes_wetlands_willows.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome properties, structures, inheritance, environmental settings, generation probabilities
**Concepts:** biome configuration, world generation

## Summary
Defines properties and structures for the 'wetlands_willows' biome in Cubyz.

## Explanation
This chunk configures the 'wetlands_willows' biome, specifying its environmental properties such as wetness (true), temperature (hot), minimum height (-2), maximum height (-2), roughness (2), chance of generation (0%), hills factor (3.5), and radius range (64 to 128). It also defines various structures that can appear within this biome, including ground patches made of mud blocks ('cubyz:mud'), willow trees with specific dimensions and probabilities, and different types of duckweed flowers with varying chances and sizes.

The willow trees have a height of 13 with a variation of 4, a leaf radius of 4.0 with a variation of 2.5, a leaf elongation of 0.4 with a delta elongation of 0.125, and are not branched. There are two types of willow trees defined, each with the same specifications.

The duckweed flowers have different configurations based on their type:
- Type 0: Chance = 0.3, Width = 8, Variation = 4, Density = 0.66, Priority = 0.2
- Type 1: Chance = 0.25, Width = 6, Variation = 3, Density = 0.66, Priority = 0.3
- Type 2: Chance = 0.1, Width = 5, Variation = 2, Density = 0.66, Priority = 0.4
- Type 3: Chance = 0.05, Width = 3, Variation = 2, Density = 0.66, Priority = 0.5
- Lily pad: Chance = 0.05, Width = 6, Variation = 6, Density = 0.05, Priority = 0.4

The biome inherits from a base wetlands biome with an 8% chance. Additionally, the music associated with this biome is 'cubyz:sinanimea/sunrise'.

## Related Questions
- What are the specific environmental properties (wetness, temperature, height range) of the 'wetlands_willows' biome?
- Which structures can appear in the 'wetlands_willows' biome and what are their exact configurations?
- How does the 'wetlands_willows' biome inherit from other biomes and with what probability?
- What is the music associated with the 'wetlands_willows' biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_wetlands_willows.zig.zon_chunk_0*
