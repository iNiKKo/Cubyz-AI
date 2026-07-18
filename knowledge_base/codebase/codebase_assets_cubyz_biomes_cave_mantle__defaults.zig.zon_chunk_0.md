# [easy/codebase_assets_cubyz_biomes_cave_mantle__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome settings, cave models, default values, terrain generation, engine configuration
**Symbols:** .isCave, .tags, .fogDensity, .fogColor, .stoneBlock, .music, .caveModels
**Concepts:** biome defaults, cave models, cave generation

## Summary
Cave Mantle Biome Defaults

## Explanation
Defines default settings for the Cave Mantle biome. The settings include:
- `.isCave = true`
- Tags: `mantle_layer`
- Fog density: `15`
- Fog color: `0x3d1a11`
- Stone block type: `cubyz:pyrolite/rough`
- Music track: `cubyz:totaldemented/scoria`

Cave models are defined with specific properties:
- First cave model:
  - ID: `partial_sphere`
  - Min amount: `10`
  - Max amount: `20`
  - Min radius: `30`
  - Max radius: `60`

- Second cave model:
  - ID: `partial_sphere`
  - Min amount: `1`
  - Max amount: `1`
  - Min radius: `60`
  - Max radius: `100`
  - Cut direction: `{0, 0, 1}`
  - Cut direction randomness: `0.1`
  - Cut percentage: `0.8`
  - Mode: `additive`

## Related Questions
- What is the fog density for the Cave Mantle biome?
- Which tags are associated with the Cave Mantle biome?
- What is the music track used in the Cave Mantle biome?
- How many cave models are defined for the Cave Mantle biome?
- What is the minimum amount of the first cave model?
- What is the maximum radius of the second cave model?
- What is the cut percentage of the second cave model?
- What mode is used for the second cave model?
- What is the id of the first cave model?
- What is the minAmount of the third cave model?
- What is the maxRadius of the third cave model?
- What is the cutDirectionRandomness of the third cave model?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mantle__defaults.zig.zon_chunk_0*
