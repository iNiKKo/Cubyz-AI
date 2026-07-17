# [easy/codebase_assets_cubyz_biomes_cave_void_void_roots.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cave biome, root layer, fog density, vegetation structures, stalagmite generation, boulder placement, sphere model, procedural chance, height variation, block references
**Symbols:** isCave, tags, fogDensity, fogColor, chance, caveRadiusFactor, music, structures, caveModels
**Concepts:** biome configuration, procedural generation, structure placement, fog rendering, tag system, model definition

## Summary
Defines a cave biome configuration with fog settings, root-layer tags, music reference, and procedural structure definitions including vegetation, stalagmites, boulders, and sphere models.

## Explanation
This chunk is a .zon configuration file containing static data for the cave void biome. It declares boolean flag isCave set to true and an array of tags identifying it as root_layer and root_transition_layer. Fog parameters are defined with fogDensity at 10 and fogColor as hex value 0x272334. A chance field is set to integer 1, while caveRadiusFactor is -1 indicating no radius scaling. The music field references the string cubyz:totaldemented/root. The structures array contains six entries defining procedural generation rules: two vegetation entries sharing id cubyz:simple_vegetation with different blocks (torch and workbench) each having chance 0.0001 and 0.000001 respectively, both at height 1; a ground_patch entry with block gravel, chance 0.064, width 5, variation 5, depth 3, smoothness 0.1; two stalagmite entries using block slate/smooth with chances 0.048 and sizes 3/6; and two boulder entries using blocks slate/rough and slate/smooth each with chance 0.016 and respective size/variance values. The caveModels array contains one entry defining a sphere model with id cubyz:sphere, minAmount and maxAmount both set to 1, fixed radius of 80, and maxBiomeCenterDistance set to 0.

## Related Questions
- What is the fog color value defined for this cave biome?
- Which tags are assigned to identify this as a root layer biome?
- How many vegetation structure definitions are present in the structures array?
- What block type is used for the ground patch generation rule?
- Is there any radius scaling applied to caves in this configuration?
- What music track is referenced by this biome definition?
- Which model ID is defined inside the caveModels array?
- What are the min and max amount values set for the sphere model?
- How many boulder entries exist and what blocks do they use?
- What is the chance value assigned to the stalagmite structure entry?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_void_void_roots.zig.zon_chunk_0*
