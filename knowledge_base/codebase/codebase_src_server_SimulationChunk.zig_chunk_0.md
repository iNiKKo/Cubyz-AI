# [easy/codebase_src_server_SimulationChunk.zig] - Chunk 0

**Type:** implementation
**Keywords:** atomic value, mutex locking, random tick speed, block onTick, chunk manager
**Symbols:** SimulationChunk, chunk, refCount, pos, blockUpdateSystem
**Concepts:** simulation chunk, server-side chunk management, block updates

## Summary
SimulationChunk manages server-side chunk data and block updates.

## Explanation
The SimulationChunk struct manages server-side chunk data and block updates. It holds an atomic reference to a ServerChunk (`chunk`), an atomic `refCount`, its position (`pos`), and a `BlockUpdateSystem`. The `initAndIncreaseRefCount` function allocates a new instance with `refCount = 1`. The `increaseRefCount` method atomically increments the reference count, asserting that the previous value wasn't 0. The `decreaseRefCount` method atomically decrements the reference count: if the value before decrementing was `2`, it calls `ChunkManager.tryRemoveSimulationChunk`; if it was `1`, it calls `deinit()` (which asserts `refCount == 0`, deinitializes the `blockUpdateSystem`, decreases the underlying chunk's ref count if set, and frees the struct). The `update(randomTickSpeed)` method calls `tickBlocksInChunk`, which picks `randomTickSpeed` random block positions using `main.random.nextInt(u15, &main.seed)`. For each position, it locks the chunk's mutex to read the block, then runs that block's `onTick()` callback. The `getChunk` function returns the current ServerChunk from a SimulationChunk. The `setChunkAndDecreaseRefCount` function sets a new ServerChunk and decreases its reference count. Mutex locking in `tickBlocksInChunk` ensures thread safety when accessing blocks within the chunk.

The `tickBlocksInChunk` function iterates over `randomTickSpeed` random block positions, picking each position using `main.random.nextInt(u15, &main.seed)`. For each position, it locks the chunk's mutex to read the block at that position and then runs the block's `onTick()` callback with a context containing the block, chunk, and block position. The `deinit` method asserts that `refCount == 0`, deinitializes the `blockUpdateSystem`, decreases the reference count of the underlying chunk if set, and frees the SimulationChunk struct.

## Code Example
```zig
pub fn update(self: *SimulationChunk, randomTickSpeed: u32) void {
	const serverChunk = self.getChunk() orelse return;
	tickBlocksInChunk(serverChunk, randomTickSpeed);
	self.blockUpdateSystem.update(serverChunk);
}
```

## Related Questions
- What is the purpose of the SimulationChunk struct?
- How does SimulationChunk manage its reference count?
- What method increases the reference count of a SimulationChunk?
- What method decreases the reference count and what actions are taken when it reaches zero?
- How is the chunk data managed within SimulationChunk?
- What is the role of BlockUpdateSystem in SimulationChunk?
- How does SimulationChunk handle block updates based on random tick speed?
- What is the function to get the current ServerChunk from a SimulationChunk?
- What is the function to set a new ServerChunk and decrease its reference count?
- What is the purpose of the mutex locking in the tickBlocksInChunk function?
- How does the SimulationChunk manage block updates for all blocks within a chunk?
- What is the function that runs onTick() for each block in the chunk?

*Source: unknown | chunk_id: codebase_src_server_SimulationChunk.zig_chunk_0*
