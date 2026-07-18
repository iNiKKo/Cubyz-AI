# [hard/codebase_src_chunk.zig] - Chunk 2

**Type:** implementation
**Keywords:** struct, method, coordinate system, distance calculation, equality check
**Symbols:** ChunkPosition, ChunkPosition.wx, ChunkPosition.wy, ChunkPosition.wz, ChunkPosition.voxelSize, ChunkPosition.initFromWorldPos, ChunkPosition.hashCode, ChunkPosition.equals, ChunkPosition.getMinDistanceSquared, ChunkPosition.getMinDistanceSquaredFloat, ChunkPosition.getMaxDistanceSquared, ChunkPosition.getCenterDistanceSquared, ChunkPosition.getPriority, BlockPos, BlockPos.z, BlockPos.y, BlockPos.x, BlockPos.fromCoords, BlockPos.fromWorldCoords, BlockPos.fromLodCoords, BlockPos.fromIndex, BlockPos.toIndex, BlockPos.neighbor
**Concepts:** chunk management, block positioning

## Summary
Defines structures and methods for handling chunk positions and block positions within those chunks.

## Explanation
This chunk defines two main structures: `ChunkPosition` and `BlockPos`. The `ChunkPosition` struct represents the position of a chunk in the world, including its voxel size. It provides methods for initializing from world coordinates, calculating hash codes, checking equality with other positions, and determining distances to a player's position. The `BlockPos` struct represents the position of a block within a chunk using relative coordinates. It includes methods for converting between different coordinate systems, accessing neighboring blocks, and converting to/from an index.

## Code Example
```zig
pub fn initFromWorldPos(pos: Vec3i, voxelSize: u31) ChunkPosition {
	const mask = ~@as(i32, voxelSize*chunkSize - 1);
	return .{.wx = pos[0] & mask, .wy = pos[1] & mask, .wz = pos[2] & mask, .voxelSize = voxelSize};
}
```

## Related Questions
- How is a `ChunkPosition` initialized from world coordinates?
- What methods does the `ChunkPosition` struct provide for distance calculations?
- How does the `BlockPos` struct convert between different coordinate systems?
- What is the purpose of the `getMinDistanceSquaredFloat` method in `ChunkPosition`?
- How are neighboring blocks accessed using the `BlockPos` struct?
- What is the role of the `voxelSize` field in the `ChunkPosition` struct?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_2*
