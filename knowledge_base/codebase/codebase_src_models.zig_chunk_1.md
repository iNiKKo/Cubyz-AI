# [hard/codebase_src_models.zig] - Chunk 1

**Type:** implementation
**Keywords:** vector operations, fixed-point arithmetic, grid snapping, neighbor determination, occlusion checking
**Symbols:** Model, Model.min, Model.max, Model.internalQuads, Model.neighborFacingQuads, Model.isNeighborOccluded, Model.allNeighborsOccluded, Model.noNeighborsOccluded, Model.hasNeighborFacingQuads, Model.collision, Model.getFaceNeighbor, Model.fullyOccludesNeighbor, Model.initWithCollisionModel, Model.init, edgeInterp, solveDepth, rasterize
**Concepts:** model management, quad processing, collision detection, triangle rasterization

## Summary
The `Model` struct manages model data including its bounding box, quads, and collision information. It provides methods to initialize models with or without collision data and to rasterize triangles.

## Explanation
**Explanation**
The `Model` struct manages model data including its bounding box (`min`, `max`), internal quads (`internalQuads`), neighbor-facing quads (`neighborFacingQuads`), occlusion status of neighbors (`isNeighborOccluded`), overall occlusion flags (`allNeighborsOccluded`, `noNeighborsOccluded`), presence of neighbor-facing quads (`hasNeighborFacingQuads`), and collision boxes (`collision`). The struct provides methods to initialize models with or without collision data and to rasterize triangles.

- **Fields**:
  - `min`: Minimum coordinates of the model's bounding box.
  - `max`: Maximum coordinates of the model's bounding box.
  - `internalQuads`: Array of indices for internal quads.
  - `neighborFacingQuads`: Array of arrays, each containing indices for neighbor-facing quads in a specific direction (0-5).
  - `isNeighborOccluded`: Boolean array indicating if neighbors are occluded in each direction (0-5).
  - `allNeighborsOccluded`: Boolean flag indicating if all neighbors are occluded.
  - `noNeighborsOccluded`: Boolean flag indicating if no neighbors are occluded.
  - `hasNeighborFacingQuads`: Boolean flag indicating if there are any neighbor-facing quads.
  - `collision`: Array of collision boxes.

- **Methods**:
  - `getFaceNeighbor(quad: *const QuadInfo) ?chunk.Neighbor`: Determines the neighboring direction based on quad corners. It checks if all corners in a specific axis are either 0 or 1 to identify the neighbor direction (negX, negY, down, posX, posY, up).
  - `fullyOccludesNeighbor(quad: *const QuadInfo) bool`: Checks if a quad fully occludes a neighbor by counting the number of corners that are either all 0 or all 1 in two out of three axes.
  - `initWithCollisionModel(quadInfos: []const QuadInfo, collisionModel: ?[]const Box) ModelIndex`: Initializes a model with given quad information and optional collision data. It adjusts quads to a fixed-point grid, categorizes them into internal or neighbor-facing quads, and sets occlusion flags.
  - `init(quadInfos: []const QuadInfo) ModelIndex`: Convenience wrapper that calls `initWithCollisionModel` without collision data.

- **Functions**:
  - `edgeInterp(y: f32, x0: f32, y0: f32, x1: f32, y1: f32) f32`: Interpolates the x-value based on the given y-value and two points (x0, y0) and (x1, y1).
  - `solveDepth(normal: Vec3f, v0: Vec3f, xIndex: usize, yIndex: usize, zIndex: usize, u: f32, v: f32) f32`: Solves the depth of a point on a plane defined by a normal vector and a point (`v0`). It calculates the depth based on the normal components and the plane offset.
  - `rasterize(triangle: [3]Vec3f, grid: *[collisionGridSize][collisionGridSize]CollisionGridInteger, normal: Vec3f) void`: Rasterizes a triangle by interpolating edges, solving depth, and updating the collision grid. It converts triangle vertices to grid coordinates, calculates edge intersections, and updates the grid based on the triangle's normal.

These methods and functions work together to manage model data, determine neighbor relationships, check occlusion, initialize models with or without collision data, and handle triangle rasterization for collision detection.

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
-  What is the purpose of the `getFaceNeighbor` function? It determines the neighboring direction based on quad corners by checking if all corners in a specific axis are either all 0 or all 1.
-  How does the `fullyOccludesNeighbor` function determine if a quad fully occludes a neighbor? It checks if a quad has corners that are all 0 or all 1 in two out of three axes.
-  What steps are involved in initializing a model with collision data using `initWithCollisionModel`? It adjusts quads to a fixed-point grid, categorizes them into internal or neighbor-facing quads, and sets occlusion flags.
-  What is the role of the `init` method in the `Model` struct? It is a convenience wrapper that calls `initWithCollisionModel` without collision data.
-  How does the `edgeInterp` function work to interpolate edge values? It calculates the x-value based on the given y-value and two points (x0, y0) and (x1, y1).
-  What is the purpose of the `solveDepth` function in the context of triangle rasterization? It solves the depth of a point on a plane defined by a normal vector and a point (`v0`).
-  How does the `rasterize` function update the collision grid with triangle information? It converts triangle vertices to grid coordinates, calculates edge intersections, and updates the grid based on the triangle's normal.

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_1*
