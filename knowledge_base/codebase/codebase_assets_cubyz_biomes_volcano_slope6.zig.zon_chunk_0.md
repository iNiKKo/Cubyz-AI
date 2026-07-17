# [easy/codebase_assets_cubyz_biomes_volcano_slope6.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mountain, radius, roughness, interpolation, ground_structure, stoneBlock, music, parentBiome
**Symbols:** .mountain, .linear, cubyz:mrmayman/out_of_breath, cubyz:volcano/slope5
**Concepts:** biome configuration, parent biome reference, terrain generation parameters

## Summary
This chunk defines a volcano biome configuration with fixed height, linear interpolation, and a parent slope5 reference.

## Explanation
The chunk declares a single struct instance (implicitly named by the file) containing biome properties: .mountain type, radius 80, minHeight and maxHeight both 640, roughness 20, mountains count 20, linear interpolation, zero chance for random features, music asset 'cubyz:mrmayman/out_of_breath', a parentBiome entry pointing to 'cubyz:volcano/slope5' with chance 1 and edge distance 16, maxSubBiomeCount set to 1, ground_structure specifying '10 to 12 cubyz:magma', and stoneBlock set to 'cubyz:basalt/smooth'. All fields are literal values or inline arrays; no executable logic is present.

## Related Questions
- What is the radius of this volcano biome?
- What interpolation method is used for terrain generation here?
- Which music track is assigned to this biome?
- What is the parent biome ID referenced in this configuration?
- How many mountains are specified for this biome?
- What ground structure materials are defined for this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_volcano_slope6.zig.zon_chunk_0*
