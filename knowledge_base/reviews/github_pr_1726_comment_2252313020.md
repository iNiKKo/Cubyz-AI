# [src/models.zig] - PR #1726 review diff

**Type:** review
**Keywords:** collision generation, edge interpolation, depth solving, triangle rasterization, voxel grid, stack allocator, floodfill queue
**Symbols:** Model, generateCollision, edgeInterp, solveDepth, rasterize, Vec3f, QuadInfo, meshGridSize, CircularBufferQueue
**Concepts:** Collision Detection, Rasterization, Stack Allocation, Floodfill Algorithm

## Summary
Added collision generation functions to the Model struct, including edge interpolation, depth solving, triangle rasterization, and floodfill queue initialization.

## Explanation
The changes introduce a new function `generateCollision` within the `Model` struct that processes model quads to generate a collision grid. This involves several helper functions: `edgeInterp` for linear interpolation along an edge, `solveDepth` for calculating depth based on a normal vector and vertices, and `rasterize` for converting triangles into voxelized form in a 3D grid. The floodfill queue is initialized using a stack allocator, which the reviewer notes has zero resizing cost due to the nature of stack allocation.

## Related Questions
- What is the purpose of the `edgeInterp` function in the collision generation process?
- How does the `solveDepth` function calculate depth for a given normal and vertices?
- Can you explain the role of the `rasterize` function in converting triangles to voxelized form?
- Why is a stack allocator used for initializing the floodfill queue, and what are its benefits?
- What is the significance of the `meshGridSize` constant in these collision generation functions?
- How does the `generateCollision` function handle multiple quads when generating the collision grid?

*Source: unknown | chunk_id: github_pr_1726_comment_2252313020*
