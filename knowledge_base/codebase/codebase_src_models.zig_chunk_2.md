# [hard/codebase_src_models.zig] - Chunk 2

**Type:** implementation
**Keywords:** triangle rasterization, collision grid, voxel projection, floodfill, normal vector
**Symbols:** init, edgeInterp, solveDepth, rasterize, generateCollision
**Concepts:** model initialization, collision detection, voxelization, floodfill algorithm

## Summary
Handles model initialization and collision grid generation.

## Explanation
This chunk contains functions for initializing models, rasterizing triangles into a collision grid, and generating collision data from quad information. The `init` function initializes a model with collision data by calling `initWithCollisionModel` with the provided quad information and a null parameter. The `rasterize` function projects a triangle onto a grid and marks voxels as occupied based on the triangle's normal vector. It first determines the major axis of the normal vector to decide which axes to use for rasterization. Specifically, it checks the absolute values of the normal vector components and selects the largest one. Then, it calculates the minimum and maximum bounds of the triangle in voxel space using `collisionGridSize` (which is assumed to be a constant defining the grid size) and iterates over the y-axis range from `@intCast(@as([3]i32, voxelMin)[yIndex])` to `@intCast(@as([3]i32, voxelMax)[yIndex])`. For each y-value, it interpolates the x-values where the edges of the triangle intersect the scan line using the `edgeInterp` function. It then determines the start and end x-values for the current scan line and iterates over the x-axis range from `voxelXStart` to `voxelXEnd`. For each x-value, it calculates the depth (z-value) using the `solveDepth` function, which computes the z-coordinate based on the normal vector components and the plane offset. It marks the corresponding voxel as occupied in the collision grid if the z-value is valid. The `generateCollision` function processes each quad of the model, rasterizes its triangles, and applies a floodfill algorithm to refine the collision grid. It first initializes a hollow grid with all voxels unoccupied (`@splat(@splat(0))`) and then iterates over each quad, shifting it slightly based on its normal vector to avoid edge cases. It rasterizes both triangles of the quad into the hollow grid using the `rasterize` function. After rasterizing all quads, it initializes a full grid where all voxels are initially marked as occupied (`@splat(@splat(allOnes))`). It then uses a floodfill queue to propagate the collision information from the edges inward, ensuring that only connected components of the model are considered in the final collision grid. The floodfill algorithm uses a `CircularBufferQueue` to manage the queue operations efficiently.

## Code Example
```zig
pub fn init(quadInfos: []const QuadInfo) ModelIndex {
	return initWithCollisionModel(quadInfos, null);
}
```

## Related Questions
- What is the purpose of the `init` function?
- How does the `rasterize` function determine which voxels are occupied by a triangle?
- What algorithm is used to refine the collision grid in `generateCollision`?
- What is the role of the `edgeInterp` function in the rasterization process?
- How is the normal vector utilized in the collision detection logic?
- What is the significance of the floodfill queue in generating the final collision grid?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_2*
