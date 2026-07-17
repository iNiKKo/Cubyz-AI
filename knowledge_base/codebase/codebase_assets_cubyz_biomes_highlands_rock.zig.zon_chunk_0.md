# [easy/codebase_assets_cubyz_biomes_highlands_rock.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome, highlands_rock, structure, stalagmite, parentBiomes, chance, minRadius, maxHeight, roughness, mountains
**Symbols:** minRadius, maxRadius, chance, minHeight, maxHeight, roughness, mountains, hills, stoneBlock, parentBiomes, structures
**Concepts:** biome configuration, structure generation, parent biome inheritance, random spawn chance, height range constraints, terrain roughness, mountain count, hill count, stalagmite placement

## Summary
This chunk defines the configuration for the highlands_rock biome, specifying its generation parameters including radius bounds, height ranges, mountain/hill counts, parent biomes, and a list of stalagmite structures with their block types, spawn chances, sizes, and slopes.

## Explanation
The chunk is a .zon configuration file containing static data for the highlands_rock biome. It declares a properties map that includes numeric fields minRadius (16), maxRadius (48), minHeight (150), maxHeight (155), roughness (0), mountains (50), hills (2). The chance field is set to 0, indicating this biome does not spawn randomly via the general biome chance mechanism. It defines a parentBiomes array with a single entry pointing to cubyz:highlands/base with a sub-chance of 6. The structures array contains two entries for the same structure id cubyz:stalagmite; both use block cubyz:slate/smooth, but differ in spawn chance (0.08 vs 0.01) and size (9 vs 12), while sharing identical size_variation (6), baseSlope (5), and topSlope (1). No executable logic is present; this chunk serves purely as data for the biome generation system to read.

## Related Questions
- What is the minimum radius for highlands_rock biome generation?
- What is the maximum height range defined for this biome?
- Which block type is used for stalagmite structures in this configuration?
- How many mountains are configured to generate in this biome?
- What is the sub-chance weight of the parent highlands/base biome?
- Are there any random spawn chances set for this biome itself?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_highlands_rock.zig.zon_chunk_0*
