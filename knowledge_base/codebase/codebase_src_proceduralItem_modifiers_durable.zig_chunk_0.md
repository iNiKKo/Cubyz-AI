# [easy/codebase_src_proceduralItem_modifiers_durable.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, hypotenuse formula, property modification, tooltip formatting, ZonElement parsing
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, durability increase, data loading, modifier combination, tooltip generation

## Summary
Defines a modifier for procedural items that increases their durability.

## Explanation
This chunk defines a modifier for procedural items that affects their durability, with `priority = 1`. It includes a packed struct `Data` (`packed struct(u128) { strength: f32, pad: u96 = undefined }`) to store the strength of the modifier, a function `loadData` to load data from a ZonElement, a function `combineModifiers` to combine two modifiers' strengths using the hypotenuse formula (`std.math.hypot`), a function `changeProceduralItemParameters` that multiplies the item's `maxDurability` by `(1 + strength)`, and a function `printTooltip` to generate a tooltip string describing the modifier's effect as a percentage increase.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data {
	return .{.strength = @max(0, zon.get(f32, "strength") orelse 0)};
}
```

## Related Questions
- What is the purpose of the `Data` struct in this chunk?
- How does the `loadData` function handle missing strength values?
- Which mathematical operation is used to combine two modifier strengths?
- What effect does the `changeProceduralItemParameters` function have on a procedural item?
- How is the tooltip string formatted in the `printTooltip` function?
- What is the value of the `priority` constant in this chunk?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_durable.zig_chunk_0*
