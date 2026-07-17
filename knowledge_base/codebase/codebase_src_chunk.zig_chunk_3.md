# [hard/codebase_src_chunk.zig] - Chunk 3

**Type:** implementation
**Keywords:** reference counting, mutex locking, block entities, voxel data, position conversion
**Symbols:** Chunk, Chunk.pos, Chunk.data, Chunk.width, Chunk.voxelSizeShift, Chunk.voxelSizeMask, Chunk.blockPosToEntityDataMap, Chunk.blockPosToEntityDataMapMutex, Chunk.init, Chunk.deinit, Chunk.deinitContent, Chunk.unloadBlockEntities, Chunk.updateBlock, Chunk.getBlock, Chunk.liesInChunk, Chunk.getLocalBlockPos, Chunk.localToGlobalPosition, ServerChunk, ServerChunk.super, ServerChunk.wasChanged, ServerChunk.generated, ServerChunk.wasStored, ServerChunk.shouldStoreNeighbors, ServerChunk.mutex, ServerChunk.refCount, ServerChunk.initAndIncreaseRefCount, ServerChunk.deinit, ServerChunk.setChanged
**Concepts:** chunk meshing, entity ECS, world generation

## Summary
Defines the `Chunk` and `ServerChunk` structures, managing voxel data and block entities within a cubic region of the world.

## Explanation
The chunk module defines two main structures: `Chunk` and `ServerChunk`. The `Chunk` structure manages basic voxel data and block entities, including initialization, deinitialization, updating blocks, retrieving blocks, checking bounds, converting positions between local and global coordinates, and unloading block entities. The `ServerChunk` extends `Chunk` with additional server-specific functionality such as tracking changes, managing reference counts, saving modified chunks, and handling chunk updates. Both structures use mutexes for thread safety when accessing shared data.

## Code Example
```zig
pub fn init(pos: ChunkPosition) *Chunk {
	const self = memoryPool.create();
	std.debug.assert((pos.voxelSize - 1 & pos.voxelSize) == 0);
	std.debug.assert(@mod(pos.wx, pos.voxelSize) == 0 and @mod(pos.wy, pos.voxelSize) == 0 and @mod(pos.wz, pos.voxelSize) == 0);
	const voxelSizeShift: u5 = @intCast(std.math.log2_int(u31, pos.voxelSize));
	self.* = Chunk{
		.pos = pos,
		.width = pos.voxelSize*chunkSize,
		.voxelSizeShift = voxelSizeShift,
		.voxelSizeMask = pos.voxelSize - 1,
		.blockPosToEntityDataMap = .{},
		.blockPosToEntityDataMapMutex = .{},
	};
	self.data.init();
	return self;
}
```

## Related Questions
- What is the purpose of the `init` method in the `Chunk` struct?
- How does the `ServerChunk` structure extend the functionality of the `Chunk` structure?
- What role do mutexes play in the `Chunk` and `ServerChunk` structures?
- How are block entities managed within a chunk?
- What is the process for updating a block within a chunk?
- How does the `ServerChunk` handle changes to its data?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_3*
