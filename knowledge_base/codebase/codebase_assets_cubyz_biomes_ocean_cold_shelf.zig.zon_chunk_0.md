# [easy/codebase_assets_cubyz_biomes_ocean_cold_shelf.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** ocean biome, radius bounds, ground structure, interpolation mode, music reference, structure chance, smoothness parameter, variation depth, block list
**Symbols:** properties, radius, minHeight, maxHeight, chance, interpolation, hills, music, ground_structure, structures
**Concepts:** biome configuration, terrain generation, procedural structures, block composition

## Summary
Configuration data defining the cold ocean shelf biome with terrain bounds, ground structure composition, and procedural generation parameters.

## Explanation
This chunk is a .zon configuration file containing static biome settings. It declares properties for an ocean biome (radius 500, height range -4 to 0) with linear interpolation, hills count of 10, and music reference 'cubyz:totaldemented/tides'. The ground_structure field specifies a list of block strings ('2 to 4 cubyz:gravel') defining the terrain composition. The structures field contains an array of structure definitions; each entry includes id ('cubyz:ground_patch'), block type, chance (0.064), width (6), variation (2), depth (2), and smoothness (0.2). No executable logic is present.

## Related Questions
- What is the radius of the cold ocean shelf biome?
- Which music track plays in this biome?
- How many hills are generated for this biome?
- What interpolation method is used for terrain generation?
- What blocks make up the ground structure?
- What is the chance of spawning a ground patch structure?
- What dimensions does the ground patch structure have?
- What smoothness value is applied to structures in this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_ocean_cold_shelf.zig.zon_chunk_0*
