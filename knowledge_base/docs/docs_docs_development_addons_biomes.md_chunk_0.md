# [easy/docs_docs_development_addons_biomes.md] - Chunk 0

**Type:** documentation
**Keywords:** zig.zon, GenerationProperties, hot, temperate, cold, inland, land, ocean, wet, dry, barren, balanced, overgrown, mountain
**Symbols:** properties: GenerationProperties, .cold, .wet

## Summary
The `properties: GenerationProperties` field of a Cubyz biome `zig.zon` file: its 15 valid climate/terrain tag values, distinct from the biome's other top-level fields (covered in chunk 1).

## Explanation
Every biome is defined by a `zig.zon` file that contains all the data the world generator needs to generate it. The `properties: GenerationProperties` field gives basic information about the biome that helps the game decide where it should be generated -- it's a list of tags, not a single value. Example usage:
```zig
.properties = .{
    .cold,
    .wet,
},
```
The 15 valid values for this field, grouped by category, are: temperature -- `.hot` / `.temperate` / `.cold`; land/water -- `.inland` / `.land` / `.ocean`; moisture -- `.wet` / `.neitherWetNorDry` / `.dry`; vegetation density -- `.barren` / `.balanced` / `.overgrown`; terrain shape -- `.mountain` / `.lowTerrain` / `.antiMountain`.

## Related Questions
- What are the 15 valid values for a Cubyz biome's generation properties field?
- What does the .properties field of a Cubyz biome zig.zon file contain?
- How do you mark a Cubyz biome as cold and wet using the properties field?

*Source: unknown | chunk_id: docs_docs_development_addons_biomes.md_chunk_0*
