# [easy/codebase_src_proceduralItem_modifiers_durable.zig] - Chunk 0

**Type:** implementation
**Keywords:** data struct, modifier func, durability inc, tooltip print, property set
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, durable item, data structure, functionality

## Summary
Data structure and modifiers for durable procedural items

## Explanation
This chunk defines a data structure `Data` with fields `strength` and `pad`. It also provides functions to load, combine, change parameters of procedural items, and print tooltips related to durability.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data {
	return .{.strength = @max(0, zon.get(f32, "strength") orelse 0)};
}
```

## Related Questions
- What is the priority level for this data structure?
- How does loadData function to load durability data from a ZonElement?
- What is the purpose of the combineModifiers function?
- In what way does changeProceduralItemParameters modify procedural item properties?
- How is the tooltip printed using printTooltip function?
- What is the maximum length of the strength field in the Data structure?
- Which data fields are used by loadData to load durability data?
- What is the purpose of the pad field in the Data structure?
- In what format is the strength value stored in the Data structure?
- How does the combineModifiers function calculate the combined strength?
- What is the maximum possible value for the strength field in the Data structure?
- Which data fields are used by changeProceduralItemParameters to modify procedural item properties?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_durable.zig_chunk_0*
