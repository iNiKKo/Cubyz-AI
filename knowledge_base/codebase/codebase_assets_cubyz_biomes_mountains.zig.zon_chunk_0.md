# [easy/codebase_assets_cubyz_biomes_mountains.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mountain biome, oak trees, radius, minHeightLimit, maxHeight, smoothBeaches, roughness, ground_structure, structures, degradable
**Symbols:** .mountain, .oak, .radius, .minHeightLimit, .minHeight, .maxHeight, .smoothBeaches, .roughness, .mountains, .rivers, .music, .ground_structure, .structures
**Concepts:** biome configuration, terrain generation, structure placement, height limits, smooth beaches, roughness scaling, ground layering, tree spawning chance

## Summary
This chunk defines a biome configuration for mountains with terrain generation parameters including radius, height limits, smooth beaches, roughness, mountain count, rivers, music, ground structure layers, and a single oak tree structure definition.

## Explanation
The chunk declares a struct-like object containing properties for biome generation: .mountain tag, .oak tags, numeric values for radius (400), minHeightLimit (7), minHeight (60), maxHeight (256), smoothBeaches flag, roughness (10), mountains count (100), rivers flag, music path string, ground_structure array with two entries specifying grass and soil layers, and structures array containing one object defining an oak tree structure with id 'cubyz:sbb', structure reference 'cubyz:tree/oak/young', placeMode set to .degradable, and chance probability 0.4.

## Related Questions
- What is the radius value defined for this mountain biome configuration?
- Which tags are assigned to this biome in the properties section?
- What is the minHeightLimit specified for terrain generation?
- What is the maxHeight limit set for this biome's vertical range?
- Is smoothBeaches enabled or disabled in this configuration?
- What roughness value is applied to the mountain generation algorithm?
- How many mountains are configured to generate in this biome?
- Are rivers included in the ground structure definition?
- What music path is assigned for this biome's audio layer?
- Which ground_structure entries define the terrain layers?
- What id and structure reference are used for the oak tree spawning configuration?
- What placeMode is set for the oak tree structures?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_mountains.zig.zon_chunk_0*
