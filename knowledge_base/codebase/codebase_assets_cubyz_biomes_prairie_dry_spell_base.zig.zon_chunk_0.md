# [easy/codebase_assets_cubyz_biomes_prairie_dry_spell_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** terrain retention, parent biomes, structures, configuration, probability, dimensions
**Concepts:** world generation, biome configuration

## Summary
Defines configuration for the dry spell prairie biome with a terrain retention probability of 0.5, inheriting from 'cubyz:prairie/base' with a chance of 3. It includes configurations for ground patches, boulders, flower patches, simple trees, and fallen trees, detailing their block types, occurrence probabilities, dimensions, variations, and other properties.

## Explanation
This chunk is a configuration file in the Cubyz voxel engine that specifies settings for the 'dry spell prairie' biome. It includes parameters such as terrain retention probability (0.5), parent biomes ('cubyz:prairie/base' with a chance of 3), and maximum sub-biome count (1). Detailed configurations are provided for various structures like ground patches, boulders, flower patches, simple trees, and fallen trees. Each structure entry defines its ID, block types, occurrence probability, dimensions, variations, and other specific properties as follows:

- **Ground Patch:**
  - ID: 'cubyz:ground_patch'
  - Block: 'cubyz:grass/dry'
  - Chance: 0.05
  - Width: 15
  - Variation: 7
  - Depth: 1
  - Smoothness: 0.5
- **Boulder:**
  - ID: 'cubyz:boulder'
  - Block: 'cubyz:leaves/dead'
  - Chance: 0.05
  - Size: 3
  - Size Variance: 3
- **Flower Patch (Dead Leaf Pile):**
  - ID: 'cubyz:flower_patch'
  - Blocks: ['cubyz:dead_leaf_pile:1', 'cubyz:dead_leaf_pile:0']
  - Chance: 0.05 for 'cubyz:dead_leaf_pile:1' and 0.06 for 'cubyz:dead_leaf_pile:0'
  - Width: 4
  - Variation: 3
  - Density: 0.6 for both patches, with priority of 0.2 for 'cubyz:dead_leaf_pile:1' and 0.1 for 'cubyz:grass/vegetation/dry'
- **Simple Tree:**
  - ID: 'cubyz:simple_tree'
  - Leaves: 'cubyz:air'
  - Log: 'cubyz:log/oak'
  - Chance: 0.01
  - Type: Round
  - Height: 3
  - Height Variation: 3
- **Fallen Tree:**
  - ID: 'cubyz:fallen_tree'
  - Log: 'cubyz:log/oak'
  - Chance: 0.025
  - Height: 5
  - Height Variation: 1

## Related Questions
- What is the terrain retention probability for the dry spell prairie biome?
- Which parent biome does the dry spell prairie inherit from and with what chance?
- How many different structures are defined in the dry spell prairie biome configuration?
- What are the block types used in the ground patches of the dry spell prairie biome?
- What is the maximum number of sub-biomes allowed in the dry spell prairie biome?
- Which structure has the highest chance of occurrence in the dry spell prairie biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_prairie_dry_spell_base.zig.zon_chunk_0*
