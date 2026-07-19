# [hard/codebase_src_chunk.zig] - Chunk 3

**Type:** implementation
**Keywords:** memory pool, mutex locking, block update, position conversion, entity unloading
**Symbols:** Chunk, Chunk.pos, Chunk.data, Chunk.width, Chunk.voxelSizeShift, Chunk.voxelSizeMask, Chunk.blockPosToEntityDataMap, Chunk.blockPosToEntityDataMapMutex, Chunk.init, Chunk.deinit, Chunk.deinitContent, Chunk.unloadBlockEntities, Chunk.updateBlock, Chunk.getBlock, Chunk.liesInChunk, Chunk.getLocalBlockPos, Chunk.localToGlobalPosition
**Concepts:** chunk management, block entity handling, voxel data storage

## Summary
The Chunk struct manages voxel data and block entities within a defined spatial region.

## Explanation
This chunk defines the `Chunk` struct, which represents a section of the world in the Cubyz engine. The struct includes several fields such as `pos`, `data`, `width`, `voxelSizeShift`, and `voxelSizeMask`. The `init` method initializes the chunk with specific values for these fields, including calculating `voxelSizeShift` using the logarithm base 2 of `pos.voxelSize`. The `deinitContent` function ensures proper cleanup by deinitializing the block entity map and deferring the destruction of voxel data. The `blockPosToEntityDataMapMutex` is used to manage concurrent access to the block position-to-entity data map. The `updateBlock` method updates a block within the chunk if it lies within bounds, and the `getBlock` method retrieves a block at a specified position. The `liesInChunk` method checks if given coordinates lie within the chunk's bounds. The Chunk struct also includes methods for converting between local and global positions using `getLocalBlockPos` and `localToGlobalPosition`. Additionally, the `unloadBlockEntities` method unloads block entities based on the client or server side.

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
- What is the purpose of the `init` method in the Chunk struct?
- How does the `deinitContent` function ensure proper cleanup?
- What role does the `blockPosToEntityDataMapMutex` play in the Chunk struct?
- How are blocks updated within a chunk using the `updateBlock` method?
- What is the functionality of the `liesInChunk` method?
- How does the Chunk struct handle converting between local and global positions?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_3*
