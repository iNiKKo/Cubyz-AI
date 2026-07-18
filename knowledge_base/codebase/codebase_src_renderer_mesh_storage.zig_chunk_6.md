# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 6

**Type:** implementation
**Keywords:** mutex locking, face data, light index, quad iteration, block removal
**Symbols:** addBreakingAnimationFace, removeBreakingAnimationFace, removeBreakingAnimation
**Concepts:** breaking animation, block rendering, mesh management

## Summary
Handles adding and removing breaking animation faces for blocks in the renderer.

## Explanation
This chunk contains functions to manage breaking animations of block faces. `addBreakingAnimationFace` adds a breaking face by locking the mesh mutex, finding the light index, and appending the face data. `removeBreakingAnimationFace` removes a breaking face by iterating through the list and swapping removing the matching face. `removeBreakingAnimation` iterates over all quads of a block and its neighbors to remove their breaking faces.

## Code Example
```zig
fn removeBreakingAnimationFace(pos: Vec3i, quadIndex: main.models.QuadIndex, neighbor: ?chunk.Neighbor) void {
	const worldPos = pos +% if (neighbor) |n| n.relPos() else Vec3i{0, 0, 0};
	const relPos = worldPos & @as(Vec3i, @splat(main.chunk.chunkMask));
	const mesh = getMesh(.{.wx = worldPos[0], .wy = worldPos[1], .wz = worldPos[2], .voxelSize = 1}) orelse return;
	for (mesh.blockBreakingFaces.items, 0..) |face, i| {
		if (face.position.x == relPos[0] and face.position.y == relPos[1] and face.position.z == relPos[2] and face.blockAndQuad.quadIndex == quadIndex) {
			_ = mesh.blockBreakingFaces.swapRemove(i);
			mesh.blockBreakingFacesChanged = true;
			break;
		}
	}
}
```

## Related Questions
- How does the function `addBreakingAnimationFace` determine the world position of a block?
- What is the purpose of locking and unlocking the mesh mutex in `addBreakingAnimationFace`?
- How does `removeBreakingAnimationFace` handle removing a breaking face from the mesh?
- What steps are involved in the `removeBreakingAnimation` function to remove all breaking animations for a block?
- How does the code ensure that only the correct face is removed in `removeBreakingAnimationFace`?
- What is the role of the `blockBreakingFacesChanged` flag in managing breaking animations?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_6*
