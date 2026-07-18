# [easy/codebase_assets_cubyz_biomes_cave_curl_forest.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave biome, structure settings, fog density, chance, music
**Symbols:** CaveBiome, CaveBiome.isCave, CaveBiome.tags, CaveBiome.maxHeight, CaveBiome.fogDensity, CaveBiome.chance, CaveBiome.music, CaveBiome.structures, CaveBiome.caveModels
**Concepts:** biome configuration, structure placement, cave model generation

## Summary
Cave biome configuration with structures and cave models

## Explanation
This chunk defines a cave biome with specific settings including fog density, chance of occurrence, music, and structures. The biome is identified by `isCave = true` and has tags `.cave_layer`. It has a maximum height of -512. The fog density is set to 2, and the chance of occurrence for the cave biome is 0.01. The music associated with this biome is 'cubyz:ikabod/live'.

The structures defined include:
- A structure with id `cubyz:sbb` using the template 'cubyz:tree/curl' and place mode `.degradable`, with a chance of 0.15.
- A ground patch structure with id `cubyz:ground_patch` that places gravel blocks, has a chance of 0.064, width of 5, variation of 5, depth of 3, and smoothness of 0.1.
- Two boulder structures both with id `cubyz:boulder`, one placing 'cubyz:slate/rough' blocks with a size of 4 and variance of 3, the other placing 'cubyz:slate/smooth' blocks with a size of 4 and variance of 4.

Cave model configurations include:
- A partial sphere cave model with id `cubyz:partial_sphere`, having a minimum amount of 10, maximum amount of 30, minimum radius of 10, and maximum radius of 20.

## Related Questions
- What is the fog density of this cave biome?
- How many structures are defined for this cave biome?
- What is the maximum height of the cave biome?
- Which structure has an id of 'cubyz:sbb'?
- What is the chance of occurrence for the ground patch structure?
- What is the size variance for the boulder structure with block 'cubyz:slate/smooth'?
- How many partial sphere cave models are defined?
- What is the maximum amount of partial sphere cave models that can be generated?
- What is the minimum radius of a partial sphere cave model?
- What is the maximum radius of a partial sphere cave model?
- Which structure has an id of 'cubyz:ground_patch' and what block does it place?
- What is the width of the ground patch structure?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_curl_forest.zig.zon_chunk_0*
