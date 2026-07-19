# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 1

**Type:** api
**Keywords:** atomic operations, level of detail (LOD), chunk meshing, world coordinates, render thread
**Symbols:** getMapPiecePointer, getLightMapPiece, getBlockFromRenderThread, getLight, getBlockFromAnyLodFromRenderThread, getMesh, getMeshFromAnyLod, getNeighbor, reduceRenderDistance, isInRenderDistance, isMapInRenderDistance
**Concepts:** mesh storage, lighting data, block retrieval, render distance checks

## Summary
This chunk provides functions for accessing and managing mesh storage, including retrieving light maps, blocks, and meshes at various levels of detail.

## Explanation
This chunk provides functions for accessing and managing mesh storage, including retrieving light maps, blocks, and meshes at various levels of detail. The chunk defines several functions to interact with the mesh storage system.

- **`getMapPiecePointer`**: Calculates a pointer to a light map fragment based on coordinates and voxel size. It computes the level of detail (LOD) using `std.math.log2_int(u31, voxelSize)` and then calculates the index by shifting the coordinates right by the sum of LOD and `LightMap.LightMapFragment.mapShift`. The indices are masked with `storageMask` to ensure they fit within bounds. Finally, it returns a pointer to the light map fragment from `mapStorageLists[lod]` at the calculated index.

- **`getLightMapPiece`**: Loads the light map fragment from the pointer returned by `getMapPiecePointer`. It uses an atomic load operation with `.acquire` ordering to ensure memory consistency.

- **`getBlockFromRenderThread`**: Retrieves a block from a specific position in the render thread. It first gets a node pointer using `getNodePointer`, then loads the mesh with `.acquire` ordering. If the mesh is null, it returns null. Otherwise, it retrieves the block from the mesh's chunk at the specified local coordinates.

- **`getLight`**: Fetches lighting data for a given world coordinate. It gets a node pointer and loads the mesh with `.acquire` ordering. If the mesh is null, it returns null. It then calculates the block position using `fromWorldCoords` and retrieves the lighting data from `mesh.lightingData[1]` and `mesh.lightingData[0]`, concatenating them into a single array.

- **`getBlockFromAnyLodFromRenderThread`**: Searches through different levels of detail to find a block. It iterates from LOD 0 up to `settings.highestLod`. For each LOD, it calculates the node pointer and loads the mesh with `.acquire` ordering. If the mesh is null, it continues to the next LOD. Otherwise, it retrieves the block from the mesh's chunk at the specified local coordinates.

- **`getMesh`**: Retrieves a chunk mesh based on its position and voxel size, ensuring it matches the expected position. It calculates the LOD using `std.math.log2_int(u31, pos.voxelSize)` and creates a mask to align the world coordinates with the chunk boundaries. It then gets the node pointer and loads the mesh with `.acquire` ordering. If the mesh's position does not match the expected position, it returns null.

- **`getMeshFromAnyLod`**: Attempts to find a mesh at any level of detail up to the highest LOD. It iterates from the current LOD down to 0. For each LOD, it calculates the node pointer and loads the mesh with `.acquire` ordering. If the mesh is null, it continues to the next LOD.

- **`getNeighbor`**: Fetches a neighboring chunk mesh based on relative coordinates. It adjusts the world coordinates by adding the product of the voxel size, chunk size, and relative coordinates for each axis. It then retrieves the mesh using `getMesh` with the adjusted position.

- **`reduceRenderDistance`**: Calculates a reduced render distance considering a reduction factor. It computes the square of the full render distance minus the reduction squared, takes the square root, and rounds up to ensure the result is an integer.

- **`isInRenderDistance`**: Checks if a chunk position is within the current render distance. It calculates the maximum render distance based on `lastRD`, chunk size, and voxel size. It then checks if the world coordinates are within the calculated bounds for each axis, adjusting for the chunk size and position.

- **`isMapInRenderDistance`**: Performs a similar check for light map fragments. It calculates the maximum render distance and checks if the fragment's world coordinates are within the calculated bounds.

## Code Example
```zig
fn getMapPiecePointer(x: i32, y: i32, voxelSize: u31) *Atomic(?*LightMap.LightMapFragment) {
	const lod = std.math.log2_int(u31, voxelSize);
	var xIndex = x >> lod + LightMap.LightMapFragment.mapShift;
	var yIndex = y >> lod + LightMap.LightMapFragment.mapShift;
	xIndex &= storageMask;
	yIndex &= storageMask;
	const index = xIndex*storageSize + yIndex;
	return &mapStorageLists[lod][@intCast(index)];
}
```

## Related Questions
- How does `getMapPiecePointer` calculate the LOD?
- What is the purpose of the `reduceRenderDistance` function?
- How does `getBlockFromAnyLodFromRenderThread` search for a block?
- What atomic operation is used in `getLightMapPiece`?
- How does `isInRenderDistance` determine if a chunk is within render distance?
- What is the role of `getNeighbor` in fetching neighboring meshes?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_1*
