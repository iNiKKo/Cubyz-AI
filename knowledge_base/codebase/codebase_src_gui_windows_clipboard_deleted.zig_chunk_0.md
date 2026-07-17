# [easy/codebase_src_gui_windows_clipboard_deleted.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, closeWindowFromRef, setColor, restoreColor, print, durationTo, timestamp, relativePosition, contentSize, isHud
**Symbols:** main.graphics, draw, Texture, Vec2f, TaskType, GuiWindow, GuiComponent
**Concepts:** GUI window lifecycle, deferred cleanup, timestamp-based timeout

## Summary
This chunk defines a GUI window that displays the message 'Your clipboard was cleared.' for up to two seconds after opening, then closes itself; it imports core graphics and utility modules from main.

## Explanation
The chunk declares several imported symbols: std (standard library), main.graphics (graphics module), draw (draw API), Texture (texture type), Vec2f (vector2f type), TaskType (thread pool task type). It also imports the gui module and re-exports GuiWindow and GuiComponent. A global var window is initialized as a GuiWindow with relativePosition set to two attachment points (middle/selfAttachmentPoint, lower/otherAttachmentPoint), contentSize 128x16, isHud false, showTitleBar false, hasBackground false, hideIfMouseIsGrabbed false. A time variable of type std.Io.Timestamp is declared and initialized undefined. The onOpen function sets time to the current timestamp via main.timestamp(). The render function computes duration since opening; if duration exceeds 2 seconds it calls gui.closeWindowFromRef(&window) and returns early. Otherwise it saves the old color by calling draw.setColor(0xffff8080), defers restoring that color, then prints 'Your clipboard was cleared.' at position (0,0) with size 16.

## Related Questions
- What is the default content size of the clipboard cleared window?
- How does the render function decide when to close the window?
- Which draw API call changes the color before printing the message?
- What happens if the duration since onOpen exceeds two seconds?
- Is the window marked as a HUD element in this chunk?
- Does the window have a title bar or background by default here?

*Source: unknown | chunk_id: codebase_src_gui_windows_clipboard_deleted.zig_chunk_0*
