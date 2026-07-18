# [easy/codebase_src_proceduralItem_modifiers_bad_at.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, packed struct, clamp, hypot, list managed string, tag name
**Symbols:** Data, priority, loadData, combineModifiers, changeBlockDamage, printTooltip
**Concepts:** data structure, procedural items, modifiers, block damage, tooltip

## Summary
Data structure and modifiers for procedural items in Cubyz

## Explanation
This chunk defines a `Data` struct for storing procedural item properties including strength (a floating-point value between 0 and 1) and tag. It includes functions to load data from a ZonElement by clamping the strength within [0, 1] range and setting the tag based on provided values or defaulting to 'incorrect'. The `combineModifiers` function calculates combined strength for items with matching tags using a specific formula involving hyperbolic tangent (hypot). The `changeBlockDamage` function reduces damage by multiplying it with `(1 - data.strength)` if the block's tag matches the item's tag. The `printTooltip` function formats and prints a tooltip string indicating the percentage of damage reduction and the affected block type.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1), .tag = .find(zon.get([]const u8, "tag") orelse "incorrect")}; }
```

## Related Questions
- What is the purpose of the `Data` struct in this chunk?
- How does the `loadData` function handle missing or invalid values for strength and tag?
- What is the logic behind combining modifiers based on tags?
- How does the `changeBlockDamage` function calculate damage reduction based on the item's tag?
- What is the format of the tooltip printed by the `printTooltip` function?
- What are the possible values for the `tag` field in this chunk?
- How is the strength value clamped within the range [0, 1]?
- What is the purpose of the `pad` field in the `Data` struct?
- How does the `find` function work with tags?
- What is the format of the tooltip string printed by the `printTooltip` function?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_bad_at.zig_chunk_0*
