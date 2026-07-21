# [hard/codebase_src_server_world.zig] - Chunk 7

**Type:** api
**Keywords:** ZON file format, base64 encoding, binary serialization, player data persistence, inventory handling
**Symbols:** loadPlayer, loadPlayerInventory, savePlayerInventory, savePlayer
**Concepts:** player loading, player saving, inventory management

## Summary
Handles player loading and saving in a server world, including inventory management.

## Explanation
This chunk manages the lifecycle of players within a server world. It includes functions to load player data from disk, update player state based on loaded data, and save player data back to disk. The `loadPlayer` function reads player data from a ZON file, checks for key mismatches, updates player permissions, gamemode, inventory, and spawn position. If the public key in the player data does not match the user's new key string, it removes the old entry from the player database and adds the new one. It also overrides the player's name with the user's name. The `savePlayer` function writes player data to a ZON file, including entity state, permissions, gamemode, and inventory. Inventory management is handled by decoding base64-encoded data into binary format and encoding it back when saving. Error handling includes logging errors encountered during reading or writing ZON files.

The direction changes and steps remaining are calculated as follows: the `stepsRemaining` variable is decremented each time a step is taken, and when it reaches zero, the direction (`dir`) is changed based on a predefined sequence (`.dirNegX => .dirNegY`, `.dirPosX => .dirPosY`, `.dirNegY => .dirPosX`, `.dirPosY => .dirNegX`). Every second turn, the number of steps needed doubles. The `spawn` variable is used to determine the initial spawn location and height based on the terrain map.

## Code Example
```zig
fn savePlayerInventory(allocator: NeverFailingAllocator, inv: main.items.Inventory) []const u8 {
		var writer = main.utils.BinaryWriter.init(main.stackAllocator);
		defer writer.deinit();

		inv.toBytes(&writer);

		const destination: []u8 = allocator.alloc(u8, std.base64.url_safe.Encoder.calcSize(writer.data.items.len));
		return std.base64.url_safe.Encoder.encode(destination, writer.data.items);
	}
```

## Related Questions
- How does the `loadPlayer` function handle player data loading?
- What is the purpose of the `savePlayerInventory` function?
- How does the chunk manage inventory encoding and decoding?
- What steps are taken to ensure player data consistency during saving?
- How does the chunk handle errors when reading or writing ZON files?
- What role does the `loadPlayerInventory` function play in the overall player loading process?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_7*
