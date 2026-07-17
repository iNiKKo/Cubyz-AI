# [easy/codebase_src_gui_windows_notification.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, Label, Button, deinit, allocPrint, closeWindowFromRef, rootComponent, updateWindowPositions, allocator
**Symbols:** window, padding, width, text, deinit, setNotificationText, raiseNotification, ack, onOpen, onClose
**Concepts:** notification window, GUI component lifecycle, formatted text rendering, button action callbacks, window positioning updates

## Summary
This chunk defines the notification window component, providing functions to raise and dismiss notifications with formatted text content.

## Explanation
The chunk declares a global GuiWindow instance named 'window' initialized with a content size of Vec2f{128, 256}. It imports Button, VerticalList, and Label from the components module. The deinit function frees the allocated text buffer using main.globalAllocator.free and resets text to an empty slice. setNotificationText is a comptime-formatted helper that allocates new formatted text via std.fmt.allocPrint into main.globalAllocator.allocator, freeing any previous allocation first; it uses catch unreachable because formatting should never fail in this context. raiseNotification closes the existing notification window (if open), calls setNotificationText with provided format and args, then opens a fresh notification window named 'notification'. ack is an internal function that closes the window from its reference using gui.closeWindowFromRef. onOpen initializes a VerticalList with padding-based margins, adds a Label displaying the current text left-aligned at full width, and adds an OK Button whose action callback invokes ack; it then finishes the list centered and assigns it as window.rootComponent, updating window.contentSize to encompass the component plus padding, and calls gui.updateWindowPositions. onClose checks if rootComponent exists and calls its deinit method.

## Code Example
```zig
pub fn deinit() void {
	main.globalAllocator.free(text);
	text = "";
}
```

## Related Questions
- What is the initial content size of the notification window?
- How does raiseNotification handle closing an already-open notification window?
- Which function is responsible for freeing allocated text memory in this chunk?
- What happens to the rootComponent when onOpen initializes the VerticalList?
- Does the Button's action callback invoke a public or internal function?
- Is gui.updateWindowPositions called synchronously after setting the rootComponent?
- How is the final content size of window computed in onOpen?

*Source: unknown | chunk_id: codebase_src_gui_windows_notification.zig_chunk_0*
