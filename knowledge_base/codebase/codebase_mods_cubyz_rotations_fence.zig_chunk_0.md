# [easy/codebase_mods_cubyz_rotations_fence.zig] - Chunk 0

**Type:** implementation
**Keywords:** FenceData, rotateZ, fenceTransform, createBlockModel, updateData, neighbor connectivity, rotation table, bit-cast, model caching
**Symbols:** dependsOnNeighbors, fenceModels, FenceData, init, deinit, reset, rotateZ, fenceTransform, createBlockModel, model, updateData
**Concepts:** neighbor connectivity state management, rotation table generation, bit-cast transformations, model caching, quad UV adjustment, packed struct layout

## Summary
Defines the fence rotation system for Cubyz blocks, providing neighbor connectivity state management, Z-axis rotation tables with bit-cast transformations, and model caching keyed by block ID.

## Explanation
The chunk declares a global FenceData packed struct with four bool fields representing connections on each cardinal direction. It maintains a std.StringHashMap of ModelIndex values under fenceModels, initialized in init() and cleared in deinit(). The rotateZ function builds a comptime rotationTable indexed by angle (0..3) and data value (0..15), using bit-cast to convert FenceData into u4 for storage; the table is populated at compile time with identity mappings for angle 0, then rotated copies are generated for angles 1..3. The fenceTransform function modifies a QuadInfo's corner positions and UV coordinates when a specific neighbor connection is missing, setting corner[0] or corner[1] to 0.5 and adjusting UVs based on the quad normal Z component. createBlockModel reads the block ID from zon, checks if a cached model exists in fenceModels, otherwise obtains the base model via main.models.getModelIndex(modelId).model() and calls transformModel with fenceTransform and a FenceData value derived from @bitCast(@as(u4, 0)) for the default case; it then iterates over all possible FenceData values (1..15) to generate rotated variants, storing each in fenceModels before returning the cached or newly created ModelIndex. The model function delegates to blocks.meshes.modelIndexStart(block).add(block.data & 15) to compute a base index plus an offset derived from the lower four bits of block.data. updateData compares the current block's FenceData with that implied by its neighbor: it computes targetVal as true when the neighbor is not replaceable, not transparent, and either shares the same base model or is occluded according to neighborModel.isNeighborOccluded[neighbor.reverse().toInt()]; then it updates the appropriate isConnected* field in a local currentData variable based on the neighbor direction, casts back to u16, and if different from block.data assigns the new value and returns true.

## Related Questions
- What does the FenceData struct represent and how are its fields named?
- How is the rotation table built inside rotateZ and what comptime logic populates it?
- When does createBlockModel fall back to using 'cubyz:cube' as the model ID?
- In fenceTransform, under which condition is cornerUV[0] set to 0.5 versus cornerUV[1]?
- How does updateData decide whether a neighbor connection should be marked as connected?
- What happens if rotateZ receives an angle value outside the range 0..3?
- Does reset clear fenceModels while preserving its capacity, and why is that important?
- Where are ModelIndex values stored after createBlockModel generates them?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_fence.zig_chunk_0*
