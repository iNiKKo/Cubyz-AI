# [easy/codebase_assets_cubyz_biomes_cave_mantle_chasm.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome configuration, cave generation, structure placement, block distribution, chance probabilities
**Concepts:** world_generation

## Summary
Defines configuration for a cave mantle chasm biome in Cubyz, including structure and cave model probabilities.

## Explanation
This chunk contains configuration data for a specific biome in the Cubyz game engine named 'cave mantle chasm'. It specifies the probability of generating caves (`caves = -0.03`), and the chance of this biome occurring (`chance = 1`). The structures that can appear within it include two types of stalagmites, one lava pool structure, and two ground patches with different blocks like magma and ash. Additionally, it defines cave models such as cylinders with specified dimensions and generation modes.

**Stalagmite Structures:*
- **First Stalagmite:**
  - ID: `cubyz:stalagmite`
  - Block type: `cubyz:pyrolite/rough`
  - Chance: `0.1`
  - Size: `12` with variation of `4`
  - Base slope: `0`
  - Top slope: `8`
- **Second Stalagmite:**
  - ID: `cubyz:stalagmite`
  - Block type: `cubyz:pyrolite/rough`
  - Chance: `0.2`
  - Size: `4` with variation of `6`

**Lava Pool Structure:**
- **ID:** `cubyz:sbb`
- **Structure:** `cubyz:cave/mantle/lava_pool`
- **Placement Mode:** `.degradable`
- **Chance:** `0.02`

**Ground Patches:*
- **First Ground Patch:**
  - ID: `cubyz:ground_patch`
  - Block type: `cubyz:magma`
  - Chance: `0.04`
  - Width: `4` with variation of `2`
  - Depth: `2`
  - Smoothness: `1`
- **Second Ground Patch:**
  - ID: `cubyz:ground_patch`
  - Block type: `cubyz:ash`
  - Chance: `0.1`
  - Width: `5` with variation of `5`
  - Depth: `4`
  - Smoothness: `0.1`

**Cave Models:**
- **ID:** `cubyz:cylinder`
- **Min Amount:** `10`
- **Max Amount:** `20`
- **Min Radius:** `6`
- **Max Radius:** `10`
- **Min Height:** `80`
- **Max Height:** `200`
- **Mode:** `.additive`

## Related Questions
- What is the chance of generating caves in this biome?
- Which structures can appear in this cave mantle chasm biome?
- How many different types of stalagmites are defined for this biome?
- What is the probability of a lava pool structure appearing in this biome?
- What are the dimensions and generation mode of the cylindrical cave models defined here?
- Which blocks are used to create ground patches in this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mantle_chasm.zig.zon_chunk_0*
