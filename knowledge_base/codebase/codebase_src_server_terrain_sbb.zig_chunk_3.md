# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 3

**Type:** implementation
**Keywords:** registration, error handling, capacity allocation, data structures, blueprint rotation
**Symbols:** registerSBB, registerChildBlock, registerBlueprints, getByStringId, list, reset
**Concepts:** structure building blocks (SBBs), blueprints, world generation

## Summary
Handles registration and management of structure building blocks (SBBs) and blueprints in the Cubyz server by ensuring proper capacity allocation for internal data structures, initializing and populating lists and maps, managing child block registration, loading and rotating blueprint entries, providing access to registered SBBs and blueprints, and resetting the registry.

## Explanation
This chunk defines functions to register structure building blocks (SBBs), child blocks, and blueprints. It includes error handling for failed registrations and ensures proper capacity allocation for internal data structures. The `registerSBB` function initializes and populates structure lists and maps by iterating through the provided structures, ensuring each entry is correctly registered with assertions and logging errors if registration fails. The `childrenToResolve` variable manages child resolution during registration. The `registerChildBlock` function registers a numeric ID and string ID for child blocks, taking only the color name from the ID and storing it in appropriate data structures. The `registerBlueprints` function loads blueprint entries, rotates them by 90 degrees increments, and stores them in lists and maps with assertions to ensure proper capacity allocation. Other functions provide access to registered SBBs and blueprints via string IDs and reset the registry entirely.

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
