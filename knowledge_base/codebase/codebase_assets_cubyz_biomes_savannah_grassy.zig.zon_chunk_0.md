# [easy/codebase_assets_cubyz_biomes_savannah_grassy.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** properties, tags, chance, keepOriginalTerrain, minHeightLimit, maxHeight, smoothBeaches, minRadius, hills, validPlayerSpawn, music, ground_structure, structures, stoneBlock, parentBiomes
**Symbols:** properties, tags, chance, keepOriginalTerrain, minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, minRadius, maxRadius, hills, validPlayerSpawn, music, ground_structure, structures, stoneBlock, parentBiomes
**Concepts:** biome configuration, structure placement probabilities, terrain height constraints, ground structure definitions

## Summary
Configuration data defining the savannah/grassy biome with terrain limits, ground structure definitions, and a list of structures (ground patches, baobab trees, flower patches) including their IDs, block types, placement chances, dimensions, and smoothness.

## Explanation
This chunk is pure configuration; it contains no executable logic. It defines the biome's properties (.hot, .dry), tags (.baobab), height constraints (minHeight 30, maxHeight 46, minHeightLimit 7, maxHeightLimit 42), terrain smoothing settings (smoothBeaches true, keepOriginalTerrain 0.6), radius bounds (minRadius 16, maxRadius 128), hill count (10), spawn validity (.validPlayerSpawn true), music reference ('cubyz:mischol/desert_firefly'), ground structure entries ('cubyz:grass/dry', '7 to 8 cubyz:limestone/smooth'), and a .structures array with multiple entries. Each structure entry specifies an id, block or blocks (single or array), chance probability, width, variation, depth, smoothness, density, priority, and optionally placeMode (.degradable for baobab trees). The parentBiomes field lists the base savannah biome with its own chance value.

## Related Questions
- What are the biome properties defined in this configuration?
- Which tags are associated with this biome?
- What is the chance value for this biome?
- How does keepOriginalTerrain affect terrain generation?
- What are the minHeight and maxHeight limits?
- Does smoothBeaches enable beach smoothing?
- What radius bounds constrain structure placement?
- Is player spawning allowed in this biome?
- What music track plays in this biome?
- Which ground structures are defined here?
- What is the stoneBlock used for this biome?
- How does parentBiomes relate to other biomes?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_savannah_grassy.zig.zon_chunk_0*
