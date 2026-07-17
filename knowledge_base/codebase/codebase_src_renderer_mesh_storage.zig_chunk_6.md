# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 6

**Type:** implementation
**Keywords:** mesh storage, thread synchronization, priority queue, block updates, animation frames
**Symbols:** addToUpdateList, addMeshToStorage, finishMesh, updateBlock, updateLightMap, addBreakingAnimation, addBreakingAnimationFace
**Concepts:** chunk meshing, block breaking animation, light map updates

## Summary
Handles mesh storage, updates, and block breaking animations.

## Explanation
This chunk manages the lifecycle of meshes within the renderer. It includes functions to upload mesh data, add meshes to update lists, finish mesh processing, update blocks, and handle light maps. The code also handles block breaking animations by updating specific faces of blocks with animated textures based on the breaking progress.

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
- How does the mesh storage handle adding a mesh to the update list?
- What error conditions can occur when adding a mesh to storage?
- How is block breaking animation data structured and updated?
- What synchronization mechanisms are used in this chunk?
- How does the code determine which mesh to update next based on priority?
- What happens if a block update occurs for a position without an existing mesh?
- How are light map updates managed in this chunk?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_6*
