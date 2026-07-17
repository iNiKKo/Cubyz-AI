# [hard/codebase_src_gui_gui.zig] - Chunk 2

**Type:** api
**Keywords:** window management, positioning logic, error handling, callback functions, hud elements, selected text inputs
**Symbols:** getWindowById, updateGuiScale, addWindow, openWindow, openWindowFromRef, toggleWindow, openHud, openWindowCallback, closeWindowFromRef, closeWindow, isWindowOpen, setSelectedTextInput
**Concepts:** GUI window management, window positioning, window lifecycle, HUD initialization, text input handling

## Summary
Handles GUI window management, including initialization, positioning, and interaction.

## Explanation
This chunk manages the lifecycle of GUI windows within the Cubyz engine. It includes functions for updating window positions based on their configuration, adding new windows to the list, opening and closing windows by ID or reference, toggling window visibility, initializing HUD elements, and managing selected text inputs. The code also handles error logging when operations fail, such as attempting to open a non-existent window.

## Code Example
```zig
pub fn openWindowFromRef(window: *GuiWindow) void {
	GuiCommandQueue.scheduleCommand(.{.action = .open, .window = window});
}
```

## Related Questions
- How does the code handle unknown window attachment types?
- What function is responsible for updating the GUI scale?
- How are duplicate window IDs managed in the code?
- What steps are taken to open a HUD window?
- How is a window closed from its reference?
- What is the process for toggling a window's visibility?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_2*
