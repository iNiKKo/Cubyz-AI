# [easy/codebase_assets_cubyz_biomes_rocky_grassland.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** properties, tags, chance, minHeightLimit, maxHeightLimit, smoothBeaches, radius bounds, mountains, ground_structure, structures
**Symbols:** properties, tags, chance, minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, minRadius, maxRadius, mountains, music, ground_structure, structures
**Concepts:** biome configuration, terrain generation, structure placement rules, oak tree generation, boulder generation, height limits, radius bounds, music assignment, ground layering

## Summary
Configuration data defining a rocky grassland biome with terrain generation parameters, structure placement rules for oak trees and boulders, and associated music.

## Explanation
This chunk is a .zon configuration file containing static biome settings. It defines properties including tags (oak), chance values (0.25), height limits (minHeight=20, maxHeight=40, minHeightLimit=7, maxHeightLimit=50), smoothBeaches flag (true), radius bounds (minRadius=256, maxRadius=320), mountains count (30), and music reference ('cubyz:sinanimea/sunrise'). The ground_structure field lists two entries: 'cubyz:grass/temperate' for the base layer and a conditional soil layer defined as '0 to 1 cubyz:soil'. The structures array contains three distinct structure definitions: first, an oak tree with id 'cubyz:simple_tree', leaves material 'cubyz:leaves/oak', log material 'cubyz:log/oak', placement chance 0.014, type .round, height 6, and height_variation 3; second, a structure with id 'cubyz:sbb' referencing 'cubyz:tree/oak/young' using placeMode .degradable at chance 0.002; third, a boulder with id 'cubyz:boulder', block material 'cubyz:slate/rough', size 5, and size_variance 4.

## Related Questions
- What tags are assigned to this biome configuration?
- What is the chance value for generating structures in this biome?
- What height limits are defined for terrain generation here?
- Which music track is associated with this rocky grassland biome?
- What ground layers are specified for this biome's surface?
- How many mountains are configured to generate in this biome?
- What structure definition corresponds to the oak tree in this configuration?
- What place mode is used for the sbb structure entry?
- Which block material is assigned to the boulder structure?
- What size and size_variance values are set for the boulder?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rocky_grassland.zig.zon_chunk_0*
