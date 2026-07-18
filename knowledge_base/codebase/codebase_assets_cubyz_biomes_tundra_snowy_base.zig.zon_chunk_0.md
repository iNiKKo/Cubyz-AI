# [easy/codebase_assets_cubyz_biomes_tundra_snowy_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome configuration, terrain features, structures, height limits, radius
**Concepts:** world generation

## Summary
Defines configuration for the snowy tundra biome, including height limits, radius, terrain features, and structures.

## Explanation
This chunk contains a JSON-like structure defining various parameters for the snowy tundra biome in Cubyz. It specifies minHeightLimit as 0, minHeight as 18, maxHeight as 20, maxHeightLimit as 30, minRadius as 256, maxRadius as 320, hills as 15, mountains as 15, stoneBlock as 'cubyz:glacite/smooth', chance as 0.5, ground_structure as ['1 cubyz:snow', '1 to 2 cubyz:permafrost'], and structures array including different types of ground patches with specific chances, blocks, sizes, and other attributes such as:

- Ground patch with block 'cubyz:ice' having a generationMode of .water_surface, chance of 0.9, width of 8, variation of 4, depth of 1, and smoothness of 0.5.
- Ground patch with block 'cubyz:permafrost' having a chance of 0.01, width of 6, variation of 4, depth of 1, and smoothness of 0.3.
- Boulder structure with block 'cubyz:snow', chance of 0.01, size of 5, and size_variance of 2.

## Related Questions
- What is the minimum height limit for the snowy tundra biome?
- Which block type is used for the stone in the snowy tundra biome?
- How many different types of ground patches are defined for the snowy tundra biome?
- What is the chance of generating a boulder in the snowy tundra biome?
- What is the maximum height limit for the snowy tundra biome?
- Which block types are included in the ground structure of the snowy tundra biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_tundra_snowy_base.zig.zon_chunk_0*
