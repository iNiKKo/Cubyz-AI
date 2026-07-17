# [easy/codebase_assets_cubyz_biomes_cave_stone_forest.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** shallow_cave_layer, ground_structure, spawn chance, size_variance, height_variation, partial_sphere, biome tags
**Symbols:** isCave, tags, chance, music, ground_structure, structures, caveModels
**Concepts:** biome configuration, structure spawning, cave generation, block placement rules

## Summary
Defines a cave biome configuration with shallow layer tags, gravel and slate ground structures, boulder and vegetation spawn rules, tree generation variants, and partial sphere cave models.

## Explanation
This chunk is a .zon configuration file that declares a single biome object containing static settings for world generation. The biome is identified as a cave via the isCave flag set to true and tagged with shallow_cave_layer. Ground structure defines two block types: gravel from 0-1 height and smooth slate elsewhere. Structures array lists spawnable entities each with an id, chance probability, block identifier, size parameters (size and size_variance for boulders), or height parameters (height and height_variation for vegetation/trees). Two simple_tree entries differ only in their leaves block type (rough vs smooth) while sharing the same log block and generation probabilities. CaveModels array defines partial_sphere cave models with min/max amount counts and radius ranges.

## Related Questions
- What is the probability of spawning a boulder in this cave biome?
- Which block types are used for ground generation at heights 0 to 1?
- How many distinct tree variants are defined and what distinguishes them?
- What radius range does the partial_sphere cave model support?
- Is there any music associated with this biome configuration?
- Does the structures array include any non-vegetation entities besides boulders?
- What is the minimum amount of partial spheres generated per chunk?
- How does size_variance affect boulder generation in this config?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_stone_forest.zig.zon_chunk_0*
