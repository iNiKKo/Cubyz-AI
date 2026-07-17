# [easy/codebase_assets_cubyz_biomes_cave_slate_low.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, structures, caveModels, ground_patch, stalagmite, cylinder, block, variation, smoothness, radius
**Symbols:** .chance, .maxHeight, .structures, .id, .block, .width, .variation, .depth, .smoothness, .size, .size_variation, .caveModels, .minAmount, .maxAmount, .minRadius
**Concepts:** biome configuration, structure generation, model definition, randomized placement

## Summary
Configuration data defining cave biome generation parameters including ground patch structures and cylinder models.

## Explanation
This chunk contains static configuration values for the cave biome generator. It defines a .chance of 0.8, a maxHeight of -100, and an array of .structures containing two entries: one with id cubyz:ground_patch using block cubyz:slate/rough (chance 0.064, width 5, variation 5, depth 3, smoothness 0.1) and another with id cubyz:stalagmite using block cubyz:slate/smooth (size 3, size_variation 6). It also defines an array of .caveModels containing one entry with id cubyz:cylinder specifying minAmount 6, maxAmount 16, minRadius 10, maxHeight 2.

## Related Questions
- What is the chance value for cave generation in this configuration?
- Which block type is used for the ground_patch structure?
- How many structures are defined in the .structures array?
- What is the width parameter of the ground_patch structure?
- What is the size_variation for the stalagmite structure?
- What is the minAmount for the cylinder cave model?
- Which block type is used for the stalagmite structure?
- What is the maxRadius value defined in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_slate_low.zig.zon_chunk_0*
