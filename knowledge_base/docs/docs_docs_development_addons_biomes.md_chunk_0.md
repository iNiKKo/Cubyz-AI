# [easy/docs_docs_development_addons_biomes.md] - Chunk 0

**Type:** documentation
**Keywords:** zig.zon, GenerationProperties, hot, temperate, cold, inland, land, ocean, wet, dry, barren, balanced, overgrown, mountain
**Symbols:** properties: GenerationProperties, .cold, .wet

## Summary
The `properties: GenerationProperties` field of a Cubyz biome `zig.zon` file: its 15 valid climate/terrain tag values, distinct from the biome's other top-level fields (covered in chunk 1).

## Explanation
Every biome is defined by a `zig.zon` file that contains all the data the world generator needs to generate it. The `properties: GenerationProperties` field gives basic information about the biome that helps the game decide where it should be generated. This field includes various properties such as climate, terrain type, moisture level, vegetation density, and terrain shape. Each property can be combined to define the unique characteristics of a biome.

### Valid Properties
- **Temperature:** `.hot`, `.temperate`, `.cold`
- **Land/Water:** `.inland`, `.land`, `.ocean`
- **Moisture Level:** `.wet`, `.neitherWetNorDry`, `.dry`
- **Vegetation Density:** `.barren`, `.balanced`, `.overgrown`
- **Terrain Shape:** `.mountain`, `.lowTerrain`, `.antiMountain`

### Example Usage
```zig
.properties = .{
    .cold,
    .wet,
},
```

### Default Values
- `isCave`: `false`
- `radius`: `256`
- `minRadius`: Not specified by default
- `maxRadius`: Not specified by default
- `minHeight`: Not specified by default
- `maxHeight`: Not specified by default
- `minHeightLimit`: Not specified by default
- `maxHeightLimit`: Not specified by default
- `smoothBeaches`: `false`
- `interpolation`: `.square`
- `interpolationWeight`: `1`
- `roughness`: Not specified by default
- `hills`: Not specified by default
- `mountains`: Not specified by default
- `keepOriginalTerrain`: Not specified by default
- `caves`: Not specified by default
- `caveRadiusFactor`: Not specified by default
- `crystals`: Not specified by default
- `soilCreep`: Not specified by default
- `stoneBlock`: `slate`
- `fogLower`: Not specified by default
- `fogHigher`: Not specified by default
- `fogDensity`: Not specified by default
- `fogColor`: Not specified by default
- `skyColor`: `{0.46, 0.7, 1.0}`
- `stripes`: Not specified by default
- `subBiomes`: Not specified by default
- `parentBiomes`: Not specified by default
- `transitionBiomes`: Not specified by default
- `ground_structure`: Not specified by default
- `structures`: Not specified by default
- `maxSubBiomeCount`: Not specified by default
- `music`: Not specified by default
- `isValidPlayerSpawn`: `true`
- `chance`: Not specified by default

## Related Questions
- What are the valid values for a Cubyz biome's generation properties field?
- What does the .properties field of a Cubyz biome zig.zon file contain?
- How do you mark a Cubyz biome as cold and wet using the properties field?
- What is the default value for the `isCave` property in a Cubyz biome?
- What is the default radius value for a Cubyz biome?
- What are the possible values for the `stoneBlock` property in a Cubyz biome?

*Source: unknown | chunk_id: docs_docs_development_addons_biomes.md_chunk_0*
