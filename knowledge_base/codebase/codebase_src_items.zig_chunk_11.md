# [hard/codebase_src_items.zig] - Chunk 11

**Type:** api
**Keywords:** ZonElement, ItemStack, BaseItemIndex, pixel sources, recipes
**Symbols:** parseRecipeItem, registerRecipes
**Concepts:** procedural item registration, recipe parsing

## Summary
Handles procedural item registration and recipe parsing from Zon data.

## Explanation
This chunk processes Zon elements to register procedural items and parse recipes. It iterates over disabled, optional, and parameter matrices for items, loading pixel sources and overlays. It also registers these items in a list and maps their IDs to indices. For recipes, it parses each recipe element, handling errors by logging them and skipping problematic recipes.

## Code Example
```zig
fn parseRecipeItem(zon: ZonElement) !ItemStack {
	var id = zon.as([]const u8, "");
	id = std.mem.trim(u8, id, &std.ascii.whitespace);
	var result: ItemStack = .{.amount = 1};
	if (std.mem.indexOfScalar(u8, id, ' ')) |index| blk: {
		result.amount = std.fmt.parseInt(u16, id[0..index], 0) catch break :blk;
		id = id[index + 1 ..];
		id = std.mem.trim(u8, id, &std.ascii.whitespace);
	}
	result.item = .{.baseItem = BaseItemIndex.fromId(id) orelse return error.ItemNotFound};
	return result;
}
```

## Related Questions
- How does the chunk handle errors when parsing recipes?
- What is the maximum number of entries allowed in the disabled array?
- How are pixel sources and overlays loaded for procedural items?
- What data structure is used to store parameter matrices for procedural items?
- How are procedural item IDs mapped to indices?
- What is the role of the `parseRecipeItem` function in this chunk?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_11*
