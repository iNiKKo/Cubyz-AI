# [easy/codebase_assets_cubyz_biomes_savannah_elevated.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** savannah biome, elevated variant, baobab trees, vegetation tags, ground structure references, spawnable structures, player spawn validation, roughness parameter, height limits, parent biome linking
**Symbols:** properties, tags, minHeight, maxHeight, minRadius, maxRadius, roughness, chance, hills, validPlayerSpawn, ground_structure, stoneBlock, structures, parentBiomes
**Concepts:** biome configuration, terrain generation parameters, structure spawning rules

## Summary
Defines the elevated savannah biome configuration with terrain height limits, vegetation tags, ground structure references, and a list of spawnable structures including baobab trees and various patches.

## Explanation
This chunk is a .zon configuration file defining the 'elevated' variant of the savannah biome. It sets environmental properties (.hot, .dry) and tags (.baobab, .cactus). Terrain generation parameters include minHeight=64, maxHeight=65, minRadius=80, maxRadius=128, roughness=15, hills=2. The validPlayerSpawn flag is true. Ground structure references cubyz:grass/temperate. StoneBlock is set to cubyz:limestone/smooth. Structures are defined as an array of objects with id, blocks (or block), chance, width, variation, density, priority, height, depth, smoothness, placeMode, and structure fields; entries include flower_patch variants using cubyz:grass/vegetation/dry or cubyz:marigold, simple_vegetation using cubyz:cactus, ground_patch using cubyz:dirt or cubyz:grass/dry, sbb (baobab) structures referencing cubyz:tree/baobab/young and cubyz:tree/baobab/grandidieri with placeMode .degradable. ParentBiomes contains a single entry pointing to cubyz:savannah/base with chance=8.

## Related Questions
- What are the environmental properties defined for this elevated savannah biome?
- Which vegetation tags are associated with this biome configuration?
- What is the minimum and maximum height range for terrain generation in this biome?
- How many hills are configured for this biome variant?
- Is player spawning allowed in this biome according to its configuration?
- What ground structure block type does this biome reference by default?
- Which stone block type is specified as the primary stone for this biome?
- List all structure entries defined within this biome's configuration.
- What baobab tree structures are included and what are their spawn chances?
- How do the flower_patch variants differ in terms of blocks used and density settings?
- What parent biome does this elevated savannah reference and with what chance value?
- Are any structures marked as degradable and which ones?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_savannah_elevated.zig.zon_chunk_0*
