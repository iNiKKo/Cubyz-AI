# [easy/codebase_assets_cubyz_biomes_cave_sky_islands_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** partial sphere, torus, cut direction, amount range, radius bounds, additive mode, chance weight, voxel generation, biome data
**Symbols:** caveModels
**Concepts:** biome configuration, model spawning, geometric primitives, additive blending, randomized generation parameters

## Summary
Defines the base configuration for cave biome generation by specifying a set of additive partial sphere and torus models with their respective quantity ranges and geometric parameters.

## Explanation
This chunk contains only static data definitions within a .zon file, serving as configuration input for the world generation system. It declares a single object containing a chance field set to 1 (indicating this biome is always attempted) and an array of caveModels. Each model entry specifies an id string ('cubyz:partial_sphere' or 'cubyz:torus'), minAmount, maxAmount defining the random spawn count range, minRadius and maxRadius for size variation, cutDirection as a normalized vector (all entries use {0, 0, 1}), cutDirectionRandomness set to 0.1 allowing slight angular deviation from the primary axis, cutPercentage at 0.8 determining how much of the primitive is retained after cutting, and mode fixed to additive for all entries. No executable logic or functions are present; this data would be consumed by a separate generation routine that iterates over these models to instantiate voxel structures.

## Related Questions
- What is the default chance value for cave biome generation in this configuration?
- Which model IDs are defined within the caveModels array of this biome config?
- How does cutDirectionRandomness affect the orientation of generated partial spheres?
- What geometric primitive corresponds to the id 'cubyz:torus' in this file?
- Are all cave models configured with additive blending mode or is there variation?
- What are the minimum and maximum radius bounds for the first partial sphere model entry?
- How many distinct model entries are present in the caveModels array of this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_sky_islands_base.zig.zon_chunk_0*
