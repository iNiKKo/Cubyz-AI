# [easy/codebase_assets_cubyz_biomes_desert_hoodoos_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** desert hoodoos, biome config, structure chance, block probability, height limits
**Symbols:** DesertHoodoosBiomeConfig
**Concepts:** biome configuration, structure placement, block types

## Summary
Desert Hoodoos Biome Configuration

## Explanation
This chunk defines a desert hoodoos biome configuration with specific parameters for height, radius, structure placement, and block types. It includes details on the tags associated with the biome, chance of occurrence, minimum and maximum heights, valid player spawn status, structures to place, and their respective probabilities.

- **Tags:** `.cactus`
- **Chance:** `0.2`
- **Minimum Height Limit:** `7`
- **Minimum Height:** `22`
- **Maximum Height:** `40`
- **Maximum Height Limit:** `50`
- **Minimum Radius:** `150`
- **Maximum Radius:** `240`
- **Hills:** `15`
- **Valid Player Spawn:** `false`

**Structures:***
- **cubyz:sbb (small_medium hoodoo):** 
  - Structure: `cubyz:rock/hoodoo/small_medium`
  - Place Mode: `.degradable`
  - Chance: `0.05`
- **cubyz:sbb (large hoodoo):**
  - Structure: `cubyz:rock/hoodoo/large`
  - Place Mode: `.degradable`
  - Chance: `0.002`
- **cubyz:sbb (saguaro cactus):** 
  - Structure: `cubyz:cactus/saguaro`
  - Place Mode: `.degradable`
  - Chance: `0.01`
- **cubyz:sbb (young cactus):**
  - Structure: `cubyz:cactus/young`
  - Place Mode: `.degradable`
  - Chance: `0.006`
- **cubyz:ground_patch (sand block):** 
  - Block: `cubyz:sand`
  - Chance: `0.2`
  - Width: `7`
  - Variation: `4`
  - Depth: `3`
  - Smoothness: `0.4`
- **cubyz:flower_patch (tussock block):** 
  - Blocks: `["cubyz:tussock"]`
  - Chance: `0.03`
  - Width: `4`
  - Variation: `4`
  - Density: `0.2`
  - Priority: `0.1`

**Stone Block:**
- **Block Type:** `cubyz:sandstone/rough`

## Related Questions
- What is the minimum height limit for this desert hoodoos biome?
- How many structures are defined in the configuration?
- What is the maximum radius of the desert hoodoos biome?
- Which block type has a chance of 0.2 to be placed?
- What is the probability of placing a cactus saguaro structure?
- What is the width of the flower patch structure?
- How many blocks are in the flower patch structure's block list?
- What is the priority of the flower patch structure?
- What is the chance of placing a ground patch structure with a specific block type?
- What is the depth of the ground patch structure?
- What is the smoothness of the ground patch structure?
- What are the tags associated with this desert hoodoos biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_desert_hoodoos_base.zig.zon_chunk_0*
