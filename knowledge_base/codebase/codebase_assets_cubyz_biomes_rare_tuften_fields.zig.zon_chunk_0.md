# [easy/codebase_assets_cubyz_biomes_rare_tuften_fields.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** minHeightLimit, maxHeight, smoothBeaches, ground_structure, structures, chance, placeMode, degradable, flower_patch, boulder
**Symbols:** minHeightLimit, minHeight, maxHeight, maxHeightLimit, smoothBeaches, minRadius, maxRadius, roughness, hills, chance, music, validPlayerSpawn, ground_structure, structures
**Concepts:** biome configuration, procedural generation parameters, structure placement rules, height limits, radius constraints, degradable structures, flower patch generation, boulder generation

## Summary
This chunk defines the configuration data for a rare biome named 'tuften_fields', specifying height limits, generation parameters, music, spawn rules, ground structures, and a list of procedural structures including boulders, flower patches, and tuft trees.

## Explanation
The chunk is a .zon file containing only static configuration data with no executable logic. It declares a single object with a set of properties: minHeightLimit (7), minHeight (40), maxHeight (60), maxHeightLimit (50), smoothBeaches (true), minRadius (256), maxRadius (320), roughness (1), hills (15), chance (0.01), music ('cubyz:ikabod/chimes'), validPlayerSpawn (true). The ground_structure field contains an array of two entries: 'cubyz:grass/temperate' and a string specifying '2 to 3 cubyz:soil'. The structures field is an array of six objects, each defining a procedural structure with fields such as id, chance, block/blocks, size, size_variance, width, variation, density, priority, placeMode, or structure. The first entry defines a boulder (id 'cubyz:boulder', chance 0.00016, block 'cubyz:slate/smooth', size 5, size_variance 1). The next two entries define flower patches with id 'cubyz:flower_patch' and different block arrays ('cubyz:daisies' vs 'cubyz:dandelions'), each with width, variation, density, priority. Two entries use the id 'cubyz:sbb' to reference tree structures via a structure string ('cubyz:tree/tuften/tuft_tree', 'cubyz:tree/tuften/young_tuft_tree') and placeMode '.degradable'. The final entry defines another flower patch with blocks from 'cubyz:grass/vegetation/temperate' and higher chance/density/priority values. All identifiers are preserved exactly as written.

## Related Questions
- What is the minimum height limit for this biome?
- Which music track plays in this biome?
- Is player spawning allowed here?
- How many hills are generated per chunk?
- What is the chance of a boulder appearing?
- Which blocks make up the ground structure?
- Are beach smoothing enabled?
- What is the radius range for generation?
- Does any structure use degradable placement mode?
- How many flower patch entries are defined?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_tuften_fields.zig.zon_chunk_0*
