# [hard/codebase_src_server_world.zig] - Chunk 2

**Type:** implementation
**Keywords:** task scheduling, reference counting, thread pool, priority queue, resource management, binary serialization, mutex locking
**Symbols:** ChunkLoadTask, LightMapLoadTask, vtable, scheduleAndDecreaseRefCount, getPriority, isStillNeeded, run, clean, init, deinit, queueLightMapAndDecreaseRefCount, queueChunkAndDecreaseRefCount, generateChunk, chunkInitFunctionForCacheAndIncreaseRefCount
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
Handles chunk and light map generation tasks, including scheduling, execution, and cleanup.

## Explanation
This chunk defines the `ChunkLoadTask` and `LightMapLoadTask` structures, which manage the loading and processing of chunks and light maps respectively. The `ChunkManager` struct initializes and deinitializes world-related resources, queues tasks for chunk and light map generation, and generates chunks based on given positions and sources. Functions like `clean`, `scheduleAndDecreaseRefCount`, `getPriority`, `isStillNeeded`, `run`, and `generateChunk` are implemented to manage task lifecycle, priority, execution, and resource cleanup. The code also includes utility functions for initializing and loading chunks from storage or generating them if they don't exist.

## Code Example
```zig
pub fn clean(self: *ChunkLoadTask) void {
	switch (self.source) {
		.user => |user| user.decreaseRefCount(),
		.simulationChunk => |ch| ch.decreaseRefCount(),
	}
	main.globalAllocator.destroy(self);
}
```

## Related Questions
- How does the `clean` method in `ChunkLoadTask` work?
- What is the purpose of the `scheduleAndDecreaseRefCount` function in `LightMapLoadTask`?
- How are priorities determined for tasks in the thread pool?
- What happens if a task is no longer needed during execution?
- How does chunk generation handle both user and simulation sources?
- What role does the mutex play in initializing chunks?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_2*
