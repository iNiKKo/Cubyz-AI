# [easy/codebase_src_proceduralItem_modifiers_weak.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, clamp, hypot, property management, tooltip printing
**Symbols:** ProceduralItem, Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** data manipulation, procedural items, modifiers, weakness, damage reduction

## Summary
Data manipulation and procedural item modifiers

## Explanation
This chunk defines data structures and functions for weak procedural item modifiers. It includes a packed struct `Data` with fields for strength (a floating-point value representing the reduction factor) and an unused padding field (`pad`). The priority level is set to 1.

The `loadData` function loads the strength value from a ZonElement, clamping it between 0 and 1. The `combineModifiers` function combines two modifier strengths using a specific formula: 

```zig
pub fn combineModifiers(data1: Data, data2: Data) ?Data {
    return .{.strength = 1.0 - 1.0/(1.0 + std.math.hypot(1.0/(1.0 - data1.strength) - 1.0, 1.0/(1.0 - data2.strength) - 1.0))};
}
```
The `changeProceduralItemParameters` function reduces the damage of a procedural item by multiplying its current damage value with `(1 - data.strength)`. The `printTooltip` function prints a tooltip that displays the percentage reduction in damage.

The priority level for these modifiers is set to 1.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = std.math.clamp(zon.get(f32, "strength") orelse 0, 0, 1)}; }
```

## Related Questions
- What is the purpose of the `Data` struct?
- How does the `loadData` function work?
- What is the `combineModifiers` function used for?
- Where is the `changeProceduralItemParameters` function located?
- How is the tooltip printed using the `printTooltip` function?
- What is the priority level of these modifiers?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_weak.zig_chunk_0*
