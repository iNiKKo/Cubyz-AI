# [hard/codebase_src_models.zig] - Chunk 1

**Type:** implementation
**Keywords:** vector operations, fixed-point arithmetic, grid snapping, neighbor determination, occlusion checking
**Symbols:** Model, Model.min, Model.max, Model.internalQuads, Model.neighborFacingQuads, Model.isNeighborOccluded, Model.allNeighborsOccluded, Model.noNeighborsOccluded, Model.hasNeighborFacingQuads, Model.collision, Model.getFaceNeighbor, Model.fullyOccludesNeighbor, Model.initWithCollisionModel, Model.init, edgeInterp, solveDepth, rasterize
**Concepts:** model management, quad processing, collision detection, triangle rasterization

## Summary
The `Model` struct manages model data including its bounding box, quads, and collision information. It provides methods to initialize models with or without collision data and to rasterize triangles.

## Explanation
The `Model` struct contains fields for the minimum and maximum coordinates (`min`, `max`), internal quads (`internalQuads`), neighbor-facing quads (`neighborFacingQuads`), occlusion status of neighbors (`isNeighborOccluded`), overall occlusion flags (`allNeighborsOccluded`, `noNeighborsOccluded`), presence of neighbor-facing quads (`hasNeighborFacingQuads`), and collision boxes (`collision`). The `getFaceNeighbor` function determines the neighboring direction based on quad corners. The `fullyOccludesNeighbor` function checks if a quad fully occludes a neighbor. The `initWithCollisionModel` method initializes a model with given quad information and optional collision data, adjusting quads to a fixed-point grid, categorizing them into internal or neighbor-facing quads, and setting occlusion flags. The `init` method is a convenience wrapper that calls `initWithCollisionModel` without collision data. The `edgeInterp`, `solveDepth`, and `rasterize` functions handle triangle rasterization by interpolating edges, solving depth, and updating the collision grid.

## Code Example
```zig
fn getFaceNeighbor(quad: *const QuadInfo) ?chunk.Neighbor {
	var allZero: @Vector(3, bool) = .{true, true, true};
	var allOne: @Vector(3, bool) = .{true, true, true};
	for (quad.corners) |corner| {
		allZero = allZero & (corner == @as(Vec3f, @splat(0)));
		allOne = allOne & (corner == @as(Vec3f, @splat(1)));
	}
	if (allZero[0]) return .dirNegX;
	if (allZero[1]) return .dirNegY;
	if (allZero[2]) return .dirDown;
	if (allOne[0]) return .dirPosX;
	if (allOne[1]) return .dirPosY;
	if (allOne[2]) return .dirUp;
	return null;
}
```

## Related Questions
- What is the purpose of the `getFaceNeighbor` function?
- How does the `fullyOccludesNeighbor` function determine if a quad fully occludes a neighbor?
- What steps are involved in initializing a model with collision data using `initWithCollisionModel`?
- What is the role of the `init` method in the `Model` struct?
- How does the `edgeInterp` function work to interpolate edge values?
- What is the purpose of the `solveDepth` function in the context of triangle rasterization?
- How does the `rasterize` function update the collision grid with triangle information?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_1*
