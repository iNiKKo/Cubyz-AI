# [medium/codebase_src_gui_windows_creative_inventory.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, inventory slots, search filtering, window initialization, resource management
**Symbols:** window, padding, slotsPerRow, items, inventory, searchInput, searchString, lessThan, onOpen, onClose, hasMatchingTag, initContent, deinitContent, update
**Concepts:** GUI window management, item inventory display, user input handling, search functionality

## Summary
Handles the creative inventory GUI window, including initialization, content management, and user interactions.

## Explanation
This chunk manages the creative inventory GUI window in Cubyz. It initializes and deinitializes the window's components, handles search functionality, and updates the displayed items based on user input. The `onOpen` function sets up the window with a search bar and item slots by setting `searchString = "";` and calling `initContent()`. The `onClose` function cleans up resources by freeing memory allocated for `searchString`, deinitializing content, and releasing inventory resources. The `initContent` method initializes GUI components such as labels, text inputs, and item slots with padding values defined in the variable `padding: f32 = 8;`. It also populates the inventory with items matching search criteria using tags or direct string matches, sorts them according to a custom comparator function (`lessThan`), which compares items based on their folder count and ID if both are base items, otherwise it prioritizes base items. The exact number of slots per row is specified by `slotsPerRow: u32 = 10;`. The `deinitContent` method releases allocated memory by deinitializing components and freeing resources associated with the window's content. The `update` function checks for changes in the search input and triggers a filter to refresh the displayed items.

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
