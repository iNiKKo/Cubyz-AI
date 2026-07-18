# [medium/codebase_src_vec.zig] - Chunk 0

**Type:** implementation
**Keywords:** vector types, swizzling, dot product, normalization, rotation, coordinate systems
**Symbols:** Vec2i, Vec2f, Vec2d, Vec3i, Vec3f, Vec3d, Vec4i, Vec4f, Vec4d, Vec4fComponent, swizzle, combine, xyz, xy, dot, lengthSquare, length, normalize, clampMag, cross, rotateX, rotateY, rotateZ, rotate2d, CoordinateSystem, CoordinateSystem.right_handed_z_up, CoordinateSystem.right_handed_y_up, CoordinateSystem.left_handed_z_up, CoordinateSystem.left_handed_y_up, CoordinateSystem.convertVec, CoordinateSystem.convertQuat, CoordinateSystem.convertScale
**Concepts:** vector operations, coordinate system conversion

## Summary
This chunk defines various vector types and operations for 2D and 3D vectors, including swizzling, normalization, rotation, and coordinate system conversion.

## Explanation
The code defines several vector types using Zig's `@Vector` type, supporting integer (`i32`) and floating-point (`f32`, `f64`) components in dimensions 2 through 4. It includes functions for common vector operations such as swizzling, dot product, length calculation, normalization, clamping magnitude, cross product, and rotation around axes. Additionally, it provides a coordinate system enum with methods to convert vectors, quaternions, and scales between different handedness and axis conventions.

## Code Example
```zig
pub inline fn swizzle(
	v: Vec4f,
	comptime x: Vec4fComponent,
	comptime y: Vec4fComponent,
	comptime z: Vec4fComponent,
	comptime w: Vec4fComponent,
) Vec4f {
	return @shuffle(f32, v, undefined, [4]i32{@intFromEnum(x), @intFromEnum(y), @intFromEnum(z), @intFromEnum(w)});
}
```

## Related Questions
- What are the different vector types defined in this chunk?
- How does the `swizzle` function work?
- What operations are available for 3D vectors?
- How is a vector normalized?
- What is the purpose of the `CoordinateSystem` enum?
- How do you rotate a 2D vector around a center point?

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_0*
