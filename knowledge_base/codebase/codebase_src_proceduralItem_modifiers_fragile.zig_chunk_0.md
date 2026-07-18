# [easy/codebase_src_proceduralItem_modifiers_fragile.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, clamp function, hyperbolic functions, property modification, string formatting
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, durability effects, data loading, modifier combination, tooltip generation

## Summary
This chunk defines a modifier for procedural items that affects their durability, with functions to load data, combine modifiers, apply changes, and print tooltips.

## Explanation
The chunk declares a `Data` struct packed into a u128 integer, containing a float `strength` and padding. It provides a priority level of 1. The `loadData` function reads strength from a ZonElement, clamping it between 0 and 1. The `combineModifiers` function combines two Data instances using a specific formula involving hyperbolic functions to determine the resulting strength. The `changeProceduralItemParameters` method adjusts the maxDurability of a ProceduralItem based on the calculated strength. The `printTooltip` function appends a formatted tooltip string to an output list, indicating the durability decrease percentage.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data {
	return .{.strength = std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1)};
}
```

## Related Questions
- What is the priority level of this modifier?
- How does the `loadData` function read and process strength data?
- What formula is used in `combineModifiers` to combine two Data instances?
- How does `changeProceduralItemParameters` affect the ProceduralItem's maxDurability?
- What string is appended by the `printTooltip` function?
- What is the purpose of the padding field in the Data struct?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_fragile.zig_chunk_0*
