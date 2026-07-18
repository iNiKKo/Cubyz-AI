# [hard/codebase_src_renderer.zig] - Chunk 6

**Type:** implementation
**Keywords:** frustum culling, plane equations, vector math, matrix operations, field of view
**Symbols:** Frustum, Frustum.Plane, Frustum.planes, Frustum.init, Frustum.testAAB
**Concepts:** camera frustum, collision detection, axis-aligned bounding box (AABB)

## Summary
Defines the Frustum struct for camera frustum calculations and collision testing.

## Explanation
The Frustum struct represents a camera's view frustum, used to determine which objects are visible. It contains four planes (right, left, top, bottom) defined by their position and normal vectors. The init function calculates these planes based on the camera's position, rotation matrix, field of view, and screen dimensions. The testAAB method checks if an axis-aligned bounding box (AABB) is within the frustum by testing its corners against each plane.

## Code Example
```zig
pub fn init(cameraPos: Vec3f, rotationMatrix: Mat4f, fovY: f32, width: u31, height: u31) Frustum {
		const invRotationMatrix = rotationMatrix.transpose();
		const cameraDir = vec.xyz(invRotationMatrix.mulVec(Vec4f{0, 1, 0, 1}));
		const cameraUp = vec.xyz(invRotationMatrix.mulVec(Vec4f{0, 0, 1, 1}));
		const cameraRight = vec.xyz(invRotationMatrix.mulVec(Vec4f{1, 0, 0, 1}));

		const halfVSide = std.math.tan(std.math.degreesToRadians(fovY)*0.5);
		const halfHSide = halfVSide*@as(f32, @floatFromInt(width))/@as(f32, @floatFromInt(height));

		var self: Frustum = undefined;
		self.planes[0] = Plane{.pos = cameraPos, .norm = vec.cross(cameraUp, cameraDir + cameraRight*@as(Vec3f, @splat(halfHSide)))}; // right
		self.planes[1] = Plane{.pos = cameraPos, .norm = vec.cross(cameraDir - cameraRight*@as(Vec3f, @splat(halfHSide)), cameraUp)}; // left
		self.planes[2] = Plane{.pos = cameraPos, .norm = vec.cross(cameraRight, cameraDir - cameraUp*@as(Vec3f, @splat(halfVSide)))}; // top
		self.planes[3] = Plane{.pos = cameraPos, .norm = vec.cross(cameraDir + cameraUp*@as(Vec3f, @splat(halfVSide)), cameraRight)}; // bottom
		return self;
	}
```

## Related Questions
- How is the Frustum struct initialized?
- What does the testAAB method do?
- How are the frustum planes calculated in the init function?
- What is the purpose of the Plane struct within Frustum?
- How does the code handle vector and matrix operations in the init function?
- What is the role of the field of view (fovY) in the frustum calculation?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_6*
