# [easy/codebase_assets_cubyz_biomes_cave_mantle_crystal.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome configuration, cave generation, structure placement, probability settings, block types
**Concepts:** world_generation

## Summary
Defines configuration for the cave mantle crystal biome, including generation probabilities and structures.

## Explanation
This chunk contains a JSON-like configuration structure defining properties of the cave mantle crystal biome. It specifies the generation probability of this biome at 0.02 and parameters related to cave formation with an adjustment factor of -0.05 for caves. The chunk also includes details about various structures that can appear within it, such as stalagmites and ground patches. Each structure entry includes specific attributes: 

- **Stalagmite (pyrolite/rough)**:
  - ID: `cubyz:stalagmite`
  - Block type: `cubyz:pyrolite/rough`
  - Generation chance: 0.08 and 0.1 for two different configurations
  - Size: 12 (with size variation of 4) and 4 (with size variation of 6)
  - Slope attributes: baseSlope = 0, topSlope = 8 for the first configuration
- **Ground Patch**:
  - ID: `cubyz:ground_patch`
  - Block type: `cubyz:magma`
  - Generation chance: 0.05
  - Width: 4 with variation of 2
  - Depth: 2
  - Smoothness factor: 1

## Related Questions
- What is the generation probability for the cave mantle crystal biome?
- How does the configuration adjust the chance for caves within this biome?
- What are the specific block types used for stalagmites in this biome?
- What are the exact sizes and variations for each stalagmite structure?
- What slope attributes define the first stalagmite configuration?
- What is the generation probability, width, depth, and smoothness factor for ground patches?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mantle_crystal.zig.zon_chunk_0*
