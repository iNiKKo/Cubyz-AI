# [medium/codebase_src_vec.zig] - Chunk 2

**Type:** api
**Keywords:** matrix multiplication, quaternion rotation, perspective projection, vector operations, transpose matrix
**Symbols:** Mat4f, Mat4f.rows, Mat4f.identity, Mat4f.translation, Mat4f.scale, Mat4f.rotationX, Mat4f.rotationY, Mat4f.rotationZ, Mat4f.rotationQuat, Mat4f.perspective, Mat4f.transpose, Mat4f.mul, Mat4f.mulVec
**Concepts:** matrix operations, linear algebra, 3D transformations

## Summary
This chunk defines the `Mat4f` struct, representing a 4x4 floating-point matrix with various transformation methods including identity, translation, scaling, rotation around X, Y, and Z axes, quaternion-based rotation, perspective projection, transposition, multiplication with another matrix, and multiplication with a vector. It includes an internal helper function `andInt` for bitwise operations on vectors used in quaternion calculations.

## Explanation
This chunk defines the `Mat4f` struct, representing a 4x4 floating-point matrix with various transformation methods including identity, translation, scaling, rotation around X, Y, and Z axes, quaternion-based rotation, perspective projection, transposition, multiplication with another matrix, and multiplication with a vector. The internal helper function `andInt` is used for bitwise operations on vectors to optimize quaternion calculations.

### Methods:
- **identity()**: Returns an identity matrix where the diagonal elements are 1 and all other elements are 0.
- **translation(pos: Vec3f)**: Creates a translation matrix based on the given position `pos`. For example, if `pos` is `(2.5, -3.0, 4.7)`, it generates a matrix that translates objects by these coordinates.
- **scale(vector: Vec3f)**: Scales the matrix along each axis according to the provided vector. If `vector` is `(1.5, 2.0, 0.8)`, it scales the object by these factors in X, Y, and Z directions respectively.
- **rotationX(rad: f32)**, **rotationY(rad: f32)**, **rotationZ(rad: f32)**: Rotates the matrix around the X, Y, and Z axes by a given angle `rad` in radians. Uses sine (`@sin`) and cosine (`@cos`) functions to compute rotation values.
- **rotationQuat(quat: Quat)**: Applies quaternion-based rotation using bitwise operations for efficiency. The `andInt` function is used internally within this method to optimize calculations involving quaternions.
- **perspective(fovY: f32, aspect: f32, near: f32, far: f32)**: Generates a perspective projection matrix based on the field of view (`fovY`), aspect ratio (`aspect`), and clipping planes (`near`, `far`). For instance, calling this method with `fovY = 45.0`, `aspect = 16/9`, `near = 0.1`, and `far = 100.0` creates a projection matrix suitable for rendering scenes in perspective view.
- **transpose()**: Transposes the matrix by swapping rows with columns.
- **mul(other: Mat4f)**: Multiplies this matrix with another matrix `other` to combine transformations.
- **mulVec(vec: Vec4f)**: Multiplies this matrix with a vector `vec`, typically used for transforming vertices in 3D space.

## Code Example
```zig
pub fn identity() Mat4f {
	return Mat4f{
		.rows = [4]Vec4f{
			Vec4f{1, 0, 0, 0},
			Vec4f{0, 1, 0, 0},
			Vec4f{0, 0, 1, 0},
			Vec4f{0, 0, 0, 1},
		},
	};
}
```

## Related Questions
-  How does the `Mat4f` struct handle matrix multiplication?
-  What is the purpose of the `andInt` function in the `Mat4f` struct?
-  Can you explain how perspective projection is implemented in the `Mat4f` struct?
-  What are the different types of transformations provided by the `Mat4f` struct?
-  How does the `transpose` method work in the `Mat4f` struct? Provide an example.
-  Explain the role of quaternions in the `rotationQuat` method of the `Mat4f` struct.

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_2*
