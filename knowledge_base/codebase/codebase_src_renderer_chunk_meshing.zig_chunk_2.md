# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 2

**Type:** implementation
**Keywords:** data structures, meshing, faces, chunks, rendering, enums, structs
**Symbols:** FaceData, FaceData.position, FaceData.blockAndQuad, FaceData.init, ChunkData, ChunkData.position, ChunkData.min, ChunkData.max, ChunkData.voxelSize, ChunkData.lightStart, ChunkData.vertexStartOpaque, ChunkData.faceCountsByNormalOpaque, ChunkData.vertexStartTransparent, ChunkData.vertexCountTransparent, ChunkData.visibilityState, ChunkData.oldVisibilityState, IndirectData, IndirectData.count, IndirectData.instanceCount, IndirectData.firstIndex, IndirectData.baseVertex, IndirectData.baseInstance, FaceGroups, FaceGroups.core, FaceGroups.neighbor0, FaceGroups.neighbor1, FaceGroups.neighbor2, FaceGroups.neighbor3, FaceGroups.neighbor4, FaceGroups.neighbor5, FaceGroups.neighborLod0, FaceGroups.neighborLod1, FaceGroups.neighborLod2, FaceGroups.neighborLod3, FaceGroups.neighborLod4, FaceGroups.neighborLod5, FaceGroups.optional, FaceGroups.neighbor, FaceGroups.neighborLod
**Concepts:** chunk meshing, face data, chunk data, indirect rendering

## Summary
Defines data structures for chunk meshing, including face and chunk data.

## Explanation
This chunk defines several structs and enums used in the process of chunk meshing. The `FaceData` struct contains information about a single face, including its position, texture, and lighting details. The `position` field is a packed struct with fields for x, y, z coordinates (each 5 bits), a boolean indicating if it's a back face, and a light index (16 bits). The `blockAndQuad` field is also a packed struct containing a texture ID (16 bits) and a quad index. It includes an `init` method for creating instances, which takes parameters for the texture, quad index, block position, and whether it's a back face.

The `ChunkData` struct holds metadata about a chunk, such as its position (a Vec3i aligned to 16 bytes), minimum and maximum coordinates (Vec3f aligned to 16 bytes), voxel size (an integer), light start index (a 32-bit unsigned integer), vertex start indices for opaque and transparent faces (32-bit unsigned integers), face counts by normal for opaque faces (an array of 14 32-bit unsigned integers), vertex count for transparent faces (a 32-bit unsigned integer), visibility state (a 32-bit unsigned integer), and old visibility state (a 32-bit unsigned integer).

The `IndirectData` struct is used for indirect rendering, storing counts and indices. It contains fields for count (a 32-bit unsigned integer), instance count (a 32-bit unsigned integer), first index (a 32-bit unsigned integer), base vertex (a 32-bit signed integer), and base instance (a 32-bit unsigned integer).

The `FaceGroups` enum categorizes faces into core groups and neighbor LODs, with methods to map neighbors to these categories. It includes values for core, six neighbor levels (0 to 5), six neighbor LOD levels (0 to 5), and an optional group.

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
