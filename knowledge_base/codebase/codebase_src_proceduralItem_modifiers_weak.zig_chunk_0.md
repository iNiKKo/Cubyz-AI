# [easy/codebase_src_proceduralItem_modifiers_weak.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, clamp, hypot, property management, tooltip printing
**Symbols:** ProceduralItem, Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** data manipulation, procedural items, modifiers, weakness, damage reduction

## Summary
Data manipulation and procedural item modifiers

## Explanation
This chunk defines data structures and functions for weak procedural item modifiers. It includes a packed struct `Data` with fields for strength, a priority level, methods to load data from a ZonElement, combine modifiers, change procedural item parameters, and print tooltips.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1)}; }
```

## Related Questions
- What is the purpose of the `Data` struct?
- How does the `loadData` function work?
- What is the `combineModifiers` function used for?
- Where is the `changeProceduralItemParameters` function located?
- How is the tooltip printed using the `printTooltip` function?
- What is the priority level of these modifiers?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_weak.zig_chunk_0*
