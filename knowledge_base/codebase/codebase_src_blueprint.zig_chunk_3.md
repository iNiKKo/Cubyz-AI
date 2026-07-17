# [hard/codebase_src_blueprint.zig] - Chunk 3

**Type:** api
**Keywords:** string parsing, weighted entries, block types, logical operations, resource management
**Symbols:** Pattern, Pattern.weightSeparator, Pattern.expressionSeparator, Pattern.blocks, Pattern.Entry, Pattern.Entry.block, Pattern.Entry.chance, Pattern.initFromString, Pattern.deinit, Mask, Mask.AndList, Mask.OrList, Mask.entries, Mask.or_, Mask.and_, Mask.inverse, Mask.tag, Mask.property, Mask.Entry, Mask.Entry.inner, Mask.Entry.isInverse, Mask.Entry.Inner, Mask.Entry.Inner.block, Mask.Entry.Inner.blockType, Mask.Entry.Inner.blockTag, Mask.Entry.Inner.blockProperty, Mask.Entry.Inner.Property, Mask.Entry.Inner.initFromString, Mask.Entry.Inner.match, Mask.Entry.initFromString, Mask.Entry.match, Mask.initFromString
**Concepts:** pattern initialization, block matching, logical expressions

## Summary
Defines data structures and methods for pattern initialization and deinitialization, including parsing from strings.

## Explanation
The chunk defines a `Pattern` struct with an `initFromString` method that parses a string into weighted block entries. It also includes a `deinit` method to clean up resources. The `Mask` struct is defined with nested structures for handling logical expressions involving blocks, including parsing from strings and matching blocks against these expressions.

## Code Example
```zig
pub fn deinit(self: @This(), allocator: NeverFailingAllocator) void {
	self.blocks.deinit(allocator);
	allocator.free(self.blocks.items);
}
```

## Related Questions
- How does the `Pattern` struct initialize from a string?
- What is the purpose of the `deinit` method in the `Pattern` struct?
- How are logical expressions parsed and matched in the `Mask` struct?
- What types of block properties can be specified in a mask expression?
- How does the `initFromString` method handle invalid weights in a pattern string?
- What is the role of the `AliasTable` in the `Pattern` struct?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_3*
