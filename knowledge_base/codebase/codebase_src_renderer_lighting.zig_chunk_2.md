# [hard/codebase_src_renderer_lighting.zig] - Chunk 2

**Type:** implementation
**Keywords:** mutex locking, circular buffer queue, light value updates, neighbor checks, thread safety
**Symbols:** propagateDestructive, propagateFromNeighbor, propagateDestructiveFromNeighbor, propagateLights
**Concepts:** lighting propagation, thread safety, queue processing, neighbor interactions

## Summary
Handles lighting propagation within a chunk, including destructive and constructive updates.

## Explanation
The code defines functions for propagating light changes within a chunk. `propagateDestructive` processes entries in a queue to update light values and handle neighbor interactions. It uses mutex locking to ensure thread safety. `propagateFromNeighbor` and `propagateDestructiveFromNeighbor` handle light propagation from neighboring chunks. `propagateLights` initializes the process by setting up a queue with initial light positions and optionally checking neighbors for further propagation.

## Code Example
```zig
fn propagateDestructive(self: *ChannelChunk, lightQueue: *main.utils.CircularBufferQueue(Entry), constructiveEntries: *main.List(ChunkEntries), isFirstBlock: bool, lightRefreshList: *main.ListManaged(chunk.ChunkPosition)) main.List(BlockPos) {
		var neighborLists: [6]main.List(Entry) = @splat(.empty);
		var constructiveList: main.List(BlockPos) = .empty;
		defer {
			for (&neighborLists) |*list| {
				list.deinit(main.stackAllocator);
			}
		}
		var isFirstIteration: bool = isFirstBlock;

		self.mutex.lock();
		while (lightQueue.popFront()) |entry| {
			const pos: BlockPos = entry.pos;
			const oldValue: [3]u8 = self.data.getValue(pos.toIndex()).toArray();
			var activeValue: @Vector(3, bool) = @bitCast(entry.activeValue);
			var append: bool = false;
			if (activeValue[0] and entry.value[0] != oldValue[0]) {
				if (oldValue[0] != 0) append = true;
				activeValue[0] = false;
			}
			if (activeValue[1] and entry.value[1] != oldValue[1]) {
				if (oldValue[1] != 0) append = true;
				activeValue[1] = false;
			}
			if (activeValue[2] and entry.value[2] != oldValue[2]) {
				if (oldValue[2] != 0) append = true;
				activeValue[2] = false;
			}
			const blockLight = if (self.isSun) .{0, 0, 0} else extractColor(self.ch.data.getValue(pos.toIndex()).light());
			if ((activeValue[0] and blockLight[0] != 0) or (activeValue[1] and blockLight[1] != 0) or (activeValue[2] and blockLight[2] != 0)) {
				append = true;
			}
			if (append) {
				constructiveList.append(main.stackAllocator, pos);
			}
			if (entry.value[0] == 0) activeValue[0] = false;
			if (entry.value[1] == 0) activeValue[1] = false;
			if (entry.value[2] == 0) activeValue[2] = false;
			if (isFirstIteration) activeValue = .{true, true, true};
			if (!@reduce(.Or, activeValue)) {
				continue;
			}
			isFirstIteration = false;
			var insertValue: [3]u8 = oldValue;
			if (activeValue[0]) insertValue[0] = 0;
			if (activeValue[1]) insertValue[1] = 0;
			if (activeValue[2]) insertValue[2] = 0;
			self.data.setValue(pos.toIndex(), .fromArray(insertValue));
			for (chunk.Neighbor.iterable) |neighbor| {
				if (neighbor.toInt() == entry.sourceDir) continue;
				const neighborPos, const chunkLocation = pos.neighbor(neighbor);
				var result: Entry = .{.pos = neighborPos, .value = entry.value, .sourceDir = neighbor.reverse().toInt(), .activeValue = @bitCast(activeValue)};
				if (!self.isSun or neighbor != .dirDown or result.value[0] != 255 or result.value[1] != 255 or result.value[2] != 255) {
					result.value[0] -|= 8*|@as(u8, @intCast(self.ch.pos.voxelSize));
					result.value[1] -|= 8*|@as(u8, @intCast(self.ch.pos.voxelSize));
					result.value[2] -|= 8*|@as(u8, @intCast(self.ch.pos.voxelSize));
				}
				calculateOutgoingOcclusion(&result.value, self.ch.data.getValue(pos.toIndex()), self.ch.pos.voxelSize, neighbor);
				if (chunkLocation == .inNeighborChunk) {
					neighborLists[neighbor.toInt()].append(main.stackAllocator, result);
					continue;
				}
				calculateIncomingOcclusion(&result.value, self.ch.data.getValue(neighborPos.toIndex()), self.ch.pos.voxelSize, neighbor.reverse());
				lightQueue.pushBack(result);
			}
		}
		self.mutex.unlock();
		self.addSelfToLightRefreshList(lightRefreshList);

		for (chunk.Neighbor.iterable) |neighbor| {
			if (neighborLists[neighbor.toInt()].items.len == 0) continue;
			const neighborMesh = mesh_storage.getNeighbor(self.ch.pos, self.ch.pos.voxelSize, neighbor) orelse continue;
			constructiveEntries.append(main.stackAllocator, .{
				.mesh = neighborMesh,
				.entries = neighborMesh.lightingData[@intFromBool(self.isSun)].propagateDestructiveFromNeighbor(lightQueue, neighborLists[neighbor.toInt()].items, constructiveEntries, lightRefreshList),
			});
		}

		return constructiveList;
	}
```

## Related Questions
- What is the purpose of the `propagateDestructive` function?
- How does the code ensure thread safety during lighting propagation?
- What data structures are used to manage light queue and neighbor lists?
- How does the `propagateLights` function initialize the light propagation process?
- What conditions determine whether a light value is appended to the constructive list?
- How does the code handle interactions with neighboring chunks during light propagation?
- What role does the mutex play in the lighting propagation logic?
- How are light values updated for blocks within the chunk?
- What is the process for calculating outgoing and incoming occlusion during light propagation?
- How does the code manage memory allocation and deallocation for lists and queues?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_2*
