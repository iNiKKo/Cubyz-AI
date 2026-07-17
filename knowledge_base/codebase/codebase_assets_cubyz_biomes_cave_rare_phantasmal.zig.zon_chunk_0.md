# [easy/codebase_assets_cubyz_biomes_cave_rare_phantasmal.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave layer, fog density, phantasmal pillars, glimmergill, basalt smooth, mushroom structure, degradable placement, partial sphere model
**Symbols:** isCave, tags, fogDensity, fogColor, chance, maxHeight, music, stoneBlock, ground_structure, structures, caveModels
**Concepts:** biome configuration, structure placement, fog rendering, degradable structures, partial sphere models

## Summary
Defines a rare phantasmal cave biome configuration with fog settings, ground structures (obsidian), multiple structure placements including pillars and mushroom variants, and partial sphere cave models.

## Explanation
This chunk is a static configuration data file (.zon) defining the properties of a specific cave biome. It sets the biome as a cave layer with fog density 35 and color 0x000C14, a generation chance of 0.01, maximum height -5000, music 'cubyz:ikabod/xeric', and stone block 'cubyz:chalk/black'. The ground_structure field specifies obsidian blocks from 0 to 1. The structures array contains five entries: an id='cubyz:sbb' with structure='cubyz:phantasmal/phantasmal_pillars' using degradable placement mode at 0.1 chance; a flower_patch with blocks=['cubyz:glimmergill'], width=8, variation=4, density=0.06, priority=0.12; a boulder with block='cubyz:basalt/smooth', size=4, size_variance=12 at 0.008 chance; two additional sbb entries referencing mushroom structures (small/glimmergill and big/glimmergill) both degradable at chances 0.03 and 0.02 respectively. The caveModels array defines partial_sphere models with minAmount=1, maxAmount=5, minRadius=30, maxRadius=40.

## Related Questions
- What is the fog color for this biome?
- Which block type is used as the stone block in this cave?
- How many structures are defined in the structures array?
- What is the chance of generating a phantasmal pillar structure?
- Which mushroom structure variants are included and what are their chances?
- What is the maximum height limit for this biome generation?
- What music track plays when this biome generates?
- How many partial sphere models are defined in caveModels?
- What is the density setting for the flower patch structure?
- Is the ground structure obsidian and what range does it cover?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_rare_phantasmal.zig.zon_chunk_0*
