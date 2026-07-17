# [medium/codebase_src_vec.zig] - Chunk 1

**Type:** implementation
**Keywords:** CoordinateSystem, convertVec, convertQuat, convertScale, quatFromAxisAngle, Mat4f, identity, translation, scale, rotationX, rotationY, rotationZ, rotationQuat
**Symbols:** CoordinateSystem, convertVec, convertQuat, convertScale, Quat, quatFromAxisAngle, Mat4f, identity, translation, scale, rotationX, rotationY, rotationZ, rotationQuat
**Concepts:** coordinate system conversion, quaternion construction, matrix factory functions, handness variants, axis-angle rotation, bitcast masking, swizzle operations

## Summary
Defines CoordinateSystem conversion utilities and Mat4f matrix construction functions.

## Explanation
The chunk declares a CoordinateSystem struct with four variants (right_handed_z_up, right_handed_y_up, left_handed_z_up, left_handed_y_up) and provides three public methods: convertVec, which translates a position relative to a center of rotation into the appropriate coordinate system; convertQuat, which maps quaternion components according to the selected handedness and axis convention; and convertScale, which swaps Y/Z axes for y-up systems while preserving order for z-up systems. It also defines Quat as a struct containing a Vec4f field q with an initializer and a public static method quatFromAxisAngle that normalizes an axis vector, computes half-angle sine/cosine via @sin/@cos, and returns the quaternion constructed from those values. The Mat4f struct is declared with a rows field of type [4]Vec4f and includes several static factory functions: identity (returns the unit matrix), translation (places position components into the fourth column), scale (diagonal scaling with 1 on the w component), rotationX, rotationY, rotationZ (each computes sin/cos via @sin/@cos and builds the corresponding 2x2 submatrix while leaving other rows as identity), and rotationQuat which begins converting a quaternion to a matrix using bit-cast masks and swizzle operations. All functions are public except inline fn andInt, which is marked inline for performance but remains part of the Mat4f definition.

## Related Questions
- How does convertVec handle left-handed versus right-handed coordinate systems?
- What is the exact quaternion component mapping for a right_handed_y_up system in convertQuat?
- Which matrix factory function returns an identity matrix and how are its rows initialized?
- Does rotationX use @sin/@cos or precomputed constants, and what does it return?
- How does quatFromAxisAngle normalize the axis vector before constructing the quaternion?
- What is the purpose of inline fn andInt inside Mat4f and how does it operate on Vec4f values?
- In rotationQuat, what role do f32x4_mask3 and swizzle play in converting a quaternion to a matrix?
- Are any of the Matrix factory functions marked pub or private, and why might that matter for callers?
- What is the initial value of Quat.q when an instance is created without calling quatFromAxisAngle?
- How does convertScale treat scale vectors differently between z-up and y-up coordinate systems?

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_1*
