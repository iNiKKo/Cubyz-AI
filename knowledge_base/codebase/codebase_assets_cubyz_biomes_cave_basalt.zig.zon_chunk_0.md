# [easy/codebase_assets_cubyz_biomes_cave_basalt.zig.zon] - Chunk 0

**Type:** implementation
**Keywords:** biome, structure, cave generation, configuration, chance
**Symbols:** isCave, tags, maxHeight, chance, fogDensity, music, stoneBlock, structures, caveModels
**Concepts:** biome configuration, structure placement, cave generation

## Summary
Cave biome configuration for Cubyz game engine

## Explanation
This chunk defines a cave biome with various features such as height, fog density, music, stone block, structures, and cave models. It specifies the chance of each structure appearing and their properties.

- **Maximum Height:** -1000
- **Stone Block:** cubyz:basalt/smooth
- **Music:** cubyz:totaldemented/scoria
- **Fog Density:** 8
- **Structures:"
  - **Lava Spout (cubyz:sbb):** Chance = 0.06
  - **Stalagmite:** Block = cubyz:basalt/smooth, Chance = 0.1, Size = 4, Size Variation = 10
  - **Ground Patch (Magma):** Block = cubyz:magma, Chance = 0.055, Width = 4, Variation = 3, Depth = 3, Smoothness = 0.2
  - **Ground Patch (Lava):** Block = cubyz:lava, Chance = 0.007, Width = 4, Variation = 5, Depth = 1, Smoothness = 1
- **Cave Models:"
  - **Partial Sphere:** Min Amount = 10, Max Amount = 20, Min Radius = 12, Max Radius = 20

## Related Questions
- What is the maximum height of the cave biome?
- What structures are defined for this cave biome and what are their chances of appearing?
- How many partial sphere cave models are generated, and what is their range of radii?
- What is the music associated with this cave biome?
- What block is used as the stone block in this cave biome?
- Which tags does this cave biome have?
- What is the fog density for this cave biome?
- How many structures are defined for this cave biome?
- What is the chance of a stalagmite structure appearing?
- What is the size variation for ground patches?
- What is the depth of ground patches in this cave biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_basalt.zig.zon_chunk_0*
