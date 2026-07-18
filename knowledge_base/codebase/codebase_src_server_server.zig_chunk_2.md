# [hard/codebase_src_server_server.zig] - Chunk 2

**Type:** implementation
**Keywords:** reference counting, chunk management, player data, signature verification, memory optimization
**Symbols:** increaseRefCount, decreaseRefCount, identifyFromKeysAndName, identifyAsLocal, verifySignatures, initPlayer, simArrIndex, unloadOldChunk, loadNewChunk, loadUnloadChunks
**Concepts:** user management, chunk loading/unloading, reference counting, player initialization, signature verification

## Summary
Handles user management and chunk loading/unloading in the server.

## Explanation
This code defines several key functions for server-side user management and chunk handling in Cubyz. The `increaseRefCount` function increments the reference count of a user object, ensuring that it remains valid until all references are released. The `identifyFromKeysAndName` method initializes a new user by setting their name and keys from provided data, asserting that no existing key is present before proceeding. If no matching player index is found in the database, the function assigns a unique identifier to the player based on available slots or local player index if none are free.

The `identifyAsLocal` method sets up a user as a local player by assigning them a name and setting their player index directly to the local player index. The `verifySignatures` function ensures that signatures provided in binary reader data match those expected for secure communication, using both primary and legacy keys if available.

The `initPlayer` function initializes a new player object by allocating an ID from a free pool, loading player data into the world database, and setting up default models and bags. It also handles interpolation initialization and chunk loading/unloading based on player position and render distance.

Chunk management is handled through the `unloadOldChunk`, `loadNewChunk`, and `loadUnloadChunks` functions. These methods calculate bounding boxes for old and new positions relative to the current render distance, then iterate over these ranges to unload chunks outside the new range and load new ones within it. The `simArrIndex` function computes an index into a simulation array based on chunk coordinates.

Specifically, `unloadOldChunk` iterates through all loaded chunks in the old bounding box defined by:
- `lastBoxStart = (self.lastPos - self.lastRenderDistance * chunk.chunkSize) & ~chunk.chunkMask`
- `lastBoxEnd = (self.lastPos + self.lastRenderDistance * chunk.chunkSize + chunk.chunkSize - 1) & ~chunk.chunkMask`

It then unloads chunks outside the new bounding box defined by:
- `newBoxStart = (newPos - newRenderDistance * chunk.chunkSize) & ~chunk.chunkMask`
- `newBoxEnd = (newPos + newRenderDistance * chunk.chunkSize + chunk.chunkSize - 1) & ~chunk.chunkMask`

The conditions for unloading a chunk are:
- `(x -% newBoxStart[0] >= 0 and x -% newBoxEnd[0] < 0)`
- `(y -% newBoxStart[1] >= 0 and y -% newBoxEnd[1] < 0)`
- `(z -% newBoxStart[2] >= 0 and z -% newBoxEnd[2] < 0)`

Similarly, `loadNewChunk` generates and loads new chunks within the new bounding box that were not previously loaded using similar conditions.

The `simArrIndex` function computes an index into a simulation array based on chunk coordinates as follows:
- `simArrIndex(x) = (x >> log2(chunk.chunkSize))`

These functions ensure efficient memory management and performance optimization by dynamically loading and unloading chunks based on the player's position and render distance.

## Code Example
```zig
pub fn increaseRefCount(self: *User) void {
	const prevVal = self.refCount.fetchAdd(1, .monotonic);
	std.debug.assert(prevVal != 0);
}
```

## Related Questions
-  How does the `increaseRefCount` function work?
-  What is the purpose of the `identifyFromKeysAndName` method?
-  How are chunks unloaded and loaded in this code? Provide specific conditions and calculations used.
-  What does the `verifySignatures` function do?
-  How is player data initialized for a new user?
-  What is the role of the `simArrIndex` function?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_2*
