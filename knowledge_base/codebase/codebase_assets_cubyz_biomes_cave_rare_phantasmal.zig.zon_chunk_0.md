# [easy/codebase_assets_cubyz_biomes_cave_rare_phantasmal.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** fog density, chance of generation, structures, cave models, ground structure
**Concepts:** world generation, biome configuration

## Summary
Defines configuration for the Phantasmal cave biome, including fog properties, generation chances, and structures.

## Explanation
This chunk defines a configuration for the Phantasmal cave biome in Cubyz. It specifies that this is a cave biome with tags indicating it belongs to the cave layer. The fog density is set to 35, and the fog color is a dark blue (0x000C14). The chance of generating this biome is 0.01, and its maximum height is -5000. The music associated with this biome is 'cubyz:ikabod/xeric', and the stone block used is 'cubyz:chalk/black'. The ground structure includes obsidian from level 0 to 1. Structures like phantasmal pillars, flower patches, boulders, and mushrooms are defined as follows:

- **Phantasmal Pillars**: ID = `cubyz:sbb`, Structure = `cubyz:phantasmal/phantasmal_pillars`, Place Mode = degradable, Chance = 0.1.
- **Flower Patch (Glimmergill)**: ID = `cubyz:flower_patch`, Blocks = `cubyz:glimmergill`, Chance = 0.015, Width = 8, Variation = 4, Density = 0.06, Priority = 0.12.
- **Boulder (Basalt)**: ID = `cubyz:boulder`, Chance = 0.008, Block = `cubyz:basalt/smooth`, Size = 4, Size Variance = 12.
- **Small Mushroom (Glimmergill)**: ID = `cubyz:sbb`, Structure = `cubyz:mushroom/small/glimmergill`, Place Mode = degradable, Chance = 0.03.
- **Big Mushroom (Glimmergill)**: ID = `cubyz:sbb`, Structure = `cubyz:mushroom/big/glimmergill`, Place Mode = degradable, Chance = 0.02.

Additionally, cave models such as partial spheres are specified with the following details:
- **Partial Sphere**: ID = `cubyz:partial_sphere`, Min Amount = 1, Max Amount = 5, Min Radius = 30, Max Radius = 40.

## Related Questions
- What is the fog color for the Phantasmal cave biome?
- What is the maximum height of the Phantasmal cave biome?
- Which structures are defined in the Phantasmal cave biome configuration?
- What is the chance of generating a flower patch in the Phantasmal cave biome?
- What type of stone block is used in the Phantasmal cave biome?
- How many different types of cave models are specified for the Phantasmal cave biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_rare_phantasmal.zig.zon_chunk_0*
