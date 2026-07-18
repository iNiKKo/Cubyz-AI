# [easy/codebase_src_gui_windows_clipboard_deleted.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, timestamp, duration calculation, conditional rendering, window closing
**Symbols:** window, time, GuiWindow.relativePosition, GuiWindow.contentSize, GuiWindow.isHud, GuiWindow.showTitleBar, GuiWindow.hasBackground, GuiWindow.hideIfMouseIsGrabbed, onOpen, render
**Concepts:** GUI window management, clipboard interaction, time-based UI updates

## Summary
Defines a GUI window that displays a message when the clipboard is cleared and closes after 2 seconds. The window has specific relative positioning, content size, and appearance attributes.

## Explanation
This chunk defines a GUI window named 'window' with specific properties such as position, size, and appearance. The `relativePosition` property specifies that the window's middle is attached to another frame's middle and its lower edge is attached to another frame's lower edge. The `contentSize` is set to 128x16 pixels. The window does not have a title bar or background, and it does not hide if the mouse is grabbed.

The `onOpen` function records the current timestamp when the window opens using `main.timestamp()`. The `render` function calculates the duration since the window opened by subtracting `time` from `main.timestamp()` and checks if this duration exceeds 2 seconds. If it does, the window closes. It also sets a specific color (0xffff8080) for rendering the message indicating that the clipboard was cleared.

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
- What are the exact properties and values set for the 'window' variable?
- How is the color set for rendering the message?

*Source: unknown | chunk_id: codebase_src_gui_windows_clipboard_deleted.zig_chunk_0*
