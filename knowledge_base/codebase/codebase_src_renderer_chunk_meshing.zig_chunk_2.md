# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 2

**Type:** implementation
**Keywords:** data structures, meshing, faces, chunks, rendering, enums, structs
**Symbols:** FaceData, FaceData.position, FaceData.blockAndQuad, FaceData.init, ChunkData, ChunkData.position, ChunkData.min, ChunkData.max, ChunkData.voxelSize, ChunkData.lightStart, ChunkData.vertexStartOpaque, ChunkData.faceCountsByNormalOpaque, ChunkData.vertexStartTransparent, ChunkData.vertexCountTransparent, ChunkData.visibilityState, ChunkData.oldVisibilityState, IndirectData, IndirectData.count, IndirectData.instanceCount, IndirectData.firstIndex, IndirectData.baseVertex, IndirectData.baseInstance, FaceGroups, FaceGroups.core, FaceGroups.neighbor0, FaceGroups.neighbor1, FaceGroups.neighbor2, FaceGroups.neighbor3, FaceGroups.neighbor4, FaceGroups.neighbor5, FaceGroups.neighborLod0, FaceGroups.neighborLod1, FaceGroups.neighborLod2, FaceGroups.neighborLod3, FaceGroups.neighborLod4, FaceGroups.neighborLod5, FaceGroups.optional, FaceGroups.neighbor, FaceGroups.neighborLod
**Concepts:** chunk meshing, face data, chunk data, indirect rendering

## Summary
Defines data structures for chunk meshing, including face and chunk data.

## Explanation
This chunk defines several structs and enums used in the process of chunk meshing. The `FaceData` struct contains information about a single face, including its position, texture, and lighting details. It includes an `init` method for creating instances. The `ChunkData` struct holds metadata about a chunk, such as its position, size, light and vertex counts, and visibility states. The `IndirectData` struct is used for indirect rendering, storing counts and indices. The `FaceGroups` enum categorizes faces into core groups and neighbor LODs, with methods to map neighbors to these categories.

## Code Example
```zig
pub inline fn init(texture: u16, quadIndex: QuadIndex, pos: chunk.BlockPos, comptime backFace: bool) FaceData {
	return FaceData{
		.position = .{.x = pos.x, .y = pos.y, .z = pos.z, .isBackFace = backFace},
		.blockAndQuad = .{.texture = texture, .quadIndex = quadIndex},
	};
}
```

## Related Questions
- What is the purpose of the `init` method in `FaceData`?
- How many different face groups are defined in `FaceGroups`?
- What does the `ChunkData` struct contain?
- What is the role of the `IndirectData` struct in rendering?
- How are neighbors mapped to face groups in `FaceGroups`?
- What alignment is specified for fields in `ChunkData`?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_2*
