# [hard/codebase_src_chunk.zig] - Chunk 2

**Type:** implementation
**Keywords:** struct, method, coordinate system, distance calculation, equality check
**Symbols:** ChunkPosition, ChunkPosition.wx, ChunkPosition.wy, ChunkPosition.wz, ChunkPosition.voxelSize, ChunkPosition.initFromWorldPos, ChunkPosition.hashCode, ChunkPosition.equals, ChunkPosition.getMinDistanceSquared, ChunkPosition.getMinDistanceSquaredFloat, ChunkPosition.getMaxDistanceSquared, ChunkPosition.getCenterDistanceSquared, ChunkPosition.getPriority, BlockPos, BlockPos.z, BlockPos.y, BlockPos.x, BlockPos.fromCoords, BlockPos.fromWorldCoords, BlockPos.fromLodCoords, BlockPos.fromIndex, BlockPos.toIndex, BlockPos.neighbor
**Concepts:** chunk management, block positioning

## Summary
Defines structures and methods for handling chunk positions and block positions within those chunks.

## Explanation
This chunk defines two main structures: `ChunkPosition` and `BlockPos`. The `ChunkPosition` struct represents the position of a chunk in the world, including its voxel size (`voxelSize`). It provides methods for initializing from world coordinates (`initFromWorldPos`), calculating hash codes (`hashCode`), checking equality with other positions (`equals`), determining distances to a player's position (`getMinDistanceSquared`, `getMinDistanceSquaredFloat`, `getMaxDistanceSquared`, `getCenterDistanceSquared`), and calculating priority (`getPriority`). The `BlockPos` struct represents the position of a block within a chunk using relative coordinates (`x`, `y`, `z`). It includes methods for converting between different coordinate systems (`fromCoords`, `fromWorldCoords`, `fromLodCoords`), accessing neighboring blocks (`neighbor`), and converting to/from an index (`fromIndex`, `toIndex`). The `initFromWorldPos` method initializes a `ChunkPosition` from world coordinates using a mask calculated from the voxel size and chunk size. The `hashCode` method calculates a hash code for a `ChunkPosition`. The `equals` method checks if two `ChunkPosition` instances are equal, considering different types of inputs. The `getMinDistanceSquared`, `getMinDistanceSquaredFloat`, `getMaxDistanceSquared`, and `getCenterDistanceSquared` methods calculate squared distances from the chunk's center to a player's position in different ways. The `getPriority` method calculates the priority of a chunk based on its distance to the player and its voxel size. The `BlockPos` struct uses packed fields for coordinates, allowing efficient storage. The `fromCoords`, `fromWorldCoords`, and `fromLodCoords` methods convert between different coordinate systems. The `neighbor` method returns the neighboring block position and indicates whether it is in the same chunk or a neighboring chunk.

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
