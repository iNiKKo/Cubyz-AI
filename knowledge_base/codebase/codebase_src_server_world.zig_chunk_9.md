# [hard/codebase_src_server_world.zig] - Chunk 9

**Type:** implementation
**Keywords:** reference counting, mutex locking, chunk storage, block update, entity data
**Symbols:** ServerWorld, ServerWorld.tick, ServerWorld.itemDropManager.update, ServerWorld.chunkUpdateQueue.popFront, ServerWorld.regionUpdateQueue.popFront, ServerWorld.queueChunkAndDecreaseRefCount, ServerWorld.queueLightMapAndDecreaseRefCount, ServerWorld.getSimulationChunkAndIncreaseRefCount, ServerWorld.getOrGenerateChunkAndIncreaseRefCount, ServerWorld.getChunkFromCacheAndIncreaseRefCount, ServerWorld.getBiome, ServerWorld.getBlock, ServerWorld.getBlockAndBlockEntityData, ServerWorld.cmpxchgBlock
**Concepts:** world management, chunk handling, block interactions, user list updates, item entity management

## Summary
Handles server-side world updates, chunk management, and block interactions.

## Explanation
This chunk manages the server's world state, including updating user lists, handling item entities, storing chunks and regions, and managing blocks. The `tick` method updates user lists by sending time information to connected users. Item entities are managed by the `itemDropManager`, which is updated with `deltaTime`. Chunks and regions are stored within a specified storage time (`main.settings.storageTime`). At least one chunk and one region are stored per iteration, ensuring that all chunks and regions will be stored within the storage time. The insertion time is calculated as `newTime.subDuration(main.settings.storageTime)`, and chunks and regions are processed in a loop until the insertion time condition is met. Methods like `queueChunkAndDecreaseRefCount` and `queueLightMapAndDecreaseRefCount` queue chunks and light maps for processing, respectively. The `getSimulationChunkAndIncreaseRefCount`, `getOrGenerateChunkAndIncreaseRefCount`, and `getChunkFromCacheAndIncreaseRefCount` methods retrieve chunks with increased reference counts. Biome data is fetched using the `CaveBiomeMap`. Blocks are retrieved and compared using methods like `getBlock` and `cmpxchgBlock`, which also handle block entity data. Mutexes ensure proper synchronization to prevent race conditions, particularly when accessing and modifying chunk data.

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
