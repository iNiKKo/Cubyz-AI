# [hard/codebase_src_blueprint.zig] - Chunk 3

**Type:** implementation
**Keywords:** map creation, binary reading, binary writing, deflate compression, block manipulation
**Symbols:** makeGameIdToBlueprintIdMap, loadBlockPalette, storeBlockPalette, decompressBuffer, compressOutputBuffer, replace, apply
**Concepts:** blueprint management, block palette handling, data compression, block replacement, block transformation

## Summary
This chunk defines functions for managing game blueprints, including creating a map from game IDs to blueprint IDs, loading and storing block palettes, decompressing and compressing data buffers, replacing blocks based on conditions, and applying transformations to all blocks.

## Explanation
This chunk defines several functions for managing game blueprints, including creating a map from game IDs to blueprint IDs, loading and storing block palettes, decompressing and compressing data buffers, replacing blocks based on conditions, and applying transformations to all blocks. The `makeGameIdToBlueprintIdMap` function creates a map using an allocator by iterating over the blocks and assigning unique IDs. The `loadBlockPalette` function reads block names from a binary reader into a palette array by reading the size of each block name followed by the name itself. The `storeBlockPalette` function writes the block palette to a binary writer, logging each entry by converting the block ID and data to a string. The `decompressBuffer` function decompresses data using the deflate algorithm, ensuring the decompressed size matches the expected size. The `compressOutputBuffer` function compresses a buffer using the deflate algorithm. The public methods `replace` and `apply` modify the blueprint's blocks based on given conditions or transformations.

## Code Example
```zig
fn makeGameIdToBlueprintIdMap(self: Blueprint, allocator: NeverFailingAllocator) GameIdToBlueprintIdMapType {
	var gameIdToBlueprintId: GameIdToBlueprintIdMapType = .init(allocator.allocator);

	for (self.blocks.mem) |block| {
		const result = gameIdToBlueprintId.getOrPut(block) catch unreachable;
		if (!result.found_existing) {
			result.value_ptr.* = @intCast(gameIdToBlueprintId.count() - 1);
		}
	}

	return gameIdToBlueprintId;
}
```

## Related Questions
- How is the map from game IDs to blueprint IDs created?
- What does the `loadBlockPalette` function do?
- How is data decompressed in this chunk?
- What compression method is used by default?
- How are blocks replaced in a blueprint?
- What is the purpose of the `apply` method?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_3*
