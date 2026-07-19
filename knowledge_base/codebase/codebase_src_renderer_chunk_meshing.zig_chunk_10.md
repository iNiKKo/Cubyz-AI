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
