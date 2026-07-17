# [easy/codebase_assets_cubyz_biomes_peak.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** properties, tags, minHeightLimit, maxHeight, smoothBeaches, fogDensity, ground_structure, structures, chance, size_variation
**Symbols:** .properties, .tags, .mountain, .cold, .barren, .wet, .snowy, .minHeightLimit, .minHeight, .maxHeight, .smoothBeaches, .fogDensity, .fogColor, .mountains, .music, .soilCreep, .ground_structure, .structures
**Concepts:** biome configuration, terrain generation parameters, structure spawning rules, fog settings, block definitions

## Summary
Configuration data defining the peak biome with its terrain parameters, block definitions, and structure generation rules.

## Explanation
This chunk is a .zon configuration file containing static settings for the 'peak' biome. It defines an enum-like set of properties (.mountain, .cold, .barren, .wet) and tags (.snowy). Numeric parameters include minHeightLimit (7), minHeight (120), maxHeight (256), smoothBeaches (true), fogDensity (1.5), fogColor (0xe2f2ff), mountains count (125), soilCreep (1.0), music path, stoneBlock identifier ('cubyz:glacite/smooth'), and a ground_structure array specifying snow and permafrost layers with quantity ranges. It also declares a structures object containing one structure definition for 'cubyz:stalagmite' made of 'cubyz:ice' with a 0.08 chance and size parameters.

## Related Questions
- What properties are defined for the peak biome configuration?
- Which tags are associated with this biome entry?
- What is the minimum height limit set for terrain generation in this chunk?
- How many mountain structures are configured to generate here?
- What music track is assigned to this biome's environment?
- Which block type is specified as the stoneBlock for this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_peak.zig.zon_chunk_0*
