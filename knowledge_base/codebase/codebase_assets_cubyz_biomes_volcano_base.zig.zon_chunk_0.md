# [easy/codebase_assets_cubyz_biomes_volcano_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** mountain radius, uniform height, linear interpolation, ash ground, basalt stone, sub-biome parent, structure chance, soil creep, ground patch
**Symbols:** .properties, .radius, .minHeight, .maxHeight, .interpolation, .mountains, .chance, .music, .parentBiomes, .maxSubBiomeCount, .soilCreep, .ground_structure, .stoneBlock, .structures
**Concepts:** biome configuration, terrain generation parameters, parent biome hierarchy, ground structure composition, static asset definition

## Summary
Defines the Volcano Base biome configuration with a fixed mountain radius of 320 and uniform height range (128–128), linear interpolation, zero chance for random generation, ash ground structure, basalt stone block, and a single sub-biome parent pointing to cubyz:mountains.

## Explanation
This chunk is a .zon configuration file that declares the Volcano Base biome's static properties. It sets the biome type via .properties = .{.mountain}, fixes the generation radius at 320 and constrains both minHeight and maxHeight to 128, implying a perfectly flat mountainous terrain without vertical variation. Interpolation is set to linear for smooth transitions. The chance field is zero, indicating no random procedural elements are applied during generation. Music is assigned from the cubyz namespace (cubyz:mrmayman/out_of_breath). ParentBiomes contains exactly one entry with id cubyz:mountains and a 0.1 probability weight. maxSubBiomeCount is set to 1, limiting nesting depth. SoilCreep is enabled at level 1. Ground structure specifies a list containing the string '2 to 4 cubyz:ash', defining the surface layer composition. StoneBlock is explicitly set to 'cubyz:basalt/smooth'. Structures defines an array with one ground_patch entry that uses block 'cubyz:basalt/smooth' and includes parameters for chance (0.1), width (5), variation (5), depth (4), and smoothness (0.1). All fields are literal values or inline arrays; no executable logic is present.

## Related Questions
- What is the radius of the Volcano Base biome?
- Does the Volcano Base biome have any vertical height variation?
- Which parent biome does the Volcano Base reference and with what chance?
- What block type is used for the ground structure in this biome?
- Is soil creep enabled for the Volcano Base biome?
- How many sub-biomes can be nested under the Volcano Base?
- What music track is assigned to the Volcano Base biome?
- Does the Volcano Base biome include any procedural structures?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_volcano_base.zig.zon_chunk_0*
