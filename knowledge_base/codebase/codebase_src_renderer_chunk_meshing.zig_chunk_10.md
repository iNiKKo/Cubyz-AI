# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 10

**Type:** implementation
**Keywords:** BlockUpdateTask, updateBlock, block entity, thread pool, mutex locking, mesh regeneration, light refresh scheduling, stack allocator, defer cleanup
**Symbols:** appendIfNotContained, updateBlock, BlockUpdateTask, schedule, getPriority, isStillNeeded, run, clean
**Concepts:** block update pipeline, neighbor data propagation, entity data application, mesh regeneration scheduling, thread pool task execution, mutex locking, deferred cleanup

## Summary
This chunk implements the block update processing pipeline for a ChunkMesh, including neighbor data updates, entity data application/removal, mesh regeneration scheduling, and asynchronous block update task execution via a thread pool.

## Explanation
The code defines an appendIfNotContained helper that safely adds a ChunkMesh to a list. The public updateBlock method receives a BlockUpdate containing world coordinates, extracts the block position, locks the chunk mutex, retrieves the old block from self.chunk.data, and handles two cases: if the new block equals the old block it applies or removes block entity data via blockEntity.updateClientData (with error logging), then stores the new block; otherwise it replaces the block. After unlocking, it pushes the position onto self.blockUpdateQueue and schedules a BlockUpdateTask when the queue length becomes 1. The BlockUpdateTask struct is defined with a vtable using castFunctionSelfToAnyopaque for getPriority, isStillNeeded, run, and clean methods. schedule creates an allocator-owned task instance and adds it to main.threadPool. getPriority returns a high base value plus player blocking priority (with a TODO comment about mutex avoidance). isStillNeeded checks if the world is paused or null. run acquires stack-allocated lightRefreshList and regenerateMeshList, then loops over mesh.blockUpdateQueue under lock, calling mesh.updateBlockLightAndMesh for each queued position; after draining it regenerates meshes in regenerateMeshList and schedules light refreshes for positions in lightRefreshList. clean destroys the task.

## Related Questions
- What is the purpose of the appendIfNotContained function in this chunk?
- How does updateBlock handle the case when oldBlock equals newBlock?
- Under what condition is a BlockUpdateTask scheduled for execution?
- Which methods are exposed via the vtable of BlockUpdateTask and how are they implemented?
- What happens inside the run method of BlockUpdateTask regarding mesh updates?
- How does getPriority compute its return value and why is there a TODO comment?
- What does isStillNeeded check to decide if a task should remain in the pool?
- Where are lightRefreshList and regenerateMeshList allocated and how are they cleaned up?
- In what order are meshes regenerated after processing block updates?
- How does clean release resources for BlockUpdateTask?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_10*
