# [easy/codebase_assets_cubyz_biomes_hills_huge__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** height limit, radius, roughness, hill distribution, structure chance
**Symbols:** minHeightLimit, minHeight, maxHeight, smoothBeaches, minRadius, maxRadius, roughness, hills, mountains, soilCreep, chance, validPlayerSpawn, structures
**Concepts:** biome configuration, structure generation

## Summary
Huge hills biome configuration

## Explanation
Defines a huge hills biome with specific parameters for height, radius, roughness, hill/mountain distribution, soil creep, player spawn validity, and structure generation. The biome has the following properties:

- **minHeightLimit**: 50
- **minHeight**: 60
- **maxHeight**: 130
- **maxHeightLimit**: 150
- **smoothBeaches**: true
- **minRadius**: 128
- **maxRadius**: 220
- **roughness**: 3
- **hills**: 60
- **mountains**: 40
- **soilCreep**: 1.5
- **chance**: 0.2
- **validPlayerSpawn**: true

Structures included in this biome and their configurations are:

- **Ground Patch**
  - **id**: cubyz:ground_patch
  - **block**: cubyz:gravel
  - **chance**: 0.02
  - **width**: 5
  - **variation**: 5
  - **depth**: 3
  - **smoothness**: 0.1
- **Boulder**
  - **id**: cubyz:boulder
  - **block**: cubyz:slate/smooth
  - **chance**: 0.005
  - **size**: 5
  - **size_variance**: 1
- **Flower Patch (Daisies)**
  - **id**: cubyz:flower_patch
  - **blocks**: [cubyz:daisies]
  - **chance**: 0.003
  - **width**: 10
  - **variation**: 6
  - **density**: 0.3
  - **priority**: 0.1
- **Flower Patch (Dandelions)**
  - **id**: cubyz:flower_patch
  - **blocks**: [cubyz:dandelions]
  - **chance**: 0.002
  - **width**: 6
  - **variation**: 4
  - **density**: 0.3
  - **priority**: 0.1

## Related Questions
- What is the minimum height limit for this biome?
- How many hills are generated in this biome?
- What is the maximum radius of the hills?
- What is the roughness level of the terrain?
- What structures are included in this biome and their chances?
- Is it valid for players to spawn on this biome?
- What block is used for ground patches?
- How many boulders are generated per chunk?
- What blocks are used for flower patches?
- What is the width of flower patches?
- What is the density of flower patches?
- What is the priority of flower patches?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_hills_huge__defaults.zig.zon_chunk_0*
