# [easy/codebase_assets_cubyz_biomes_cave_mantle_ash.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave generation, structure placement, biome settings, stalagmites, magma patches
**Concepts:** world_generation, biome configuration

## Summary
Defines configuration for the 'cave_mantle_ash' biome in Cubyz, including cave generation parameters and structures.

## Explanation
This chunk is a configuration file for the 'cave_mantle_ash' biome in Cubyz. It specifies various properties such as the chance of occurrence (0.3), soil creep (1), ground structure ('2 to 4 cubyz:ash'), and different types of structures that can appear within caves.

The configurations include two types of stalagmites with block type 'cubyz:pyrolite/rough'. The first type has a size of 12, a size variation of 4, a base slope of 0, and a top slope of 8, with a chance of occurrence of 0.03. The second type has a size of 4, a size variation of 6, with a chance of occurrence of 0.08.

Additionally, it defines two types of ground patches for magma blocks. The first type has a width of 4, a variation of 2, a depth of 2, and a smoothness value of 0.8, with a chance of occurrence of 0.03. The second type has a width of 2, a variation of 1, a depth of 2, and a smoothness value of 0.1, with a chance of occurrence of 0.08.

Ruins structures are also defined with an ID of 'cubyz:sbb', a structure of 'cubyz:cave/mantle/ruins', in degradable mode, with a chance of occurrence at 0.003.

The cave models include cylindrical shapes with a minimum radius of 6, a maximum radius of 8, a minimum height of 80, and a maximum height of 200, generated in additive mode.

## Related Questions
- What is the chance of occurrence for the 'cave_mantle_ash' biome?
- How many different types of structures are defined in this biome configuration?
- What is the minimum and maximum radius of the cylindrical cave models?
- Which block type is used for the stalagmites in this biome?
- What is the chance of placing a ground patch with magma blocks?
- How does the soil creep parameter affect the biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mantle_ash.zig.zon_chunk_0*
