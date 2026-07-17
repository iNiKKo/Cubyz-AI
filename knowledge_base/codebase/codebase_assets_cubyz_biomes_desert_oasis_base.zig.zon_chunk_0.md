# [easy/codebase_assets_cubyz_biomes_desert_oasis_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome configuration, structure placement rules, vegetation tags, height limits, radius constraints, degradable structures, flower patches, simple trees, ground patches
**Symbols:** tags, minHeightLimit, minHeight, maxHeight, maxHeightLimit, minRadius, maxRadius, hills, maxSubBiomeCount, structures, parentBiomes
**Concepts:** biome configuration, structure placement rules, vegetation tags, height limits, radius constraints, degradable structures, flower patches, simple trees, ground patches

## Summary
Defines configuration data for a desert oasis biome including height limits, vegetation tags, and structure placement rules.

## Explanation
This chunk contains only static configuration data with no executable logic. It defines the .tags field listing palm, baobab, and cactus identifiers; sets minHeightLimit to 1, minHeight to 5, maxHeight to 10, maxHeightLimit to 10; configures minRadius at 60 and maxRadius at 80; specifies hills count as 5; limits maxSubBiomeCount to 1. The .structures field enumerates multiple structure definitions: a cactus/saguaro with id cubyz:sbb in degradable mode at 0.007 chance, a coconut palm tree also id cubyz:sbb degradable at 0.04 chance, a dry grass ground patch with id cubyz:ground_patch using block cubyz:grass/dry at 0.2 chance width 7 variation 4 depth 1 smoothness 0.4, a young cactus structure id cubyz:sbb degradable at 0.015 chance, three flower patches each id cubyz:flower_patch with varying blocks (tussock, grass/vegetation/dry, castilleja) and associated chance width variation density priority values, two simple tree definitions both id cubyz:simple_tree with leaves log top attributes type height height_variation leafRadius branched or leafRadius_variation fields set to specific block identifiers or numeric values. The .parentBiomes field contains a single entry linking this biome to cubyz:desert/base with chance 1.

## Related Questions
- What vegetation tags are defined for this desert oasis biome?
- What is the minimum height limit configured for structures in this biome?
- Which structure definitions include a degradable placement mode?
- How many hills are specified for terrain generation in this biome?
- What blocks are used for the ground patch structure definition?
- Which simple tree definition uses cubyz:leaves/baobab as its leaves block?
- What is the chance value assigned to the coconut palm tree structure?
- How many flower patches are defined in this biome configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_desert_oasis_base.zig.zon_chunk_0*
