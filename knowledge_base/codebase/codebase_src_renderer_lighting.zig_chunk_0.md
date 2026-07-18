# [hard/codebase_src_renderer_lighting.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, RGB conversion, memory pool, bit manipulation, integer packing
**Symbols:** Atomic, BlockPos, ChunkMesh, LightValue, LightValue.fromArray, LightValue.toArray, LightValue.raw, QuadIndex, Vec3f, Vec3i, extractColor, memoryPool
**Concepts:** lighting, color representation

## Summary
Defines light value handling and extraction functions.

## Explanation
This chunk defines a `LightValue` struct to represent RGB lighting values with packed fields. It includes methods for converting between array representations and raw integer values. The `extractColor` function is used to extract RGB components from a packed integer. Memory pool initialization for `ChannelChunk` is also set up.

## Code Example
```zig
fn fromArray(arr: [3]u8) LightValue {
	return .{.r = arr[0], .g = arr[1], .b = arr[2]};
}
```

## Related Questions
- How is the `LightValue` struct defined?
- What methods does the `LightValue` struct have?
- How does the `extractColor` function work?
- What is the purpose of the memory pool initialization?
- How are RGB values packed into a single integer in this code?
- What is the role of the `Atomic` import in this chunk?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_0*
