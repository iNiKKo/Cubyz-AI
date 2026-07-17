# [easy/codebase_src_proceduralItem_modifiers_light.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, hypot, clamp, swingSpeed, setProperty, getProperty, ListManaged, print, f32, u96
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** packed struct layout, property modification, swing speed scaling, tooltip rendering, mathematical combination of modifiers

## Summary
Defines a packed Data struct and four public functions that load strength from a ZonElement, combine strengths via hypot, apply the combined strength to ProceduralItem.swingSpeed, and render a tooltip string.

## Explanation
The chunk declares pub const Data as a packed u128 struct with fields strength: f32 and pad: u96 = undefined. It exposes pub const priority = 1. loadData(zon: main.ZonElement) returns a Data where strength is std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1). combineModifiers(data1: Data, data2: Data) returns ?Data with strength computed as std.math.hypot(data1.strength, data2.strength). changeProceduralItemParameters(proceduralItem: *main.items.ProceduralItem, data: Data) multiplies the existing swingSpeed property by (1 + data.strength) via setProperty and getProperty. printTooltip(outString: *main.ListManaged(u8), data: Data) writes a formatted string into outString using outString.print with the literal "#9fffde**Light**#808080" prefix, the description "Increases swing speed by **{d:.0}%", and d bound to data.strength*100.

## Code Example
```zig
pub fn printTooltip(outString: *main.ListManaged(u8), data: Data) void {
	outString.print("#9fffde**Light**#808080 *Increases swing speed by **{d:.0}%", .{data.strength*100});
}
```

## Related Questions
- What is the exact packed layout of Data and why is pad set to undefined?
- How does loadData handle a missing strength value from zon.get?
- Why use std.math.hypot instead of simple addition for combineModifiers?
- Does changeProceduralItemParameters mutate swingSpeed in place or via a setter?
- What type does printTooltip expect for outString and why ListManaged(u8)?
- How is the tooltip string formatted and what escape sequences are used?
- Is priority exported as pub const and how would another module import it?
- Could loadData be called with a non-ZonElement argument without compile error?
- What happens if data.strength exceeds 1 after clamp in loadData?
- Does combineModifiers return an optional or a guaranteed Data value?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_light.zig_chunk_0*
