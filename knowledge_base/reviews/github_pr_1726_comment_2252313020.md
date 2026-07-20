# [src/models.zig] - PR #1726 review diff

**Type:** review
**Keywords:** collision generation, edge interpolation, depth solving, rasterization, floodfill queue, voxel grid, stack allocator, triangle processing, meshGridSize, CircularBufferQueue
**Symbols:** Model, edgeInterp, solveDepth, rasterize, generateCollision, Vec3f, QuadInfo, meshGridSize, CircularBufferQueue, main.stackAllocator
**Concepts:** collision detection, triangle rasterization, voxel grid, memory management, stack allocator

## Summary
Added collision generation functions to the Model struct, including edge interpolation, depth solving, triangle rasterization, and floodfill queue initialization.

## Explanation
The changes introduce new functions for generating collision data within a model. The `edgeInterp` function calculates the x-coordinate at a given y-value between two points using linear interpolation with the formula: `xa = edgeInterp(yf, p0[0], p0[1], p1[0], p1[1])`. This is done by checking if `y1 == y0`, in which case it returns `x0`; otherwise, it computes the interpolated value using the formula `(x1 - x0) * (y - y0) / (y1 - y0)` and adds it to `x0`. The `solveDepth` function computes the depth of a point on a plane defined by a normal vector and a point using the formula: `zf = solveDepth(normal, v0, X, Y, Z, xf, yf)`. This involves extracting components of the normal vector (`nX`, `nY`, `nZ`) and checking if `abs(nZ)` is less than a small threshold (`1e-6`). If so, it returns `0.0`; otherwise, it calculates the depth using the formula `(-(nX * u + nY * v + D)) / nZ`, where `D` is computed as `- (nX * v0[X] + nY * v0[Y] + nZ * v0[Z])`. The `rasterize` function rasterizes a triangle onto a 3D grid, marking voxels that are part of the triangle based on their position relative to the triangle's edges. It first determines the major axis (`X`, `Y`, `Z`) based on the absolute values of the normal vector components. Then, it calculates the bounding box for the triangle and iterates over the x and y coordinates within this box. For each point, it computes the z-coordinate using the `solveDepth` function and marks the corresponding voxel in the grid if it is valid. The `generateCollision` function processes each quad in the model to generate collision data using these functions. It initializes a hollow grid and rasterizes each triangle of the quad onto this grid. Then, it creates a full grid initialized to true and uses a floodfill queue to mark voxels that are part of the collision mesh. The floodfill queue is initialized with a stack allocator, ensuring efficient memory management and minimizing allocation overhead. The code handles edge cases in voxel grid boundaries by clamping indices within valid ranges and checking for out-of-bounds conditions before marking voxels.

## Related Questions
-  What is the purpose of the `edgeInterp` function?
-  How does the `solveDepth` function calculate depth?
-  Explain the role of the `rasterize` function in collision generation.
-  Why is a stack allocator used for the floodfill queue?
-  What is the significance of the `meshGridSize` constant?
-  How are triangles processed to generate collision data?
-  What is the impact of using a CircularBufferQueue for floodfilling?
-  How does the code handle edge cases in voxel grid boundaries?
-  What optimizations are made with the stack allocator in this context?
-  Can you explain the logic behind sorting vertices in the `rasterize` function?

*Source: unknown | chunk_id: github_pr_1726_comment_2252313020*
