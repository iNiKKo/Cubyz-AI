# [medium/codebase_src_vec.zig] - Chunk 0

**Type:** implementation
**Keywords:** vector types, swizzling, normalization, rotation, coordinate systems
**Symbols:** Vec2i, Vec2f, Vec2d, Vec3i, Vec3f, Vec3d, Vec4i, Vec4f, Vec4d, Vec4fComponent, swizzle, combine, xyz, xy, dot, lengthSquare, length, normalize, clampMag, cross, rotateX, rotateY, rotateZ, rotate2d, CoordinateSystem, CoordinateSystem.right_handed_z_up, CoordinateSystem.right_handed_y_up, CoordinateSystem.left_handed_z_up, CoordinateSystem.left_handed_y_up, CoordinateSystem.convertVec, CoordinateSystem.convertQuat, CoordinateSystem.convertScale
**Concepts:** vector operations, coordinate system conversion, quaternion handling

## Summary
Defines various vector types and operations for 2D and 3D vectors, including swizzling, normalization, rotation, and coordinate system conversion.

## Explanation
This chunk defines several vector types (`Vec2i`, `Vec2f`, `Vec2d`, `Vec3i`, `Vec3f`, `Vec3d`, `Vec4i`, `Vec4f`, `Vec4d`) using Zig's `@Vector` type. It also provides a set of functions for vector operations such as swizzling, combining, dot product, length calculation, normalization, clamping magnitude, cross product, and 2D/3D rotation. Additionally, it includes an enumeration `CoordinateSystem` with methods to convert vectors, quaternions, and scales between different coordinate systems.

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
- What is the purpose of the `normalize` function?
- How do you calculate the cross product of two vectors?
- What coordinate systems are supported by the `CoordinateSystem` enum?
- How can you convert a vector between different coordinate systems?

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_0*
