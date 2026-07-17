# [hard/codebase_src_models.zig] - Chunk 1

**Type:** implementation
**Keywords:** snapToGrid, getFaceNeighbor, addQuad, fullyOccludesNeighbor, generateCollision, collisionGridSize, CollisionGridInteger, edge interpolation, depth solving, normal component selection
**Symbols:** ModelIndex, edgeInterp, solveDepth, rasterize
**Concepts:** quad snapping to grid, neighbor vs internal quad classification, per-face neighbor arrays, collision model generation, triangle rasterization against a collision grid, edge interpolation for depth calculation

## Summary
Defines ModelIndex and its initialization via initWithCollisionModel/initWithQuadInfos, snapping quad data to a fixed point grid, counting neighbor-facing vs internal quads, allocating per-face neighbor arrays and an internal array, then rasterizing triangles against a collision grid using edge interpolation and depth solving.

## Explanation
The chunk declares pub const ModelIndex = enum { ... } (the exact enum values are not shown here but the type is referenced). It provides pub fn initWithCollisionModel(quadInfos: []const QuadInfo, collisionModel: ?[]const Box) ModelIndex which allocates a stack buffer adjustedQuads, copies each QuadInfo into it, snaps corners and cornerUV to grid via snapToGrid, snaps normals, then initializes self.min/max by iterating over all snapped corners. It counts neighbor-facing quads (via getFaceNeighbor) and internal quads, storing per-face indices in amounts[6] and a single internalAmount. For each face i it allocates QuadIndex[] with main.globalAllocator; similarly allocates internalQuads. Then it iterates adjustedQuads again: if the quad has a neighbor it subtracts the normal from corners, calls addQuad(quad) catch continue to get a ModelIndex, stores that index into self.neighborFacingQuads[neighbor.toInt()][indices[...]] and increments indices; otherwise it just adds the quad internally. After populating all faces it reallocates each face array to its final length (using main.globalAllocator.realloc) and the internal array. It sets flags hasNeighborFacingQuads, allNeighborsOccluded, noNeighborsOccluded, then loops over 0..6: for each neighbor's array it calls fullyOccludesNeighbor(quad.quadInfo()) on every quad; if true it marks self.isNeighborOccluded[neighbor] = true. It also updates the three boolean flags (hasNeighborFacingQuads becomes true if any face has quads, allNeighborsOccluded is ANDed with each occlusion result, noNeighborsOccluded is ANDed with NOT of each occlusion). If a collisionModel is provided it dupe‑copies Box into self.collision; otherwise it calls generateCollision(self, adjustedQuads). The chunk also defines pub fn init(quadInfos: []const QuadInfo) ModelIndex which simply forwards to initWithCollisionModel with null. It declares edgeInterp(y, x0, y0, x1, y1) f32 returning linear interpolation or the endpoint when y1==y0. It declares solveDepth(normal, v0, xIndex, yIndex, zIndex, u, v) f32 which extracts normal components by index, computes planeOffset = -vec.dot(v0, normal), then returns -(nX*u + nY*v + planeOffset)/nZ. Finally it declares rasterize(triangle: [3]Vec3f, grid: *[collisionGridSize][collisionGridSize]CollisionGridInteger, normal: Vec3f) void which sets up xIndex/yIndex/zIndex based on the absolute largest normal component (choosing 1/2/0, 0/2/1, or 0/1/2 respectively), scales triangle vertices by collisionGridSize via @splat(@floatFromInt(...)), computes min/max of the three vertices, then builds voxelMin and voxelMax using @floor/@ceil and clamping to >=0. It constructs p0/p1/p2 as Vec2f from the chosen x/y components of each vertex.

## Related Questions
- What does ModelIndex represent in this file and how is it constructed?
- How are quad corners snapped to the fixed point grid before any neighbor checks?
- In initWithCollisionModel, what determines whether a quad is counted as neighbor-facing or internal?
- Why are per-face QuadIndex arrays allocated separately from the internal array?
- What happens when addQuad fails inside the second loop over adjustedQuads?
- How does fullyOccludesNeighbor decide if a neighbor quad occludes the current face?
- If collisionModel is provided, how is it stored in ModelIndex versus when generateCollision is called?
- What are xIndex/yIndex/zIndex chosen for rasterize based on and why?
- How does solveDepth compute the plane offset and which normal component is used as divisor?
- Does rasterize modify the grid or just read from it, and what is its return type?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_1*
