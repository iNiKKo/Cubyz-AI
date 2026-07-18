# [hard/codebase_src_server_storage.zig] - Chunk 3

**Type:** serialization
**Keywords:** compression, serialization, binary data, mutex locking, block entities
**Symbols:** ChunkCompression, ChunkCompression.ChunkCompressionAlgo, ChunkCompression.BlockEntityCompressionAlgo, ChunkCompression.Target, ChunkCompression.storeChunk, ChunkCompression.loadChunk, ChunkCompression.compressBlockData, ChunkCompression.decompressBlockData, ChunkCompression.compressBlockEntityData, ChunkCompression.decompressBlockEntityData
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
Handles chunk compression and decompression for storage to disk or client transmission.

## Explanation
The `ChunkCompression` struct provides methods to compress and decompress chunk data, including both block data and block entity data. It supports multiple compression algorithms tailored to different scenarios, such as lossless and lossy compression based on the palette size and block properties. The `storeChunk` function compresses a chunk's data into a byte slice suitable for storage or transmission, while the `loadChunk` function decompresses this data back into a chunk structure. The `compressBlockData` and `decompressBlockData` methods handle the compression and decompression of block data using various algorithms, optimizing for different cases like uniform palettes or large palettes. Similarly, `compressBlockEntityData` and `decompressBlockEntityData` manage the serialization and deserialization of block entity data, ensuring that entities are correctly stored and loaded with their respective states.

## Code Example
```zig
pub fn storeChunk(allocator: main.heap.NeverFailingAllocator, ch: *chunk.Chunk, comptime target: Target, allowLossy: bool) []const u8 {
	var writer = BinaryWriter.init(allocator);

	compressBlockData(ch, allowLossy, &writer);
	compressBlockEntityData(ch, target, &writer);

	return writer.data.toOwnedSlice();
}
```

## Related Questions
- What are the different compression algorithms supported by ChunkCompression?
- How does ChunkCompression handle block entity data during storage and loading?
- What is the role of the `allowLossy` parameter in compressBlockData?
- How does ChunkCompression ensure thread safety when handling block entities?
- Can you explain the process of decompressing block data in more detail?
- What error handling is implemented during the decompression of block entity data?
- How does ChunkCompression optimize storage for chunks with uniform palettes?
- What are the differences between `storeChunk` and `loadChunk` methods?
- Can you describe the use of mutexes in the compression and decompression process?
- How does ChunkCompression manage memory allocation during compression and decompression?

*Source: unknown | chunk_id: codebase_src_server_storage.zig_chunk_3*
