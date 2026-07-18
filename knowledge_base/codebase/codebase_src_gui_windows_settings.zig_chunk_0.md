# [easy/codebase_src_gui_windows_settings.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI component, event handling, window management, layout calculation, deinitialization
**Symbols:** window, padding, onOpen, onClose
**Concepts:** GUI settings window, button components, vertical list layout

## Summary
Defines the Settings window GUI for Cubyz, including button components with specific actions linked to open various settings sub-windows when clicked. It initializes a vertical list of buttons and handles layout calculation and deinitialization logic.

## Explanation
This chunk defines the GUI settings window in Cubyz, which includes a vertical list of buttons each linked to open a specific settings sub-window upon click. The `onOpen` function initializes this list with five buttons: 'Graphics', 'Sound', 'Controls', 'Advanced Controls', and 'Social'. Each button is associated with an action that opens the corresponding sub-window using the `gui.openWindowCallback` method. For example, clicking the 'Graphics' button triggers opening the graphics settings window. The function also sets up the window's content size based on the root component's dimensions plus padding. The `onClose` function deinitializes the root component when the window is closed.

## Code Example
```zig
pub fn onClose() void {
	if (window.rootComponent) |*comp| {
		comp.deinit();
	}
}
```

## Related Questions
- What is the purpose of the `onOpen` function in this chunk?
- How does the chunk handle window content size calculation?
- Which components are added to the vertical list in the `onOpen` function?
- What action is triggered when a button in the settings window is clicked?
- How is the root component deinitialized in this chunk?
- What is the role of the `padding` constant in the layout?

*Source: unknown | chunk_id: codebase_src_gui_windows_settings.zig_chunk_0*
