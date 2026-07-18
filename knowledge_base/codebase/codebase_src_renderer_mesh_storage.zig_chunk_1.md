# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 1

**Type:** api
**Keywords:** atomic operations, level of detail (LOD), chunk meshing, world coordinates, render thread
**Symbols:** getMapPiecePointer, getLightMapPiece, getBlockFromRenderThread, getLight, getBlockFromAnyLodFromRenderThread, getMesh, getMeshFromAnyLod, getNeighbor, reduceRenderDistance, isInRenderDistance, isMapInRenderDistance
**Concepts:** mesh storage, lighting data, block retrieval, render distance checks

## Summary
This chunk provides functions for accessing and managing mesh storage, including retrieving light maps, blocks, and meshes at various levels of detail.

## Explanation
The chunk defines several functions to interact with the mesh storage system. `getMapPiecePointer` calculates a pointer to a light map fragment based on coordinates and voxel size. `getLightMapPiece` loads the light map fragment from the calculated pointer. `getBlockFromRenderThread` retrieves a block from a specific position in the render thread. `getLight` fetches lighting data for a given world coordinate. `getBlockFromAnyLodFromRenderThread` searches through different levels of detail to find a block. `getMesh` retrieves a chunk mesh based on its position and voxel size, ensuring it matches the expected position. `getMeshFromAnyLod` attempts to find a mesh at any level of detail up to the highest LOD. `getNeighbor` fetches a neighboring chunk mesh based on relative coordinates. `reduceRenderDistance` calculates a reduced render distance considering a reduction factor. `isInRenderDistance` checks if a chunk position is within the current render distance. `isMapInRenderDistance` performs a similar check for light map fragments.

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
