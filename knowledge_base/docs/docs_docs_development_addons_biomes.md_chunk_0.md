# [easy/docs_docs_development_addons_biomes.md] - Chunk 0

**Type:** documentation
**Keywords:** zig.zon, biomes, world generation, properties, isCave, radius, minHeight, maxHeight, smoothBeaches, interpolation, roughness, hills, mountains, stoneBlock, fogColor
**Symbols:** zig.zon, properties: GenerationProperties, isCave, radius, minRadius, maxRadius, minHeight, maxHeight, minHeightLimit, maxHeightLimit, smoothBeaches, interpolation, interpolationWeight, roughness, hills, mountains, keepOriginalTerrain, caves, caveRadiusFactor, crystals, soilCreep, stoneBlock, fogLower, fogHigher, fogDensity, fogColor, skyColor, stripes, subBiomes, parentBiomes, transitionBiomes, ground_structure, structures, maxSubBiomeCount, music, isValidPlayerSpawn, chance
**Concepts:** Biome Definition, World Generation, Generation Properties, Biome Characteristics, Environmental Effects

## Summary
Describes the structure and properties of `zig.zon` files used to define biomes in Cubyz, including various generation parameters and settings.

## Explanation
Every biome in Cubyz is defined by a `zig.zon` file that contains essential data for world generation. The `properties: GenerationProperties` field specifies basic information about the biome's characteristics, such as temperature, terrain type, and moisture levels. The table lists various properties like `isCave`, `radius`, `minHeight`, `maxHeight`, and others that control the biome's behavior, appearance, and environmental effects. For example, `smoothBeaches` enables smooth beach generation, while `interpolation` defines how biomes blend with their neighbors. Each property has a specific type and default value, allowing for precise customization of biome generation.

## Related Questions
- What is the purpose of the `zig.zon` file in Cubyz?
- How do you define a cave biome using the `properties: GenerationProperties` field?
- What are the valid values for the `interpolation` property in a `zig.zon` file?
- How does the `smoothBeaches` property affect beach generation in Cubyz?
- What is the default value for the `radius` property in a biome definition?
- How can you specify multiple parent biomes for a single biome using the `parentBiomes` field?
- What role does the `stoneBlock` property play in defining a biome's terrain?
- How do you control the fog density and color in a Cubyz biome?
- Can you explain the purpose of the `stripes` property in a `zig.zon` file?
- What is the significance of the `isValidPlayerSpawn` property in a biome definition?

*Source: unknown | chunk_id: docs_docs_development_addons_biomes.md_chunk_0*
