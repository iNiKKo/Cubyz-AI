# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 5

**Type:** implementation
**Keywords:** mutex, deferredDeinit, swap, renderDistance, frustum, LOD, meshUpdateList, mapUpdatableList, updatableList
**Symbols:** updateMeshes, getMesh, isMapInRenderDistance, deferredDeinit, getMapPiecePointer, swap, isInRenderDistance, getPriority
**Concepts:** mesh update loop, LOD neighbor updates, frustum culling, mutex locking, map piece swapping, render distance checks, priority-based selection

## Summary
This chunk implements the mesh update loop that processes pending mesh uploads under a mutex, handles LOD neighbor updates by checking frustum visibility and marking nodes as rendered or inactive, removes empty meshes from the global list, and swaps out map pieces when they enter render distance.

## Explanation
The code iterates over priorityMeshUpdateList with mutex locking to ensure only one thread uploads at a time; it skips meshes that do not need updates. It then processes mapUpdatableList: if a map is outside render distance it calls deferredDeinit, otherwise it swaps the map piece out and deinitializes the old pointer. Finally it walks updatableList items, removes those outside render distance (with mutex unlock/defer lock), computes priority relative to player eye position, and tracks the closest priority index for further selection logic.

## Related Questions
- How does the code ensure only one thread uploads a mesh at a time?
- What condition causes a map piece to be deinitialized immediately instead of being swapped out?
- Where is the player eye position retrieved for priority calculations?
- Which function is called when a map is outside render distance in updatableList processing?
- How does the code handle meshes that do not need an update?
- What happens to the old map piece pointer after swapping out a new one?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_5*
