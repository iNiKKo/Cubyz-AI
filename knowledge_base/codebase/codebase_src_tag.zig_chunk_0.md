# [easy/codebase_src_tag.zig] - Chunk 0

**Type:** api
**Keywords:** enum, hashmap, allocator, string manipulation, error handling
**Symbols:** Tag, Tag.air, Tag.fluid, Tag.sbbChild, Tag.fluidPlaceable, Tag.chiselable, Tag.playerModel, tagList, tagIds
**Concepts:** tag management, Zon file parsing, memory allocation

## Summary
Manages tags for Cubyz engine, including initialization, resetting, retrieval, and loading from Zon files.

## Explanation
This chunk defines the `Tag` enum (`u32`-backed) with 6 built-in values: `air = 0`, `fluid = 1`, `sbbChild = 2`, `fluidPlaceable = 3`, `chiselable = 4`, `playerModel = 5`, plus an open `_` catch-all for dynamically-created tags. `find(tag)` returns the existing `Tag` for a string if `tagIds` already has one; otherwise it creates a new one (index = current `tagList` length), duplicates the string into `main.worldArena`, and registers it in both `tagList` and `tagIds`. `loadTagsFromZon` converts a Zon array into a `[]Tag`: for each element that isn't a string, it logs an error (`"Tag array field {s} has incorrect type, expected string"`) and falls back to `Tag.find("incorrect")` instead of failing the whole load. `get(tag)` looks up a tag by name without creating one (returns `null` if absent). `resetTags`/`initTags` reset/verify the tag registry. The `main.worldArena` allocator is used for all string/hashmap memory.

## Code Example
```zig
pub fn initTags() void {
	inline for (comptime std.meta.fieldNames(Tag)) |tag| {
		std.debug.assert(Tag.find(tag) == @field(Tag, tag));
	}
}
```

## Related Questions
- How do you initialize the tags in the Cubyz engine?
- What is the purpose of the `resetTags` function?
- How does the `find` function work if a tag is not found?
- What type of allocator is used for memory management in this chunk?
- How are tags loaded from Zon files?
- What is the role of the `tagList` variable in this code?

*Source: unknown | chunk_id: codebase_src_tag.zig_chunk_0*
