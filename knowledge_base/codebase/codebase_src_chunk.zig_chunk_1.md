# [hard/codebase_src_chunk.zig] - Chunk 1

**Type:** implementation
**Keywords:** enum, methods, navigation, conversion, masks, unit tests
**Symbols:** Lod, Lod.min, Lod.max, Lod.next, Lod.previous, Lod.toInt, Lod.voxelSize, Lod.chunkWidth, Lod.voxelSizeShift, Lod.voxelSizeMask, Lod.localMask
**Concepts:** Level of Detail (LOD)

## Summary
Defines the Level of Detail (LOD) enumeration and associated methods for managing LOD values in a voxel engine.

## Explanation
This chunk defines an enum `Lod` representing different levels of detail, each with a corresponding integer value. It includes methods to navigate between LODs (`next`, `previous`), convert LODs to integers (`toInt`), calculate voxel sizes (`voxelSize`), and determine chunk widths (`chunkWidth`). Additional utility functions provide masks for converting global coordinates to LOD resolution and chunk local coordinates (`voxelSizeMask`, `localMask`). The chunk also contains unit tests verifying the correctness of these methods.

## Code Example
```zig
pub inline fn next(self: Lod) Lod {
	return @enumFromInt(@intFromEnum(self) + 1);
}
```

## Related Questions
- What are the possible values of the Lod enum?
- How do you get the next LOD level from a given LOD?
- What is the minimum LOD value and its voxel size?
- How does the chunkWidth method calculate the width based on LOD?
- What is the purpose of the voxelSizeMask method in this context?
- How are unit tests structured for the Lod enum methods?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_1*
