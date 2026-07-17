# [hard/codebase_src_renderer.zig] - Chunk 7

**Type:** implementation
**Keywords:** frustum, AABB, voxel traversal, collision detection, graphics pipeline
**Symbols:** Frustum, Frustum.planes, Frustum.init, Frustum.testAAB, MeshSelection, MeshSelection.pipeline, MeshSelection.uniforms, MeshSelection.init, MeshSelection.deinit, MeshSelection.posBeforeBlock, MeshSelection.neighborOfSelection, MeshSelection.selectedBlockPos, MeshSelection.lastSelectedBlockPos, MeshSelection.currentBlockProgress, MeshSelection.currentSwingProgress, MeshSelection.currentSwingTime, MeshSelection.selectionMin, MeshSelection.selectionMax, MeshSelection.selectionNormal, MeshSelection.lastPos, MeshSelection.lastDir, MeshSelection.select, MeshSelection.canPlaceBlock, MeshSelection.placeBlock
**Concepts:** frustum culling, block selection, voxel traversal, graphics pipeline

## Summary
Handles frustum calculations and block selection logic in the renderer.

## Explanation
This chunk defines a `Frustum` struct with methods for initialization (`init`) and testing if an axis-aligned bounding box (AABB) is within the frustum (`testAAB`). It also includes a `MeshSelection` struct managing graphics pipeline setup, block selection, and placement logic. The `select` method implements a voxel traversal algorithm to find blocks in the player's line of sight, while `placeBlock` checks for collisions before placing a new block.

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
- What is the purpose of the `init` method in the `Frustum` struct?
- How does the `testAAB` method determine if an AABB is within the frustum?
- What are the key components of the `MeshSelection` struct?
- How does the `select` method implement voxel traversal for block selection?
- What steps does the `placeBlock` method take to place a new block?
- How is collision detection handled in the `canPlaceBlock` method?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_7*
