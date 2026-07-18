# [hard/codebase_src_gui_gui.zig] - Chunk 2

**Type:** api
**Keywords:** window management, GUI scaling, duplicate detection, command scheduling, text input selection
**Symbols:** getWindowById, updateGuiScale, addWindow, openWindow, openWindowFromRef, toggleWindow, openHud, openWindowCallback, closeWindowFromRef, closeWindow, isWindowOpen, setSelectedTextInput
**Concepts:** GUI window management, window lifecycle, error handling, command queue

## Summary
Handles GUI window management, including opening, closing, toggling, and scaling windows.

## Explanation
This chunk manages the lifecycle of GUI windows within the application. It includes functions to get a window by ID, update the GUI scale based on settings or screen size, add new windows while checking for duplicates, open and close windows with error handling if the window is not found, toggle window visibility, initialize HUD windows, and manage selected text inputs. The chunk also defines callback functions for opening windows and schedules commands for window actions using a command queue.

## Code Example
```zig
fn getWindowById(id: []const u8) ?*GuiWindow {
	for (windowList.items) |window| {
		if (std.mem.eql(u8, id, window.id)) {
			return window;
		}
	}
	std.log.err("Could not find window with id: {s}", .{id});
	return null;
}
```

## Related Questions
- How does the function `getWindowById` work?
- What is the purpose of the `updateGuiScale` function?
- How are duplicate windows handled in this code?
- What happens when a window is opened using `openWindowFromRef`?
- How is the GUI scale determined if no specific setting is provided?
- What does the `toggleWindow` function do?
- How are HUD windows initialized and managed?
- What is the role of the `openWindowCallback` function?
- How is a window closed using this codebase?
- How is the selected text input managed in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_2*
