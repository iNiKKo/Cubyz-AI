# [hard/codebase_src_models.zig] - Chunk 2

**Type:** implementation
**Keywords:** triangle rasterization, collision grid, voxel projection, floodfill, normal vector
**Symbols:** init, edgeInterp, solveDepth, rasterize, generateCollision
**Concepts:** model initialization, collision detection, voxelization, floodfill algorithm

## Summary
Handles model initialization and collision grid generation.

## Explanation
This chunk contains functions for initializing models, rasterizing triangles into a collision grid, and generating collision data from quad information. The `init` function initializes a model with collision data. The `rasterize` function projects a triangle onto a grid and marks voxels as occupied based on the triangle's normal vector. The `generateCollision` function processes each quad of the model, rasterizes its triangles, and applies a floodfill algorithm to refine the collision grid.

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
