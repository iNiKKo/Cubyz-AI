# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 0

**Type:** implementation
**Keywords:** atomic operations, memory pool, concurrent queue, chunk storage, node retrieval
**Symbols:** ChunkMeshNode, storageSize, storageMask, storageLists, mapStorageLists, meshList, priorityMeshUpdateList, updatableList, mapUpdatableList, lastPx, lastPy, lastPz, lastRD, mutex, BlockUpdate, meshMemoryPool
**Concepts:** chunk meshing, memory management, concurrency control

## Summary
Manages chunk mesh storage and updates, including initialization, deinitialization, and node retrieval.

## Explanation
This chunk defines the structure and logic for managing chunk mesh storage in the Cubyz voxel engine. It includes functions for initializing and deinitializing mesh storage, retrieving nodes based on positions, and updating higher LOD nodes' meshing status. The chunk uses atomic operations to manage concurrent access to mesh data and employs a memory pool for efficient allocation of chunk meshes.

## Code Example
```zig
pub fn init() void { // MARK: init()
	lastRD = 0;
	for (&storageLists) |*storageList| {
		storageList.* = main.globalAllocator.create([storageSize*storageSize*storageSize]ChunkMeshNode);
		for (storageList.*) |*val| {
			val.* = .{};
		}
	}
	for (&mapStorageLists) |*mapStorageList| {
		mapStorageList.* = main.globalAllocator.create([storageSize*storageSize]Atomic(?*LightMap.LightMapFragment));
		@memset(mapStorageList.*, .init(null));
	}
	priorityMeshUpdateList = .init(main.globalAllocator, 16);
	mapUpdatableList = .init(main.globalAllocator, 16);
}
```

## Related Questions
- How is the `ChunkMeshNode` structure defined?
- What is the purpose of the `storageLists` array?
- How does the `getNodePointer` function work?
- What role does the `meshMemoryPool` play in this module?
- How are higher LOD nodes' meshing statuses updated?
- What happens during the initialization of mesh storage?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_0*
