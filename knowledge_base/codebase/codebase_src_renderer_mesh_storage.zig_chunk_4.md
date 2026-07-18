# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 4

**Type:** implementation
**Keywords:** frustum, networking, meshing, LOD, breadth-first search, mutex locking
**Symbols:** updateAndGetRenderChunks, meshList, playerPosInt, meshRequests, mapRequests, olderPx, olderPy, olderPz, olderRD, mutex, lastPx, lastPy, lastPz, lastRD, freeOldMeshes, createNewMeshes, searchList, firstPos, lod, getNodePointer, node, hasMesh, relPos, chunkSizeVector, neighbor, component, neighborPos, node2, relPosFloat, frustum, testAAB, lowerLodBit, startPos, nextPos, relNextPos, isNeighborLod, nodeList, mesh, uploadData, isEmpty
**Concepts:** chunk meshing, frustum culling, network requests, LOD management

## Summary
Handles updating and retrieving render chunks based on player position and frustum.

## Explanation
The `updateAndGetRenderChunks` function manages the process of updating and fetching renderable chunks for rendering. It starts by clearing the existing mesh list and preparing to handle new requests. The function updates the last known player position and render distance, then frees old meshes that are no longer needed. New meshes are requested from the network, and a breadth-first search is performed to find visible chunks within the frustum. Nodes representing these chunks are processed, checking their visibility and LOD (Level of Detail) status. The function ensures that only relevant chunks are marked for rendering and uploaded to the GPU. Finally, it returns the list of meshes ready for rendering.

## Code Example
```zig
fn updateAndGetRenderChunks(conn: *network.Connection, frustum: *const main.renderer.Frustum, playerPos: Vec3d, renderDistance: u16) []*chunk_meshing.ChunkMesh { // MARK: updateAndGetRenderChunks()
	meshList.clearRetainingCapacity();

	const playerPosInt: Vec3i = @floor(playerPos);

	var meshRequests: main.ListManaged(chunk.ChunkPosition) = .init(main.stackAllocator);
	defer meshRequests.deinit();
	var mapRequests: main.ListManaged(LightMap.MapFragmentPosition) = .init(main.stackAllocator);
	defer mapRequests.deinit();

	const olderPx = lastPx;
	const olderPy = lastPy;
	const olderPz = lastPz;
	const olderRD = lastRD;
	mutex.lock();
	lastPx = @trunc(playerPos[0]);
	lastPy = @trunc(playerPos[1]);
	lastPz = @trunc(playerPos[2]);
	lastRD = renderDistance;
	mutex.unlock();
	freeOldMeshes(olderPx, olderPy, olderPz, olderRD);

	createNewMeshes(olderPx, olderPy, olderPz, olderRD, &meshRequests, &mapRequests);

	// Make requests as soon as possible to reduce latency:
	network.protocols.lightMapRequest.sendRequest(conn, mapRequests.items);
	network.protocols.chunkRequest.sendRequest(conn, meshRequests.items, .{lastPx, lastPy, lastPz}, lastRD);

	// Finds all visible chunks and lod chunks using a breadth-first hierarchical search.

	var searchList = main.utils.CircularBufferQueue(*ChunkMeshNode).init(main.stackAllocator, 1024);
	defer searchList.deinit();
	{
		var firstPos = chunk.ChunkPosition{
			.wx = playerPosInt[0],
			.wy = playerPosInt[1],
			.wz = playerPosInt[2],
			.voxelSize = 1,
		};
		const lod: u3 = settings.highestLod;
		firstPos.wx &= ~@as(i32, chunk.chunkMask << lod | (@as(i32, 1) << lod) - 1);
		firstPos.wy &= ~@as(i32, chunk.chunkMask << lod | (@as(i32, 1) << lod) - 1);
		firstPos.wz &= ~@as(i32, chunk.chunkMask << lod | (@as(i32, 1) << lod) - 1);
		firstPos.voxelSize <<= lod;
		const node = getNodePointer(firstPos);
		const hasMesh = node.finishedMeshing;
		if (hasMesh) {
			node.active = true;
			node.rendered = true;
			searchList.pushBack(node);
		}
	}
	var nodeList: main.ListManaged(*ChunkMeshNode) = .initCapacity(main.stackAllocator, 1024);
	defer nodeList.deinit();
	while (searchList.popFront()) |node| {
		std.debug.assert(node.finishedMeshing);
		std.debug.assert(node.active);
		if (!node.active) continue;
		node.active = false;

		const pos = node.pos;

		const relPos: Vec3i = Vec3i{pos.wx, pos.wy, pos.wz} - playerPosInt;

		const chunkSizeVector: Vec3i = @splat(chunk.chunkSize*pos.voxelSize);

		if (pos.voxelSize == @as(i32, 1) << settings.highestLod) {
			for (chunk.Neighbor.iterable) |neighbor| {
				const component = neighbor.extractDirectionComponent(relPos);
				if (neighbor.isPositive() and component + chunk.chunkSize*pos.voxelSize <= 0) continue;
				if (!neighbor.isPositive() and component > 0) continue;
				const neighborPos = chunk.ChunkPosition{
					.wx = pos.wx +% neighbor.relX()*chunk.chunkSize*pos.voxelSize,
					.wy = pos.wy +% neighbor.relY()*chunk.chunkSize*pos.voxelSize,
					.wz = pos.wz +% neighbor.relZ()*chunk.chunkSize*pos.voxelSize,
					.voxelSize = pos.voxelSize,
				};
				const node2 = getNodePointer(neighborPos);
				if (!node2.active and node2.finishedMeshing) {
					const relPosFloat: Vec3f = @floatCast(@as(Vec3d, @floatFromInt(Vec3i{pos.wx, pos.wy, pos.wz})) - playerPos);
					if (!frustum.testAAB(relPosFloat + @as(Vec3f, @floatFromInt(neighbor.relPos()*chunkSizeVector)), @floatFromInt(chunkSizeVector))) continue;
					node2.active = true;
					node2.rendered = true;
					searchList.pushBack(node2);
				}
			}
		}

		if (node.finishedMeshingHigherResolution == 0xff) {
			node.rendered = false;
			const lowerLodBit: i32 = pos.voxelSize*chunk.chunkSize >> 1;
			const startPos: chunk.ChunkPosition = .{
				.wx = pos.wx | if ((pos.wx | lowerLodBit) -% playerPosInt[0] > 0) lowerLodBit else 0,
				.wy = pos.wy | if ((pos.wy | lowerLodBit) -% playerPosInt[1] > 0) lowerLodBit else 0,
				.wz = pos.wz | if ((pos.wz | lowerLodBit) -% playerPosInt[2] > 0) lowerLodBit else 0,
				.voxelSize = pos.voxelSize >> 1,
			};
			for (0..2) |dx| {
				for (0..2) |dy| {
					for (0..2) |dz| {
						var nextPos = startPos;
						if (dx == 1) nextPos.wx ^= lowerLodBit;
						if (dy == 1) nextPos.wy ^= lowerLodBit;
						if (dz == 1) nextPos.wz ^= lowerLodBit;
						const node2 = getNodePointer(nextPos);
						const relNextPos: Vec3d = @as(Vec3d, @floatFromInt(Vec3i{nextPos.wx, nextPos.wy, nextPos.wz})) - playerPos;
						if (!frustum.testAAB(@floatCast(relNextPos), @floatFromInt(chunkSizeVector))) continue;
						std.debug.assert(node2.finishedMeshing);
						node2.active = true;
						node2.rendered = true;
						searchList.pushFront(node2);
					}
				}
			}
		} else {
			nodeList.append(node);
		}
	}
	for (nodeList.items) |node| {
		const pos = node.pos;
		var isNeighborLod: [6]bool = @splat(false);
		if (pos.voxelSize != @as(i32, 1) << settings.highestLod) {
			for (chunk.Neighbor.iterable) |neighbor| {
				var neighborPos = chunk.ChunkPosition{
					.wx = pos.wx +% neighbor.relX()*chunk.chunkSize*pos.voxelSize,
					.wy = pos.wy +% neighbor.relY()*chunk.chunkSize*pos.voxelSize,
					.wz = pos.wz +% neighbor.relZ()*chunk.chunkSize*pos.voxelSize,
					.voxelSize = pos.voxelSize,
				};
				neighborPos.wx &= ~@as(i32, neighborPos.voxelSize*chunk.chunkSize);
				neighborPos.wy &= ~@as(i32, neighborPos.voxelSize*chunk.chunkSize);
				neighborPos.wz &= ~@as(i32, neighborPos.voxelSize*chunk.chunkSize);
				neighborPos.voxelSize *= 2;
				const node2 = getNodePointer(neighborPos);
				isNeighborLod[neighbor.toInt()] = node2.finishedMeshingHigherResolution != 0xff;
			}
		}
		if (!std.meta.eql(node.isNeighborLod, isNeighborLod)) {
			const mesh = node.mesh.load(.acquire).?; // no other thread is allowed to overwrite the mesh (unless it's null).
			mesh.isNeighborLod = isNeighborLod;
			node.isNeighborLod = isNeighborLod;
			mesh.uploadData();
		}
	}
	for (nodeList.items) |node| {
		node.rendered = false;
		if (!node.finishedMeshing) continue;

		const mesh = node.mesh.load(.acquire).?; // no other thread is allowed to overwrite the mesh (unless it's null).

		if (mesh.needsMeshUpdate) {
			mesh.needsMeshUpdate = false;
			mesh.uploadData();
		}
		// Remove empty meshes.
		if (!mesh.isEmpty()) {
			meshList.append(main.globalAllocator, mesh);
		}
	}

	return meshList.items;
}
```

## Related Questions
- What is the purpose of the `updateAndGetRenderChunks` function?
- How does the function handle network requests for mesh and light map data?
- What mechanism ensures that only visible chunks are marked for rendering?
- How does the function manage LOD (Level of Detail) transitions between chunks?
- What role does the mutex play in this function?
- How is the frustum used to cull non-visible chunks?
- What steps are taken to free old meshes and create new ones?
- How does the function ensure that only relevant chunks are uploaded to the GPU?
- What data structures are used to manage mesh requests and search lists?
- How does the function handle empty meshes?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_4*
