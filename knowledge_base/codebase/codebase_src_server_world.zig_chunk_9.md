# [hard/codebase_src_server_world.zig] - Chunk 9

**Type:** implementation
**Keywords:** reference counting, mutex locking, chunk storage, block update, entity data
**Symbols:** ServerWorld, ServerWorld.tick, ServerWorld.itemDropManager.update, ServerWorld.chunkUpdateQueue.popFront, ServerWorld.regionUpdateQueue.popFront, ServerWorld.queueChunkAndDecreaseRefCount, ServerWorld.queueLightMapAndDecreaseRefCount, ServerWorld.getSimulationChunkAndIncreaseRefCount, ServerWorld.getOrGenerateChunkAndIncreaseRefCount, ServerWorld.getChunkFromCacheAndIncreaseRefCount, ServerWorld.getBiome, ServerWorld.getBlock, ServerWorld.getBlockAndBlockEntityData, ServerWorld.cmpxchgBlock
**Concepts:** world management, chunk handling, block interactions, user list updates, item entity management

## Summary
Handles server-side world updates, chunk management, and block interactions.

## Explanation
This chunk manages the server's world state, including updating user lists, handling item entities, storing chunks and regions, and managing blocks. It includes methods for queuing chunks and light maps, retrieving simulation and cached chunks, getting biome data, fetching blocks, comparing and exchanging block states, and handling block entity data. The code ensures proper reference counting and synchronization using mutexes to prevent race conditions.

## Code Example
```zig
pub fn queueChunkAndDecreaseRefCount(self: *ServerWorld, pos: ChunkPosition, source: *User) void {
		self.chunkManager.queueChunkAndDecreaseRefCount(pos, source);
	}
```

## Related Questions
- What method is called to handle item entities?
- How does the server manage chunk updates and storage?
- What function retrieves a simulation chunk with increased reference count?
- How are blocks compared and exchanged in the world?
- What role do mutexes play in this chunk's logic?
- How is block entity data fetched and updated?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_9*
