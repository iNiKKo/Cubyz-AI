# [hard/codebase_src_server_world.zig] - Chunk 6

**Type:** implementation
**Keywords:** Level of Detail, task queue, multi-threading, directory traversal, synchronization
**Symbols:** RegenerateLODTask, RegenerateLODTask.clean, RegenerateLODTask.getPriority, RegenerateLODTask.isStillNeeded, RegenerateLODTask.run, regenerateLOD
**Concepts:** chunk LOD regeneration, task scheduling, thread pool management, file I/O operations

## Summary
Handles LOD (Level of Detail) regeneration for chunks in a server world.

## Explanation
This chunk defines the `RegenerateLODTask` struct and its associated methods, which manage the process of regenerating LODs for chunks. The `schedule` method creates and adds a task to the thread pool. The `run` method performs the actual LOD regeneration by iterating through regions and updating lower-resolution chunks based on higher-resolution data. The `regenerateLOD` function orchestrates the entire LOD regeneration process, including deleting old LOD files, finding stored chunks, scheduling tasks for each chunk, and processing update requests until all tasks are completed.

## Code Example
```zig
pub fn getPriority(_: *RegenerateLODTask) f32 {
	return std.math.floatMax(f32);
}
```

## Related Questions
- How does the `regenerateLOD` function delete old LOD directories?
- What is the purpose of the `clean` method in the `RegenerateLODTask` struct?
- How are tasks scheduled for LOD regeneration in this chunk?
- What synchronization mechanisms are used to manage access to chunks and regions?
- How does the `run` method update lower-resolution chunks from higher-resolution data?
- What is the role of the `schedule` method in the LOD regeneration process?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_6*
