# [easy/codebase_src_gui_windows_multiplayer.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, button, window, multiplayer selection, deinitialization
**Symbols:** gui, GuiComponent, GuiWindow, Button, VerticalList, Vec2f, window, padding, multiplayerSelection, onOpen, onClose
**Concepts:** GUI management, button handling, window switching

## Summary
Handles multiplayer selection and window management in the GUI.

## Explanation
This chunk manages the multiplayer selection screen within the GUI. It initializes a vertical list with two buttons: 'Host World' and 'Join Server'. When the 'Host World' button is clicked, it sets the save selection mode to multiplayer, closes the 'save_selection' window, and then reopens it. The 'Join Server' button opens the 'multiplayer_join' window. The `onOpen` function initializes the list with buttons and positions them correctly within the window. The `onClose` function deinitializes the root component of the window if it exists.

## Code Example
```zig
fn multiplayerSelection() void {
	gui.windowlist.save_selection.mode = .multiplayer;
	gui.closeWindow("save_selection");
	gui.openWindow("save_selection");
}
```

## Related Questions
- What is the purpose of the `onOpen` function in this chunk?
- How does the `onClose` function handle the root component of the window?
- What are the two buttons available on the multiplayer selection screen?
- What action does clicking the 'Host World' button trigger?
- What action does clicking the 'Join Server' button trigger?
- What is the purpose of the `padding` variable in this chunk?
- How is the size of the window calculated after opening the list?
- What is the mode set for save selection when the 'Host World' button is clicked?
- What function is called when the 'Join Server' button is clicked?
- What does the `initText` method do in this chunk?
- How are the buttons positioned within the window?
- What is the purpose of the `finish` method in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_multiplayer.zig_chunk_0*
