# [easy/codebase_assets_cubyz_biomes_rare_spawn.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** spawn chance, height limits, ground structure, simple tree, vegetation patch, flower patch, slate block, torch placement, smooth beaches
**Symbols:** chance, minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, minRadius, maxRadius, roughness, hills, music, validPlayerSpawn, ground_structure, structures
**Concepts:** biome configuration, terrain generation, structure placement rules, sparse world seeding

## Summary
Defines a rare biome configuration with terrain generation parameters and sparse structure placement rules.

## Explanation
This chunk contains only static data fields defining the properties of a rare biome. It sets a 1% spawn chance, height limits between 22 and 40 blocks (with smoothing beaches enabled), and radius bounds from 256 to 320. The ground_structure field lists temperate grass and soil layers. The structures array defines multiple sparse placements: simple oak trees with varying log/leaf block IDs and heights, plus several vegetation patches using slate/smooth, slate/rough, soil, workbench blocks, and flower patches composed of torches or slates.

## Related Questions
- What is the spawn chance for this biome?
- Which ground structures are defined in this configuration?
- How many simple tree entries exist and what are their chances?
- List all vegetation patch block IDs used here.
- Are torches included in any flower patches?
- Does this biome allow player spawning?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_spawn.zig.zon_chunk_0*
