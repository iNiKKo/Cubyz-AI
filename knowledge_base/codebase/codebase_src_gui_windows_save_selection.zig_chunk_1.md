# [medium/codebase_src_gui_windows_save_selection.zig] - Chunk 1

**Type:** implementation
**Keywords:** directory iteration, ZON file reading, GUI component creation, error handling, memory deallocation
**Symbols:** iterator, entry, worldInfoPath, worldInfo, worldList, row, list, window, buttonNameArena
**Concepts:** GUI management, file I/O, memory allocation, sorting

## Summary
Handles the logic for displaying and managing save selection in a GUI window.

## Explanation
This chunk manages the display of saved worlds in a GUI window. It iterates over the saves directory, reads world information from each subdirectory's 'world.zig.zon' file, and populates a list with buttons for each world. The list is sorted by the last used time, and each entry includes buttons to open, explore, or delete the world. Memory management is handled by freeing allocated strings and clearing lists when the window closes.

## Code Example
```zig
fn lessThan(_: void, lhs: WorldInfo, rhs: WorldInfo) bool {
			return rhs.lastUsedTime -% lhs.lastUsedTime < 0;
		}
```

## Related Questions
- How does the chunk handle errors when iterating over the saves directory?
- What file format is used to store world information?
- How are memory allocations managed in this chunk?
- What sorting algorithm is used for the list of worlds?
- How are buttons created and associated with actions in the GUI?
- What happens when a user closes the save selection window?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_selection.zig_chunk_1*
