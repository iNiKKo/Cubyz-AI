# [easy/codebase_src_gui_windows_pause.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, VerticalList, Button, onAction, deinit
**Symbols:** window, padding, reorderHudCallbackFunction, onOpen, onClose
**Concepts:** GUI, Pause menu, Button actions, Window management

## Summary
Defines the Pause menu window for the GUI, including its layout and button actions.

## Explanation
This chunk defines a Pause menu window within the game's graphical user interface (GUI). It initializes a `GuiWindow` with specific content size and behavior. The `onOpen` function sets up the window's root component as a `VerticalList`, adding several buttons for different actions like opening player, invite, settings, reordering HUD, and exiting the world. Each button is conditionally enabled or disabled based on game state. The `onClose` function deinitializes the window's components when it closes.

## Code Example
```zig
fn reorderHudCallbackFunction() void {
	gui.reorderWindows = !gui.reorderWindows;
}
```

## Related Questions
- What is the size of the Pause menu window?
- How are buttons conditionally enabled or disabled in the Pause menu?
- What action does the 'Reorder HUD' button perform?
- How is the content size of the Pause menu window calculated?
- What happens when the Pause menu window is closed?
- Which components are initialized when the Pause menu opens?

*Source: unknown | chunk_id: codebase_src_gui_windows_pause.zig_chunk_0*
