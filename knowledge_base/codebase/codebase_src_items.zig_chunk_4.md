# [hard/codebase_src_items.zig] - Chunk 4

**Type:** implementation
**Keywords:** property calculation, durability, speed, crafting grid, material modifiers, floodfill algorithm, slot info, property matrix, method enumeration
**Symbols:** ProceduralItemPhysics, ProceduralItemPhysics.evaluateProceduralItem, ProceduralItemPhysics.checkConnectivity, SlotInfo, SlotInfo.disabled, SlotInfo.optional, PropertyMatrix, PropertyMatrix.source, PropertyMatrix.destination, PropertyMatrix.weights, PropertyMatrix.resultScale, PropertyMatrix.method, PropertyMatrix.Method, PropertyMatrix.Method.average, PropertyMatrix.Method.sum, PropertyMatrix.Method.fromString
**Concepts:** procedural item physics, property evaluation, material properties, modifiers, connectivity check

## Summary
The chunk defines the logic for evaluating procedural item physics and properties.

## Explanation
This chunk contains the `ProceduralItemPhysics` struct which includes a method to evaluate the physical properties of procedural items. The `evaluateProceduralItem` function calculates durability, speed, and other parameters based on the crafting grid and material properties using specific weights and result scales defined in `PropertyMatrix`. For each property, it sums or averages values from materials in the crafting grid according to specified weights and applies a scaling factor. Durability is set to at least 1 if less than 1 after calculation. The function also handles modifiers by applying them based on restrictions and priorities. Connectivity within the item's material grid is checked using a floodfill algorithm, ensuring all cells are reachable from each other or setting durability to 0 otherwise.

The `PropertyMatrix` struct defines properties such as source, destination, weights, result scale, and method for calculating property values. The `weights` array contains 25 floating-point numbers representing the weight of each cell in the crafting grid. The `resultScale` is a scaling factor applied to the calculated sum or average value. The `method` can be either 'average' or 'sum', determining whether the final value is an average or a sum of weighted material properties.

The connectivity check uses a floodfill algorithm implemented in the `checkConnectivity` function, which initializes a grid to track visited cells and iterates through the item's material grid. It starts from any non-null cell and performs a breadth-first search (BFS) to mark all reachable cells as connected. If any non-null cell is unreachable, durability is set to 0; otherwise, it remains intact.

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
