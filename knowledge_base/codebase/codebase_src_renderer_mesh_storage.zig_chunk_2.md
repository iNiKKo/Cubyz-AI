# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 2

**Type:** implementation
**Keywords:** render distance, mesh management, LOD handling, memory freeing, position checking
**Symbols:** deltaY, maxZRenderDistance, minZ, maxZ, isMapInRenderDistance, pos, maxRenderDistance, size, mask, invMask, minX, maxX, deltaX, maxYRenderDistance, minY, maxY, freeOldMeshes, olderPx, olderPy, olderPz, olderRD, _lod, lod, maxRenderDistanceNew, maxRenderDistanceOld, storageSize, xIndex, deltaXNew, deltaXOld, maxYRenderDistanceNew, maxYRenderDistanceOld, minZOld, maxZOld, minZNew, maxZNew, zValues, zValuesLen, zIndex, index, node, oldMesh, mesh, updateHigherLodNodeFinishedMeshing, isNeighborLod
**Concepts:** mesh storage, render distance checking, level of detail (LOD), memory management

## Summary
Handles mesh storage and management, including checking render distances and freeing old meshes.

## Explanation
This chunk contains functions for managing mesh storage in the Cubyz voxel engine. It includes logic to determine if a map fragment is within render distance (`isMapInRenderDistance`) and to free old meshes that are no longer needed (`freeOldMeshes`). The `isMapInRenderDistance` function calculates whether a given position is within the maximum render distance, considering various dimensions and positions. The `freeOldMeshes` function iterates through different levels of detail (LOD) and frees mesh data that is outside the new render distance, updating storage lists and handling deferred deinitialization of old meshes.

## Code Example
```zig
fn isMapInRenderDistance(pos: LightMap.MapFragmentPosition) bool {
	const maxRenderDistance = lastRD*chunk.chunkSize*pos.voxelSize;
	const size: u31 = @as(u31, LightMap.LightMapFragment.mapSize)*pos.voxelSize;
	const mask: i32 = size - 1;
	const invMask: i32 = ~mask;

	const minX = lastPx -% maxRenderDistance & invMask;
	const maxX = lastPx +% maxRenderDistance +% size & invMask;
	if (pos.wx -% minX < 0) return false;
	if (pos.wx -% maxX >= 0) return false;
	var deltaX: i64 = @abs(pos.wx +% size/2 -% lastPx);
	deltaX = @max(0, deltaX - size/2);

	const maxYRenderDistance: i32 = reduceRenderDistance(maxRenderDistance, deltaX);
	if (maxYRenderDistance == 0) return false;
	const minY = lastPy -% maxYRenderDistance & invMask;
	const maxY = lastPy +% maxYRenderDistance +% size & invMask;
	if (pos.wy -% minY < 0) return false;
	if (pos.wy -% maxY >= 0) return false;
	return true;
}
```

## Related Questions
- What is the purpose of the `isMapInRenderDistance` function?
- How does the `freeOldMeshes` function determine which meshes to free?
- What role do LODs play in mesh storage management?
- How is render distance calculated for a map fragment?
- What happens to old meshes that are outside the new render distance?
- How is memory managed when freeing old meshes?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_2*
