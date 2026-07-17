# [medium/codebase_src_gui_windows_creative_inventory.zig] - Chunk 1

**Type:** implementation
**Keywords:** window initialization, content deinitialization, search input handling, cursor state preservation, inventory update
**Symbols:** deinitContent, filter, update
**Concepts:** GUI window management, inventory filtering, resource cleanup

## Summary
Handles the creative inventory GUI window's content initialization, deinitialization, and update logic.

## Explanation
This chunk manages the lifecycle of the creative inventory GUI window. It initializes the window content by setting up components and calculating sizes. The `deinitContent` function cleans up resources when the window is closed or reloaded. The `update` method checks for changes in the search input and triggers a filter if necessary. The `filter` function handles the logic to update the inventory display based on the current search string, preserving the cursor and selection state.

## Code Example
```zig
pub fn update() void {
	if (std.mem.eql(u8, searchInput.currentString.items, searchString)) return;
	filter();
}
```

## Related Questions
- What is the purpose of the `deinitContent` function?
- How does the `update` method determine if a filter should be applied?
- What steps are taken to preserve the cursor and selection state during filtering?
- What role does the `main.globalAllocator` play in this chunk?
- How is the window content size calculated in this code?
- What happens if the search input string changes?

*Source: unknown | chunk_id: codebase_src_gui_windows_creative_inventory.zig_chunk_1*
