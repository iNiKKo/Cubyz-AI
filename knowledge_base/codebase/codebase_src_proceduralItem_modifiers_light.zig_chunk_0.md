# [easy/codebase_src_proceduralItem_modifiers_light.zig] - Chunk 0

**Type:** implementation
**Keywords:** data struct, clamp function, hypot function, property modification, tooltip printing
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifiers, light enhancement, swing speed

## Summary
ProceduralItem modifiers for light

## Explanation
This chunk defines procedural item modifiers for enhancing light properties. It includes a packed struct `Data` with a `strength` field that is clamped between 0 and 1 when loading data from `zon`. The clamp function used is `std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1)`, which ensures the strength value is within the specified range. This value affects the swing speed property of procedural items by increasing it based on the formula `proceduralItem.getProperty(.swingSpeed)*(1 + data.strength)`. The tooltip printed by `printTooltip` displays the percentage increase in swing speed as `#9fffde**Light**#808080 *Increases swing speed by **{d:.0}%`, where `{d:.0}` is replaced with `data.strength*100`. Additionally, two `Data` structs are combined using the hypotenuse function `std.math.hypot(data1.strength, data2.strength)`, which calculates the Euclidean norm of the two strength values. The priority of this chunk is set to 1.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data {
	return .{.strength = std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1)};
}
```

## Related Questions
- What is the exact formula used in the `loadData` function to clamp the strength value?
- How does the `hypot` function combine two `Data` structs?
- What is the specific effect on swing speed when applying a `Data` struct with a given strength value?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_light.zig_chunk_0*
