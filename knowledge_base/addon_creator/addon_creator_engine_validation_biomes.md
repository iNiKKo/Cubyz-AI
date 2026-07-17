# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk biomes

**Type:** reference
**Keywords:** minRadius, maxRadius, music, totaldemented, cave-layer, validPlayerSpawn, biome-defaults
**Symbols:** server/terrain/biomes.zig, Biome.init
**Concepts:** engine-default-values, validation-errors, silent-fallback

## Summary
Exact engine-side default values and error messages for every Cubyz biome field, read directly
from `server/terrain/biomes.zig: Biome.init()`.

## Explanation
Engine defaults if a field is missing:
- `.minRadius`/`.maxRadius` (or legacy `.radius`): `256` for min, `= minRadius` for max if unset
- `.stoneBlock`: `"cubyz:slate/smooth"`
- `.fogColor`/`.skyColor`: `u32`, default `0xffbfe2ff` / a hardcoded light-blue vector -- the website exports a 3-component float vector instead of a packed u32, a real format mismatch (see the bugs chunk)
- `.fogDensity`: `1.0` (then internally divided by `15.0*128.0` -- purely internal math)
- `.roughness`/`.hills`/`.mountains`/`.keepOriginalTerrain`: `0` each
- `.interpolation`: `"square"` if missing or invalid
- `.caveSmoothness`: `4.0`, clamped to `[0.00001, 4.0]` -- not exposed by the website form at all
- `.caveNoiseStrength`: `8` -- not exposed by the website form
- `.caveRadiusFactor`: `1`, clamped to `[-2, 2]`
- `.crystals`: `0`
- `.soilCreep`: `0.5` (website form default is `1.0` -- different)
- `.minHeight`/`.maxHeight`: full i32 range; logs `"Biome {id} has invalid height range ({min}, {max})"` if min > max
- `.minHeightLimit`/`.maxHeightLimit`: full i32 range
- `.smoothBeaches`: `false`
- `.rivers`: `false` -- not exposed by the website form at all
- `.music`: `"cubyz:totaldemented/cubyz"` (the website's own form default is `'cubyz:sunrise'` instead -- different, only matters if hand-omitted)
- `.validPlayerSpawn`: `false` -- the website writes `.isValidPlayerSpawn` instead, a field-name mismatch (see the bugs chunk)
- `.chance`: `1` normally, `0` if the whole biome entry is null
- `.tags`: empty list. Cave biomes (`isCave = true`) specifically require a tag ending in `"_layer"`, or the engine logs `"Cave biome {id} is missing a '_layer' tag to assign it to a cave layer."` -- the website's generic tag-pill UI doesn't prompt for or validate this
- Radius sanity checks: logs `"Biome {id} has invalid radius range ({min}, {max})"` if minRadius > maxRadius, and `"Biome {id} has radius {r}, smaller than grid resolution..."` if minRadius is too small relative to the world's biome grid size
- `.parentBiomes`, `.transitionBiomes`: no default, sub-biome nesting and biome-transition-blending systems, entirely unexposed by the website
- `.caveModels`, `.stripes`: no default, additional advanced generation features, hand-edit only

## Related Questions
- What do min/max radius default to for a Cubyz biome if not set?
- What does a Cubyz biome's music field default to if omitted?
- What music does the Addon Creator website itself default to for biomes, and how does that differ from the engine's default?
- What tag convention do cave biomes need in Cubyz, and what happens if it's missing?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_biomes*
