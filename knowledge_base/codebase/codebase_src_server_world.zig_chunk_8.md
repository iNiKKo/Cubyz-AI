# [hard/codebase_src_server_world.zig] - Chunk 8

**Type:** implementation
**Keywords:** inventory serialization, ZON file format, base64 encoding, chunk updates, game time synchronization, item entity collection
**Symbols:** savePlayerInventory, savePlayer, saveAllPlayers, saveItemdrops, isValidSpawnLocation, dropWithCooldown, drop, tick, update
**Concepts:** player data management, item drop handling, world update logic

## Summary
Handles saving player data, item drops, and world updates.

## Explanation
This chunk contains functions for saving player inventories, player data, all players' data, and item drops. It also includes logic for ticking the server world, updating game time, sending unimportant data to users, and managing item entities.

The `savePlayerInventory` function serializes inventory data into a base64-encoded string using `main.utils.BinaryWriter` to convert the inventory to bytes and then encoding those bytes with `std.base64.url_safe.Encoder`. The `savePlayer` function writes player data to a ZON file, including inventory, permissions, and spawn position. The path for the ZON file is constructed using `std.fmt.allocPrint`, and the player data is written using `files.cubyzDir().writeZon`. The `saveAllPlayers` function iterates over all users and saves their data by calling `savePlayer` on each user.

The `saveItemdrops` function serializes item drop data to a binary file. It uses `main.utils.BinaryWriter` to convert the item drop manager's data to bytes and writes it to a file named `itemdrops.bin` in the save directory.

The `isValidSpawnLocation` function checks if a location is valid for player spawning by retrieving the biome at the given coordinates using `terrain.SurfaceMap.getOrGenerateFragment` and checking if the biome allows player spawning with `map.getBiome(wx, wy).isValidPlayerSpawn`.

The `dropWithCooldown` and `drop` functions manage item drops with optional cooldowns. The `dropWithCooldown` function calculates the velocity vector from the direction and speed, generates a random rotation vector, and adds the item drop to the manager with a specified pickup cooldown. The `drop` function is a simplified version of `dropWithCooldown` that sets the cooldown to 0.

The `tick` function updates simulation chunks by locking the chunk manager's mutex, iterating over all simulation chunks, updating each chunk, and then unlocking the mutex. The `update` function manages game time, user data sending, and item entity collection. It calculates the delta time since the last update, adjusts it if necessary, and updates the game time in 100ms increments. It also sends unimportant data to users every 2 seconds and calls `tick` to update simulation chunks. The function handles item entities by checking for collected items from each user.

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
- How is player inventory data serialized?
- What file format is used for saving player data?
- How are item drops managed in the server world?
- What checks are performed to validate spawn locations?
- How does the server handle item drop cooldowns?
- What is the process for updating simulation chunks?
- How is game time synchronized across users?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_8*
