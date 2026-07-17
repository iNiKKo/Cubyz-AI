# [hard/codebase_src_models.zig] - Chunk 2

**Type:** implementation
**Keywords:** flood fill, collision grid, quad rasterization, packed integer mask, voxel box extraction, normal aligned shift, circular buffer queue, 2D grid iteration, bit manipulation, triangle decomposition, solid voxel detection, grid initialization, neighbor expansion, diagonal neighbor push, box disable
**Symbols:** generateCollision, hollowGrid, allOnes, floodfillQueue, grid, triangle1, triangle2, shift, boxMin, boxMax, startZ, height, mask, min
**Concepts:** collision grid generation, flood-fill algorithm, quad rasterization, packed integer bit masks, voxel box extraction, normal-aligned shift, circular buffer queue, 2D grid iteration, bit manipulation, triangle decomposition

## Summary
Implements Model collision grid generation by rasterizing quad triangles into a 2D packed integer grid and then performing flood-fill to compute solid voxel boxes.

## Explanation
The chunk defines the private function generateCollision(self: *Model, modelQuads: []QuadInfo) void. It first allocates a hollowGrid initialized to zero using @splat(@splat(0)). For each quad in modelQuads it computes a shift vector based on normals that are exactly aligned with an axis (abs(normalVec()[i]) == 1.0 and the corner coordinate is integer after scaling). The shift is applied to all four corners, producing two triangles (triangle1 from corners 0-2, triangle2 from corners 1-3) which are passed to the rasterize helper along with the quad's normal vector. After processing all quads, a grid is initialized to allOnes (~0 as CollisionGridInteger). A floodfillQueue of type main.utils.CircularBufferQueue is created holding struct { x: usize, y: usize, val: CollisionGridInteger }. The queue is seeded by pushing every (x,y) in the collisionGridSize range; boundary cells receive a special mask allOnes while interior cells start with a value that has only the lowest bit set. The main loop pops front elements and computes newValue = oldValue & ~(~hollowGrid[elem.x][elem.y] & elem.val). If oldValue == newValue it continues; otherwise it updates grid[elem.x][elem.y] to newValue and pushes neighbors (x-1, x+1, y-1, y+1) with ~newValue mask. Additionally a diagonal neighbor is pushed using the expression ~newValue << 1 | ~newValue >> 1. After the flood-fill finishes, the chunk begins iterating over grid[x][y] while it is non-zero, extracting startZ via @ctz(grid[x][y]), computing height as min(@bitSizeOf(CollisionGridInteger) - startZ, @ctz(~grid[x][y] >> @intCast(startZ))), and forming a mask that isolates the contiguous block of set bits. It constructs boxMin = Vec3i{x, y, startZ} and boxMax with x+1, y+1, startZ+height. The chunk then calls canExpand(&grid, boxMin, boxMax, .x, mask) in a while loop to increment boxMax[0], similarly for .y, and finally disables the region via disableAll(&grid, boxMin, boxMax, mask). At the end of this function body (which is cut off by the provided snippet), it computes min = @as(Vec3f, @floatFromInt(boxMin))/@as(Vec3f, @splat(collisionGridSize)). The rasterize helper is invoked with triangle vertices and hollowGrid; its implementation is not in this chunk. canExpand and disableAll are called but their definitions are external.

## Related Questions
- What is the purpose of the shift vector computed inside generateCollision?
- How does rasterize contribute to building hollowGrid from model quads?
- Why are boundary cells given a special allOnes mask in the flood-fill initialization?
- What does the expression ~newValue << 1 | ~newValue >> 1 compute and why push it?
- Describe how startZ is derived from grid[x][y] using @ctz.
- How is height calculated to determine the vertical extent of a voxel box?
- What role do canExpand and disableAll play after extracting boxMin/boxMax?
- Why does generateCollision iterate over modelQuads instead of directly over Model's mesh data?
- Is hollowGrid ever mutated outside of rasterize calls within this function?
- How is the packed integer grid layout interpreted as a 3D voxel field?
- What happens to voxels that are not part of any quad after flood-fill completes?
- Where does the min Vec3f computed at the end of generateCollision get used?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_2*
