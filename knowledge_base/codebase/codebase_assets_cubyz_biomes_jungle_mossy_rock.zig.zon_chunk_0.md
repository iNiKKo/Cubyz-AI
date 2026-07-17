# [easy/codebase_assets_cubyz_biomes_jungle_mossy_rock.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, radius, minHeight, maxHeight, roughness, mountains, hills, ground_structure, structures, parentBiomes
**Symbols:** ground_structure, structures, parentBiomes
**Concepts:** biome configuration, terrain generation, structure spawning, world chunk data

## Summary
This chunk defines the configuration data for a jungle biome variant featuring mossy rock terrain generation, including parameters for height ranges, roughness, mountain/hill distribution, and specific ground structure blocks with associated spawn chances.

## Explanation
The chunk is a .zon file containing static configuration values used by the world generation system. It defines a biome entry with fields: chance (0), radius (20), minHeight (1500), maxHeight (3000), keepOriginalTerrain (0.99), roughness (1), mountains (70), hills (20). The ground_structure field specifies the base terrain block as cubyz:slate/smooth. The structures array contains three entries: two ground_patch variants differing by block type (cubyz:moss:cubyz:slate/rough vs cubyz:moss:cubyz:slate/smooth) with respective spawn chances of 0.2 and 0.1, each having width=5, smoothness=0.6, and depth values of 2 and 1; the third entry defines a stalagmite structure using cubyz:slate/smooth block with size=4 and size_variation=3. The parentBiomes array lists two parent biome references: cubyz:jungle/sparse (chance=5) and cubyz:jungle/base (chance=4). No executable logic is present; this chunk serves purely as data for the biome configuration system.

## Related Questions
- What is the spawn chance for the ground_patch structure using cubyz:moss:cubyz:slate/rough?
- Which block type is used for the stalagmite structure in this biome configuration?
- What are the minHeight and maxHeight values defined for this jungle mossy rock biome?
- How many parent biomes are referenced in this chunk's configuration data?
- What is the roughness parameter set to for terrain generation in this chunk?
- Which ground_structure block is specified as the base terrain for this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_jungle_mossy_rock.zig.zon_chunk_0*
