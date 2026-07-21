# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 4

**Type:** documentation
**Keywords:** biomes.zig, Biome.init, minRadius, maxRadius, caveSmoothness, caveNoiseStrength, soilCreep, rivers, parentBiomes, transitionBiomes, tags _layer
**Symbols:** Biome.init()

## Summary
Engine-side default values and error messages for every Cubyz biome field, read directly from `server/terrain/biomes.zig: Biome.init()`.

## Explanation
`.minRadius`/`.maxRadius` (or legacy `.radius`) default to `256` for min, `= minRadius` for max if unset -- the engine derives internal `radius`/`radiusVariation` from these, not stored raw. `.stoneBlock` defaults to `"cubyz:slate/smooth"`. `.fogColor`/`.skyColor` are **u32**, defaulting to `0xffbfe2ff` / a hardcoded light-blue vector (see the bug note in chunk 0 -- website exports a vector, not a packed int). `.fogDensity` defaults to `1.0`, then internally divided by `15.0*128.0` (the website's raw value is what's stored; the division is purely internal math). `.roughness`/`.hills`/`.mountains`/`.keepOriginalTerrain` default to `0` each. `.interpolation` defaults to `"square"` if missing or invalid. `.caveSmoothness` defaults to `4.0`, clamped to `[0.00001, 4.0]` -- **not exposed by the website form at all**. `.caveNoiseStrength` defaults to `8` -- **not exposed by the website form**. `.caveRadiusFactor` defaults to `1`, clamped to `[-2, 2]`, website field name matches. `.crystals` defaults to `0`. `.soilCreep` defaults to `0.5` (website form default is `1.0` -- different). `.minHeight`/`.maxHeight` default to the full i32 range; logs `"Biome {id} has invalid height range ({min}, {max})"` if min > max. `.minHeightLimit`/`.maxHeightLimit` default to the full i32 range. `.smoothBeaches` defaults to `false`. `.rivers` defaults to `false`, field name is `rivers`, **not exposed by the website form at all**. `.music` defaults to `"cubyz:totaldemented/cubyz"` (website form default is `'cubyz:sunrise'` -- different, only matters if hand-omitted). `.validPlayerSpawn` defaults to `false` (see bug note in chunk 0 -- website writes `.isValidPlayerSpawn` instead). `.chance` defaults to `1` normally, `0` if the whole biome entry is null. `.tags` defaults to empty -- **cave biomes (`isCave = true`) specifically require a tag ending in `"_layer"`**, or logs `"Cave biome {id} is missing a '_layer' tag to assign it to a cave layer."`

Radius sanity checks: if minRadius > maxRadius, the engine logs the exact message **`"Biome {id} has invalid radius range ({min}, {max})"`**; if minRadius is too small relative to the world's biome grid size, it logs **`"Biome {id} has radius {r}, smaller than grid resolution..."`**. `.parentBiomes`, `.transitionBiomes` (sub-biome nesting and biome-transition-blending) are entirely unexposed by the website. `.ground_structure`/`.structures` match the website's own formats. `.caveModels`, `.stripes` are additional advanced generation features, hand-edit only.

## Related Questions
- What does a Cubyz biome's .stoneBlock/.fogDensity/.roughness/.interpolation/.caveSmoothness/.caveNoiseStrength/.caveRadiusFactor/.crystals/.soilCreep/.smoothBeaches field default to if omitted?
- Is a Cubyz biome's .rivers field exposed on the Addon Creator website?
- What happens if a Cubyz biome's minimum height is greater than its maximum height?
- What happens if a Cubyz biome's minRadius is greater than its maxRadius, or too small relative to the grid?
- What are Cubyz's .parentBiomes and .transitionBiomes fields used for?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_4*
