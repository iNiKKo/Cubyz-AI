# [hard/codebase_src_renderer_lighting.zig] - Chunk 3

**Type:** implementation
**Keywords:** mutex locking, lighting data, neighbor chunks, circular buffer, destructive lighting
**Symbols:** ChannelChunk, ChannelChunk.propagateDirect, ChannelChunk.propagateUniformSun, ChannelChunk.propagateLightsDestructive
**Concepts:** lighting propagation, voxel engine, thread safety, circular buffer queue

## Summary
Handles lighting propagation within a chunk, including direct, uniform sun, and destructive light propagation.

## Explanation
This chunk contains methods for managing lighting in a voxel engine. The `propagateDirect` method processes individual light sources by calculating their effects on neighboring voxels and updating the light queue accordingly. The `propagateUniformSun` method fills the chunk with uniform sunlight, adjusting values based on voxel size and neighbor direction. The `propagateLightsDestructive` method handles destructive lighting propagation, where lights are removed from the scene and their effects recalculated. Each method uses mutexes for thread safety, circular buffer queues for managing light entries, and interacts with mesh storage to get neighboring chunks' lighting data.

## Code Example
```zig
pub fn propagateLightsDestructive(self: *ChannelChunk, lights: []const BlockPos, lightRefreshList: *main.ListManaged(chunk.ChunkPosition)) void {
		var lightQueue = main.utils.CircularBufferQueue(Entry).init(main.stackAllocator, 1 << 12);
		defer lightQueue.deinit();
		for (lights) |pos| {
			lightQueue.pushBack(.{.pos = pos, .value = self.data.getValue(pos.toIndex()).toArray(), .sourceDir = 6, .activeValue = 0b111});
		}
		var constructiveEntries: main.List(ChunkEntries) = .empty;
		defer constructiveEntries.deinit(main.stackAllocator);
		constructiveEntries.append(main.stackAllocator, .{
			.mesh = null,
			.entries = self.propagateDestructive(&lightQueue, &constructiveEntries, true, lightRefreshList),
		});
		for (constructiveEntries.items) |entries| {
			const mesh = entries.mesh;
			var entryList = entries.entries;
			defer entryList.deinit(main.stackAllocator);
			const channelChunk = if (mesh) |_mesh| _mesh.lightingData[@intFromBool(self.isSun)] else self;
			channelChunk.mutex.lock();
			for (entryList.items) |entry| {
				var value = channelChunk.data.getValue(entry.toIndex()).toArray();
				const light = if (self.isSun) .{0, 0, 0} else extractColor(channelChunk.ch.data.getValue(entry.toIndex()).light());
				value = .{
					@max(value[0], light[0]),
					@max(value[1], light[1]),
					@max(value[2], light[2]),
				};
				if (value[0] == 0 and value[1] == 0 and value[2] == 0) continue;
				channelChunk.data.setValue(entry.toIndex(), .fromArray(.{0, 0, 0}));
				lightQueue.pushBack(.{.pos = entry, .value = value, .sourceDir = 6, .activeValue = 0b111});
			}
			channelChunk.mutex.unlock();
			channelChunk.propagateDirect(&lightQueue, lightRefreshList);
		}
	}
```

## Related Questions
- How does the `propagateDirect` method calculate light effects on neighboring voxels?
- What is the purpose of the mutex in the `propagateUniformSun` method?
- How does the `propagateLightsDestructive` method handle destructive lighting propagation?
- What data structure is used to manage light entries in these methods?
- How does the chunk interact with mesh storage for neighboring chunks' lighting data?
- What conditions determine whether a light value is updated in the `propagateDirect` method?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_3*
