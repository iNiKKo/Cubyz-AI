# [hard/codebase_src_server_storage.zig] - Chunk 2

**Type:** serialization
**Keywords:** reference counting, binary serialization, compression algorithms, chunk data, region files
**Symbols:** loadRegionFileAndIncreaseRefCount, ChunkCompression, ChunkCompression.ChunkCompressionAlgo, ChunkCompression.BlockEntityCompressionAlgo, ChunkCompression.Target, ChunkCompression.storeChunk, ChunkCompression.loadChunk, compressBlockData, decompressBlockData
**Concepts:** chunk meshing, entity ECS, world generation, binary serialization

## Summary
Handles loading and storing region files with reference counting and compressing/decompressing chunk data.

## Explanation
This chunk provides functions for managing region files, including loading them while increasing their reference count. It also defines a `ChunkCompression` struct that handles the compression and decompression of chunk data using various algorithms. The `storeChunk` function compresses block and block entity data into a binary format, while the `loadChunk` function reads this binary data back into a chunk structure. The compression algorithms include options for different levels of lossiness and palette usage.

## Code Example
```zig
pub fn loadRegionFileAndIncreaseRefCount(wx: i32, wy: i32, wz: i32, voxelSize: u31) *RegionFile {
	const compare = chunk.ChunkPosition{
		.wx = wx & ~@as(i32, RegionFile.regionSize*voxelSize - 1),
		.wy = wy & ~@as(i32, RegionFile.regionSize*voxelSize - 1),
		.wz = wz & ~@as(i32, RegionFile.regionSize*voxelSize - 1),
		.voxelSize = voxelSize,
	};
	const result = cache.findOrCreate(compare, cacheInit, RegionFile.increaseRefCount);
	return result;
}
```

## Related Questions
- How does the `loadRegionFileAndIncreaseRefCount` function determine the region file to load?
- What are the different compression algorithms available in the `ChunkCompression` struct?
- How is chunk data compressed and stored using the `storeChunk` function?
- What steps are involved in decompressing chunk data with the `decompressBlockData` function?
- What is the purpose of the reference counting mechanism in region file management?
- How does the `ChunkCompression` struct handle different levels of lossiness during compression?

*Source: unknown | chunk_id: codebase_src_server_storage.zig_chunk_2*
