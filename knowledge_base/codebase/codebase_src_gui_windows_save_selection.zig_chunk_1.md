# [medium/codebase_src_gui_windows_save_selection.zig] - Chunk 1

**Type:** implementation
**Keywords:** arena allocator, directory iteration, binary serialization, button creation, error handling, list layout
**Symbols:** onOpen, onClose, buttonNameArena, VerticalList, Label, Button, readingSaves, dir, iterator, entry, worldInfoPath, worldInfo, worldList, WorldInfo, row, HorizontalList, fileExplorerIcon, deleteIcon, openWorldWrap, openFolder, deleteWorld, window, gui
**Concepts:** GUI window management, world selection, file I/O, memory allocation

## Summary
Handles the logic for opening and closing a save selection window in the Cubyz GUI.

## Explanation
The chunk defines two main functions, `onOpen` and `onClose`, which manage the lifecycle of a save selection window. `onOpen` initializes a button name arena allocator, creates a vertical list layout, adds labels and buttons for creating new worlds, reads world information from files in the 'saves' directory, sorts the world list by last used time, and populates the list with buttons for each world. `onClose` cleans up resources by freeing allocated memory, deinitializing allocators, and deinitializing components.

## Code Example
```zig
pub fn onClose() void {
	for (worldList.items) |worldInfo| {
		main.globalAllocator.free(worldInfo.fileName);
		main.globalAllocator.free(worldInfo.name);
	}
	worldList.clearAndFree(main.globalAllocator);
	buttonNameArena.deinit();
	if (window.rootComponent) |*comp| {
		comp.deinit();
	}
}
```

## Related Questions
- What does the `onOpen` function do?
- How are world information files read in the `onOpen` function?
- What is the purpose of the `buttonNameArena` allocator?
- How are errors handled when reading directories or files in the `onOpen` function?
- What steps are taken to clean up resources in the `onClose` function?
- How is the world list sorted by last used time?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_selection.zig_chunk_1*
