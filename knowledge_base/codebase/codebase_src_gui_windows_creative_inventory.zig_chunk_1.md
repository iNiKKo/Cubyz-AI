# [medium/codebase_src_gui_windows_creative_inventory.zig] - Chunk 1

**Type:** implementation
**Keywords:** search input, selection management, content initialization, global allocator, string duplication
**Symbols:** filter
**Concepts:** inventory filtering, user input handling

## Summary
Handles filtering inventory items based on user input.

## Explanation
The `filter` function manages the process of filtering inventory items in a creative mode GUI. It starts by capturing the current selection start and cursor positions from the search input field. The existing search string is then freed, and a new copy of the current search input string is made using the global allocator. After freeing and duplicating the search string, the function calls `deinitContent` to clean up any previously displayed content and `initContent` to reinitialize the inventory display based on the new filter criteria. Finally, it restores the selection start and cursor positions to their previous states and selects the text in the search input field.

## Code Example
```zig
fn filter() void {
	const selectionStart = searchInput.selectionStart;
	const cursor = searchInput.cursor;

	main.globalAllocator.free(searchString);
	searchString = main.globalAllocator.dupe(u8, searchInput.currentString.items);
	deinitContent();
	initContent();

	searchInput.selectionStart = selectionStart;
	searchInput.cursor = cursor;

	searchInput.select();
}
```

## Related Questions
- What does the `filter` function do in the creative inventory GUI?
- How does the function handle user input for filtering items?
- What steps are taken to update the inventory display after a filter change?
- How is memory managed within the `filter` function?
- What happens if there is no current search string when filtering?
- How does the function ensure that the cursor position remains consistent after filtering?

*Source: unknown | chunk_id: codebase_src_gui_windows_creative_inventory.zig_chunk_1*
