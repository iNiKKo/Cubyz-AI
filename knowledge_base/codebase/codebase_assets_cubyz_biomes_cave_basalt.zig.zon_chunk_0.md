# [easy/codebase_assets_cubyz_biomes_cave_basalt.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** isCave, tags, maxHeight, chance, fogDensity, music, stoneBlock, structures, caveModels, degradable
**Symbols:** isCave, tags, maxHeight, chance, fogDensity, music, stoneBlock, structures, caveModels
**Concepts:** biome configuration, structure generation, degradable placement, partial sphere models

## Summary
Defines a cave biome configuration with basalt stone blocks and lava structures.

## Explanation
This chunk declares a single biome object containing the isCave flag set to true, tags of .cave_layer, maxHeight of -1000, generation chance of 0.2, fogDensity of 8, music reference cubyz:totaldemented/scoria, stoneBlock identifier cubyz:basalt/smooth, and a structures array with four entries defining id, block/structure references, placeMode (degradable), and probability values for stalagmites, ground patches, and lava spouts. The caveModels field holds one partial_sphere model entry specifying minAmount 10, maxAmount 20, minRadius 12, and maxRadius 20.

## Related Questions
- What is the generation chance for this cave biome?
- Which music track plays in this biome?
- What stone block identifier is used for the cave floor?
- How many structure definitions are included in this biome configuration?
- What is the fog density value set for this biome?
- Which partial sphere model is defined and what are its radius bounds?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_basalt.zig.zon_chunk_0*
