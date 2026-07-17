# [easy/codebase_assets_cubyz_biomes_desert_hoodoos_mound.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome config, hoodoo, cactus, sandstone, placeMode, structure chance, terrain preservation, parent biome, flower patch, degradable
**Symbols:** .cactus, .degradable, .properties, .tags, chance, density, height, id, minHeight, maxHeight, mountains, hills, placeMode, priority, roughness, stoneBlock, structure, width
**Concepts:** biome configuration, structure placement, terrain generation parameters, parent biome linking, degradable structures

## Summary
This chunk defines the configuration data for a desert biome featuring hoodoo formations and cactus structures.

## Explanation
The chunk declares a single top-level struct (unnamed in this snippet) containing static configuration values for a biome. It sets properties to an empty map, tags the biome with .cactus, defines generation bounds via minRadius=32 and maxRadius=48, disables chance-based generation (.chance=0), and specifies vertical bounds minHeight=1500 and maxHeight=3000. Terrain preservation is enabled at 99% (keepOriginalTerrain=0.99) with roughness=1. The mountains field is set to 50 and hills to 20. A stoneBlock string points to cubyz:sandstone/rough. The structures array lists four entries: two hoodoo variants (small_medium and cactus/saguaro) plus a young cactus, all using .degradable placeMode with varying chances; one flower_patch entry referencing tussock blocks with width=4, variation=4, density=0.2, priority=0.1. The parentBiomes array contains a single entry linking to cubyz:desert/hoodoos/base with chance=15.

## Related Questions
- What tags are assigned to this desert biome configuration?
- Which stone block type is specified for the terrain surface in this biome?
- How many hoodoo structure variants are defined under structures?
- What placeMode is used for all listed structures in this chunk?
- What is the chance value for the young cactus structure entry?
- Which parent biome ID does this configuration reference?
- What vertical height bounds (minHeight, maxHeight) are set for generation?
- How many hills and mountains counts are configured here?
- What is the keepOriginalTerrain percentage defined in this chunk?
- Does this biome have any chance-based structure generation enabled?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_desert_hoodoos_mound.zig.zon_chunk_0*
