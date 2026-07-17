# [hard/codebase_src_renderer_lighting.zig] - Chunk 0

**Type:** implementation
**Keywords:** mutex locking, light value, occlusion calculation, light queue, thread safety
**Symbols:** memoryPool, LightValue, extractColor, ChannelChunk, ChannelChunk.data, ChannelChunk.mutex, ChannelChunk.ch, ChannelChunk.isSun, ChannelChunk.init, ChannelChunk.deinit, ChannelChunk.getValue, calculateIncomingOcclusion, calculateOutgoingOcclusion, propagateDirect
**Concepts:** lighting system, chunk lighting, block occlusion, light propagation

## Summary
Handles lighting calculations and propagation within chunks.

## Explanation
This chunk manages the lighting system for voxel chunks in the Cubyz engine. It defines a `ChannelChunk` struct that holds lighting data for a specific chunk, including mutex locking for thread safety. The `LightValue` struct represents RGB light values with packed storage. Functions like `extractColor`, `calculateIncomingOcclusion`, and `calculateOutgoingOcclusion` handle the computation of light absorption and occlusion based on block properties. The `propagateDirect` function processes a queue of lighting changes, updating neighboring blocks' lighting and handling inter-chunk interactions.

## Code Example
```zig
fn extractColor(in: u32) [3]u8 {
	return .{
		@truncate(in >> 16),
		@truncate(in >> 8),
		@truncate(in),
	};
}
```

## Related Questions
- What is the purpose of the `ChannelChunk` struct?
- How does the `LightValue` struct store color information?
- What function calculates incoming occlusion for a block?
- How is mutex locking used in this chunk?
- What is the role of the `propagateDirect` function?
- How are light values propagated between neighboring chunks?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_0*
