# [easy/codebase_assets_cubyz_biomes_ocean_cold_archipelago.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, properties, minHeight, maxHeight, smoothBeaches, radius, roughness, hills, music, ground_structure, structures, transitionBiomes
**Symbols:** cold_ocean_archipelago
**Concepts:** biome configuration, ground structure generation, transition biome handling

## Summary
Defines the cold ocean archipelago biome configuration with height ranges, beach smoothing, radius, roughness parameters, music reference, ground structure blocks, and transition biomes.

## Explanation
This chunk is a .zon configuration file containing static data for an ocean biome. It declares a single biome object with chance 0.1 and properties cold and ocean. Height constraints are minHeight -15, maxHeight -10, maxHeightLimit 7, smoothBeaches true, radius 500, roughness 20, hills 10. Music is set to cubyz:totaldemented/tides. Ground structure specifies one block range cubyz:slate/rough with weight 1-2. Structures array defines two ground_patch entries: first uses cubyz:moss:cubyz:slate/rough with chance 0.064, width 6, variation 2, depth 2, smoothness 0.2; second uses cubyz:gravel with chance 0.02, width 10, variation 5, depth 2, smoothness 0.4. TransitionBiomes array lists three entries: cubyz:beach/cold/wide (chance 0.2, width 2, properties land and inland), cubyz:beach/cold/base (chance 1, width 1, properties land and inland), and cubyz:ocean/cold/shelf (chance 1, width 3, properties land and inland).

## Related Questions
- What is the chance value for this biome?
- Which properties are assigned to this biome?
- What are the minHeight and maxHeight limits?
- Is smoothBeaches enabled?
- What is the radius of this biome?
- What roughness and hills values are set?
- Which music track is referenced?
- What blocks are included in ground_structure?
- How many structure entries are defined under structures?
- What are the block, chance, width, variation, depth, and smoothness for each structure entry?
- What transition biomes are listed and what are their chances and widths?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_ocean_cold_archipelago.zig.zon_chunk_0*
