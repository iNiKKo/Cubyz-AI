# [easy/codebase_assets_cubyz_biomes_bushlands_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, placeMode, width, variation, density, priority, depth, smoothness, ground_structure, structures, degradable
**Symbols:** .ground_structure, .structures
**Concepts:** biome configuration, structure placement probabilities, degradable structures, vegetation generation rules

## Summary
This chunk defines the static biome configuration for Bushlands, specifying ground layer structures and a collection of structure definitions with their placement modes, probabilities, block types, dimensions, and density parameters.

## Explanation
The chunk declares a single top-level anonymous struct containing two fields: .ground_structure and .structures. The .ground_structure field is an array literal defining the base terrain layers for Bushlands: first 'cubyz:grass/temperate' followed by 1 to 2 instances of 'cubyz:dirt'. The .structures field is an array literal containing nine distinct structure definitions, each represented as an anonymous struct with fields id, structure (or block), placeMode, chance, and optional width, variation, depth, smoothness, density, priority, or height/height_variation. All entries in the structures array share the same id 'cubyz:sbb' except for two flower_patch entries which use 'cubyz:ground_patch', 'cubyz:flower_patch', and 'cubyz:simple_vegetation'. The placeMode is set to .degradable for all entries, indicating these structures are intended to degrade over time. Each entry specifies a chance value ranging from 0.001 to 0.8, with some including width (e.g., 12), variation (e.g., 4 or 8), depth (2), smoothness (0.2), density (0.3 or 0.4), priority (0.2), and height/height_variation fields for vegetation patches.

## Related Questions
- What is the chance value for the baobab young tree structure in Bushlands?
- Which block types are included in the ground_structure array for Bushlands?
- How many structures are defined under .structures in this biome configuration?
- What placeMode is assigned to all structure definitions in this chunk?
- Does any structure definition include a depth parameter, and if so what value?
- Which entries use 'cubyz:flower_patch' as their id instead of 'cubyz:sbb'?
- What is the maximum chance value among all structures defined here?
- Are there any structures that specify both width and variation fields together?
- Does this configuration include any height_variation parameters for vegetation patches?
- Which structure definition includes a priority field, and what value does it use?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_bushlands_base.zig.zon_chunk_0*
