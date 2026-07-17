# [hard/codebase_src_blueprint.zig] - Chunk 2

**Type:** serialization
**Keywords:** blueprint, block palette, compression, pattern, replacement, transformation
**Symbols:** Blueprint, blockPaletteSizeBytes, makeBlueprintIdToGameIdMap, makeGameIdToBlueprintIdMap, loadBlockPalette, storeBlockPalette, decompressBuffer, compressOutputBuffer, replace, apply, Pattern, weightSeparator, expressionSeparator, Entry, initFromString
**Concepts:** blueprint creation, block palette management, compression and decompression, pattern application

## Summary
Handles blueprint creation and manipulation, including block palette storage, compression, and pattern application.

## Explanation
This chunk defines the Blueprint struct with methods for creating, compressing, decompressing, and applying patterns to blueprints. It includes functions for converting between game IDs and blueprint IDs, loading and storing block palettes, and replacing or applying transformations to blocks within a blueprint. The Pattern struct is used to define block replacement rules based on weights.

## Code Example
```zig
fn compressOutputBuffer(_: Blueprint, allocator: NeverFailingAllocator, decompressedData: []u8) struct { mode: BlueprintCompression, data: []u8 }
```

## Related Questions
- How does the Blueprint struct handle block palette storage?
- What is the purpose of the makeGameIdToBlueprintIdMap function?
- How is compression applied to blueprint data in this chunk?
- What methods are available for replacing blocks within a blueprint?
- How is the Pattern struct used to define block replacement rules?
- What steps are involved in decompressing a blueprint buffer?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_2*
