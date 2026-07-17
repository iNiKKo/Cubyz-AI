# [medium/codebase_mods_cubyz_rotations_stairs.zig] - Chunk 1

**Type:** implementation
**Keywords:** model index, quad info, collision boxes, texture slots, neighbor directions, greedy meshing, visibility arrays, subblock masks, UV coordinates, stack allocator, defer cleanup, Vec3f splat, hasSubBlock check, mergeFaces call, Box struct literal
**Symbols:** createBlockModel, QuadInfo, GreedyFaceInfo, Box, Neighbor, hasSubBlock, mergeFaces, subBlockMask, main.ListManaged, main.models.Model.initWithCollisionModel, main.physics.collision.Box
**Concepts:** block model creation, neighbor texture handling, collision box generation, greedy meshing, visibility culling, UV coordinate mapping, stack allocator management, mask-based subblock iteration

## Summary
Implements block model creation with neighbor texture handling and collision box generation.

## Explanation
The chunk defines a public function createBlockModel that takes a Block, a pointer to u16 (modelIndex), and a ZonElement. It first checks if modelIndex is already set; if so it returns the existing index. Otherwise it iterates over 0..256 (block indices). For each block it initializes a managed list of QuadInfo quads using main.ListManaged(main.models.QuadInfo) with a stack allocator, deferring deinit. It then loops over Neighbor.iterable to process each neighbor direction. For each neighbor it computes absolute texture components xComponent and yComponent via @abs(neighbor.textureX()) and @abs(neighbor.textureY()), and the normal vector from neighbor.relX/relY/relZ. The zComponent is derived as @abs(normal). A two-element array zMap is constructed: if the sum of normal components exceeds 0 it becomes [{splat(0), splat(1)}] else [{splat(1), splat(0)}]. Two visibility arrays visibleFront and visibleMiddle are declared undefined. Nested loops over x and y (0..2) compute xSplat and ySplat as @splat(@intCast(x)) and @splat(@intCast(y)). Positions posFront and posBack are calculated using component splats and zMap entries. hasSubBlock is called for each position with the block index i cast to u32; results populate visibleFront[x][y] and visibleMiddle[x][y] (middle visibility is true only if front is false and subblock exists). The neighbor texture components are converted to Vec3f via @floatFromInt. A faces array of GreedyFaceInfo is declared undefined. mergeFaces is called with visibleFront and &faces; the returned frontFaces are iterated. For each face, xLower and xUpper are computed as @abs(xAxis) multiplied by splatted min/max values from face.min[0]/face.max[0]; if xAxis sum is negative std.mem.swap swaps them. Similarly yLower/yUpper are derived from yAxis and face.min[1]/face.max[1] with swap on negative sum. zValue is @floatFromInt(zComponent*zMap[1]). Neighbor-specific transformations apply: for dirNegX or dirPosY, min/max x coordinates are mirrored via 1 - value and a temporary swap variable; for dirUp, both min and max are inverted using Vec2f{1,1} - face.min/max and then swapped; for dirDown, only the y component is mirrored with a swap. A QuadInfo struct literal is appended to quads containing normal = zAxis, corners computed as xLower+yLower+zValue etc., cornerUV derived from face min/max values, and textureSlot = neighbor.toInt(). The same pattern repeats for middleFaces using visibleMiddle; here zValue uses splat(0.5) instead of the full component. After processing all neighbors, a managed list boxes of main.physics.collision.Box is initialized with capacity 4 (deferred deinit). A remaining mask variable holds ~@intCast(i). Nested loops over dx/dy/dz (0..2) compute subBlockMask for each offset; if remaining & mask == 0 the iteration continues. Offsets are incremented by 1 to form dx2/dy2/dz2. Additional logic expands masks when dz==0 and remaining has bit at mask<<1, similarly for dy and dx using shifts of 2 and 4 respectively; in those cases dx2/dy2/dz2 is incremented and the mask bits are ORed with their shifted counterparts. A Box struct literal is appended via appendAssumeCapacity with min = @floatFromInt(@Vector{dx,dy,dz}) / splat(2) and max = @floatFromInt(@Vector{dx2,dy2,dz2}) / splat(2). remaining is updated by masking out the processed bits. After all loops, main.models.Model.initWithCollisionModel is called with quads.items and boxes.items; if i == 0 the returned index is stored into modelIndex.

## Related Questions
- How does createBlockModel handle an already-set modelIndex?
- What is the purpose of the zMap array in neighbor processing?
- How are front and middle face visibilities computed differently?
- Why are dx2/dy2/dz2 incremented when certain mask bits are set?
- Which neighbor directions trigger UV mirroring transformations?
- How does the chunk ensure quad normals align with block faces?
- What role does appendAssumeCapacity play in box list construction?
- Is there any error handling for failed subblock checks?
- How is the final collision model constructed from quads and boxes?
- Does the chunk allocate memory on the heap or stack?
- Are texture slots mapped directly to neighbor enum values?
- What happens if hasSubBlock returns false for all neighbors?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_stairs.zig_chunk_1*
