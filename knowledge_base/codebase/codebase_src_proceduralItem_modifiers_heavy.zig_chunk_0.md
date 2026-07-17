# [easy/codebase_src_proceduralItem_modifiers_heavy.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, max function, hypot function, property getters/setters, list managed strings
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, heavy, data structures, priority, loading, combining, changing parameters, printing tooltips

## Summary
Handles heavy procedural item modifiers

## Explanation
This chunk defines data structures, priority, loading and combining modifiers, changing procedural item parameters, and printing tooltips for heavy procedural items. It uses packed structs, max function, hypot function from std.math, property getters/setters, and list managed strings.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = @max(0, zon.get(f32, "strength") orelse 0)}; }
```

## Related Questions
- What is the priority of heavy procedural item modifiers?
- How does loadData function in the context of heavy procedural items?
- What data structure is used for storing heavy procedural item modifier data?
- What is the purpose of the combineModifiers function?
- How does changeProceduralItemParameters modify a procedural item based on heavy modifiers?
- What is the format for printing tooltips for heavy procedural items?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_heavy.zig_chunk_0*
