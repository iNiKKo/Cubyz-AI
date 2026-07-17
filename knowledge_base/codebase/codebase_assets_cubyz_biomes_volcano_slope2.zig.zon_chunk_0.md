# [easy/codebase_assets_cubyz_biomes_volcano_slope2.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mountain, volcano, radius, height, interpolation, chance, music, parentBiomes, soilCreep, ground_structure, stoneBlock, structures
**Symbols:** .properties, .radius, .minHeight, .maxHeight, .mountains, .interpolation, .chance, .music, .parentBiomes, .maxSubBiomeCount, .soilCreep, .ground_structure, .stoneBlock, .structures
**Concepts:** biome configuration, terrain generation, parent biome linking, structure placement, music assignment

## Summary
Configuration data defining a volcano biome with fixed terrain height, parent slope references, ground structure composition, and associated music.

## Explanation
This chunk contains only configuration values for a biome named 'volcano_slope2'. The properties are set to '.mountain' type with a radius of 220 blocks. Height is locked at minHeight=384 and maxHeight=384, indicating a flat mountain surface. It includes 50 mountains (likely procedural generation parameters). Interpolation is linear. Chance for additional features is 0. Music is set to 'cubyz:mrmayman/out_of_breath'. The biome has exactly one parent: 'cubyz:volcano/slope1' with a chance of 1 and a parentEdgeDistance of 16 blocks. maxSubBiomeCount is 1, meaning no sub-biomes are allowed. SoilCreep is enabled (value 1). Ground structure consists of ash ('2 to 4 cubyz:ash'). Stone block is 'cubyz:basalt/smooth'. Structures include a single ground_patch with id 'cubyz:ground_patch', using the same basalt smooth block, chance 0.1, width 5, variation 5, depth 4, and smoothness 0.1.

## Related Questions
- What is the radius of the volcano_slope2 biome?
- Which music track is assigned to this biome configuration?
- How many mountains are configured for generation in this biome?
- What is the interpolation method used for terrain smoothing?
- Which parent biome does this configuration reference and what is its edge distance?
- What block type is specified as the stoneBlock for ground structures?
- Is soil creep enabled or disabled in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_volcano_slope2.zig.zon_chunk_0*
