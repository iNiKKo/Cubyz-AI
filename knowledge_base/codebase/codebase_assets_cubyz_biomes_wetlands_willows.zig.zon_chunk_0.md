# [easy/codebase_assets_cubyz_biomes_wetlands_willows.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** wetlands, willow trees, duckweed patches, lily pads, generation chances, height variation, water surface mode
**Symbols:** properties, tags, minHeight, maxHeight, roughness, chance, hills, minRadius, maxRadius, music, ground_structure, structures, parentBiomes
**Concepts:** biome configuration, terrain generation, structure placement probabilities, water surface flora

## Summary
Configuration data defining wetland biome properties including terrain heights, generation chances, and structure definitions for willow trees and duckweed patches.

## Explanation
This chunk contains a .zon configuration file that defines the Wetlands/Willows biome. It sets environmental properties (wet/hot tags, height range -2 to -2, roughness 2) and specifies ground composition with mud blocks. The structures array defines multiple generation entries: two willow tree variants differing in height (13 vs 11), a flower patch entry for duckweed block variant 0, another for variant 1, one for variant 2, one for variant 3, and a lily pad entry. Each structure includes chance probabilities, width/variation parameters, density values where applicable, priority ordering, generation mode (water_surface for aquatic plants), and specific block identifiers using the cubyz: namespace prefix.

## Related Questions
- What are the wetland biome tags defined in this configuration?
- How is the ground structure composed for the willows biome?
- Which blocks are used for the flower patches in water_surface generation mode?
- What height range does the wetlands biome occupy?
- Are there multiple variants of simple_tree structures and how do they differ?
- What is the chance probability for each duckweed block variant?
- How is priority ordering applied among the structure entries?
- Which music track is associated with this biome configuration?
- What parent biome ID is referenced in the parentBiomes array?
- Does this configuration include any hills or terrain variation parameters?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_wetlands_willows.zig.zon_chunk_0*
