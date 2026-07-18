# [easy/codebase_assets_cubyz_sbb_deco_side.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprint, chance, decoration, side placement, probability distribution
**Concepts:** world_generation, decoration

## Summary
Defines a list of decoration blueprints with associated chances for side placement in the Cubyz voxel engine.

## Explanation
This chunk contains a configuration structure defining various decoration blueprints that can be placed on the sides of voxels within the Cubyz world. Each blueprint has an ID and a chance value, which determines the probability of it being selected during the decoration generation process. The specific blueprints defined are as follows:

- `cubyz:deco/ivy_side_2` with a chance of 0.1
- `cubyz:deco/ivy_side_3` with a chance of 0.05
- `cubyz:deco/bolete_side` with a chance of 0.025
- A null entry with a chance of 0.825

The sum of all chances equals 1, ensuring a valid probability distribution.

## Related Questions
- What is the total probability of selecting a decoration blueprint in this configuration?
- Which blueprint has the highest chance of being selected?
- How many different blueprints are defined in this configuration?
- What is the purpose of the 'null' entry in the blueprints list?
- Can you provide the ID and chance for each decoration blueprint defined here?
- How does the sum of all chances ensure a valid probability distribution?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_deco_side.zig.zon_chunk_0*
