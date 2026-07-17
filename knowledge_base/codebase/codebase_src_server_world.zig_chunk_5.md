# [hard/codebase_src_server_world.zig] - Chunk 5

**Type:** implementation
**Keywords:** world versioning, file I/O, data migration, thread pool, mutex locking
**Symbols:** worldDataVersion, ServerWorld.loadWorldConfig, ServerWorld.saveWorldConfig, ServerWorld.loadPlayerLoginInfo, RegenerateLODTask, RegenerateLODTask.pos, RegenerateLODTask.storeMaps, RegenerateLODTask.vtable, RegenerateLODTask.schedule, RegenerateLODTask.getPriority, RegenerateLODTask.isStillNeeded, RegenerateLODTask.run, RegenerateLODTask.clean
**Concepts:** world migration, configuration management, player login processing, chunk LOD regeneration

## Summary
Handles world migration, configuration loading/saving, and player login info processing.

## Explanation
This chunk manages the migration of world data from older versions to the current version by updating specific settings and file structures. It also includes functions for loading and saving world configurations, as well as processing player login information by reading player files and updating internal databases. The `RegenerateLODTask` struct defines a task for regenerating level-of-detail maps for chunks, including methods for scheduling, priority determination, execution, and cleanup.

## Code Example
```zig
pub fn schedule(pos: ChunkPosition, storeMaps: bool) void {
	const task = main.globalAllocator.create(RegenerateLODTask);
	task.* = .{
		.pos = pos,
		.storeMaps = storeMaps,
	};
	main.threadPool.addTask(task, &vtable);
}
```

## Related Questions
- How does the world migration process work in this chunk?
- What is the purpose of the `RegenerateLODTask` struct?
- How are player login files processed and stored internally?
- What version of the world data is expected by this module?
- How does the chunk handle errors during file operations?
- What methods are available for saving world configurations?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_5*
