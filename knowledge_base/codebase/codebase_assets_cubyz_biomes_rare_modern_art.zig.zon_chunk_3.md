# [hard/codebase_assets_cubyz_biomes_rare_modern_art.zig.zon] - Chunk 3

**Type:** configuration
**Keywords:** tree configuration, leaf color, generation chance, height variation, leaf radius
**Concepts:** world_generation

## Summary
Defines configuration for various tree types with different leaf colors.

## Explanation
This chunk contains a series of configurations for different types of trees, each specified by its unique ID and properties such as leaf color, log type, generation chance, shape type, height, height variation, leaf radius, leaf radius variation, leaf elongation, and delta leaf elongation. All tree configurations have the same basic structure with varying leaf colors, indicating a consistent template for tree generation in the Cubyz engine.

- **Generation Chance:** Each tree type has a generation chance of 0.02.
- **Leaf Colors:** The defined leaf colors are pink, purple, red, violet, viridian, white, and yellow, totaling seven different colors.
- **Default Height:** The default height for all trees is 5 units.
- **Leaf Radius Variation Field:** The field that specifies the variation in leaf radius for the trees is `leafRadius_variation`, which is set to 1 unit.
- **Log Field:** For all tree types listed here, the 'log' field is set to 'cubyz:air', indicating no log block is used.
- **Leaf Elongation Property:** The 'leafElongation' property affects the appearance of the trees by elongating the leaves. It is set to 0.5 for all tree types, with a variation specified by `deltaLeafElongation` of 0.15.

## Related Questions
- What is the generation chance for each tree type?
- How many different leaf colors are defined for trees in this configuration?
- What is the default height of the trees specified in this chunk?
- Which field specifies the variation in leaf radius for the trees?
- What does the 'log' field indicate for all tree types listed here?
- How does the 'leafElongation' property affect the appearance of the trees?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_modern_art.zig.zon_chunk_3*
