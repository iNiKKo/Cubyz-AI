# [easy/docs_docs_development_addons_biomes.md] - Chunk 0

**Type:** documentation
**Keywords:** zig.zon, biomes, world generation, properties, isCave, radius, minHeight, maxHeight, smoothBeaches, interpolation, roughness, hills, mountains, stoneBlock, fogColor
**Symbols:** zig.zon, properties: GenerationProperties, isCave, radius, minRadius, maxRadius, minHeight, maxHeight, minHeightLimit, maxHeightLimit, smoothBeaches, interpolation, interpolationWeight, roughness, hills, mountains, keepOriginalTerrain, caves, caveRadiusFactor, crystals, soilCreep, stoneBlock, fogLower, fogHigher, fogDensity, fogColor, skyColor, stripes, subBiomes, parentBiomes, transitionBiomes, ground_structure, structures, maxSubBiomeCount, music, isValidPlayerSpawn, chance
**Concepts:** Biome Definition, World Generation, Generation Properties, Biome Characteristics, Environmental Effects

## Summary
Describes the structure and properties of `zig.zon` files used to define biomes in Cubyz, including various generation parameters and settings.

## Explanation
Every biome in Cubyz is defined by a `zig.zon` file which contains essential data for world generation. The `properties: GenerationProperties` field specifies basic information about the biome's characteristics, such as temperature, terrain type, and moisture levels. Each property has a specific type and default value that allows precise customization of biome generation.

The table lists various properties like `isCave`, `radius`, `minHeight`, `maxHeight`, and others that control the biome's behavior, appearance, and environmental effects:
- `isCave`: A boolean indicating whether the biome is a cave (`true`) or surface biome (`false`). Default: —
- `radius`: Size of the biome. Use `minRadius` and `maxRadius` for variable sizes. Default: 256
- `minHeight`: Lowest terrain height the biome can generate. Default: —
- `maxHeight`: Highest terrain height the biome can generate. Default: —
- `smoothBeaches`: Enables smooth beach generation. Default: false
- `interpolation`: Border interpolation method (`none`, `linear`, or `square`). Default: square
- `roughness`: Applies terrain roughness by scattering blocks. Default: —
- `hills`: Controls rolling hill generation. Default: —\n- `mountains`: Controls spiky mountain generation. Default: —
- `stoneBlock`: Base block the biome is constructed from (e.g., slate). Default: slate
- `fogColor`: Fog color in RGB format. Default: —
- `skyColor`: Sky color in RGB format. Default: {0.46, 0.7, 1.0}
- `subBiomes`: Collection of sub-biomes. Default: —
- `parentBiomes`: Parent biomes this biome can generate within. Default: —

Each property has a specific type and default value that allows precise customization of biome generation.

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
