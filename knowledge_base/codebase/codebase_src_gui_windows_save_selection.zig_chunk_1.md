# [medium/codebase_src_gui_windows_save_selection.zig] - Chunk 1

**Type:** implementation
**Keywords:** arena allocator, directory iteration, binary serialization, button creation, error handling, list layout
**Symbols:** onOpen, onClose, buttonNameArena, VerticalList, Label, Button, readingSaves, dir, iterator, entry, worldInfoPath, worldInfo, worldList, WorldInfo, row, HorizontalList, fileExplorerIcon, deleteIcon, openWorldWrap, openFolder, deleteWorld, window, gui
**Concepts:** GUI window management, world selection, file I/O, memory allocation

## Summary
Handles the logic for opening and closing a save selection window in the Cubyz GUI.

## Explanation
The chunk defines two main functions, `onOpen` and `onClose`, which manage the lifecycle of a save selection window. The `onOpen` function initializes a button name arena allocator (`buttonNameArena`) and creates a vertical list layout (`VerticalList`). It adds labels for selecting worlds based on whether the mode is singleplayer or multiplayer. Additionally, it handles errors encountered while opening the 'saves' directory and iterating over its contents. For each world directory found, it constructs a `worldInfoPath` to read world information from files in the form of `world.zig.zon`. If reading fails, an error message is logged with the specific error name. The function then populates a list (`worldList`) with `WorldInfo` items containing file names (`fileName`), last used times (`lastUsedTime`), and names (`name`). These items are sorted by their last used time before being added to the GUI layout as buttons, where each button corresponds to opening, exploring, or deleting a specific world. The exact structure of `WorldInfo` is defined as follows: `fileName`, `lastUsedTime`, and `name`. In contrast, the `onClose` function cleans up resources by freeing allocated memory for file names (`fileName`) and names (`name`), deinitializing allocators (`buttonNameArena`), and deinitializing components.

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
