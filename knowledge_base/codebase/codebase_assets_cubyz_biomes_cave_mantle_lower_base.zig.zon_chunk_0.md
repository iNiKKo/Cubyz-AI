# [easy/codebase_assets_cubyz_biomes_cave_mantle_lower_base.zig.zon] - Chunk 0

**Type:** implementation
**Keywords:** cave biome, configuration, block IDs, chances, sizes, smoothness, generation modes
**Symbols:** isCave, tags, music, chance, caves, soilCreep, fogDensity, fogColor, stoneBlock, ground_structure, structures, caveModels
**Concepts:** biome configuration, cave generation, structure generation, cave models

## Summary
Cave biome configuration

## Explanation
This chunk defines the configuration for a cave biome in Cubyz, including tags, music, chance of occurrence, cave density, soil creep, fog settings, stone block, ground structure, structures to generate, and cave models. Specific parameters include:

- **Tags:** `.lower_mantle_layer`
- **Music Track:** `cubyz:totaldemented/scoria`
- **Chance of Occurrence:** 1 (always present)
- **Cave Density:** -0.03
- **Soil Creep Rate:** 1
- **Fog Settings:**
  - Fog Density: 15
  - Fog Color: `0x3d1a11`
- **Stone Block:** `cubyz:pyrolite/rough`
- **Ground Structures:**
  - Lava (2 to 3 cubyz:lava)
  - Magma (1 to 2 cubyz:magma)
- **Structures:**
  - ID: `cubyz:ground_patch`
    - Block: `cubyz:pyrolite/rough`
    - Chance: 0.05
    - Width: 5
    - Variation: 2
    - Depth: 2
    - Smoothness: 0.9
  - ID: `cubyz:stalagmite` (first entry)
    - Block: `cubyz:pyrolite/rough`
    - Chance: 0.05
    - Size: 12
    - Size Variation: 4
    - Base Slope: 0
    - Top Slope: 8
    - Generation Mode: ceiling
  - ID: `cubyz:stalagmite` (second entry)
    - Block: `cubyz:pyrolite/rough`
    - Chance: 0.1
    - Size: 4
    - Size Variation: 6
    - Generation Mode: ceiling
- **Cave Models:**
  - ID: `cubyz:partial_sphere` (first entry)
    - Min Amount: 10
    - Max Amount: 20
    - Min Radius: 30
    - Max Radius: 60
  - ID: `cubyz:partial_sphere` (second entry)
    - Min Amount: 1
    - Max Amount: 6
    - Min Radius: 60
    - Max Radius: 100
    - Cut Direction: `{0, 0, 1}`
    - Cut Direction Randomness: 0.1
    - Cut Percentage: 0.8
    - Mode: additive

## Related Questions
- What is the name of the cave biome?
- How many tags are associated with this cave biome?
- What music track is played in this cave biome?
- What is the chance of occurrence for this cave biome?
- What is the density of caves in this cave biome?
- What is the soil creep rate in this cave biome?
- What is the fog color used in this cave biome?
- What block is used as the stone block in this cave biome?
- What are the ground structures generated in this cave biome?
- How many structures are defined for this cave biome?
- What is the ID of the first structure in the list?
- What is the chance of occurrence for the first structure?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mantle_lower_base.zig.zon_chunk_0*
