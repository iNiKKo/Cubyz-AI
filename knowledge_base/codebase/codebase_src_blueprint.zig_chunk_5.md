# [hard/codebase_src_blueprint.zig] - Chunk 5

**Type:** implementation
**Keywords:** filtering, logical operations, union types, string parsing, memory management
**Symbols:** Mask, Mask.AndList, Mask.OrList, Mask.entries, Mask.or_, Mask.and_, Mask.inverse, Mask.tag, Mask.property, Mask.Entry, Mask.Entry.inner, Mask.Entry.isInverse, Mask.Entry.Inner, Mask.Entry.Inner.block, Mask.Entry.Inner.blockType, Mask.Entry.Inner.blockTag, Mask.Entry.Inner.blockProperty, Mask.Entry.Inner.Property, Mask.Entry.Inner.initFromString, Mask.Entry.Inner.match, Mask.Entry.initFromString, Mask.Entry.match, Mask.initFromString, Mask.deinit, Mask.clone, Mask.match
**Concepts:** block filtering, logical expressions, union types, string parsing

## Summary
The Mask struct defines a complex filtering mechanism for blocks based on various criteria like type, tag, and properties.

## Explanation
The Mask struct defines a complex filtering mechanism for blocks based on various criteria like type, tag, and properties. It includes nested structures like AndList and OrList to manage these combinations. The Entry struct represents individual filter criteria, which can be inverted using the '!' operator. The Inner union within Entry handles different types of block properties such as type, tag, and specific property checks.

The Mask struct uses constants for logical operations: `or_` is '|', `and_` is '&', `inverse` is '!', `tag` is '$', and `property` is '@'. The `initFromString` method parses string specifications into Mask instances, handling different types of block properties. The `match` methods evaluate whether a given block meets the specified conditions. The deinit method ensures proper memory cleanup, and clone creates a deep copy of the Mask instance.

The Entry struct includes an inner union that can represent block type, block tag, or specific property checks. The `initFromString` method in Entry parses string specifications into individual entries, handling inversion with '!' and different types of properties. The `match` method evaluates whether a block matches the specified criteria.

The Mask struct's methods include `initFromString`, which parses a string into a Mask instance, and `deinit`, which cleans up memory. The `clone` method creates a deep copy of the Mask instance. The `match` method evaluates whether a given block meets the specified conditions.

The Inner union within Entry has four possible types: block, blockType, blockTag, and blockProperty. The block type is represented by a Block struct with typ and data fields. The blockType is represented by a u16 value. The blockTag is represented by a Tag struct. The blockProperty is represented by an enum of boolean properties of the Block struct.

The `initFromString` method in Entry handles different types of block properties based on the first character of the specifier: '!' for inversion, '$' for tags, '@' for properties, and default for block-like specifications. It returns an error if the tag or property is not found.

The `parseBlockLike` function parses block-like specifications into Mask.Entry.Inner instances, handling errors for data parsing and ID parsing.

## Code Example
```zig
fn initFromString(specifier: []const u8) !Entry {
			const isInverse = specifier[0] == '!';
			const entry = try Inner.initFromString(specifier[if (isInverse) 1 else 0..]);
			return .{.inner = entry, .isInverse = isInverse};
		}
```

## Related Questions
- How does the Mask struct initialize from a string?
- What are the possible inner types for a Mask Entry?
- How does the Mask handle inverse conditions?
- What error can occur when parsing block-like specifications?
- How is memory managed in the Mask struct?
- How does the Mask evaluate whether a block matches its criteria?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_5*
