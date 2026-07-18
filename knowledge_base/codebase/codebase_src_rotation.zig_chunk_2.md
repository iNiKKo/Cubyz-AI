# [medium/codebase_src_rotation.zig] - Chunk 2

**Type:** api
**Keywords:** matrix transformation, ray intersection, mode registration, allocator management, map operations
**Symbols:** rotationMatrixTransform, rayTriangleIntersection, init, reset, deinit, getByID, register
**Concepts:** 3D model transformations, rotation modes, intersection testing

## Summary
Handles rotation transformations and mode registration for 3D models.

## Explanation
This chunk defines functions for rotating 3D model quads using a transformation matrix and registering different rotation modes. The `rotationMatrixTransform` function applies a rotation to a quad's normal and corners by transforming the quad's normal vector and each corner of the quad using the provided transformation matrix. Specifically, it first transforms the normal vector and then adjusts each corner based on the transformation matrix after centering around (0.5, 0.5, 0.5) and shifting back to original coordinates.

The `rayTriangleIntersection` function implements the Möller–Trumbore intersection algorithm to determine if a ray intersects with a triangle. It calculates vectors e1 and e2 from the vertices of the triangle, computes the cross product between the direction vector of the ray and e2, and checks for determinant value det. If det is close to zero (within epsilon), it returns null indicating no intersection.

The function then calculates invDet as 1/det and uses this to compute u and v values based on the dot products with sCrossE1 and rayCrossE2 respectively. It ensures that both u and v are within [0, 1] range for valid barycentric coordinates. Finally, it computes t using e2 and sCrossE1; if t is positive, it returns t indicating intersection distance, otherwise null.

The chunk also includes initialization (`init`), reset (`reset`), deinitialization (`deinit`), and registration functions (`register`) for managing different rotation modes. It uses an allocator (`main.globalAllocator.allocator`) and a map (`rotationModes`) to store and manage these modes. The `getByID` function retrieves the specified mode, defaulting to 'cubyz:no_rotation' if not found.

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
