# [src/blocks.zig] - Chunk 2117642766

**Type:** review
**Keywords:** tickFunctions, TickEventTableMap, tableMap, vTableMap, Block, generic, comptime, hash map, per-block callbacks, modularity, type safety, runtime overhead
**Symbols:** Block, TickEventTableMap, tableMap, vTableMap
**Concepts:** event-driven architecture, per-block callbacks, generic comptime helpers, hash map lookups, modularity, type safety, runtime overhead reduction

## Summary
Replaced a global tick function registry with a per-block event table map to support multiple tick handlers and better modularity.

## Explanation
The original code used a single `tickFunctions` named callback array, which limited extensibility and made it hard to attach different behaviors to individual block types. The new design introduces `TickEventTableMap`, a generic helper that creates a struct containing two string hash maps: one for parsing tick event names (`tableMap`) and another for v-table lookups (`vTableMap`). This shift moves from a monolithic global registry to a per-block, comptime-configurable table of callbacks. Reviewers likely wanted this change because it enables multiple handlers per block type without overwriting previous ones, improves type safety via the generic `Child` parameter, and aligns with Cubyz's event-driven architecture where each block can define its own tick behavior. The refactor also reduces runtime overhead by avoiding a single large array lookup in favor of hash map lookups keyed by string identifiers, which is more scalable as the number of block types grows.

## Related Questions
- What is the type of `tableMap` in `TickEventTableMap`?
- How does `TickEventTableMap` differ from the original `tickFunctions`?
- Which hash map is used for v-table lookups and why?
- Is `TickEventTableMap` generic over any block type, or only specific ones?
- What happens if a tick event name is not found in `tableMap`?
- Does the new design allow multiple handlers per block type simultaneously?
- Where are the string keys for `tableMap` and `vTableMap` parsed from?
- How does this change affect the initialization of blocks at runtime?
- What is the memory layout impact of replacing a fixed array with hash maps?
- Are there any comptime constraints on the `Child` type parameter?

*Source: unknown | chunk_id: github_pr_1476_comment_2117642766*
