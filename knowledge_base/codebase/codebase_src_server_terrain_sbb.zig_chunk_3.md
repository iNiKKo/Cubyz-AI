# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 3

**Type:** implementation
**Keywords:** registration, error handling, capacity allocation, data structures, blueprint rotation
**Symbols:** registerSBB, registerChildBlock, registerBlueprints, getByStringId, list, reset
**Concepts:** structure building blocks (SBBs), blueprints, world generation

## Summary
Handles registration and management of structure building blocks (SBBs) and blueprints in the Cubyz server.

## Explanation
This chunk defines functions to register SBBs, child blocks, and blueprints. It includes error handling for failed registrations and ensures proper capacity allocation for internal data structures. The `registerSBB` function initializes and populates structure lists and maps, while `registerChildBlock` manages child block registration. The `registerBlueprints` function loads and rotates blueprint entries. Other functions provide access to registered SBBs and blueprints, as well as resetting the registry.

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
- How does the `registerSBB` function handle errors during structure registration?
- What is the purpose of the `childrenToResolve` variable in the `registerSBB` function?
- How are blueprints rotated in the `registerBlueprints` function?
- What does the `getByStringId` function return if a string ID is not found?
- How does the `reset` function clear all registered SBBs and blueprints?
- What assertion checks are performed at the beginning of the `registerChildBlock` function?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_3*
