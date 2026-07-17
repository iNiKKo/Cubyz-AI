# [easy/codebase_assets_cubyz_biomes_cave_crystal_forest.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** isCave, tags, maxHeight, chance, crystals, stoneBlock, ground_structure, structures, caveModels, partial_sphere
**Symbols:** isCave, tags, maxHeight, chance, crystals, music, stoneBlock, ground_structure, structures, caveModels
**Concepts:** biome configuration, cave generation, structure placement, crystal spawning, music referencing, block composition

## Summary
Defines a cave biome configuration with crystal generation parameters, music references, ground structures, and cave model definitions.

## Explanation
This chunk declares a single struct instance representing a cave biome. It sets isCave to true and includes tags for cave_layer and oak. The maxHeight is -512, indicating the vertical extent of the cave layer. A chance of 0.01 governs overall generation probability. Crystals are set to 32 with music reference cubyz:mischol/crystals. StoneBlock is defined as cubyz:slate/smooth. Ground structure includes a grass/temperate block and two soil blocks (2 to 3). Structures array contains one entry for id cubyz:sbb using tree/oak/young with placeMode degradable and chance 0.32. CaveModels array defines partial_sphere models with minAmount 10, maxAmount 20, minRadius 20, maxRadius 30.

## Related Questions
- What is the vertical extent of this cave biome?
- Which tags are associated with this cave configuration?
- How many crystals does this biome generate?
- What music track plays in this biome?
- What stone block type is used for this biome?
- What ground structures compose the surface layer?
- What structure ID is defined and what is its placement mode?
- What cave model is configured and what are its radius bounds?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_crystal_forest.zig.zon_chunk_0*
