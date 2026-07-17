# [hard/codebase_src_chunk.zig] - Chunk 4

**Type:** implementation
**Keywords:** ServerChunk, voxelSizeShift, voxelSizeMask, refCount, mutex, block updates, reference counting
**Symbols:** ServerChunk, ServerChunk.voxelSizeShift, ServerChunk.voxelSizeMask, ServerChunk.blockPosToEntityDataMap, ServerChunk.blockPosToEntityDataMapMutex, ServerChunk.refCount, ServerChunk.init, ServerChunk.deinit, ServerChunk.setChanged, ServerChunk.increaseRefCount, ServerChunk.decreaseRefCount, ServerChunk.liesInChunk, ServerChunk.startIndex, ServerChunk.getBlock, ServerChunk.updateBlockAndSetChanged, ServerChunk.updateBlockIfDegradable, ServerChunk.updateBlockInGeneration, ServerChunk.updateBlockColumnInGeneration, ServerChunk.updateFromLowerResolution
**Concepts:** voxel data management, reference counting, thread safety, block updates, chunk lifecycle

## Summary
This chunk defines the ServerChunk struct and its associated methods for managing voxel data, reference counting, and block updates.

## Explanation
The ServerChunk struct manages voxel data for a server-side chunk in the Cubyz engine. It includes methods for initialization (`init`), deinitialization (`deinit`), setting changed status (`setChanged`), increasing and decreasing reference counts (`increaseRefCount`, `decreaseRefCount`), checking if coordinates lie within the chunk bounds (`liesInChunk`), converting start indices for reduced resolution (`startIndex`), getting blocks (`getBlock`), updating blocks with change tracking (`updateBlockAndSetChanged`), updating blocks conditionally (`updateBlockIfDegradable`), and updating blocks during generation (`updateBlockInGeneration`, `updateBlockColumnInGeneration`). The chunk also handles updating from lower resolution chunks (`updateFromLowerResolution`). It uses mutexes for thread safety and reference counting to manage the lifecycle of chunk data.

## Code Example
```zig
pub fn deinit(self: *ServerChunk) void {
	std.debug.assert(self.refCount.raw == 0);
	const oldContext = main.sync.threadContext;
	defer main.sync.threadContext = oldContext;
	main.sync.threadContext = .chunkDeiniting;
	if (self.wasChanged) {
		self.save(main.server.world.?);
	}
	self.super.unloadBlockEntities(.server);
	self.super.deinitContent();
	serverPool.destroy(@alignCast(self));
}
```

## Related Questions
- What is the purpose of the `deinit` method in ServerChunk?
- How does the `increaseRefCount` method work in ServerChunk?
- What checks are performed before updating a block in ServerChunk?
- How does ServerChunk handle updates from lower resolution chunks?
- What is the role of the `startIndex` method in ServerChunk?
- How does ServerChunk ensure thread safety during operations?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_4*
