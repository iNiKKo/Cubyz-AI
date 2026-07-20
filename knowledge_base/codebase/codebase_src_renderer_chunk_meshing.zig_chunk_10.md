# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 10

**Type:** implementation
**Keywords:** mutex locking, block dependencies, mesh regeneration, thread scheduling, lighting update
**Symbols:** appendIfNotContained, updateBlock, BlockUpdateTask, BlockUpdateTask.vtable, BlockUpdateTask.schedule, BlockUpdateTask.getPriority, BlockUpdateTask.isStillNeeded, BlockUpdateTask.run, BlockUpdateTask.clean, scheduleLightRefresh
**Concepts:** chunk meshing, block updates, lighting refresh, thread pool tasks

## Summary
Handles block updates and mesh regeneration in a chunk.

## Explanation
This chunk manages the process of updating blocks within a chunk, including handling dependencies on neighboring blocks, updating lighting, and scheduling mesh regeneration. It includes functions for appending items to lists without duplication, updating individual blocks, and managing tasks related to block updates.

The `appendIfNotContained` function checks if a mesh is already in the list before adding it, ensuring no duplicates are present. Block entity data updates are handled by reading the new data and applying it to the block entity, or removing existing data when the block changes. The `BlockUpdateTask` struct defines a task that processes block updates in a thread pool, ensuring efficient execution of update operations. Lighting refresh is scheduled for chunks by marking them as needing a light refresh, which triggers the regeneration of the mesh with updated lighting information.

When a block update occurs, the chunk first checks if the new block depends on its neighbors. If it does, it iterates through the neighboring blocks and updates their data accordingly. The block's lighting is then updated, and if the block position is at the edge of the chunk (x=0, x=31, y=0, y=31, z=0, z=31), the corresponding neighbor information in `lastNeighborsHigherLod` and `lastNeighborsSameLod` arrays is set to null. The mutex is locked during these operations to ensure thread safety.

If the old block has a block entity, its data is updated or removed based on whether the new block also has a block entity. The chunk's data is then updated with the new block, and the block update position is added to the `blockUpdateQueue`. If this is the first item in the queue, a `BlockUpdateTask` is scheduled for execution.

The `BlockUpdateTask` struct defines a task that processes block updates in a thread pool. It includes methods for getting the priority of the task, checking if it is still needed, running the task, and cleaning up after the task. The `schedule` method adds a new `BlockUpdateTask` to the thread pool.

Lighting refresh is scheduled by marking chunks as needing a light refresh, which triggers the regeneration of the mesh with updated lighting information.

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
