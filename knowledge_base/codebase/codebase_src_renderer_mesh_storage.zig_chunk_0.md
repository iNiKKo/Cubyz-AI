# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 0

**Type:** implementation
**Keywords:** atomic operations, memory pool, concurrent queue, chunk storage, node retrieval
**Symbols:** ChunkMeshNode, storageSize, storageMask, storageLists, mapStorageLists, meshList, priorityMeshUpdateList, updatableList, mapUpdatableList, lastPx, lastPy, lastPz, lastRD, mutex, BlockUpdate, meshMemoryPool
**Concepts:** chunk meshing, memory management, concurrency control

## Summary
Manages chunk mesh storage and updates, including initialization, deinitialization, and node retrieval.

## Explanation
This chunk defines the structure and logic for managing chunk mesh storage in the Cubyz voxel engine. It includes functions for initializing and deinitializing mesh storage, retrieving nodes based on positions, and updating higher LOD nodes' meshing status. The chunk uses atomic operations to manage concurrent access to mesh data and employs a memory pool for efficient allocation of chunk meshes.

The `ChunkMeshNode` structure is defined as follows:
```zig
const ChunkMeshNode = struct {
    mesh: Atomic(?*chunk_meshing.ChunkMesh) = .init(null),
    active: bool = false,
    rendered: bool = false,
    finishedMeshing: bool = false, // Must be synced with mesh.finishedMeshing
    finishedMeshingHigherResolution: u8 = 0, // Must be synced with finishedMeshing of the 8 higher resolution chunks.
    pos: chunk.ChunkPosition = undefined,
    isNeighborLod: [6]bool = @splat(false), // Must be synced with mesh.isNeighborLod
};
```
The `storageLists` array is used to store `ChunkMeshNode` instances for different levels of detail (LOD). Each element in the array corresponds to a specific LOD level, and it contains a 3D array of `ChunkMeshNode` instances.

The `getNodePointer` function retrieves a pointer to a `ChunkMeshNode` based on a given chunk position. It calculates the index into the appropriate storage list using the chunk's world coordinates and LOD level.

The `meshMemoryPool` is used for efficient allocation of `ChunkMesh` instances, reducing memory fragmentation and improving performance.

Higher LOD nodes' meshing statuses are updated by the `updateHigherLodNodeFinishedMeshing` function. This function updates the `finishedMeshingHigherResolution` field of a higher LOD node based on the status of its corresponding lower LOD nodes.

During the initialization of mesh storage, various lists and arrays are created and initialized. The `storageLists` array is populated with 3D arrays of `ChunkMeshNode` instances, and the `mapStorageLists` array is populated with atomic pointers to `LightMap.LightMapFragment` instances. Additionally, concurrent queues for priority updates and map updates are initialized.

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
