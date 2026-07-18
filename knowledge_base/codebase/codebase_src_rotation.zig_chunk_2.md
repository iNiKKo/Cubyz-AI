# [medium/codebase_src_rotation.zig] - Chunk 2

**Type:** api
**Keywords:** matrix transformation, ray intersection, mode registration, allocator management, map operations
**Symbols:** rotationMatrixTransform, rayTriangleIntersection, init, reset, deinit, getByID, register
**Concepts:** 3D model transformations, rotation modes, intersection testing

## Summary
Handles rotation transformations and mode registration for 3D models.

## Explanation
This chunk defines functions for rotating 3D model quads using a transformation matrix and registering different rotation modes. The `rotationMatrixTransform` function applies a rotation to a quad's normal and corners. The `rayTriangleIntersection` function implements the Möller–Trumbore intersection algorithm to determine if a ray intersects with a triangle. The chunk also includes initialization, reset, deinitialization, and registration functions for managing different rotation modes. It uses an allocator (`main.globalAllocator.allocator`) and a map (`rotationModes`) to store and manage these modes.

## Code Example
```zig
pub fn rotationMatrixTransform(quad: *main.models.QuadInfo, transformMatrix: Mat4f) void {
	quad.normal = vec.xyz(Mat4f.mulVec(transformMatrix, vec.combine(quad.normal, 0)));
	for (&quad.corners) |*corner| {
		corner.* = vec.xyz(Mat4f.mulVec(transformMatrix, vec.combine(corner.* - Vec3f{0.5, 0.5, 0.5}, 1))) + Vec3f{0.5, 0.5, 0.5};
	}
}
```

## Related Questions
- How does the `rotationMatrixTransform` function apply a rotation to a quad?
- What algorithm is used in the `rayTriangleIntersection` function?
- How are rotation modes initialized and managed in this chunk?
- What happens if a requested rotation mode is not found?
- How does the `register` function handle different field types when creating a `RotationMode` instance?
- What is the purpose of the `deinit` function in this chunk?

*Source: unknown | chunk_id: codebase_src_rotation.zig_chunk_2*
