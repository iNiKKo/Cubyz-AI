# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 3

**Type:** implementation
**Keywords:** mesh generation, render distance calculation, LOD management, chunk position iteration, mesh request handling
**Symbols:** createNewMeshes, reduceRenderDistance
**Concepts:** chunk meshing, level of detail (LOD)

## Summary
Handles the creation and management of new meshes based on LOD changes.

## Explanation
The `createNewMeshes` function manages the creation and updating of mesh data for chunks in a voxel engine. It calculates the render distances for different levels of detail (LOD) and determines which chunks need to be updated or requested. The function iterates over potential chunk positions, checks their distances from the player's current position, and updates the mesh storage accordingly. If a mesh is not available, it adds the request to `meshRequests`. Similarly, it handles light map fragment requests by iterating over potential positions and updating the light map storage.

## Code Example
```zig
fn createNewMeshes(olderPx: i32, olderPy: i32, olderPz: i32, olderRD: u16, meshRequests: *main.ListManaged(chunk.ChunkPosition), mapRequests: *main.ListManaged(LightMap.MapFragmentPosition)) void { // MARK: createNewMeshes()
	for (0..settings.highestLod + 1) |_lod| {
		const lod: u5 = @intCast(_lod);
		const maxRenderDistanceNew = lastRD*chunk.chunkSize << lod;
		const maxRenderDistanceOld = olderRD*chunk.chunkSize << lod;
		const size: u31 = chunk.chunkSize << lod;
		const mask: i32 = size - 1;
		const invMask: i32 = ~mask;

		std.debug.assert(@divFloor(2*maxRenderDistanceNew + size - 1, size) + 2 <= storageSize);

		const minX = lastPx -% maxRenderDistanceNew & invMask;
		const maxX = lastPx +% maxRenderDistanceNew +% size & invMask;
		var x = minX;
		while (x != maxX) : (x +%= size) {
			const xIndex = @divExact(x, size) & storageMask;
			var deltaXNew: i64 = @abs(x +% size/2 -% lastPx);
			deltaXNew = @max(0, deltaXNew - size/2);
			var deltaXOld: i64 = @abs(x +% size/2 -% olderPx);
			deltaXOld = @max(0, deltaXOld - size/2);
			const maxYRenderDistanceNew: i32 = reduceRenderDistance(maxRenderDistanceNew, deltaXNew);
			const maxYRenderDistanceOld: i32 = reduceRenderDistance(maxRenderDistanceOld, deltaXOld);

			const minY = lastPy -% maxYRenderDistanceNew & invMask;
			const maxY = lastPy +% maxYRenderDistanceNew +% size & invMask;
			var y = minY;
			while (y != maxY) : (y +%= size) {
				const yIndex = @divExact(y, size) & storageMask;
				var deltaYOld: i64 = @abs(y +% size/2 -% olderPy);
				deltaYOld = @max(0, deltaYOld - size/2);
				var deltaYNew: i64 = @abs(y +% size/2 -% lastPy);
				deltaYNew = @max(0, deltaYNew - size/2);
				var maxZRenderDistanceNew: i32 = reduceRenderDistance(maxYRenderDistanceNew, deltaYNew);
				if (maxZRenderDistanceNew == 0) maxZRenderDistanceNew -= size/2;
				var maxZRenderDistanceOld: i32 = reduceRenderDistance(maxYRenderDistanceOld, deltaYOld);
				if (maxZRenderDistanceOld == 0) maxZRenderDistanceOld -= size/2;

				const minZOld = olderPz -% maxZRenderDistanceOld & invMask;
				const maxZOld = olderPz +% maxZRenderDistanceOld +% size & invMask;
				const minZNew = lastPz -% maxZRenderDistanceNew & invMask;
				const maxZNew = lastPz +% maxZRenderDistanceNew +% size & invMask;

				var zValues: [storageSize]i32 = undefined;
				var zValuesLen: usize = 0;
				if (minZOld -% minZNew > 0) {
					var z = minZNew;
					while (z != minZOld and z != maxZNew) : (z +%= size) {
						zValues[zValuesLen] = z;
						zValuesLen += 1;
					}
				}
				if (maxZNew -% maxZOld > 0) {
					var z = minZNew +% @max(0, maxZOld -% minZNew);
					while (z != maxZNew) : (z +%= size) {
						zValues[zValuesLen] = z;
						zValuesLen += 1;
					}
				}

				for (zValues[0..zValuesLen]) |z| {
					const zIndex = @divExact(z, size) & storageMask;
					const index = (xIndex*storageSize + yIndex)*storageSize + zIndex;
					const pos = chunk.ChunkPosition{.wx = x, .wy = y, .wz = z, .voxelSize = @as(u31, 1) << lod};

					const node = &storageLists[_lod][@intCast(index)];
					node.pos = pos;
					if (node.mesh.load(.acquire)) |mesh| {
						std.debug.assert(std.meta.eql(pos, mesh.pos));
					} else {
						meshRequests.append(pos);
					}
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

		const minX = lastPx -% maxRenderDistanceNew & invMask;
		const maxX = lastPx +% maxRenderDistanceNew +% size & invMask;
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
			if (minYOld -% minYNew > 0) {
				var y = minYNew;
				while (y != minYOld and y != maxYNew) : (y +%= size) {
					yValues[yValuesLen] = y;
					yValuesLen += 1;
				}
			}
			if (maxYNew -% maxYOld > 0) {
				var y = minYNew +% @max(0, maxYOld -% minYNew);
				while (y != maxYNew) : (y +%= size) {
					yValues[yValuesLen] = y;
					yValuesLen += 1;
				}
			}

			for (yValues[0..yValuesLen]) |y| {
				const yIndex = @divExact(y, size) & storageMask;
				const index = xIndex*storageSize + yIndex;
				const pos = LightMap.MapFragmentPosition{.wx = x, .wy = y, .voxelSize = @as(u31, 1) << lod, .voxelSizeShift = lod};

				const map = mapStorageLists[_lod][@intCast(index)].load(.monotonic);
				if (map) |_map| {
					std.debug.assert(std.meta.eql(pos, _map.pos));
				} else {
					mapRequests.append(pos);
				}
			}
		}
	}
}
```

## Related Questions
- How does the function handle LOD changes in chunk meshing?
- What is the purpose of the `reduceRenderDistance` function in this context?
- How are mesh requests managed and appended during the execution of this function?
- Can you explain the logic behind calculating render distances for different LOD levels?
- What role does the `storageLists` array play in this implementation?
- How is the light map fragment handling integrated into the same function?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_3*
