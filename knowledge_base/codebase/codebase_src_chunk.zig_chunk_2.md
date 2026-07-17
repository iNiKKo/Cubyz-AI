# [hard/codebase_src_chunk.zig] - Chunk 2

**Type:** implementation
**Keywords:** ctz shift, modulo arithmetic, optional handling, ServerChunk super, packed struct u15, logarithmic term, AutoHashMapUnmanaged, Mutex zero-init, power-of-two assertion, voxelSizeShift log2_int
**Symbols:** ChunkPosition, ChunkPosition.hashCode, ChunkPosition.equals, ChunkPosition.getMinDistanceSquared, ChunkPosition.getMaxDistanceSquared, ChunkPosition.getCenterDistanceSquared, ChunkPosition.getPriority, BlockPos, BlockPos.fromCoords, BlockPos.fromWorldCoords, BlockPos.fromLodCoords, BlockPos.fromIndex, BlockPos.toIndex, BlockPos.neighbor, Chunk, Chunk.init
**Concepts:** hash computation, type-safe equals, distance clamping, packed coordinate storage, neighbor lookup, chunk initialization, memory pool allocation

## Summary
Defines ChunkPosition (hash, distance metrics), BlockPos (packed coords, neighbor lookup), and Chunk struct with initialization and data fields.

## Explanation
ChunkPosition exposes hashCode using ctz-based shift and modulo arithmetic; equals handles optional/pointer/ServerChunk types via super.pos or .pos; getMinDistanceSquared/getMaxDistanceSquared/getCenterDistanceSquared compute squared distances by clamping player position to the chunk half-width range with @mod/@splat adjustments; getPriority returns a float priority derived from min distance and voxel-size logarithmic term. BlockPos is a packed u15 struct holding x,y,z each as u5, providing static constructors fromCoords/fromWorldCoords/fromLodCoords (which shift by voxelSizeShift) and fromIndex/bitCast roundtrips; neighbor returns a tuple of the adjacent BlockPos and an enum indicating whether the neighbor lies in the same chunk or an adjacent one, using switch on dirUp/dirDown etc. Chunk is a struct containing pos:ChunkPosition, data:PaletteCompressedRegion(Block,chunkVolume)=undefined, width,u31; voxelSizeShift,u5; voxelSizeMask,i32; blockPosToEntityDataMap:AutoHashMapUnmanaged(BlockPos,BlockEntity); blockPosToEntityDataMapMutex:Mutex. The init function allocates via memoryPool.create(), asserts pos.voxelSize is a power of two and that wx/wy/wz are multiples of voxelSize, computes voxelSizeShift as log2_int(u31,pos.voxelSize), sets width to pos.voxelSize*chunkSize, voxelSizeMask to pos.voxelSize-1, zero-initializes the map and mutex with .{}, initializes self.data.init(), then returns self.

## Code Example
```zig
pub fn fromCoords(x: u5, y: u5, z: u5) BlockPos {
	return .{
		.x = x,
		.y = y,
		.z = z,
	};
}
```

## Related Questions
- How does ChunkPosition.hashCode handle the ctz shift and modulo 31 combination?
- What types are accepted by ChunkPosition.equals and how is each case resolved?
- Explain the @mod/@splat adjustment used in distance squared methods for player position.
- Which BlockPos constructor should be used when converting world coordinates to chunk-relative values?
- How does the neighbor method determine whether a direction stays within the same chunk or crosses into an adjacent one?
- What assertions are performed inside Chunk.init before any fields are assigned?
- Why is blockPosToEntityDataMap initialized with .{} instead of std.AutoHashMapUnmanaged.empty?
- Where is voxelSizeMask derived from and what does it represent in terms of bit masking?
- How does the init function compute width using chunkSize and pos.voxelSize?
- What is the purpose of @bitCast in BlockPos.fromIndex and toIndex methods?
- In getPriority, how are float casts applied to integer distance metrics before division?
- Does ChunkPosition.hashCode ever use a standard Zig hash function or does it rely entirely on manual arithmetic?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_2*
