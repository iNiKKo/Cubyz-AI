# [medium/codebase_src_vec.zig] - Chunk 2

**Type:** api
**Keywords:** matrix multiplication, quaternion rotation, perspective projection, vector operations, transpose matrix
**Symbols:** Mat4f, Mat4f.rows, Mat4f.identity, Mat4f.translation, Mat4f.scale, Mat4f.rotationX, Mat4f.rotationY, Mat4f.rotationZ, Mat4f.rotationQuat, Mat4f.perspective, Mat4f.transpose, Mat4f.mul, Mat4f.mulVec
**Concepts:** matrix operations, linear algebra, 3D transformations

## Summary
Defines a 4x4 matrix structure with various transformation methods.

## Explanation
This chunk defines the `Mat4f` struct, representing a 4x4 floating-point matrix. It includes several methods for creating matrices: identity, translation, scaling, rotation around X, Y, and Z axes, rotation from quaternion, perspective projection, transposition, multiplication with another matrix, and multiplication with a vector. The chunk also contains an internal helper function `andInt` for bitwise operations on vectors.

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
- How does the `Mat4f` struct handle matrix multiplication?
- What is the purpose of the `andInt` function in the `Mat4f` struct?
- Can you explain how perspective projection is implemented in the `Mat4f` struct?
- What are the different types of transformations provided by the `Mat4f` struct?
- How does the `transpose` method work in the `Mat4f` struct? Provide an example.
- Explain the role of quaternions in the `rotationQuat` method of the `Mat4f` struct.

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_2*
