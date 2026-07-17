# [easy/codebase_assets_cubyz_biomes_hills_large__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** minHeightLimit, maxHeight, smoothBeaches, minRadius, maxRadius, roughness, hills, mountains, soilCreep, validPlayerSpawn
**Symbols:** minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, minRadius, maxRadius, roughness, hills, mountains, soilCreep, chance, validPlayerSpawn, structures
**Concepts:** biome configuration, height limits, structure spawning, terrain generation parameters

## Summary
Defines biome configuration parameters for hills terrain including height limits, generation radius, structure spawn chances, and specific boulder/flower patch definitions.

## Explanation
This chunk contains only static configuration data with no executable logic. It defines minHeightLimit (16), minHeight (30), maxHeight (90), maxHeightLimit (100) for vertical bounds; smoothBeaches flag set to true; minRadius (128) and maxRadius (256) for generation area; roughness value of 3; hills count of 40 and mountains count of 10; soilCreep factor of 1.5; chance parameter of 0.4; validPlayerSpawn flag set to true. The structures array defines three entries: a boulder structure with id cubyz:boulder, block cubyz:slate/smooth, size 5, size_variance 1; two flower_patch structures both sharing the same id cubyz:flower_patch but differing in blocks (cubyz:daisies vs cubyz:dandelions), each with their own chance values (0.003 and 0.002), width dimensions (10 and 6), variation counts (6 and 4), density of 0.3, and priority of 0.1.

## Related Questions
- What is the minimum height limit for hills biome generation?
- How many hills structures are configured to spawn in this biome?
- What block type is used for the boulder structure definition?
- Is smooth beach generation enabled by default in this configuration?
- What is the maximum radius value set for hills terrain generation?
- Which flower patch variant uses daisies as its blocks array?
- What is the chance probability for spawning a cubyz:boulder structure?
- Does this biome allow valid player spawn locations?
- What roughness factor is applied to hills terrain generation?
- How many mountain structures are defined in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_hills_large__defaults.zig.zon_chunk_0*
