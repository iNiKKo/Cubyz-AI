# [easy/codebase_src_gui_windows_chest.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, item slots, inventory management, deinitialization, component creation
**Symbols:** window, padding, itemSlots, deinit, openInventory, setInventory, onOpen, onClose
**Concepts:** GUI window management, inventory display, component initialization and deinitialization

## Summary
Manages the GUI window for a chest inventory, initializing and deinitializing item slots and handling open/close events.

## Explanation
This chunk defines the logic for a GUI window that represents a chest inventory: `contentSize = {64*10, 64*3}`, `scale = 0.75`, positioned attached above the player's inventory window. The `deinit` function clears and frees the memory used by item slots. The `setInventory` function sets the currently selected inventory. The `onOpen` function creates a **2-row by 10-column grid of item slots (20 total)**, one `HorizontalList` row per `y` (0-1), 10 slots per row indexed `y*10 + x`, bound to `openInventory`. The `onClose` function deinitializes the open inventory, clears item slots while retaining capacity, and deinitializes the root component of the window.

## Code Example
```zig
pub fn deinit() void {
	itemSlots.clearAndFree(main.globalAllocator);
}
```

## Related Questions
- How is the chest inventory window initialized?
- What function sets the currently selected inventory?
- How are item slots created when the inventory window opens?
- What happens to the open inventory when the window closes?
- How is memory managed for item slots in this module?
- What is the role of the `padding` constant in the GUI layout?

*Source: unknown | chunk_id: codebase_src_gui_windows_chest.zig_chunk_0*
