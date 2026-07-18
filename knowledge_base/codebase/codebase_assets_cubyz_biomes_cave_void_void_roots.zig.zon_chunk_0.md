# [easy/codebase_assets_cubyz_biomes_cave_void_void_roots.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave biome, fog properties, structures, music, ground patches, stalagmites, boulders
**Concepts:** world generation, biome configuration

## Summary
Defines configuration for the Void Roots cave biome in Cubyz, including fog properties, music, and various structures.

## Explanation
This chunk defines a configuration for the Void Roots cave biome in Cubyz. It specifies that it is a cave biome with tags .root_layer and .root_transition_layer, fog density of 10, fog color of #272334 (in hexadecimal), generation chance of 1, and a cave radius factor of -1. The biome has associated music 'cubyz:totaldemented/root'. It contains several structures such as simple vegetation with blocks like torches and workbenches, ground patches made of gravel, stalagmites made of slate/smooth, and boulders made of both rough and smooth slate. Specific details for each structure include:
- Simple vegetation (torch): chance = 0.0001
- Simple vegetation (workbench): chance = 0.000001
- Ground patch: block = gravel, chance = 0.064, width = 5, variation = 5, depth = 3, smoothness = 0.1
- Stalagmite: block = slate/smooth, chance = 0.048, size = 3, size_variation = 6
- Boulder (rough): block = slate/rough, chance = 0.016, size = 4, size_variance = 3
- Boulder (smooth): block = slate/smooth, chance = 0.016, size = 2, size_variance = 5 Additionally, it includes cave models defined by spheres with minAmount and maxAmount both set to 1, minRadius and maxRadius both set to 80, and a maximum biome center distance of 0.

## Related Questions
- What are the specific chances for generating torches and workbenches in the Void Roots cave biome?
- What is the exact block type used for ground patches in the Void Roots cave biome?
- How does the size variation differ between rough and smooth boulders in the Void Roots cave biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_void_void_roots.zig.zon_chunk_0*
