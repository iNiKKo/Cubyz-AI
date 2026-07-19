# [hard/codebase_assets_cubyz_biomes_rare_modern_art.zig.zon] - Chunk 1

**Type:** configuration
**Keywords:** ground patch, simple tree, chalk block, cloth leaf, terrain generation
**Concepts:** world generation, biome configuration

## Summary
Defines configurations for rare modern art biomes, including ground patches and simple trees with various colored chalk blocks and cloth leaves.

## Explanation
This chunk contains configuration data for rare modern art biomes in the Cubyz voxel engine. It defines multiple ground patch configurations with different colored chalk blocks (magenta, orange, pink, purple, red, violet, viridian, white, yellow) and various simple tree configurations with cloth leaves of different colors (aqua, black, blue, brown, crimson, cyan). Each configuration specifies the following attributes:

**Ground Patch Attributes:**
- **block**: The type of chalk block used.
- **chance**: The probability of the ground patch occurring (0.02 for all).
- **width**: The width of the ground patch (5 for all).
- **variation**: The variation in the ground patch's size (4 for all).
- **depth**: The depth of the ground patch (1 for all).
- **smoothness**: The smoothness of the ground patch (0.5 for all).

**Simple Tree Attributes:**
- **id**: The identifier for the tree configuration.
- **leaves**: The type of cloth leaf used.
- **log**: The type of log used (cubyz:air for all).
- **chance**: The probability of the simple tree occurring (0.02 for all).
- **type**: The type of tree (round for all).
- **height**: The base height of the tree (5 for all).
- **height_variation**: The variation in the tree's height (20 for all).
- **leafRadius**: The radius of the leaves at the top of the tree (3 for all).
- **leafRadius_variation**: The variation in the leaf radius (1 for all).
- **leafElongation**: The elongation factor of the leaves (0.5 for all).
- **deltaLeafElongation**: The change in leaf elongation (0.15 for all).

These configurations are used to generate the terrain and structures in the specified biomes.

## Related Questions
- What are the different colored chalk blocks defined for ground patches?
- How many simple tree configurations are specified in this chunk?
- What is the chance of each ground patch occurring?
- Which type of leaves does the simple trees have?
- What is the height variation for the simple trees?
- How is the smoothness of the ground patches defined?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_modern_art.zig.zon_chunk_1*
