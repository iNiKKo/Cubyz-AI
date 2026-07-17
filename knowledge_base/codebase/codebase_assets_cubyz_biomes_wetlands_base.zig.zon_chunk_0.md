# [easy/codebase_assets_cubyz_biomes_wetlands_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** wetland biome, height limits, ground structure, flower patch, willow tree, mud layer, generation chance, water surface, roughness, hills
**Symbols:** wet, hot, willow, minHeightLimit, minHeight, maxHeight, maxHeightLimit, roughness, hills, minRadius, maxRadius, music, ground_structure, chance, structures
**Concepts:** biome configuration, terrain generation, structure placement, water surface generation, randomized world features

## Summary
This chunk defines the wetland biome configuration with terrain height limits, generation chance, and a list of ground structures including mud patches, willow trees, and water surface flower patches.

## Explanation
The chunk is a .zon configuration file containing static data for the wetland biome. It declares properties (wet, hot), tags (willow), height limits (minHeight 1, maxHeight 1, minHeightLimit 0, maxHeightLimit 5), roughness (2), hills (7.5), and generation chance (0.5). The ground_structure field lists two entries: a lush grass layer and mud layers ranging from 5 to 7 blocks thick. The structures array defines multiple biome features with their own parameters: cubyz:ground_patch (mud, chance 0.33, width 5, variation 4, depth 1, smoothness 0.5), two instances of cubyz:simple_tree (willow leaves and log, type round, height 12 or 10 with variations, leafRadius 4.0, leafElongation 0.4, branched false), and three instances of cubyz:flower_patch (duckweed variants 0-3 and lily_pad variants 0-3) all using generationMode water_surface with varying chances, widths, densities, and priorities.

## Related Questions
- What are the wetland biome properties defined in this configuration?
- Which tags are associated with the wetland biome?
- What is the minimum and maximum height range for the wetland terrain?
- How does the ground_structure field define the base layers of the wetland biome?
- List all structures included in the wetland biome and their generation chances.
- What blocks are used for the flower patches on water surfaces?
- Are any of the tree structures branched, and what is their height variation?
- How does the roughness value affect terrain generation in this biome?
- What music track is assigned to the wetland biome?
- Can you explain the difference between the two ground_structure entries?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_wetlands_base.zig.zon_chunk_0*
