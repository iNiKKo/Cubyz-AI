# [hard/codebase_src_models.zig] - Chunk 0

**Type:** implementation
**Keywords:** data structures, enum, extern struct, vector operations, indexing methods
**Symbols:** quadSSBO, QuadInfo, QuadInfo.normalVec, QuadInfo.cornerVec, QuadInfo.cornerUvVec, LightSample, ExtraQuadInfo, gridSize, collisionGridSize, CollisionGridInteger, snapToGrid, Triangle, Quad, ModelIndex, ModelIndex.model, ModelIndex.add, QuadIndex, QuadIndex.quadInfo, QuadIndex.extraQuadInfo
**Concepts:** model representation, quad face properties, grid snapping, triangle and quad structures

## Summary
Defines data structures for models and quads, including their properties and methods.

## Explanation
This chunk defines several key data structures used in the Cubyz voxel engine's model representation. It includes `QuadInfo` which holds information about a quad face, such as its normal vector (`[3]f32`), corner positions (`[4][3]f32`), texture coordinates (`[4][2]f32`), and texture slot (`u32`). The `ExtraQuadInfo` struct contains additional details like neighboring faces (`?Neighbor`), lighting samples (`[]LightSample`), and alignment flags (`bool`). The chunk also defines types for triangles and quads, along with enums for model and quad indices that provide methods to access the underlying data. Functions like `snapToGrid` are used for grid snapping operations, where `gridSize` is set to 4096 and `collisionGridSize` is set to 16.

## Code Example
```zig
pub fn normalVec(self: QuadInfo) Vec3f {
	return self.normal;
}
```

## Related Questions
- What is the purpose of the `QuadInfo` struct?
- How does the `snapToGrid` function work?
- What methods are available for accessing model data through `ModelIndex`?
- What additional information does `ExtraQuadInfo` provide compared to `QuadInfo`?
- How are triangles and quads defined in this chunk?
- What is the role of the `gridSize` constant in the code?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_0*
