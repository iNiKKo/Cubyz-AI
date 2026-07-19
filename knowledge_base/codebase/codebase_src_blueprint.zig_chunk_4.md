# [hard/codebase_src_blueprint.zig] - Chunk 4

**Type:** implementation
**Keywords:** string parsing, weight assignment, resource management, deinitialization, block initialization
**Symbols:** Pattern, Pattern.weightSeparator, Pattern.expressionSeparator, Pattern.blocks, Pattern.Entry, Pattern.Entry.block, Pattern.Entry.chance, Pattern.initFromString, Pattern.deinit
**Concepts:** block generation, weighted selection

## Summary
The `Pattern` struct defines a blueprint for generating blocks with weighted chances, initializing from a string and deinitializing properly.

## Explanation
The `Pattern` struct defines a blueprint for generating blocks with weighted chances, initializing from a string and deinitializing properly. The initialization process parses a string, splits it into specifiers based on separators (`weightSeparator = '%'` and `expressionSeparator = ','`), and assigns weights to blocks. If the weight is not a valid number or less than or equal to zero, an error is returned. The deinitialization method ensures that all allocated resources are properly released by calling `deinit` on the `blocks` table and freeing its items.

The data structure used to store block entries in the `Pattern` struct is an `AliasTable(Entry)`, where each entry contains a `block` of type `Block` and a `chance` of type `f32`. The `initFromString` method returns an error if the block ID is not found or if the weight is not a valid number or less than or equal to zero.

During initialization, the string is split into specifiers using the `expressionSeparator`, which is a comma (`,`). Each specifier can optionally include a weight separated by the `weightSeparator`, which is a percent sign (`%`). If no weight is specified, it defaults to 1.0. The total weight of all blocks is calculated, and each block's chance is determined by its weight divided by the total weight.

## Code Example
```zig
pub fn deinit(self: @This(), allocator: NeverFailingAllocator) void {
	self.blocks.deinit(allocator);
	allocator.free(self.blocks.items);
}
```

## Related Questions
- How does the `Pattern` struct initialize from a string?
- What is the purpose of the `weightSeparator` and `expressionSeparator` in the `Pattern` struct?
- How are weights assigned to blocks during initialization?
- What error handling is implemented in the `initFromString` method?
- How does the `deinit` method ensure proper resource management?
- What data structure is used to store block entries in the `Pattern` struct?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_4*
