# [easy/codebase_assets_cubyz_biomes_bushlands_dry.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** properties, tags, chance, keepOriginalTerrain, minRadius, maxRadius, structures, degradable, ground_structure, parentBiomes
**Symbols:** properties, tags, chance, keepOriginalTerrain, minRadius, maxRadius, ground_structure, structures, parentBiomes
**Concepts:** biome configuration, structure generation rules, terrain preservation, radial bounds, degradable structures, flower patches, ground patches, parent biome inheritance

## Summary
This chunk defines the Bushlands Dry biome configuration with its terrain properties and structure generation rules.

## Explanation
The chunk declares a single top-level struct (implicitly named by the file path) containing .properties, .tags, .chance, .keepOriginalTerrain, .minRadius, .maxRadius, .ground_structure, .structures, and .parentBiomes fields. The properties field is an enum literal set to .dry; tags contains a single string literal .cactus; chance is the integer 0 (no random generation); keepOriginalTerrain is the integer 1 (preserve original terrain). minRadius and maxRadius are integers 20 and 64 respectively, defining the radial bounds for structure placement. ground_structure holds a single string literal 

## Related Questions
- What is the chance value for random generation in this biome configuration?
- Which tags are assigned to this biome configuration?
- What is the minimum radius defined for structure placement in this biome?
- What is the maximum radius defined for structure placement in this biome?
- Does this biome preserve original terrain or replace it entirely?
- What ground structure string is specified for this biome configuration?
- How many structures are listed under the .structures field in this chunk?
- Which parent biome ID is referenced by this configuration?
- What placeMode is used for all structures defined in this chunk?
- Are any flower patches defined with a chance greater than zero in this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_bushlands_dry.zig.zon_chunk_0*
