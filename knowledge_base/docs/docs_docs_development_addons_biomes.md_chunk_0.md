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

### Default Values and Descriptions
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `isCave` | `bool` | Whether the biome is a cave biome (`true`) or a surface biome (`false`). | — |
| `radius` | `f32` | Size of the biome. Use `minRadius` and `maxRadius` for variable sizes. | `256` |
| `minRadius` | `f32` | Minimum biome radius. | — |
| `maxRadius` | `f32` | Maximum biome radius. | — |
| `minHeight` | `i32` | Lowest terrain height the biome can generate. | — |
| `maxHeight` | `i32` | Highest terrain height the biome can generate. | — |
| `minHeightLimit` | `i32` | Hard lower terrain limit, even after interpolation. | — |
| `maxHeightLimit` | `i32` | Hard upper terrain limit, even after interpolation. | — |
| `smoothBeaches` | `bool` | Enables smooth beach generation. | `false` |
| `interpolation` | `Interpolation` | Border interpolation method: `.none`, `.linear`, or `.square`. (`.smooth` resolves to `.square`.) | `.square` |
| `interpolationWeight` | `f32` | Strength of biome interpolation. Minimum is `std.math.floatMin(f32)`. | `1` |
| `roughness` | `f32` | Applies terrain roughness by scattering blocks. | — |
| `hills` | `f32` | Controls rolling hill generation. | — |
| `mountains` | `f32` | Controls spiky mountain generation. | — |
| `keepOriginalTerrain` | `f32` | Amount of the parent biome's terrain preserved in a sub-biome (`1` = all, `0.5` = 50%). | — |
| `caves` | `f32` | Cave generation factor. | — |
| `caveRadiusFactor` | `f32` | Multiplier for cave radius. | — |
| `crystals` | `u32` | Average number of randomly placed Glow Crystals. | — |
| `soilCreep` | `f32` | Controls erosion of surface blocks based on terrain slope. | — |
| `stoneBlock` | `main.blocks.Block` | Base block the biome is constructed from. | `slate` |
| `fogLower` | `f32` | Lower fog boundary. | — |
| `fogHigher` | `f32` | Upper fog boundary. | — |
| `fogDensity` | `f32` | Density of biome fog. | — |
| `fogColor` | `vec3f` | Fog color in RGB. | — |
| `skyColor` | `vec3f` | Sky color in RGB. | `{0.46, 0.7, 1.0}` |
| `stripes` | `[]Stripe` | Stripe definitions used by the biome. | — |
| `subBiomes` | `main.utils.AliasTable(*const Biome)` | Collection of sub-biomes. | — |
| `parentBiomes` | `[]struct{id: []const u8, chance: f32}` | Parent biomes this biome can generate within. `chance` defaults to `1` if omitted. | — |
| `transitionBiomes` | `[]TransitionBiome` | Transition biome definitions. | — |
| `ground_structure` | `[][]const u8` | Ground structure definitions. | — |
| `structures` | `[]SimpleStructureModel` | Structures that can generate in the biome. | — |
| `maxSubBiomeCount` | `f32` | Maximum number of sub-biomes allowed per biome instance. | — |
| `music` | `[]const u8` | Music file that loops while the player is in the biome. | — |
| `isValidPlayerSpawn` | `bool` | Whether players can spawn in this biome. Used to ensure the player starts in a biome with trees. | Not specified by default |
| `chance` | `f32` | Generation chance or weight. | — |

## Related Questions
- What are the valid values for a Cubyz biome's generation properties field?
- What does the .properties field of a Cubyz biome zig.zon file contain?
- How do you mark a Cubyz biome as cold and wet using the properties field?
- What is the default value for the `isCave` property in a Cubyz biome?
- What is the default radius value for a Cubyz biome?
- What are the possible values for the `stoneBlock` property in a Cubyz biome?

*Source: unknown | chunk_id: docs_docs_development_addons_biomes.md_chunk_0*
