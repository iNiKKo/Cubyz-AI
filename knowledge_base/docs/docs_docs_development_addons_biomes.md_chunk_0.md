# [easy/docs_docs_development_addons_biomes.md] - Chunk 0

**Type:** configuration
**Keywords:** zig.zon, GenerationProperties, terrain height limits, border interpolation, sub-biomes, fog density, sky color, stoneBlock, SimpleStructureModel, isValidPlayerSpawn
**Symbols:** .hot, .temperate, .cold, .inland, .land, .ocean, .wet, .neitherWetNorDry, .dry, .barren, .balanced, .overgrown, .mountain, .lowTerrain, .antiMountain, isCave, radius, minRadius, maxRadius, minHeight, maxHeight, minHeightLimit, maxHeightLimit, smoothBeaches, interpolation, interpolationWeight, roughness, hills, mountains, keepOriginalTerrain, caves, caveRadiusFactor, crystals, soilCreep, stoneBlock, fogLower, fogHigher, fogDensity, fogColor, skyColor, stripes, subBiomes, parentBiomes, transitionBiomes, ground_structure, structures, maxSubBiomeCount, music, isValidPlayerSpawn, chance, .none, .linear, .square, slate
**Concepts:** biome definition files, generation properties, terrain height limits, border interpolation methods, sub-biome generation, fog and sky configuration, structure placement rules, parent biome constraints

## Summary
Biomes are defined by zig.zon files containing generation properties, terrain limits, interpolation settings, fog/sky colors, sub-biome relationships, and structure definitions.

## Explanation
The documentation specifies that every biome is generated from a zig.zon file which includes GenerationProperties for climate classification (hot/temperate/cold), wetness (wet/neitherWetNorDry/dry), terrain type (inland/land/ocean/barren/balanced/overgrown/mountain/lowTerrain/antiMountain), and cave status. Terrain generation is controlled by radius parameters, height limits (minHeight/maxHeight with hard interpolation limits minHeightLimit/maxHeightLimit), roughness factors for hills and mountains, soil creep erosion settings, and a stoneBlock base material defaulting to slate. Border smoothing uses an interpolation method (.none/.linear/.square) weighted by interpolationWeight, while sub-biome generation preserves parent terrain via keepOriginalTerrain and respects maxSubBiomeCount. Fog is configured with lower/upper boundaries, density, and RGB color; sky defaults to a specific blue vector. Biomes define ground_structure arrays, stripe definitions, SimpleStructureModel structures, and transitionBiomes for blending. ParentBiomes specify allowed generation contexts with optional chance weights, while isValidPlayerSpawn restricts spawning to biomes containing trees.

## Related Questions
- What is the default value for the stone block used in biome generation?
- Which interpolation method resolves to .square when using the .smooth alias?
- How does the isValidPlayerSpawn property affect player spawning behavior?
- What field controls the average number of randomly placed Glow Crystals in a biome?
- Can sub-biomes preserve parent terrain, and how is that percentage specified?
- Which properties determine whether a biome generates caves or surface terrain?
- How are transition biomes defined within the zig.zon file structure?
- What happens to terrain generation when interpolationWeight is set to std.math.floatMin(f32)?
- Are there any constraints on how many sub-biomes can exist per biome instance?
- Which climate categories are available for defining a biome's temperature profile?

*Source: unknown | chunk_id: docs_docs_development_addons_biomes.md_chunk_0*
