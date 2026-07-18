# [easy/codebase_assets_cubyz_biomes_hills__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** terrain height, beach smoothness, radius range, roughness, hill count, structure probability
**Concepts:** world generation, biome configuration

## Summary
Defines default configuration for hills biomes in Cubyz, including terrain height limits, beach smoothness, radius, roughness, hill count, and structure probabilities.

## Explanation
This chunk contains a JSON-like configuration object defining the properties of hills biomes in the Cubyz game engine. The specific values are as follows:

- **Minimum Height Limit:** 7
- **Minimum Height:** 22
- **Maximum Height:** 60
- **Maximum Height Limit:** 65
- **Beach Smoothness:** true
- **Minimum Radius:** 128
- **Maximum Radius:** 256
- **Terrain Roughness:** 1
- **Number of Hills:** 20
- **Structure Probability (Boulder):** ID = cubyz:boulder, Chance = 0.003, Block Type = cubyz:slate/smooth, Size = 5, Size Variance = 1
- **Structure Probability (Daisies Flower Patch):** ID = cubyz:flower_patch, Blocks = [cubyz:daisies], Chance = 0.003, Width = 10, Variation = 6, Density = 0.3, Priority = 0.1
- **Structure Probability (Dandelions Flower Patch):** ID = cubyz:flower_patch, Blocks = [cubyz:dandelions], Chance = 0.002, Width = 6, Variation = 4, Density = 0.3, Priority = 0.1

## Related Questions
- What is the minimum height limit for hills biomes?
- Is beach smoothing enabled in hills biomes?
- What is the maximum radius of hills biomes?
- How many hills are typically generated in a hills biome?
- What is the chance of generating a boulder structure in hills biomes?
- Which blocks can be found in flower patches within hills biomes?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_hills__defaults.zig.zon_chunk_0*
