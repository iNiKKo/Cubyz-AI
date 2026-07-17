# [easy/codebase_src_proceduralItem_modifiers_fragile.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, data loading, modifier combination, parameter change, tooltip formatting
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, durability adjustment, tooltip generation

## Summary
Defines the Fragile modifier for procedural items, affecting their durability and providing a tooltip.

## Explanation
This chunk defines the Fragile modifier for procedural items. It includes a packed struct `Data` to store the strength of the modifier. The `loadData` function reads the strength from a ZonElement, clamping it between 0 and 1. The `combineModifiers` function combines two Data instances using a specific formula involving hyperbolic functions. The `changeProceduralItemParameters` function adjusts the item's maximum durability based on the modifier's strength. The `printTooltip` function generates a tooltip string describing the effect of the Fragile modifier.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data {
	return .{.strength = std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1)};
}
```

## Related Questions
- What is the purpose of the Fragile modifier?
- How does the `loadData` function read the strength value?
- What formula is used in `combineModifiers` to combine two Data instances?
- How does `changeProceduralItemParameters` affect the item's durability?
- What information does the `printTooltip` function include in the tooltip?
- What is the range of values for the strength field in the Data struct?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_fragile.zig_chunk_0*
