# [easy/codebase_src_server_SimulationChunk.zig] - Chunk 0

**Type:** implementation
**Keywords:** atomic value, mutex locking, random tick speed, block onTick, chunk manager
**Symbols:** SimulationChunk, chunk, refCount, pos, blockUpdateSystem
**Concepts:** simulation chunk, server-side chunk management, block updates

## Summary
SimulationChunk manages server-side chunk data and block updates.

## Explanation
The SimulationChunk struct holds an atomic reference to a ServerChunk, an atomic `refCount`, its `pos`, and a `BlockUpdateSystem`. `initAndIncreaseRefCount` allocates a new instance with `refCount = 1`. `increaseRefCount` atomically increments (asserting the previous value wasn't 0). `decreaseRefCount` atomically decrements: if the value *before* decrementing was `2`, it calls `ChunkManager.tryRemoveSimulationChunk`; if it was `1`, it calls `deinit()` (which asserts `refCount == 0`, deinitializes the `blockUpdateSystem`, decreases the underlying chunk's ref count if set, and frees the struct). `update(randomTickSpeed)` calls `tickBlocksInChunk`, which picks `randomTickSpeed` random block positions (via `main.random.nextInt`), locks the chunk's mutex to read each block, then runs that block's `onTick()` callback.

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
