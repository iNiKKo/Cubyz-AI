# [easy/codebase_assets_cubyz_biomes_rare_rainbow_forest.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** wetness, height limits, smooth beaches, roughness, hills, generation chance, music asset, valid player spawn, ground structure, simple tree, degradable, fog colors
**Symbols:** wet, minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, roughness, hills, chance, music, validPlayerSpawn, ground_structure, structures
**Concepts:** biome configuration, terrain generation parameters, structure placement rules, fog color variation, player spawn validation

## Summary
Defines configuration parameters for the rare rainbow forest biome including terrain height limits, generation chance, music, ground structures, and a collection of simple tree structures with varying fog colors.

## Explanation
This chunk is a .zon configuration file containing static data for the rare rainbow forest biome. It defines numeric properties such as wet (boolean), minHeightLimit (7), minHeight (22), maxHeight (40), maxHeightLimit (60), smoothBeaches (true), roughness (10), hills (10), chance (0.01), and validPlayerSpawn (true). It specifies the music asset cubyz:zeahtrix/foggy_memories. The ground_structure field lists two entries: a temperate grass block and soil blocks with quantity 2 to 3. The structures field contains an array of eight simple_tree objects, each sharing identical structural parameters (type .round, height 0, height_variation 3, leafRadius 16, leafRadius_variation 3, priority 0.1) but differing in color: red, green, blue, yellow, cyan, magenta, plus one entry with id cubyz:sbb referencing structure cubyz:tree/oak/white with placeMode .degradable and chance 0.3.

## Related Questions
- What is the minimum height limit for this biome?
- Which music track plays in this biome?
- Are smooth beaches enabled by default?
- What are the ground structure entries listed here?
- How many simple tree structures are defined in this configuration?
- What fog color corresponds to the magenta entry?
- Is player spawning allowed in this biome?
- What is the chance value for the sbb oak tree structure?
- Which roughness and hills values are set here?
- Are there any structures with a placeMode other than default?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_rainbow_forest.zig.zon_chunk_0*
