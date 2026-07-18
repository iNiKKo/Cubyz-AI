# [easy/codebase_src_proceduralItem_modifiers_powerful.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, hypotenuse formula, property manipulation, tooltip generation, non-negative value
**Symbols:** Data, Data.strength, Data.pad, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, damage increase, strength calculation

## Summary
This chunk defines a powerful modifier for procedural items, affecting their strength and damage.

## Explanation
The chunk declares a `Data` struct with a packed field `strength` of type `f32` and a padding field `pad`. It sets a priority level. The `loadData` function retrieves the strength from a ZonElement, ensuring it's non-negative. The `combineModifiers` function combines two Data instances using the hypotenuse formula to calculate combined strength. The `changeProceduralItemParameters` method adjusts the damage of a procedural item based on its strength. The `printTooltip` function formats a tooltip string indicating the increase in damage.

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
