# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 5

**Type:** implementation
**Keywords:** mutex locking, mesh storage, priority queue, block update, light map, animation frame
**Symbols:** updateMeshes, mutex, priorityMeshUpdateList, mapUpdatableList, updatableList, addToUpdateList, addMeshToStorage, finishMesh, updateBlock, updateLightMap, addBreakingAnimation
**Concepts:** chunk meshing, thread safety, rendering pipeline, block updates, light map updates, animation handling

## Summary
Handles mesh updates and storage for rendering.

## Explanation
This chunk manages the updating and storage of meshes for rendering. It includes functions to update meshes based on priority, add meshes to update lists, finish mesh processing, handle block updates, update light maps, and manage block breaking animations. The code uses a mutex for thread safety, ensuring that mesh operations are synchronized across threads.

## Code Example
```zig
pub fn addToUpdateList(mesh: *chunk_meshing.ChunkMesh) void {
	mutex.lock();
	defer mutex.unlock();
	if (mesh.finishedMeshing) {
		priorityMeshUpdateList.pushBack(mesh.pos);
		mesh.needsMeshUpdate = true;
	}
}
```

## Related Questions
- What is the purpose of the `updateMeshes` function?
- How does the code ensure thread safety when updating meshes?
- What happens if a mesh is not in render distance during addition?
- How are block updates handled in this chunk?
- What is the role of the `mutex` in this module?
- How are breaking animations managed for blocks?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_5*
