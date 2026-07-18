# [easy/codebase_src_proceduralItem_modifiers_heavy.zig] - Chunk 0

**Type:** implementation
**Keywords:** data loading, modifier combination, property change, tooltip printing, heavy item
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifier, strength modification, swing speed reduction

## Summary
Heavy procedural item modifier

## Explanation
This chunk defines a heavy procedural item modifier that modifies the strength of a procedural item. It includes functions to load data, combine modifiers, change procedural item parameters, and print a tooltip.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = @max(0, zon.get(f32, "strength") orelse 0)}; }
```

## Related Questions
- What is the priority of this heavy procedural item modifier?
- How does the loadData function load data from a ZonElement?
- What is the purpose of the combineModifiers function?
- How does the changeProceduralItemParameters function modify a procedural item's swing speed?
- What information does the printTooltip function display about the heavy procedural item modifier?
- Which functions are exported by this chunk?
- What data structure is used to store the Data struct?
- What is the purpose of the strength field in the Data struct?
- How is the maximum value of strength determined in the loadData function?
- What mathematical operation is performed in the combineModifiers function?
- What is the formula for calculating the swing speed reduction?
- Which functions are called by the printTooltip function?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_heavy.zig_chunk_0*
