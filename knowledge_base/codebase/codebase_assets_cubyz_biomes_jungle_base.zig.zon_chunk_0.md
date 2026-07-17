# [easy/codebase_assets_cubyz_biomes_jungle_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** minHeightLimit, maxHeight, smoothBeaches, ground_structure, structures, degradable, chance, flower_patch, transitionBiomes
**Symbols:** minHeightLimit, minHeight, maxHeight, maxHeightLimit, hills, radius, smoothBeaches, ground_structure, structures, transitionBiomes
**Concepts:** biome configuration, structure placement probabilities, degradable trees, ground composition, flower patches, transition biomes

## Summary
Configuration data defining jungle biome generation parameters including height limits, ground structure composition, and a list of structures (trees, patches) with their placement probabilities.

## Explanation
This chunk contains static configuration values for the jungle biome. It defines minHeightLimit as 7, minHeight as 30, maxHeight as 50, maxHeightLimit as 60, hills count as 10, radius as 160, and smoothBeaches flag set to true. The ground_structure field specifies a composition of 'cubyz:grass/lush' with probability 3 to 4 occurrences followed by 'cubyz:mud'. The structures array enumerates multiple tree variants under the id cubyz:sbb (mahogany/khaya_ivorensis medium, small; mahogany/sapele ancient_short, ancient_tall, large, medium, small) each marked as degradable with varying chance values from 0.01 to 0.5, plus ground_patch entries for mud and flower_patch entries for vegetation/lush, monstera, and a mixed lush/hibiscus/fern set. TransitionBiomes includes one entry referencing cubyz:jungle/sparse with chance 1, width 3, and properties barren and balanced.

## Related Questions
- What is the minimum height limit for jungle biome generation?
- Which ground structure blocks are defined for the jungle biome and in what order?
- How many hills are configured to appear in a jungle biome?
- What is the radius value used for jungle biome generation parameters?
- Are beaches smoothed by default in this jungle configuration?
- List all tree structures under the cubyz:sbb identifier with their placement chances.
- Which flower patch entries include monstera and what are their associated probabilities?
- What properties are assigned to the transition biome cubyz:jungle/sparse?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_jungle_base.zig.zon_chunk_0*
