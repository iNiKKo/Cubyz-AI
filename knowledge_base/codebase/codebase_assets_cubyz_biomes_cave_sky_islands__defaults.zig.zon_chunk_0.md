# [easy/codebase_assets_cubyz_biomes_cave_sky_islands__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave sky islands biome, configuration defaults, fog settings, structure generation, music
**Symbols:** isCave, tags, fogColor, fogDensity, fogLower, fogHigher, music, stoneBlock, ground_structure, structures
**Concepts:** biome configuration, structure generation, fog settings

## Summary
Cave Sky Islands Biome Defaults Configuration

## Explanation
This chunk defines the configuration for the Cave Sky Islands biome in Cubyz. The properties include:
- **isCave**: true
- **tags**: sky_island_layer, cirrus
- **fogColor**: 0xbbebff
- **fogDensity**: 5.0
- **fogLower**: 1e10
- **fogHigher**: 1e10
- **music**: cubyz:mischol/sunshower
- **stoneBlock**: cubyz:nimbusite/smooth
- **ground_structure**: consists of cubyz:grass/sky and 2 to 3 layers of cubyz:aerosoil
- **structures**:
  - ID: cbb, structure: cubyz:tree/cirrus/base, placeMode: degradable, chance: 0.02
  - ID: flower_patch (daisies), blocks: cubyz:daisies, width: 6, variation: 3, density: 0.3, priority: 0.1
  - ID: flower_patch (lumiflora), blocks: cubyz:lumiflora, width: 6, variation: 3, density: 0.1, priority: 0.1
  - ID: flower_patch (grass vegetation sky), blocks: cubyz:grass/vegetation/sky, width: 5, variation: 8, density: 0.5, priority: 0.2
  - ID: simple_vegetation (sky grass), block: cubyz:grass/vegetation/sky, chance: 0.4, height: 1, height_variation: 0
  - ID: simple_vegetation (vine cirrus), block: cubyz:vine/cirrus, generationMode: ceiling, chance: 0.2, height: 9, height_variation: 8
  - ID: stalagmite, block: cubyz:nimbusite/smooth, generationMode: ceiling, chance: 0.048, size: 4, size_variation: 6

## Related Questions
- What is the fog color for the Cave Sky Islands biome?
- What are the tags associated with the Cave Sky Islands biome?
- What is the music file used in the Cave Sky Islands biome?
- What is the stone block used in the ground structure of the Cave Sky Islands biome?
- How many structures are defined for the Cave Sky Islands biome?
- What is the chance of placing a flower patch in the Cave Sky Islands biome?
- What is the width of a flower patch in the Cave Sky Islands biome?
- What is the priority of a simple vegetation structure in the Cave Sky Islands biome?
- What block is used for simple vegetation structures in the Cave Sky Islands biome?
- How many different types of flowers are defined for the Cave Sky Islands biome?
- What is the height variation of stalagmite structures in the Cave Sky Islands biome?
- What is the size variation of stalagmite structures in the Cave Sky Islands biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_sky_islands__defaults.zig.zon_chunk_0*
