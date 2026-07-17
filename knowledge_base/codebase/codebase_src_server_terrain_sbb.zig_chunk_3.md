# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 3

**Type:** api
**Keywords:** map, list, rotation, registration, reset
**Symbols:** registerChildBlock, registerBlueprints, getByStringId, list, reset
**Concepts:** structure building blocks, blueprints, registration, management

## Summary
Handles registration and management of structure building blocks (SBBs) and blueprints.

## Explanation
This chunk manages the lifecycle of structure building blocks and their associated blueprints. It includes functions to register child blocks, load blueprints with various rotations, retrieve SBBs by string ID, list all SBBs, and reset the internal state. The code uses a combination of maps and lists to store and manage these structures efficiently.

## Code Example
```zig
pub fn registerChildBlock(numericId: u16, stringId: []const u8) void {
	std.debug.assert(numericId != 0);

	const index: u16 = @intCast(childBlockNumericIdMap.count());
	childBlockNumericIdMap.put(main.worldArena.allocator, numericId, @enumFromInt(index)) catch unreachable;
	// Take only color name from the ID.
	var iterator = std.mem.splitBackwardsScalar(u8, stringId, '/');
	const colorName = iterator.first();
	const colorNameDupe = main.worldArena.dupe(u8, colorName);
	childBlockName.append(main.worldArena, colorNameDupe);

	childBlockNameToLocalIndex.put(main.worldArena.allocator, colorNameDupe, @enumFromInt(index)) catch unreachable;
}
```

## Related Questions
- How does the `registerChildBlock` function work?
- What is the purpose of the `registerBlueprints` function?
- How are blueprints rotated in this code?
- What does the `getByStringId` function return?
- How many different rotations of a blueprint are created?
- What happens if a blueprint cannot be loaded during registration?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_3*
