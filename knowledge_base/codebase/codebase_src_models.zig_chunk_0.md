# [hard/codebase_src_models.zig] - Chunk 0

**Type:** implementation
**Keywords:** extern struct, enum, stack allocator, vector operations, bitcast, popcount, select, splat, round, floatFromInt
**Symbols:** Neighbor, FaceData, NeverFailingAllocator, Box, QuadInfo, ExtraQuadInfo, LightSample, gridSize, collisionGridSize, CollisionGridInteger, snapToGrid, Triangle, Quad, ModelIndex, QuadIndex, Model
**Concepts:** chunk meshing, quad indexing, neighbor detection, collision handling, grid snapping, face occlusion logic

## Summary
Defines model data structures, quad indexing, neighbor detection, and collision handling for chunk meshing.

## Explanation
The chunk declares imports from 'chunk.zig', 'graphics.zig', 'main', 'vec.zig' to access Neighbor, FaceData, renderer.chunk_meshing.FaceData, NeverFailingAllocator, Box, and vector types. It defines QuadInfo as an extern struct with normal, corners, cornerUV, textureSlot, opaqueInLod fields; includes methods normalVec, cornerVec, cornerUvVec returning Vec3f/Vec2f. ExtraQuadInfo is a struct holding faceNeighbor (?Neighbor), isFullQuad (bool), lightSampleListForAxisAlignedModels ([]LightSample), hasOnlyCornerVertices (bool), alignedNormalDirection (?Neighbor). LightSample is a struct with weights [4]u16 and offset Vec3i. Defines gridSize = 4096, collisionGridSize = 16, CollisionGridInteger as std.meta.Int(.unsigned, collisionGridSize). Implements snapToGrid(x: anytype) returning @TypeOf(x): computes T = @TypeOf(x), Vec = @Vector(x.len, std.meta.Child(T)), int = @as(@Vector(x.len, i32), @round(@as(Vec, x)*@splat(gridSize))), returns @as(Vec, @floatFromInt(int))/@splat(gridSize). Defines Triangle struct with vertex [3]usize, normal usize, uvs [3]usize. Defines Quad struct with vertex [4]usize, normal usize, uvs [4]usize. ModelIndex is an enum(u32) with _ and methods model(self: ModelIndex) returning *const Model via &models.items()[@intFromEnum(self)], add(self: ModelIndex, offset: u32) returning @enumFromInt(@intFromEnum(self)+offset). QuadIndex is an enum(u16) with _ and methods quadInfo(self: QuadIndex) returning *const QuadInfo via &quads.items[@intFromEnum(self)], extraQuadInfo(self: QuadIndex) returning *ExtraQuadInfo via &extraQuadInfos.items[@intFromEnum(self)]. Model struct contains min Vec3f, max Vec3f, internalQuads []QuadIndex, neighborFacingQuads [6][]QuadIndex, isNeighborOccluded [6]bool, allNeighborsOccluded bool, noNeighborsOccluded bool, hasNeighborFacingQuads bool, collision []Box. Implements getFaceNeighbor(quad: *const QuadInfo) ?chunk.Neighbor: initializes allZero and allOne as @Vector(3, bool) .{true,true,true}, loops over quad.corners updating allZero = allZero & (corner == @splat(0)) and allOne = allOne & (corner == @splat(1)), returns .dirNegX if allZero[0], .dirNegY if allZero[1], .dirDown if allZero[2], .dirPosX if allOne[0], .dirPosY if allOne[1], .dirUp if allOne[2], else null. Implements fullyOccludesNeighbor(quad: *const QuadInfo) bool: initializes zeroes and ones as @Vector(3, u32) .{0,0,0}, loops over quad.corners updating zeroes += @select(u32, corner == @splat(0), .{1,1,1}, .{0,0,0}) and ones += @select(u32, corner == @splat(1), .{1,1,1}, .{0,0,0}), computes hasTwoZeroes = zeroes == {2,2,2} and hasTwoOnes = ones == {2,2,2}, returns @popCount(@as(u3, @bitCast(hasTwoOnes))) == 2 and @popCount(@as(u3, @bitCast(hasTwoZeroes))) == 2. Implements initWithCollisionModel(quadInfos: []const QuadInfo, collisionModel: ?[]const Box) ModelIndex: allocates adjustedQuads via main.stackAllocator.alloc(QuadInfo, quadInfos.len), defers free, copies src.* to dest.*, snaps all corners and cornerUV values using snapToGrid, snaps normal using snapToGrid.

## Related Questions
- What is the purpose of the snapToGrid function and how does it handle different numeric types?
- How are neighbor directions determined in getFaceNeighbor based on corner coordinates?
- What condition must be met for fullyOccludesNeighbor to return true?
- Which fields in ModelIndex allow runtime lookup of a Model pointer?
- How is the QuadIndex enum used to access QuadInfo and ExtraQuadInfo data structures?
- What role does main.stackAllocator play in initWithCollisionModel's memory management?
- Why are corners and cornerUV values snapped before comparison in getFaceNeighbor?
- Does the Model struct store per-face occlusion information or only neighbor-level occlusion?
- How does ExtraQuadInfo support lighting calculations for axis-aligned models?
- What is the significance of CollisionGridInteger being defined as an unsigned integer type?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_0*
