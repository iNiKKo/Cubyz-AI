# [issues/issue_2761.md] - Issue #2761 discussion

**Type:** review
**Keywords:** loot table, chest, SBB, structure generation, randomization, item stacking, mathematical functions, tool construction, biome definition, SbbGen generator
**Symbols:** loot table, chest, SBB, .zig.zon, cubyz:dungeon_loot_1, cubyz:diamond, cubyz:gold_ingot, k, x, tool, materials, biome definition, SbbGen generator
**Concepts:** randomization, asset management, game design

## Summary
Discussion on adding loot tables to chests in dungeon structures.

## Explanation
The discussion revolves around the implementation of loot tables for chests within dungeon structures. Users propose creating a new block specifically for use in Structure Blueprint Blocks (SBBs) that can reference loot tables, allowing for more stylized and varied chest placements. The maintainer suggests that loot tables should be separate assets referenced in biome definitions, which would be accepted by the SbbGen generator. This approach allows chests to share the same loot table, enabling easy creation of tiered treasure chests. Users also discuss potential methods for randomizing item stacking sizes using mathematical functions like Gaussian or inverse exponential distributions.

## Related Questions
- How does the proposed loot table system integrate with existing SBBs?
- What are the potential performance implications of using separate asset files for loot tables?
- Can you explain how the Gaussian or inverse exponential functions would be used to randomize item stacking sizes?
- How would the new chest block differ from existing blocks in terms of functionality and placement?
- What considerations should be made for ensuring compatibility with different biomes when defining loot tables?
- How might the proposed system handle cases where multiple chests within a structure share the same loot table?

*Source: unknown | chunk_id: github_issue_2761_discussion*
