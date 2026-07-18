# [easy/codebase_assets_cubyz_biomes_jungle_sparse.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** radius, height limits, structures, ground patches, smooth beaches
**Concepts:** biome configuration, world generation

## Summary
Defines configuration for the Jungle Sparse biome, including radius, height limits, structures, and ground patches.

## Explanation
This chunk contains a JSON-like structure defining various properties of the Jungle Sparse biome in Cubyz. The `radius` is set to 16 cubyz, with no chance for generation (`chance = 0`). Height limits are defined as follows: `minHeightLimit = 7`, `minHeight = 30`, `maxHeight = 50`, and `maxHeightLimit = 60`. The biome also has smooth beaches enabled (`smoothBeaches = true`), with hills set to a value of 12. The ground structure is composed of cubyz:grass/lush and 3-4 blocks of cubyz:mud. The `structures` array lists different structures that can appear in this biome, including mahogany trees (khaya ivorensis and sapele) of various sizes with degradable placement mode and specific probabilities (`chance = 0.05`, `0.1`, etc.). Mud patches have a chance of 7% to appear (`width = 5`, `variation = 6`, `depth = 2`, `smoothness = 0.6`). Flower patches include grass vegetation, monstera plants, ferns, and hibiscus flowers with varying probabilities and densities.

## Related Questions
- What is the radius of the Jungle Sparse biome?
- How many different structures are defined for the Jungle Sparse biome?
- What types of trees are included in the Jungle Sparse biome configuration?
- What is the chance of a mud patch appearing in the Jungle Sparse biome?
- What is the maximum height limit for the Jungle Sparse biome?
- What blocks make up the ground structure in the Jungle Sparse biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_jungle_sparse.zig.zon_chunk_0*
