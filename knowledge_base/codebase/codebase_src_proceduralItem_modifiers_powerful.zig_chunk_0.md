# [easy/codebase_src_proceduralItem_modifiers_powerful.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, hypot, property setter, getter or else, f32, u96, modifier combination, damage multiplier, tooltip formatting, priority value
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** item modifiers, damage scaling, packed struct, ZON file loading, tooltip rendering

## Summary
Defines a packed u128 data structure for powerful item modifiers and provides functions to load strength from ZON files, combine multiple modifiers via hypot, apply damage scaling to ProceduralItem instances, and render a tooltip.

## Explanation
The chunk declares a public packed struct Data with fields strength (f32) and pad (u96), sets priority 1, exports loadData which reads an optional f32 from zon.get("strength") defaulting to 0, combines two Data values by computing the hypotenuse of their strengths, applies damage scaling via changeProceduralItemParameters which multiplies existing damage property by (1 + data.strength) and sets it, and printsTooltip which formats a tooltip string with the strength percentage.

## Code Example
```zig
pub fn printTooltip(outString: *main.ListManaged(u8), data: Data) void {
	outString.print("#f84a00**Powerful**#808080 *Increases damage by **{d:.0}%", .{data.strength*100});
}
```

## Related Questions
- What is the default value of the pad field in Data?
- How does loadData handle a missing strength key in the ZON file?
- Why is Data declared as packed and what are its fields?
- What happens if combineModifiers receives two Data values with zero strength?
- Does changeProceduralItemParameters modify any other properties besides damage?
- What format string is used inside printTooltip and how does it reference data.strength?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_powerful.zig_chunk_0*
