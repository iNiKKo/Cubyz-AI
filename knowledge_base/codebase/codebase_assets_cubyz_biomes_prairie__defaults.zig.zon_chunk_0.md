# [easy/codebase_assets_cubyz_biomes_prairie__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome properties, terrain structures, configuration file, Prairie biome, Cubyz game engine
**Concepts:** biome configuration, terrain generation

## Summary
Defines default properties and structures for the Prairie biome in Cubyz.

## Explanation
This chunk is a configuration file that specifies default properties and structures for the Prairie biome in Cubyz. The biome has the following properties:
- dry: true
- minHeightLimit: 7
- maxHeightLimit: 60
- smoothBeaches: true
- roughness: 1
- hills: 6
- music: 'cubyz:mischol/simmer'
- validPlayerSpawn: true
The ground structure is defined as:
- 1 cubyz:grass/dry
- 1 to 2 cubyz:dirt
- 3 to 4 cubyz:limestone/smooth
Structures array contains multiple entries, each defining different types of terrain features with specific probabilities and sizes. These include:
- Ground patches with 'cubyz:dirt' blocks (chance: 0.01, width: 5, variation: 4)
- Ground patches with 'cubyz:grass/temperate' blocks (chance: 0.015, width: 9, variation: 7)
- Young oak trees (chance: 0.025)
- Limestone boulders (chance: 0.05, size: 3, size_variance: 6)
- Slate boulders (chance: 0.01, size: 3, size_variance: 4)
- Flower patches with 'cubyz:grass/vegetation/dry' blocks (chance: 0.15, width: 6, variation: 6, density: 0.6, priority: 0.1)
- Simple vegetation with 'cubyz:grass/vegetation/dry' blocks (chance: 0.4, height: 1, height_variation: 0)
- Flower patches with 'cubyz:grass/vegetation/temperate' blocks (chance: 0.06, width: 6, variation: 6, density: 0.6, priority: 0.1)
- Vetch flower patches (chance: 0.005, width: 3, variation: 3, density: 0.4, priority: 0.1)
- Marigold flower patches (chance: 0.01, width: 4, variation: 3, density: 0.4, priority: 0.1)
- Daisies flower patches (chance: 0.02, width: 5, variation: 6, density: 0.7, priority: 0.1)
- Dandelions flower patches (chance: 0.04, width: 5, variation: 6, density: 0.7, priority: 0.1)

## Related Questions
- What is the minimum height limit for the Prairie biome?
- Which music track is associated with the Prairie biome?
- How many different types of structures are defined in the Prairie biome configuration?
- What is the chance of generating a ground patch with 'cubyz:dirt' blocks?
- Which block type is used for young oak trees in the Prairie biome?
- What is the maximum size variance for limestone boulders in the Prairie biome?
- How many different flower types are defined to spawn in the Prairie biome?
- What is the priority level for generating 'cubyz:grass/vegetation/dry' patches in the Prairie biome?
- Is player spawning valid in the Prairie biome?
- What is the roughness setting for the Prairie biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_prairie__defaults.zig.zon_chunk_0*
