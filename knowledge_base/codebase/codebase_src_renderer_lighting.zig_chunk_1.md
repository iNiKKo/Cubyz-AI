# [hard/codebase_src_renderer_lighting.zig] - Chunk 1

**Type:** implementation
**Keywords:** mutex locking, light value propagation, occlusion calculation, chunk data management, thread safety
**Symbols:** ChannelChunk, ChannelChunk.data, ChannelChunk.mutex, ChannelChunk.ch, ChannelChunk.isSun, ChannelChunk.init, ChannelChunk.deinit, ChannelChunk.Entry, ChannelChunk.Entry.pos, ChannelChunk.Entry.value, ChannelChunk.Entry.sourceDir, ChannelChunk.Entry.activeValue, ChannelChunk.ChunkEntries, ChannelChunk.ChunkEntries.mesh, ChannelChunk.ChunkEntries.entries, ChannelChunk.getValue, ChannelChunk.calculateIncomingOcclusion, ChannelChunk.calculateOutgoingOcclusion, ChannelChunk.propagateDirect, ChannelChunk.addSelfToLightRefreshList, ChannelChunk.propagateDestructive
**Concepts:** lighting calculation, chunk management, occlusion handling, light propagation

## Summary
The ChannelChunk struct manages lighting data for a chunk, including initialization, deinitialization, and propagation of light values.

## Explanation
The ChannelChunk struct manages lighting data for a chunk, including initialization, deinitialization, and propagation of light values. The struct contains methods such as `init`, `deinit`, `getValue`, `calculateIncomingOcclusion`, `calculateOutgoingOcclusion`, `propagateDirect`, `addSelfToLightRefreshList`, and `propagateDestructive`. Each method serves a specific purpose in handling lighting calculations, chunk management, occlusion handling, and light propagation. For example, the `init` method initializes a ChannelChunk instance by setting up its mutex, associating it with a chunk, determining if it is for sun or moonlight, and initializing its data structure. The `deinit` method cleans up resources associated with the ChannelChunk instance. The `getValue` method retrieves light values from the chunk's lighting data using the `data.getValue(pos.toIndex())` function. The `calculateIncomingOcclusion` and `calculateOutgoingOcclusion` methods handle occlusion calculations based on block properties and neighbor relationships, adjusting light values accordingly. Specifically, these methods use the block's absorption property to calculate how much light is absorbed by a neighboring block. For instance, if a block has an absorption value of `[10, 20, 30]`, it will absorb `voxelSize * 10` units of red light, `voxelSize * 20` units of green light, and `voxelSize * 30` units of blue light from the incoming or outgoing light. The `propagateDirect` method updates light values within a chunk by considering incoming and outgoing occlusions and propagating changes to neighboring chunks if necessary. It uses the `lightQueue.popFront()` function to process entries, updating light values based on neighbor relationships and voxel size adjustments. The `addSelfToLightRefreshList` function adds the current chunk's position to a list for refreshing lighting data. The `propagateDestructive` method handles more complex scenarios involving block destruction, managing entries in lists and ensuring proper propagation of light values under these conditions. Additionally, the struct includes specific data structures such as `Entry`, which contains fields like `pos`, `value`, `sourceDir`, and `activeValue`. Another structure is `ChunkEntries`, which includes fields like `mesh` and `entries` for managing lighting entries within a chunk.

## Code Example
```zig
pub fn init(ch: *chunk.Chunk, isSun: bool) *ChannelChunk {
	const self = memoryPool.create();
	self.mutex = .{};
	self.ch = ch;
	self.isSun = isSun;
	self.data.init();
	return self;
}
```

## Related Questions
-  What is the purpose of the ChannelChunk struct?
-  How does the init method initialize a ChannelChunk instance?
-  What does the deinit method do in the ChannelChunk struct?
-  How are light values propagated directly within a chunk?
-  What role does the mutex play in the ChannelChunk operations?
-  How is occlusion calculated for incoming and outgoing light?
-  What is the purpose of the propagateDestructive method?
-  How does the addSelfToLightRefreshList function work?
-  What data structures are used to manage lighting entries within a chunk?
-  How is thread safety ensured in the ChannelChunk operations?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_1*
