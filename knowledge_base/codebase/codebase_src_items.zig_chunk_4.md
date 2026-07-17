# [hard/codebase_src_items.zig] - Chunk 4

**Type:** implementation
**Keywords:** property setting, modifier combination, priority sorting, floodfill algorithm, binary serialization
**Symbols:** ProceduralItem, SlotInfo, PropertyMatrix, PropertyMatrix.Method, ProceduralItemTypeIndex, ProceduralItemTypeIterator, BinaryWriter, BinaryReader
**Concepts:** procedural item generation, property evaluation, material grid connectivity

## Summary
Handles procedural item generation and property evaluation.

## Explanation
This chunk contains logic for generating procedural items, evaluating their properties, and checking connectivity within the material grid. It includes functions to set properties based on crafting grid materials, combine modifiers, sort them by priority, and adjust durability. The `checkConnectivity` function uses a floodfill algorithm to ensure all connected components are reachable.

## Code Example
```zig
fn checkConnectivity(proceduralItem: *ProceduralItem) bool {
	var gridCellsReached: [16][16]bool = @splat(@splat(false));
	var floodfillQueue = main.utils.CircularBufferQueue(Vec2i).init(main.stackAllocator, 16);
	defer floodfillQueue.deinit();
	outer: for (proceduralItem.materialGrid, 0..) |row, x| {
		for (row, 0..) |entry, y| {
			if (entry != null) {
				floodfillQueue.pushBack(.{@intCast(x), @intCast(y)});
				gridCellsReached[x][y] = true;
				break :outer;
			}
		}
	}
	while (floodfillQueue.popFront()) |pos| {
		for ([4]Vec2i{.{-1, 0}, .{1, 0}, .{0, -1}, .{0, 1}}) |delta| {
			const newPos = pos + delta;
			if (newPos[0] < 0 or newPos[0] >= gridCellsReached.len) continue;
			if (newPos[1] < 0 or newPos[1] >= gridCellsReached.len) continue;
			const x: usize = @intCast(newPos[0]);
			const y: usize = @intCast(newPos[1]);
			if (gridCellsReached[x][y]) continue;
			if (proceduralItem.materialGrid[x][y] == null) continue;
			gridCellsReached[x][y] = true;
			floodfillQueue.pushBack(newPos);
		}
	}
	for (proceduralItem.materialGrid, 0..) |row, x| {
		for (row, 0..) |entry, y| {
			if (entry != null and !gridCellsReached[x][y]) {
				return false;
			}
		}
	}
	return true;
}
```

## Related Questions
- How does the procedural item generation handle property setting?
- What method is used to combine modifiers in the procedural item generation process?
- Can you explain how the floodfill algorithm works in the checkConnectivity function?
- What are the steps involved in evaluating the properties of a procedural item?
- How is durability adjusted during the procedural item generation?
- What data structure is used to store grid cell reachability status in the connectivity check?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_4*
