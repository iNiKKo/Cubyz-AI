# [medium/codebase_src_gui_windows_creative_inventory.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, inventory slots, search filtering, window initialization, resource management
**Symbols:** window, padding, slotsPerRow, items, inventory, searchInput, searchString, lessThan, onOpen, onClose, hasMatchingTag, initContent, deinitContent, update
**Concepts:** GUI window management, item inventory display, user input handling, search functionality

## Summary
Handles the creative inventory GUI window, including initialization, content management, and user interactions.

## Explanation
This chunk manages the creative inventory GUI window in Cubyz. It initializes and deinitializes the window's components, handles search functionality, and updates the displayed items based on user input. The `onOpen` function sets up the window with a search bar and item slots, while `onClose` cleans up resources. The `initContent` method populates the inventory with items matching the search criteria, sorts them, and creates item slots for display. The `deinitContent` method releases allocated memory when the window is closed. The `update` function checks for changes in the search input and triggers a filter to refresh the displayed items.

## Code Example
```zig
pub fn onOpen() void {
	searchString = "";
	initContent();
}
```

## Related Questions
- What is the purpose of the `onOpen` function?
- How does the `initContent` method populate the inventory with items?
- What happens when the user changes the search input?
- How are items sorted in the creative inventory window?
- What resources are cleaned up by the `deinitContent` method?
- How is the GUI window positioned and sized?

*Source: unknown | chunk_id: codebase_src_gui_windows_creative_inventory.zig_chunk_0*
