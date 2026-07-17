# [easy/codebase_assets_cubyz_biomes_desert_hoodoos_pit.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** minRadius, maxRadius, chance, stoneBlock, structures, degradable, parentBiomes, roughness, rivers, height limits
**Symbols:** minRadius, maxRadius, minHeightLimit, chance, minHeight, maxHeight, rivers, roughness, stoneBlock, structures, parentBiomes
**Concepts:** biome configuration, structure placement, height generation limits, parent biome linking

## Summary
This chunk defines a biome configuration for desert hoodoo pits, specifying generation parameters such as radius limits, height ranges, river presence, roughness, stone block type, and associated structures with placement modes.

## Explanation
The chunk declares a struct-like object containing properties: minRadius (16), maxRadius (32), minHeightLimit (1), chance (0), minHeight (1), maxHeight (10), rivers (false), roughness (1), stoneBlock set to cubyz:sandstone/rough, and structures array with one entry defining id cubyz:sbb referencing structure cubyz:rock/hoodoo/small_medium in degradable mode with chance 0.08. It also includes parentBiomes array containing a single entry linking to biome cubyz:desert/hoodoos/base with chance 12.

## Related Questions
- What is the minimum radius for desert hoodoo pit biome generation?
- Which stone block type is assigned to this biome configuration?
- How does the chance value affect structure spawning in this biome?
- What placement mode is used for the sbb structure entry?
- Is river generation enabled by default in this biome config?
- What are the minimum and maximum height limits defined here?
- Which parent biome ID is linked to this configuration?
- How many structures are included in the structures array of this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_desert_hoodoos_pit.zig.zon_chunk_0*
