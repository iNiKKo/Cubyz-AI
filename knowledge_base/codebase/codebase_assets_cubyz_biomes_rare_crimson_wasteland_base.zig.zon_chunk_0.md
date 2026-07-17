# [easy/codebase_assets_cubyz_biomes_rare_crimson_wasteland_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** properties, minHeightLimit, maxHeight, smoothBeaches, structures, stalagmite, ground_patch, chance, validPlayerSpawn
**Symbols:** properties, hot, dry, barren, minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, minRadius, maxRadius, roughness, hills, chance, validPlayerSpawn, stoneBlock, structures
**Concepts:** biome configuration, terrain generation parameters, structure spawning rules, ground patch placement, stalagmite generation, height limits, roughness control, spawn restrictions

## Summary
This chunk defines the configuration data for the Crimson Wasteland biome, specifying terrain generation parameters including height limits, roughness, hills count, spawn validity, and a list of possible structures with their IDs, blocks, chances, sizes, and variations.

## Explanation
The chunk is a .zon file containing only static configuration data for the Crimson Wasteland biome. It declares properties such as hot, dry, barren flags; minHeightLimit (7), minHeight (42), maxHeight (60), maxHeightLimit (65); smoothBeaches (true); minRadius (256), maxRadius (320); roughness (1); hills (15); chance (0.01); validPlayerSpawn (false). It also sets stoneBlock to cubyz:obsidian. The structures field is an array of objects, each defining a potential structure or ground patch with id, block type, chance probability, size parameters (size, size_variation for stalagmites; width, variation, depth, smoothness for ground patches), and in some cases the specific block variant used.

## Related Questions
- What are the minimum and maximum height limits for the Crimson Wasteland biome?
- Which block is designated as the stoneBlock for this biome configuration?
- How many hills are configured to generate in this biome?
- What is the probability chance value set for general structure spawning?
- Is player spawn allowed in the Crimson Wasteland biome according to this config?
- List all unique structure IDs defined in the structures array.
- What block type is used for the ground_patch entries with a 1.0 chance?
- How does the size_variation parameter affect stalagmite generation?
- What are the width, variation, depth, and smoothness values for ground patches?
- Are there any structures defined that use cubyz:obsidian as their block type?
- What is the roughness value set for terrain noise in this biome?
- Does the configuration include a flag to smooth beaches?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_crimson_wasteland_base.zig.zon_chunk_0*
