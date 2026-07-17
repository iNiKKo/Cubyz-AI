# [easy/codebase_assets_cubyz_biomes_cave_mushroom_big_glimmergill.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, structures, placeMode, id, blocks, width, variation, density, priority, generationMode, height
**Symbols:** .chance, .structures
**Concepts:** biome configuration, structure spawning, vegetation placement rules, degradable structures, ceiling generation mode

## Summary
Configuration data defining spawn chances and placement rules for mushroom structures (big/small glimmergill) and vegetation blocks within the cave biome.

## Explanation
This chunk is a .zon configuration file containing static data with no executable logic. It defines a top-level object exposing a chance field set to 0.02, followed by an array of structure definitions under the structures key. Each structure entry includes an id (cubyz:sbb for mushroom variants), a structure path string pointing to specific glimmergill models (big/small), and a placeMode enum value of degradable indicating how these structures interact with terrain. Additional entries define simple_vegetation blocks using cubyz:vine/glimmer_worms with ceiling generation mode, varying chance values (0.4 and 0.2) and height parameters (9/7 variation and 15/8 variation). One entry defines a flower_patch structure composed of cubyz:glimmergill blocks with explicit width, variation, density, and priority fields set to numeric constants.

## Related Questions
- What is the default chance value defined at the top level of this biome configuration?
- Which structure IDs are associated with the mushroom glimmergill variants in this file?
- How does the placeMode field affect the behavior of structures defined here?
- What generation mode is specified for the vine blocks in this configuration?
- Are any of the defined structures marked as non-degradable or permanent?
- Which block type is used to compose the flower_patch structure definition?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mushroom_big_glimmergill.zig.zon_chunk_0*
