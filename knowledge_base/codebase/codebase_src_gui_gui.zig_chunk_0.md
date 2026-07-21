# [hard/codebase_src_gui_gui.zig] - Chunk 0

**Type:** implementation
**Keywords:** window list, command execution, concurrent queue, initialization, deinitialization
**Symbols:** windowList, hudWindows, openWindows, selectedWindow, selectedTextInput, hoveredAWindow, reorderWindows, hideGui, scale, hoveredItemSlot, GuiCommandQueue, GuiCommandQueue.Action, GuiCommandQueue.Command, GuiCommandQueue.init, GuiCommandQueue.deinit, GuiCommandQueue.scheduleCommand, GuiCommandQueue.executeCommands, GuiCommandQueue.executeOpenWindowCommand, GuiCommandQueue.executeCloseWindowCommand, initWindowList, deinitWindowList, GuiWindow, tooltip, windowlist
**Concepts:** GUI window management, command queue, window lifecycle

## Summary
Manages GUI windows and their lifecycle, including initialization, deinitialization, and command execution.

## Explanation
This chunk defines the core logic for managing GUI windows in the Cubyz engine. It includes structures for window management, such as `GuiCommandQueue`, which handles opening and closing commands through a concurrent queue. The `initWindowList` function initializes various lists and sets up window functions based on imported configurations. The `deinitWindowList` function cleans up resources when GUI components are no longer needed.

Key functionalities include adding windows to the list, executing open and close commands, and updating window positions. The `GuiCommandQueue` struct has an `Action` enum with values `open`, `openModal`, and `close`. The `Command` struct includes a window pointer of type `*GuiWindow` and an action of type `Action`. The `init` function initializes the command queue with a capacity of 16 using `main.globalAllocator`. The `deinit` function deinitializes the command queue. The `scheduleCommand` function pushes a command into the queue, and the `executeCommands` function processes commands by popping them from the queue and executing the corresponding actions (`open`, `openModal`, or `close`). The `executeOpenWindowCommand` function handles opening a window by reordering it in the open windows list and calling its `onOpenFn`. The `executeCloseWindowCommand` function handles closing a window by removing it from the open windows list and calling its `onCloseFn`.

The `initWindowList` function initializes `windowList`, `hudWindows`, and `openWindows` using `main.globalAllocator`. It then iterates over the imported window configurations, sets their IDs, adds them to the window list, and assigns functions like `render`, `update`, `updateSelected`, `updateHovered`, `onOpen`, and `onClose` if they exist. The `deinitWindowList` function clears and frees `windowList`, deinitializes `hudWindows` and `openWindows`, and deinitializes the command queue.

## Code Example
```zig
fn init() void {
		commands = .init(main.globalAllocator, 16);
	}
```

## Related Questions
- How are GUI windows initialized in the Cubyz engine?
- What is the purpose of the `GuiCommandQueue` struct?
- How does the engine handle opening and closing GUI windows?
- What functions are responsible for updating window positions?
- How are window functions set up during initialization?
- What resources are cleaned up when deinitializing GUI components?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_0*
