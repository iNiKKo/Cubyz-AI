# [easy/codebase_assets_cubyz_biomes_rare_crimson_wasteland_magma_rock.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** minHeight, maxHeight, roughness, ground_patch, magma block, parentBiomes, interpolation, chance, width variation, depth smoothing
**Symbols:** properties, minHeight, maxHeight, minRadius, maxRadius, roughness, chance, hills, interpolation, stoneBlock, structures, ground_patch, block, parentBiomes
**Concepts:** biome configuration, structure generation parameters, height layering, roughness interpolation

## Summary
Configuration data defining the Crimson Wasteland biome with height bounds, roughness parameters, and a single ground_patch structure using magma blocks.

## Explanation
This chunk is a .zon configuration file containing static biome settings. It declares no executable logic or functions. The properties object includes minHeight (84), maxHeight (85), minRadius (16), maxRadius (36), roughness (24), chance (0), hills (2), interpolation (.linear), and stoneBlock ('cubyz:obsidian'). The structures array contains one entry with id 'cubyz:ground_patch', block 'cubyz:magma', chance 0.4, width 3, variation 2, depth 3, smoothness 0.8. The parentBiomes array references a base biome 'cubyz:rare/crimson_wasteland/base' with chance 6.

## Related Questions
- What is the minimum height for the Crimson Wasteland biome?
- Which block type is used for ground patches in this biome configuration?
- What is the chance value assigned to the ground_patch structure?
- How many hills are configured for this biome layer?
- What interpolation method is specified for terrain generation?
- Which parent biome does this configuration reference and with what chance?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_crimson_wasteland_magma_rock.zig.zon_chunk_0*
