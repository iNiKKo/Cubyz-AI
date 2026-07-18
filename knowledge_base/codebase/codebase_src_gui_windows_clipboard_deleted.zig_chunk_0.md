# [easy/codebase_src_gui_windows_clipboard_deleted.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, timestamp, duration calculation, conditional rendering, window closing
**Symbols:** window, time, GuiWindow.relativePosition, GuiWindow.contentSize, GuiWindow.isHud, GuiWindow.showTitleBar, GuiWindow.hasBackground, GuiWindow.hideIfMouseIsGrabbed, onOpen, render
**Concepts:** GUI window management, clipboard interaction, time-based UI updates

## Summary
Defines a GUI window that displays a message when the clipboard is cleared and closes after 2 seconds.

## Explanation
This chunk defines a GUI window named 'window' with specific properties such as position, size, and appearance. The `onOpen` function records the current timestamp when the window opens. The `render` function calculates the duration since the window opened and closes it if more than 2 seconds have passed. It also renders a message indicating that the clipboard was cleared.

## Code Example
```zig
pub fn onOpen() void {
	time = main.timestamp();
}
```

## Related Questions
- What is the purpose of the 'onOpen' function?
- How does the window determine when to close?
- What message is displayed in the GUI window?
- How is the color set for rendering the message?
- What are the properties of the 'window' variable?
- How is the duration since the window opened calculated?

*Source: unknown | chunk_id: codebase_src_gui_windows_clipboard_deleted.zig_chunk_0*
