# [easy/codebase_src_proceduralItem_modifiers_powerful.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, hypotenuse formula, property manipulation, tooltip generation, non-negative value
**Symbols:** Data, Data.strength, Data.pad, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, damage increase, strength calculation

## Summary
This chunk defines a powerful modifier for procedural items, affecting their strength and damage.

## Explanation
This chunk defines a powerful modifier for procedural items, affecting their strength and damage. The `Data` struct contains a packed field `strength` of type `f32` and a padding field `pad`. It sets the priority level to 1. The `loadData` function retrieves the strength from a ZonElement, ensuring it's non-negative by using `@max(0, zon.get(f32, "strength") orelse 0)`. The `combineModifiers` function combines two Data instances using the hypotenuse formula to calculate combined strength with `std.math.hypot(data1.strength, data2.strength)`. The `changeProceduralItemParameters` method adjusts the damage of a procedural item based on its strength by multiplying the current damage property by `(1 + data.strength)`. The `printTooltip` function formats a tooltip string indicating an increase in damage by `{d:.0}%`, where the percentage is calculated as `data.strength * 100`.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data {
	return .{.strength = @max(0, zon.get(f32, "strength") orelse 0)};
}
```

## Related Questions
- What is the priority level of this modifier?
- How does the `loadData` function ensure non-negative strength values?
- Which mathematical operation is used to combine two strengths in `combineModifiers`?
- What property of a procedural item is adjusted by `changeProceduralItemParameters`?
- How is the tooltip string formatted in `printTooltip`?
- What is the purpose of the padding field in the `Data` struct?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_powerful.zig_chunk_0*
