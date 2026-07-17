# [medium/codebase_assets_cubyz_biomes_autumn_forest.zig.zon] - Chunk 1

**Type:** configuration
**Keywords:** chance probability, block type identifier, priority ordering, variation count, density factor, spawn chance, width dimension, biome data structure
**Concepts:** biome configuration, flower patch generation

## Summary
Defines a collection of autumn forest flower patch biome configurations with varying block types, spawn chances, and priority levels.

## Explanation
This chunk contains only static configuration data for multiple flower_patch entries. Each entry specifies an id (cubyz:flower_patch), a blocks field containing a single block type identifier (e.g., cubyz:red_leaf_pile:1), a chance probability, width dimension, variation count, density factor, and priority ordering value. The data is structured as an array of anonymous objects with identical schema repeated for different block variants including red leaf piles 0-3 and yellow leaf piles 0-3.

## Related Questions
- What block types are available for flower patches in the autumn forest biome?
- How does the chance field affect flower patch generation probability?
- What is the relationship between width and variation parameters in this configuration?
- Are there any priority ordering rules applied to these flower patch entries?
- Which leaf pile variants (red vs yellow) are defined in this chunk?
- Does this chunk contain executable logic or only static data definitions?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_autumn_forest.zig.zon_chunk_1*
