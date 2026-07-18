# [easy/codebase_src_proceduralItem_modifiers_good_at.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, function, modifier, tooltip, block damage
**Symbols:** Data, priority, loadData, combineModifiers, changeBlockDamage, printTooltip
**Concepts:** data structure, modifiers, procedural items

## Summary
Data structure and modifiers for procedural items

## Explanation
This chunk defines a `Data` struct with fields for strength and tag. It provides functions to load data from a ZonElement, combine modifiers based on tags, change block damage based on the item's tag, and print a tooltip.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = @max(0, zon.get(f32, "strength") orelse 0), .tag = .find(zon.get([]const u8, "tag") orelse "incorrect")}; }
```

## Related Questions
- What is the purpose of the `Data` struct?
- How does the `loadData` function work?
- What is the `combineModifiers` function used for?
- How does the `changeBlockDamage` function modify block damage based on item tags?
- What information does the `printTooltip` function display?
- What are the fields of the `Data` struct?
- Which functions use the `Data` struct?
- What is the priority of this chunk?
- How is the strength value calculated in the `loadData` function?
- What happens if the tag is not found in the ZonElement?
- What is the purpose of the `find` function used in the `loadData` function?
- How does the `combineModifiers` function handle different tags?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_good_at.zig_chunk_0*
