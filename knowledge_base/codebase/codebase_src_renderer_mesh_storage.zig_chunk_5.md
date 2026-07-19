# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 5

**Type:** implementation
**Keywords:** mutex locking, mesh storage, priority queue, block update, light map, animation frame
**Symbols:** updateMeshes, mutex, priorityMeshUpdateList, mapUpdatableList, updatableList, addToUpdateList, addMeshToStorage, finishMesh, updateBlock, updateLightMap, addBreakingAnimation
**Concepts:** chunk meshing, thread safety, rendering pipeline, block updates, light map updates, animation handling

## Summary
Handles mesh updates and storage for rendering.

## Explanation
This chunk manages the updating and storage of meshes for rendering. It includes functions to update meshes based on priority, add meshes to update lists, finish mesh processing, handle block updates, update light maps, and manage block breaking animations. The code uses a mutex for thread safety, ensuring that mesh operations are synchronized across threads.

### `updateMeshes` Function
The `updateMeshes` function processes mesh updates based on priority and other criteria. It locks the mutex to ensure thread safety, then iterates through lists of meshes that need updating. For each mesh, it checks if the mesh needs an update and uploads the data if necessary. It also handles map updatable lists and ensures that at least one mesh is updated per call.

### `addToUpdateList` Function
The `addToUpdateList` function adds a mesh to the priority update list if it has finished meshing. It locks the mutex, checks the mesh's status, and updates the list accordingly.

### `addMeshToStorage` Function
The `addMeshToStorage` function adds a mesh to storage, ensuring that it is within render distance. If the mesh is already stored or no longer needed, it returns an error. It also updates higher-level LOD nodes if necessary.

### `finishMesh` Function
The `finishMesh` function appends a position to the updatable list, indicating that the mesh processing for that position is finished.

### `updateBlock` Function
The `updateBlock` function updates a block in a mesh if the mesh exists. It locks the mutex and processes the block update.

### `updateLightMap` Function
The `updateLightMap` function adds a light map fragment to the updatable list, ensuring that it is processed later.

### `addBreakingAnimation` Function
The `addBreakingAnimation` function manages block breaking animations by calculating the animation frame based on the breaking progress and adding the animation to the appropriate faces of the block model.

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
