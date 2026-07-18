# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 2

**Type:** implementation
**Keywords:** mesh storage, player position, render distance, memory management, deferred deinitialization
**Symbols:** freeOldMeshes
**Concepts:** mesh management, level of detail (LOD)

## Summary
The chunk manages the freeing of old mesh data based on new and old player positions and render distances.

## Explanation
The `freeOldMeshes` function iterates over different levels of detail (LOD) to determine which mesh data needs to be freed. It calculates the maximum render distance for both the current and previous player positions, then determines the range of x, y, and z coordinates that need to be checked. For each coordinate within this range, it checks if the corresponding mesh or light map fragment should be freed. If a mesh is found, it swaps it out with `null`, marks the node as not finished meshing, and defers its deinitialization. The same process is applied to light map fragments.

## Code Example
```zig
fn freeOldMeshes(olderPx: i32, olderPy: i32, olderPz: i32, olderRD: u16) void { // MARK: freeOldMeshes()
	for (0..settings.highestLod + 1) |_lod| {
		const lod: u5 = @intCast(_lod);
		const maxRenderDistanceNew = lastRD*chunk.chunkSize << lod;
		const maxRenderDistanceOld = olderRD*chunk.chunkSize << lod;
		const size: u31 = chunk.chunkSize << lod;
		const mask: i32 = size - 1;
		const invMask: i32 = ~mask;

		std.debug.assert(@divFloor(2*maxRenderDistanceNew + size - 1, size) + 2 <= storageSize);

		const minX = olderPx -% maxRenderDistanceOld & invMask;
		const maxX = olderPx +% maxRenderDistanceOld +% size & invMask;
		var x = minX;
		while (x != maxX) : (x +%= size) {
			const xIndex = @divExact(x, size) & storageMask;
			var deltaXNew: i64 = @abs(x +% size/2 -% lastPx);
			deltaXNew = @max(0, deltaXNew - size/2);
			var deltaXOld: i64 = @abs(x +% size/2 -% olderPx);
			deltaXOld = @max(0, deltaXOld - size/2);
			const maxYRenderDistanceNew: i32 = reduceRenderDistance(maxRenderDistanceNew, deltaXNew);
			const maxYRenderDistanceOld: i32 = reduceRenderDistance(maxRenderDistanceOld, deltaXOld);

			const minY = olderPy -% maxYRenderDistanceOld & invMask;
			const maxY = olderPy +% maxYRenderDistanceOld +% size & invMask;
			var y = minY;
			while (y != maxY) : (y +%= size) {
				const yIndex = @divExact(y, size) & storageMask;
				var deltaYOld: i64 = @abs(y +% size/2 -% olderPy);
				deltaYOld = @max(0, deltaYOld - size/2);
				var deltaYNew: i64 = @abs(y +% size/2 -% lastPy);
				deltaYNew = @max(0, deltaYNew - size/2);
				var maxZRenderDistanceOld: i32 = reduceRenderDistance(maxYRenderDistanceOld, deltaYOld);
				if (maxZRenderDistanceOld == 0) maxZRenderDistanceOld -= size/2;
				var maxZRenderDistanceNew: i32 = reduceRenderDistance(maxYRenderDistanceNew, deltaYNew);
				if (maxZRenderDistanceNew == 0) maxZRenderDistanceNew -= size/2;

				const minZOld = olderPz -% maxZRenderDistanceOld & invMask;
				const maxZOld = olderPz +% maxZRenderDistanceOld +% size & invMask;
				const minZNew = lastPz -% maxZRenderDistanceNew & invMask;
				const maxZNew = lastPz +% maxZRenderDistanceNew +% size & invMask;

				var zValues: [storageSize]i32 = undefined;
				var zValuesLen: usize = 0;
				if (minZNew -% minZOld > 0) {
					var z = minZOld;
					while (z != minZNew and z != maxZOld) : (z +%= size) {
						zValues[zValuesLen] = z;
						zValuesLen += 1;
					}
				}
				if (maxZOld -% maxZNew > 0) {
					var z = minZOld +% @max(0, maxZNew -% minZOld);
					while (z != maxZOld) : (z +%= size) {
						zValues[zValuesLen] = z;
						zValuesLen += 1;
					}
				}

				for (zValues[0..zValuesLen]) |z| {
					const zIndex = @divExact(z, size) & storageMask;
					const index = (xIndex*storageSize + yIndex)*storageSize + zIndex;

					const node = &storageLists[_lod][@intCast(index)];
					const oldMesh = node.mesh.swap(null, .monotonic);
					node.pos = undefined;
					if (oldMesh) |mesh| {
						node.finishedMeshing = false;
						updateHigherLodNodeFinishedMeshing(mesh.pos, false);
						mesh.deferredDeinit();
					}
					node.isNeighborLod = @splat(false);
				}
			}
		}
	}
	for (0..settings.highestLod + 1) |_lod| {
		const lod: u5 = @intCast(_lod);
		const maxRenderDistanceNew = lastRD*chunk.chunkSize << lod;
		const maxRenderDistanceOld = olderRD*chunk.chunkSize << lod;
		const size: u31 = @as(u31, LightMap.LightMapFragment.mapSize) << lod;
		const mask: i32 = size - 1;
		const invMask: i32 = ~mask;

		std.debug.assert(@divFloor(2*maxRenderDistanceNew + size - 1, size) + 2 <= storageSize);

		const minX = olderPx -% maxRenderDistanceOld & invMask;
		const maxX = olderPx +% maxRenderDistanceOld +% size & invMask;
		var x = minX;
		while (x != maxX) : (x +%= size) {
			const xIndex = @divExact(x, size) & storageMask;
			var deltaXNew: i64 = @abs(x +% size/2 -% lastPx);
			deltaXNew = @max(0, deltaXNew - size/2);
			var deltaXOld: i64 = @abs(x +% size/2 -% olderPx);
			deltaXOld = @max(0, deltaXOld - size/2);
			var maxYRenderDistanceNew: i32 = reduceRenderDistance(maxRenderDistanceNew, deltaXNew);
			if (maxYRenderDistanceNew == 0) maxYRenderDistanceNew -= size/2;
			var maxYRenderDistanceOld: i32 = reduceRenderDistance(maxRenderDistanceOld, deltaXOld);
			if (maxYRenderDistanceOld == 0) maxYRenderDistanceOld -= size/2;

			const minYOld = olderPy -% maxYRenderDistanceOld & invMask;
			const maxYOld = olderPy +% maxYRenderDistanceOld +% size & invMask;
			const minYNew = lastPy -% maxYRenderDistanceNew & invMask;
			const maxYNew = lastPy +% maxYRenderDistanceNew +% size & invMask;

			var yValues: [storageSize]i32 = undefined;
			var yValuesLen: usize = 0;
			if (minYNew -% minYOld > 0) {
				var y = minYOld;
				while (y != minYNew and y != maxYOld) : (y +%= size) {
					yValues[yValuesLen] = y;
					yValuesLen += 1;
				}
			}
			if (maxYOld -% maxYNew > 0) {
				var y = minYOld +% @max(0, maxYNew -% minYOld);
				while (y != maxYOld) : (y +%= size) {
					yValues[yValuesLen] = y;
					yValuesLen += 1;
				}
			}

			for (yValues[0..yValuesLen]) |y| {
				const yIndex = @divExact(y, size) & storageMask;
				const index = xIndex*storageSize + yIndex;

				const oldMap = mapStorageLists[_lod][@intCast(index)].swap(null, .monotonic);
				if (oldMap) |map| {
					map.deferredDeinit();
				}
			}
		}
	}
}
```

## Related Questions
- What is the purpose of the `freeOldMeshes` function?
- How does the function determine which mesh data to free?
- What happens to a mesh when it is freed?
- How are light map fragments managed in this chunk?
- What is the role of LOD (Level of Detail) in this implementation?
- How does the function handle memory management for old meshes?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_2*
