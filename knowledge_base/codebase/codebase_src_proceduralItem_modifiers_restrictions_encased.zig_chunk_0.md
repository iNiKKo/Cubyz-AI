# [easy/codebase_src_proceduralItem_modifiers_restrictions_encased.zig] - Chunk 0

**Type:** implementation
**Keywords:** 3x3 grid check, tag matching, allocator usage, zon element parsing, error logging
**Symbols:** Encased, Encased.tag, Encased.amount, Encased.satisfied, Encased.loadFromZon, Encased.printTooltip
**Concepts:** item restrictions, surrounding item checks, tooltip generation

## Summary
The `Encased` struct and its methods handle restrictions based on surrounding items with specific tags.

## Explanation
The `Encased` struct represents a restriction where an item must be encased by a certain number of other items with a specified tag. The `satisfied` method checks if the given procedural item is surrounded by at least the required amount of items with the specified tag within a 3x3 grid centered on the item's position. The `loadFromZon` function creates an `Encased` instance from a ZonElement, extracting the tag and amount from the ZonElement data. If the tag field is missing, it logs an error and defaults to 'not specified'. The `printTooltip` method formats a tooltip string describing the encased restriction.

## Code Example
```zig
pub fn satisfied(self: *const Encased, proceduralItem: *const ProceduralItem, x: i32, y: i32) bool {
	var count: usize = 0;
	for ([_]i32{-1, 0, 1}) |dx| {
		for ([_]i32{-1, 0, 1}) |dy| {
			if ((proceduralItem.getItemAt(x + dx, y + dy) orelse continue).hasTag(self.tag)) count += 1;
		}
	}
	return count >= self.amount;
}
```

## Related Questions
- What does the `satisfied` method check for?
- How is the `Encased` struct loaded from a ZonElement?
- What happens if the 'tag' field is missing in the ZonElement?
- How does the `printTooltip` method format its output?
- What is the purpose of the 3x3 grid check in the `satisfied` method?
- How does the `Encased` struct handle memory allocation?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_encased.zig_chunk_0*
