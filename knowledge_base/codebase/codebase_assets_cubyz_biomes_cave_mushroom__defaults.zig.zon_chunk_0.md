# [easy/codebase_assets_cubyz_biomes_cave_mushroom__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** shallow_cave_layer, cubyz:clay, stalagmite, boulder, partial_sphere, fogDensity, spawn chance, size variation
**Symbols:** isCave, tags, fogDensity, music, structures, caveModels
**Concepts:** biome configuration, structure generation, fog density, ambient music, block type selection, spawn chance weighting, size variation parameters, model instance limits

## Summary
Defines default configuration for the cave mushroom biome including fog density, music track, and a list of generated structures with their spawn chances and block types.

## Explanation
This chunk is a .zon configuration file containing static data for the 'cave_mushroom' biome. It sets the biome flag to true, assigns the tag '.shallow_cave_layer', defines fog density as 2, and specifies the music track path. The structures array lists four distinct generation entries: ground patches of clay with a 0.08 chance and size parameters; stalagmites made from slate/smooth blocks at 0.048 chance; two separate boulder entries both using slate but one rough and one smooth block type each at 0.016 chance, differing only in their size_variance values (3 vs 4). The caveModels array contains a single partial_sphere model with min/max amount and radius constraints.

## Related Questions
- What is the fog density value for this biome configuration?
- Which music track is assigned to the cave mushroom biome by default?
- How many distinct structure definitions are included in the structures array?
- What block type is used for the ground patch structure generation?
- Are there multiple boulder entries and if so, how do they differ?
- What is the spawn chance percentage for stalagmite structures?
- Which tag is applied to identify this biome as a shallow cave layer?
- What are the min/max amount constraints for the partial_sphere model?
- Does this configuration include any models other than partial_sphere?
- How does size_variation affect the ground patch generation parameters?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mushroom__defaults.zig.zon_chunk_0*
