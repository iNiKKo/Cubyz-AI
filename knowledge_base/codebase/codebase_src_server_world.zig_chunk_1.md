# [hard/codebase_src_server_world.zig] - Chunk 1

**Type:** implementation
**Keywords:** reference counting, hash map, mutex locking, thread pool, asynchronous loading
**Symbols:** ChunkManager, ChunkManager.world, ChunkManager.terrainGenerationProfile, ChunkManager.reducedChunkCacheMask, ChunkManager.chunkCache, ChunkManager.HashContext, ChunkManager.simulationChunkHashMap, ChunkManager.mutex, ChunkManager.getSimulationChunkAndIncreaseRefCount, ChunkManager.getOrGenerateSimulationChunkAndIncreaseRefCount, ChunkManager.tryRemoveSimulationChunk, ChunkManager.Source, ChunkManager.Source.user, ChunkManager.Source.simulationChunk, ChunkManager.ChunkLoadTask, ChunkManager.ChunkLoadTask.pos, ChunkManager.ChunkLoadTask.source, ChunkManager.ChunkLoadTask.vtable, ChunkManager.ChunkLoadTask.scheduleAndDecreaseRefCount, ChunkManager.ChunkLoadTask.getPriority, ChunkManager.ChunkLoadTask.isStillNeeded, ChunkManager.ChunkLoadTask.run, ChunkManager.ChunkLoadTask.clean, ChunkManager.LightMapLoadTask, ChunkManager.LightMapLoadTask.pos, ChunkManager.LightMapLoadTask.source, ChunkManager.LightMapLoadTask.vtable, ChunkManager.LightMapLoadTask.scheduleAndDecreaseRefCount
**Concepts:** chunk meshing, world generation, asynchronous task scheduling

## Summary
The ChunkManager handles chunk loading, caching, and generation in a server environment.

## Explanation
ChunkManager manages chunks for a ServerWorld, using a cache to store up to 1 GiB of chunks. It includes methods for getting or generating simulation chunks with reference counting, removing chunks when no longer needed, and scheduling tasks for chunk loading and light map generation. The ChunkLoadTask struct defines how chunks are loaded asynchronously, prioritizing user requests and checking if tasks are still needed based on player proximity. LightMapLoadTask handles the asynchronous loading of light maps.

## Code Example
```zig
fn getSimulationChunkAndIncreaseRefCount(pos: chunk.ChunkPosition) ?*SimulationChunk {
	std.debug.assert(pos.voxelSize == 1);
	mutex.lock();
	defer mutex.unlock();
	if (simulationChunkHashMap.get(pos)) |ch| {
		ch.increaseRefCount();
		return ch;
	}
	return null;
}
```

## Related Questions
- How does ChunkManager handle chunk caching?
- What is the purpose of the getSimulationChunkAndIncreaseRefCount method in ChunkManager?
- How are tasks scheduled for chunk loading and light map generation?
- What conditions determine if a ChunkLoadTask is still needed?
- How does ChunkManager manage reference counting for chunks?
- What role does the mutex play in ChunkManager's operations?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_1*
