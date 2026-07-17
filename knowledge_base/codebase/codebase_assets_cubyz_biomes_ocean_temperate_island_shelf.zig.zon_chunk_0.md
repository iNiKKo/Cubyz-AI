# [easy/codebase_assets_cubyz_biomes_ocean_temperate_island_shelf.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** minHeight, maxHeight, radius, hills, ground_structure, structures, chance, smoothness, depth, variation
**Symbols:** minHeight, maxHeight, radius, hills, maxSubBiomeCount, ground_structure, structures, parentBiomes
**Concepts:** biome configuration, terrain generation parameters, structure spawning rules, parent biome transitions

## Summary
Defines a temperate ocean island shelf biome configuration with height constraints, ground structure composition, and parent biome transition probabilities.

## Explanation
This chunk declares a static biome definition containing minHeight (-10), maxHeight (-1), radius (70), hills count (3), maxSubBiomeCount (1). The ground_structure field specifies the terrain material as '2 to 3 cubyz:sand'. The structures array defines one ground_patch with id 'cubyz:ground_patch', block type 'cubyz:amber_ore:cubyz:sand', spawn chance 0.012, width 1, variation 2, depth 1, and smoothness 0.1. The parentBiomes array lists two possible parent biomes: cubyz:ocean/temperate/base with probability 1 and cubyz:ocean/temperate/archipelago with probability 15.

## Related Questions
- What is the minimum height value for this biome?
- What is the maximum height value for this biome?
- What radius defines the extent of this biome?
- How many hills are configured in this biome?
- What material composes the ground structure?
- Which block type is used for the ground patch structure?
- What is the spawn chance for the ground patch structure?
- What width and depth parameters define the ground patch structure?
- What smoothness value is applied to the ground patch structure?
- Which parent biome has a transition probability of 15?
- How many entries are in the parentBiomes array?
- Does this biome configuration include any additional structures beyond the defined ground patch?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_ocean_temperate_island_shelf.zig.zon_chunk_0*
