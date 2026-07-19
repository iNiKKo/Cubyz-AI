# [hard/codebase_src_chunk.zig] - Chunk 1

**Type:** implementation
**Keywords:** enum, methods, navigation, conversion, masks, unit tests
**Symbols:** Lod, Lod.min, Lod.max, Lod.next, Lod.previous, Lod.toInt, Lod.voxelSize, Lod.chunkWidth, Lod.voxelSizeShift, Lod.voxelSizeMask, Lod.localMask
**Concepts:** Level of Detail (LOD)

## Summary
Defines the Level of Detail (LOD) enumeration and associated methods for managing LOD values in a voxel engine.

## Explanation
This chunk defines an enum `Lod` representing different levels of detail (LOD) with specific integer values: 1, 2, 4, 8, 16, and 32. The enum includes methods to navigate between LODs (`next`, `previous`), convert LODs to integers (`toInt`), calculate voxel sizes (`voxelSize`), determine chunk widths (`chunkWidth`), and provide masks for converting global coordinates to LOD resolution and chunk local coordinates (`voxelSizeMask`, `localMask`). The minimum LOD value is 1 with a voxel size of 1, and the maximum LOD value is 32 with a voxel size of 32. The `next` method returns the next LOD level by incrementing the integer value, while the `previous` method decrements it. The `voxelSize` method calculates the voxel size as 2 raised to the power of the LOD's integer value. The `chunkWidth` method calculates the chunk width by multiplying the voxel size by a constant `chunkSize`. The `voxelSizeShift` method returns the integer value of the LOD, which is used in bitwise operations. The `voxelSizeMask` method creates a mask for converting global coordinates to LOD resolution coordinates, and the `localMask` method creates a mask for converting global coordinates to chunk local coordinates. The chunk also contains unit tests verifying the correctness of these methods, such as checking the minimum and maximum values for voxel sizes, chunk widths, and masks.

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
