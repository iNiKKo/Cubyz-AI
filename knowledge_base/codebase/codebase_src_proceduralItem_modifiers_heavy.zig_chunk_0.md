# [easy/codebase_src_proceduralItem_modifiers_heavy.zig] - Chunk 0

**Type:** implementation
**Keywords:** data loading, modifier combination, property change, tooltip printing, heavy item
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** procedural item modifier, strength modification, swing speed reduction

## Summary
Heavy procedural item modifier

## Explanation
This chunk defines a heavy procedural item modifier that modifies the strength of a procedural item. It includes functions to load data from a ZonElement, combine modifiers using a specific mathematical operation, change procedural item parameters based on the calculated swing speed reduction, and print a tooltip with detailed information about the modifier's effect.

The `Data` struct contains a `strength` field which is loaded from a `ZonElement`. The strength value is determined by taking the maximum of 0 and the value retrieved from the ZonElement. If no value is provided, it defaults to 0.

The `combineModifiers` function combines two modifier instances using the formula: 

```zig
1 - 1/(1 + std.math.hypot(1/(1 - data1.strength) - 1, 1/(1 - data2.strength) - 1))
```

The `changeProceduralItemParameters` function modifies the swing speed of a procedural item based on the strength value. The new swing speed is calculated as:

```zig
proceduralItem.getProperty(.swingSpeed)*(1 - data.strength)
```

The `printTooltip` function displays information about the heavy procedural item modifier, including the percentage reduction in swing speed.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = @max(0, zon.get(f32, "strength") orelse 0)}; }
```

## Related Questions
- What is the priority of this heavy procedural item modifier?
- How does the loadData function load data from a ZonElement?
- What is the purpose of the combineModifiers function?
- How does the changeProceduralItemParameters function modify a procedural item's swing speed?
- What information does the printTooltip function display about the heavy procedural item modifier?
- Which functions are exported by this chunk?
- What data structure is used to store the Data struct?
- What is the purpose of the strength field in the Data struct?
- How is the maximum value of strength determined in the loadData function?
- What mathematical operation is performed in the combineModifiers function?
- What is the formula for calculating the swing speed reduction?
- Which functions are called by the printTooltip function?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_heavy.zig_chunk_0*
