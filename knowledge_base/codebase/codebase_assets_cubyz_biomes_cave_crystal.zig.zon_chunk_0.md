# [easy/codebase_assets_cubyz_biomes_cave_crystal.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave biome, crystals, boulder structures, sphere models, partial sphere models
**Concepts:** world generation, biome configuration

## Summary
Defines configuration for a cave biome with crystal features.

## Explanation
This chunk is a configuration file defining the properties of a specific cave biome in Cubyz. It specifies that this is a cave biome, tags it as part of the cave layer, and sets its maximum height to -512. The biome has a 20% chance of occurring (chance = 0.2) and contains up to 32 crystals (crystals = 32). It also defines music with the track 'cubyz:mischol/crystals', uses slate blocks for stone types ('stoneBlock' = 'cubyz:slate/smooth'), and specifies structures like boulders with varying sizes and chances. For instance, there are two types of boulder structures defined:

- The first type has an ID of 'cubyz:boulder', a chance of 0.016, uses the block 'cubyz:slate/rough', and can have a size ranging from 2 to 8 (size = 5, size_variance = 3).
- The second type also has an ID of 'cubyz:boulder', a chance of 0.016, uses the block 'cubyz:slate/smooth', and can have a size ranging from 2 to 6 (size = 4, size_variance = 2).

Additionally, it specifies cave models such as spheres and partial spheres with their respective amounts and radii:

- The sphere model has an ID of 'cubyz:sphere', a minimum amount of 1, a maximum amount of 1, a minimum radius of 30, a maximum radius of 40, and no maxBiomeCenterDistance.
- The partial sphere model has an ID of 'cubyz:partial_sphere', a minimum amount of 20, a maximum amount of 30, a minimum radius of 8, a maximum radius of 16, and a maxBiomeCenterDistance of 50.

## Related Questions
- What is the maximum height of this cave biome?
- How many crystals can be found in this biome?
- What are the chances of encountering a boulder in this biome?
- Which music track is associated with this cave biome?
- What types of stone blocks are used in this biome?
- How many different cave models are defined for this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_crystal.zig.zon_chunk_0*
