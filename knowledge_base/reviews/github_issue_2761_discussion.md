# [issues/issue_2761.md] - Issue #2761 discussion

**Type:** review
**Keywords:** loot table, chest, SBB, structure generation, randomization, item stacking, mathematical functions, tool construction, biome definition, SbbGen generator
**Symbols:** loot table, chest, SBB, .zig.zon, cubyz:dungeon_loot_1, cubyz:diamond, cubyz:gold_ingot, k, x, tool, materials, biome definition, SbbGen generator
**Concepts:** randomization, asset management, game design

## Summary
Discussion on adding loot tables to chests in dungeon structures.

## Explanation
The discussion revolves around adding loot tables to chests within dungeon structures. Users propose creating a new block specifically for use in Structure Blueprint Blocks (SBBs) that can reference loot tables, allowing for more stylized and varied chest placements. The maintainer suggests that loot tables should be separate assets referenced in biome definitions, which would be accepted by the SbbGen generator. This approach allows chests to share the same loot table, enabling easy creation of tiered treasure chests. Users also discuss potential methods for randomizing item stacking sizes using mathematical functions like Gaussian or inverse exponential distributions.

The proposed loot table format is as follows:
```.{
   .id = "cubyz:dungeon_loot_1",
   
   .items = .{
     .{.id = "cubyz:diamond", .amount = "1 to 2", .stacked = false},
     .{.id = "cubyz:gold_ingot", .amount = "1 to 4", .stacked = true},
  },
}
```

For stacking, users suggest using a mathematical function like `1+(k-1)(1-sqrt(1-x^2))`, where `k` is the max stack size and `x` is a random value from 0 to 1. The maintainer also mentions that it would be good to define randomized tools, so tool is constructed on the fly out of predefined materials instead of being always the same or requiring a lot of separate definitions.

The maintainer notes that placing the chest in the blueprint and using an adjacent SBB block won't work for buried chests, emphasizing the need for loot tables as separate assets referenced in biome definitions.

## Related Questions
- How does the proposed loot table system integrate with existing SBBs?
- What are the potential performance implications of using separate asset files for loot tables?
- Can you explain how the Gaussian or inverse exponential functions would be used to randomize item stacking sizes?
- How would the new chest block differ from existing blocks in terms of functionality and placement?
- What considerations should be made for ensuring compatibility with different biomes when defining loot tables?
- How might the proposed system handle cases where multiple chests within a structure share the same loot table?

*Source: unknown | chunk_id: github_issue_2761_discussion*
