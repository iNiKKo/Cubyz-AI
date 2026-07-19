# [hard/codebase_src_server_storage.zig] - Chunk 3

**Type:** serialization
**Keywords:** compression, serialization, binary data, mutex locking, block entities
**Symbols:** ChunkCompression, ChunkCompression.ChunkCompressionAlgo, ChunkCompression.BlockEntityCompressionAlgo, ChunkCompression.Target, ChunkCompression.storeChunk, ChunkCompression.loadChunk, ChunkCompression.compressBlockData, ChunkCompression.decompressBlockData, ChunkCompression.compressBlockEntityData, ChunkCompression.decompressBlockEntityData
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
Handles chunk compression and decompression for storage to disk or client transmission.

## Explanation
The `ChunkCompression` struct provides methods to compress and decompress chunk data, including both block data and block entity data. It supports multiple compression algorithms tailored to different scenarios, such as lossless and lossy compression based on the palette size and block properties. The specific compression algorithms are defined in enums: `ChunkCompressionAlgo` (e.g., `deflate_with_position_no_block_entities`, `uniform`) and `BlockEntityCompressionAlgo` (`raw`). The `storeChunk` function compresses a chunk's data into a byte slice suitable for storage or transmission, while the `loadChunk` function decompresses this data back into a chunk structure. The `compressBlockData` method handles the compression of block data using various algorithms, optimizing for different cases like uniform palettes or large palettes. Similarly, `decompressBlockData` manages the decompression of block data based on the specified algorithm. The `compressBlockEntityData` and `decompressBlockEntityData` methods manage the serialization and deserialization of block entity data, ensuring that entities are correctly stored and loaded with their respective states. Additionally, thread safety is ensured through mutex locking when handling block entities.

The `ChunkCompressionAlgo` enum includes the following algorithms:
- `deflate_with_position_no_block_entities`
- `deflate_no_block_entities`
- `uniform`
- `deflate_with_8bit_palette_no_block_entities`
- `deflate`
- `deflate_with_8bit_palette`

The `BlockEntityCompressionAlgo` enum includes the following algorithm:
- `raw`

During compression, if the palette length is 1, the `uniform` algorithm is used. If the palette length is less than 256, a lossy compression with an 8-bit palette is applied. For larger palettes, a standard deflate algorithm is used. The decompression process reverses these steps based on the specified algorithm.

Block entity data is serialized and deserialized using the `compressBlockEntityData` and `decompressBlockEntityData` methods, respectively. These methods ensure that block entities are correctly stored and loaded with their respective states. Thread safety is maintained through mutex locking when handling block entities.

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
- What specific compression algorithms are supported by ChunkCompression?
- How does ChunkCompression handle block entity data during storage and loading?
- What is the role of the `allowLossy` parameter in compressBlockData?
- How does ChunkCompression ensure thread safety when handling block entities?
- Can you explain the process of decompressing block data in more detail, including specific algorithms used?
- What error handling is implemented during the decompression of block entity data?

*Source: unknown | chunk_id: codebase_src_server_storage.zig_chunk_3*
