# [hard/codebase_src_server_world.zig] - Chunk 8

**Type:** serialization
**Keywords:** readToZon, writeZon, makePath, BinaryReader, BinaryWriter, base64 URL-safe, createExternallyManagedInventory, getInventoryFromSource, toBytes, calcSizeForSlice
**Symbols:** loadPlayer, savePlayer, saveAllPlayers, saveItemdrops, isValidSpawnLocation, dropWithCooldown, drop, loadPlayerInventory, savePlayerInventory
**Concepts:** player persistence, inventory serialization, base64 URL-safe encoding, ZON file I/O, spawn position restoration, permission loading, gamemode parsing, thread context assertion

## Summary
This chunk implements server-side player persistence and inventory serialization. It loads a player's ZON file from disk into a User struct, handling key updates, gamemode parsing, spawn position restoration, and inventory decoding via base64 URL-safe encoding. It also provides savePlayer to write the same fields back to disk, including permissions, entity data, and both main inventory and hand inventory encoded as base64 strings.

## Explanation
The chunk defines loadPlayer which reads a player's ZON file from files.cubyzDir() using readToZon into a stack-allocated buffer. It then processes user.newKeyString: if the stored publicKey differs, it removes the old key entry and inserts the new one; otherwise it enters removeOld block to delete any name-based entry before inserting the new key. After that it calls player.loadFrom with .server context to deserialize entity data. The chunk frees any existing name string from main.globalAllocator and assigns a duplicated copy of user.name. If playerData is null (new player), it sets position to self.spawn; otherwise it loads permissions via user.permissions.fromZon, parses gamemode using std.meta.stringToEnum with fallbacks, and calls loadPlayerInventory for both the main inventory and hand inventory. loadPlayerInventory decodes base64 URL-safe data: first it calculates required size via Decoder.calcSizeForSlice, allocates bytes on main.stackAllocator, then runs Decoder.decode; any error logs to std.log.err and returns an empty slice. It creates a BinaryReader from the decoded bytes and passes it to Inventory.server.createExternallyManagedInventory with source set to .playerInventory or .hand. savePlayer constructs a path under saves/{self.path}/players/{user.playerIndex}.zon, reads existing data (or creates an object), then populates fields: name, publicKey if user.newKeyString is true, entity via user.player().save(.disk), permissions via toZon, gamemode as @tagName of the loaded enum, and both inventories using savePlayerInventory which writes to a BinaryWriter, calls inv.toBytes, calculates base64 size with Encoder.calcSize, allocates destination on allocator, encodes, and returns the string. It asserts correct thread context before retrieving inventories via getInventoryFromSource; if either is missing it panics. Finally it ensures the saves directory exists via makePath and writes the ZON file. saveAllPlayers iterates over a user list obtained from server.getUserListAndIncreaseRefCount (deferred free via freeUserListAndDecreaseRefCount) and calls savePlayer for each. saveItemdrops serializes self.itemDropManager to bytes using BinaryWriter, then writes to saves/{self.path}/itemdrops.bin. isValidSpawnLocation queries terrain.SurfaceMap.getOrGenerateFragment for a 1x1 map at (wx, wy) and returns the biome's isValidPlayerSpawn flag. dropWithCooldown computes velocity vector from dir scaled by velocity, generates random rotation via main.random.nextFloatVector(3, &main.seed) multiplied by 2π, then calls self.itemDropManager.add with server.updatesPerSec*900 as lifetime and pickupCooldown; drop simply calls dropWithCooldown with cooldown zero.

## Related Questions
- What happens when a player's public key is updated in the database?
- How does loadPlayerInventory handle malformed base64 data from disk?
- Which allocator is used for temporary buffers during inventory decoding?
- Under what condition does savePlayer panic instead of writing to disk?
- How are permissions persisted when a player loads on the server?
- What path pattern is used for individual player ZON files in saves directory?
- Does dropWithCooldown apply any lifetime limit to dropped items?
- Which function ensures thread context before accessing inventory sources?
- How does isValidSpawnLocation determine if a location is valid for spawning?
- What data structure holds the list of users iterated by saveAllPlayers?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_8*
