# [hard/codebase_src_gui_gui.zig] - Chunk 2

**Type:** api
**Keywords:** window management, GUI scaling, duplicate detection, command scheduling, text input selection
**Symbols:** getWindowById, updateGuiScale, addWindow, openWindow, openWindowFromRef, toggleWindow, openHud, openWindowCallback, closeWindowFromRef, closeWindow, isWindowOpen, setSelectedTextInput
**Concepts:** GUI window management, window lifecycle, error handling, command queue

## Summary
Handles GUI window management, including opening, closing, toggling, and scaling windows.

## Explanation
This chunk manages the lifecycle of GUI windows within the application. It includes functions to get a window by ID (`getWindowById`), update the GUI scale based on settings or screen size (`updateGuiScale`), add new windows while checking for duplicates (`addWindow`), open and close windows with error handling if the window is not found (`openWindow`, `closeWindow`), toggle window visibility (`toggleWindow`), initialize HUD windows (`openHud`), and manage selected text inputs (`setSelectedTextInput`). The chunk also defines callback functions for opening windows (`openWindowCallback`) and schedules commands for window actions using a command queue (`GuiCommandQueue.scheduleCommand`).

**Detailed Function Descriptions:**
- `getWindowById(id: []const u8) ?*GuiWindow`: Iterates through the `windowList.items` to find a window with the specified ID. If found, it returns the window; otherwise, logs an error and returns null.
- `updateGuiScale() void`: Updates the GUI scale based on the `settings.guiScale`. If no specific setting is provided, it calculates the scale based on the screen size, ensuring it does not go below 0.5.
- `addWindow(window: *GuiWindow) void`: Adds a new window to the `windowList` after checking for duplicate IDs. If a duplicate ID is found, it logs an error and returns without adding the window.
- `openWindow(id: []const u8) void`: Opens a window by its ID. It iterates through the `windowList.items`, finds the matching window, and calls `openWindowFromRef`. If the window is not found, it logs an error.
- `openWindowFromRef(window: *GuiWindow) void`: Schedules a command to open the specified window using the `GuiCommandQueue`.
- `toggleWindow(id: []const u8) void`: Toggles the visibility of a window by its ID. It checks if the window is already open and either closes it or opens it accordingly.
- `openHud() void`: Initializes the inventory and opens all HUD windows by iterating through the `windowList.items` and calling `openWindowFromRef` for each HUD window.
- `openWindowCallback(comptime id: []const u8) main.callbacks.SimpleCallback`: Returns a callback function that initializes with a pointer to the specified window's reference using `@field(windowlist, id).window`.
- `closeWindowFromRef(window: *GuiWindow) void`: Schedules a command to close the specified window using the `GuiCommandQueue`.
- `closeWindow(id: []const u8) void`: Closes a window by its ID. It iterates through the `windowList.items`, finds the matching window, and calls `closeWindowFromRef`. If the window is not found, it logs an error.
- `isWindowOpen(id: []const u8) bool`: Checks if a window with the specified ID is currently open by iterating through the `openWindows.items`.
- `setSelectedTextInput(newSelectedTextInput: ?*TextInput) void`: Manages the selected text input. If there is a current selected text input and it is different from the new one, it deselects the current one before setting the new selected text input.

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
