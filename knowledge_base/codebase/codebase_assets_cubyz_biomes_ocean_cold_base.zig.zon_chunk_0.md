# [easy/codebase_assets_cubyz_biomes_ocean_cold_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** arctic_ocean, ground_structure, transitionBiomes, smoothBeaches, radius, roughness, hills, chance, width, variation, depth, smoothness
**Symbols:** cold, ocean, arctic_ocean, minHeight, maxHeight, maxHeightLimit, smoothBeaches, radius, roughness, hills, music, ground_structure, structures, transitionBiomes
**Concepts:** biome configuration, terrain generation, structure placement, biome transitions

## Summary
Defines the arctic_ocean biome configuration with terrain height constraints, ground structure composition, and transition rules to adjacent biomes.

## Explanation
This chunk declares a static biome definition for an arctic ocean environment. It sets the biome type as .arctic_ocean with vertical bounds from -100 to -22 meters and a maxHeightLimit of 7. The configuration includes smoothBeaches enabled, a radius of 500 blocks, roughness of 20, hills count of 10, and an assigned music track cubyz:sinanimea/under_the_water_sky. Ground generation is restricted to a single structure type: cubyz:slate/rough with a chance range of 1 to 2. The structures array defines two ground_patch entries: one using cubyz:moss:cubyz:slate/rough (chance 0.064, width 6, variation 2, depth 2, smoothness 0.2) and another using cubyz:gravel (chance 0.02, width 10, variation 5, depth 2, smoothness 0.4). TransitionBiomes contains three entries specifying adjacent biome IDs with their respective chance weights, widths, and property flags (.land, .inland): cubyz:beach/cold/wide (chance 0.2, width 2), cubyz:beach/cold/base (chance 1, width 1), and cubyz:ocean/cold/shelf (chance 1, width 3).

## Related Questions
- What is the vertical height range for the arctic_ocean biome?
- Which ground structure types are defined in this biome configuration?
- How does the chance parameter affect structure generation frequency?
- What properties are assigned to the transition biomes for this ocean?
- Is smoothBeaches enabled and what is its impact on terrain edges?
- What music track is associated with this biome definition?
- How many hills are configured for this biome's surface detail?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_ocean_cold_base.zig.zon_chunk_0*
