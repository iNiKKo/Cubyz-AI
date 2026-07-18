# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 10

**Type:** implementation
**Keywords:** mutex locking, block dependencies, mesh regeneration, thread scheduling, lighting update
**Symbols:** appendIfNotContained, updateBlock, BlockUpdateTask, BlockUpdateTask.vtable, BlockUpdateTask.schedule, BlockUpdateTask.getPriority, BlockUpdateTask.isStillNeeded, BlockUpdateTask.run, BlockUpdateTask.clean, scheduleLightRefresh
**Concepts:** chunk meshing, block updates, lighting refresh, thread pool tasks

## Summary
Handles block updates and mesh regeneration in a chunk.

## Explanation
This chunk manages the process of updating blocks within a chunk, including handling dependencies on neighboring blocks, updating lighting, and scheduling mesh regeneration. It includes functions for appending items to lists without duplication, updating individual blocks, and managing tasks related to block updates. The `BlockUpdateTask` struct defines a task that processes block updates in a thread pool, ensuring efficient execution of update operations.

## Code Example
```zig
fn appendIfNotContained(list: *main.ListManaged(*ChunkMesh), mesh: *ChunkMesh) void {
	for (list.items) |other| {
		if (other == mesh) {
			return;
		}
	}
	list.append(mesh);
}
```

## Related Questions
- How does the chunk handle block updates that depend on neighbors?
- What is the purpose of the `appendIfNotContained` function?
- How are block entity data updates handled in this chunk?
- What role does the `BlockUpdateTask` struct play in the update process?
- How is lighting refresh scheduled for chunks?
- What mechanism ensures that only unique meshes are added to the regeneration list?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_10*
