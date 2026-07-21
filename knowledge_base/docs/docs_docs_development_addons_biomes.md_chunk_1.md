# [easy/docs_docs_development_addons_biomes.md] - Chunk 1

**Type:** documentation
**Keywords:** zig.zon, isCave, radius, minHeight, maxHeight, smoothBeaches, interpolation, roughness, hills, mountains, stoneBlock, fogColor, skyColor, isValidPlayerSpawn
**Symbols:** isCave, minRadius, maxRadius, interpolation, interpolationWeight, stoneBlock, skyColor

## Summary
The full field table for a Cubyz biome `zig.zon` file (everything except the `properties` tag list, covered separately in chunk 0), with each field's type, description, and default.

## Explanation
This doc's own field table lists "—" (undocumented) for several defaults below, but the engine source (`server/terrain/biomes.zig: Biome.init()`, see `addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_4.md` for the full authoritative breakdown) fills in real defaults for all of them -- the engine values below are correct and take precedence over "no default" wherever the two seem to conflict.

`isCave` (bool): whether the biome is a cave biome (true) or surface biome (false); defaults to `false`. `radius` (f32): size of the biome, default 256 -- use `minRadius`/`maxRadius` for variable sizes instead. `minHeight`/`maxHeight` (i32): lowest/highest terrain height the biome can generate; default to the full i32 range (`minInt`/`maxInt`), i.e. effectively unbounded. `minHeightLimit`/`maxHeightLimit` (i32): hard lower/upper terrain limit even after interpolation; also default to the full i32 range. `smoothBeaches` (bool): enables smooth beach generation, default false. `interpolation` (enum): border interpolation method, one of `.none`, `.linear`, or `.square` -- **`.smooth` resolves to `.square`** -- default `.square`. `interpolationWeight` (f32): strength of biome interpolation -- **minimum is `std.math.floatMin(f32)`, and its default value is `1`** (two separate facts: the floor is floatMin, the default is 1). `roughness`/`hills`/`mountains`/`keepOriginalTerrain` (f32): apply terrain roughness / rolling hills / spiky mountains / amount of parent biome's terrain preserved in a sub-biome (1 = all, 0.5 = 50%) respectively -- **all four default to `0`**. `caveRadiusFactor`: cave radius multiplier, defaults to `1`, clamped to `[-2, 2]`. `crystals`: average number of randomly placed Glow Crystals, defaults to `0`. `soilCreep`: controls erosion of surface blocks based on terrain slope, defaults to `0.5`. `stoneBlock`: base block the biome is constructed from, default `cubyz:slate/smooth`. `fogLower`/`fogHigher`/`fogDensity`/`fogColor`: fog boundaries default `100.0`/`1000.0`, density defaults `1.0` (then internally divided by `15.0*128.0`), color defaults `0xffbfe2ff`. `skyColor` (vec3f): sky color in RGB, default `{0.46, 0.7, 1.0}`. `stripes`/`subBiomes`/`ground_structure`/`structures`: structural/generation-nesting fields, default to empty. `maxSubBiomeCount` (f32): defaults to `std.math.floatMax(f32)` (effectively unlimited). `parentBiomes` (`[]struct{id: []const u8, chance: f32}`): parent biomes this biome can generate within -- each entry's `chance` field defaults to `1` if omitted. `transitionBiomes`: transition biome definitions, defaults to empty. `music`: music file that loops while the player is in the biome; defaults to `"cubyz:totaldemented/cubyz"`. `isValidPlayerSpawn` (bool): whether players can spawn in this biome, used to ensure the player starts in a biome with trees; defaults to `false` (the actual zon key is `validPlayerSpawn`, not `isValidPlayerSpawn`). `chance`: generation chance or weight; defaults to `1` normally, or `0` if the whole biome entry is null.

## Related Questions
- What are the three valid Cubyz biome interpolation modes, and what does .smooth resolve to?
- What is the minimum value for a Cubyz biome's interpolationWeight field?
- What does the keepOriginalTerrain field control for a Cubyz sub-biome?
- What is Cubyz's default biome sky color, per the addon development documentation?
- What is the purpose of a Cubyz biome's isValidPlayerSpawn flag, per the addon docs?
- What does the chance field default to for an entry in a Cubyz biome's parentBiomes list, if omitted?
- What do a Cubyz biome's .roughness, .hills, .mountains, and .keepOriginalTerrain fields default to if omitted?

*Source: unknown | chunk_id: docs_docs_development_addons_biomes.md_chunk_1*
