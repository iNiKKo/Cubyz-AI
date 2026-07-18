# [hard/codebase_src_items.zig] - Chunk 4

**Type:** implementation
**Keywords:** property calculation, durability, speed, crafting grid, material modifiers, floodfill algorithm, slot info, property matrix, method enumeration
**Symbols:** ProceduralItemPhysics, ProceduralItemPhysics.evaluateProceduralItem, ProceduralItemPhysics.checkConnectivity, SlotInfo, SlotInfo.disabled, SlotInfo.optional, PropertyMatrix, PropertyMatrix.source, PropertyMatrix.destination, PropertyMatrix.weights, PropertyMatrix.resultScale, PropertyMatrix.method, PropertyMatrix.Method, PropertyMatrix.Method.average, PropertyMatrix.Method.sum, PropertyMatrix.Method.fromString
**Concepts:** procedural item physics, property evaluation, material properties, modifiers, connectivity check

## Summary
The chunk defines the logic for evaluating procedural item physics and properties.

## Explanation
This chunk contains the `ProceduralItemPhysics` struct, which includes a method to evaluate the physical properties of procedural items. The `evaluateProceduralItem` function calculates durability, speed, and other parameters based on the crafting grid and material properties. It also handles modifiers and checks for connectivity within the item's material grid. Additionally, it defines `SlotInfo` and `PropertyMatrix` structs with their respective fields and methods.

## Code Example
```zig
fn lessThan(_: void, lhs: Modifier, rhs: Modifier) bool {
				return lhs.vTable.priority < rhs.vTable.priority;
			}
```

## Related Questions
- What is the purpose of the `evaluateProceduralItem` function?
- How does the `checkConnectivity` function work?
- What are the fields in the `SlotInfo` struct?
- How are methods defined in the `PropertyMatrix.Method` enum?
- What does the `fromString` method in `PropertyMatrix.Method` do?
- How is the durability of a procedural item calculated?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_4*
