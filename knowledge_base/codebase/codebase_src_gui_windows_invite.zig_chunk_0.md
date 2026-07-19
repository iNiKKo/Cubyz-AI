# [easy/codebase_src_gui_windows_invite.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, threading, IP address, error logging, memory management
**Symbols:** window, ipAddressLabel, ipAddressEntry, padding, ipAddress, gotIpAddress, thread, width, discoverIpAddress, discoverIpAddressFromNewThread, invite, copyIp, onOpen, onClose, update
**Concepts:** GUI window management, IP address sharing, multi-threading, error handling, resource management

## Summary
This chunk defines the logic for a GUI window that allows users to invite others by sharing their IP address.

## Explanation
This chunk defines a `GuiWindow` instance named `window`, which manages user-invitation logic through sharing IP addresses. The window has a content size of `(128, 256)` pixels. It contains several GUI components like `Label`, `TextInput`, and `Button`. Key functions include `discoverIpAddress`, `invite`, `copyIp`, handling window open/close events (`onOpen`, `onClose`), and updating the GUI (`update`). Threading is used to discover the local IP address in a separate thread, ensuring responsiveness. The discovered IP address is stored in `ipAddress` and displayed using `Label`. Error logging occurs when spawning threads or connecting users, with specific error messages for each case. Memory management includes freeing allocated memory for the IP address string upon window closure.

The `discoverIpAddress` function makes the server online and retrieves the external IP address using `main.server.connectionManager.externalAddress`, then formats it as a string and stores it in `ipAddress`. The `invite` function handles user invitations by connecting to the entered IP address. The `copyIp` function copies the IP address to the clipboard. The `onOpen` function initializes the GUI components, including labels, text inputs, and buttons, and starts a thread to discover the IP address. The `onClose` function joins any running threads, frees allocated memory for the IP address string, and deinitializes the GUI components. The `update` function updates the displayed IP address in the GUI if it has changed.

Threading is implemented by spawning a new thread using `std.Thread.spawn` to call `discoverIpAddressFromNewThread`, which initializes thread locals, discovers the IP address, and then deinitializes thread locals. If threading fails, the IP address discovery is done in the current thread instead.

Error handling includes logging errors when spawning threads or connecting users. Specific error messages are provided for each case, such as `"Cannot connect user: {s}"` and `"Error spawning thread: {s}. Doing it in the current thread instead."`.

## Code Example
```zig
fn discoverIpAddress() void {
	main.server.connectionManager.makeOnline();
	ipAddress = std.fmt.allocPrint(main.globalAllocator.allocator, "{f}", .{main.server.connectionManager.externalAddress}) catch unreachable;
	gotIpAddress.store(true, .release);
}
```

## Related Questions
- What is the purpose of the `discoverIpAddress` function?
- How does the chunk handle threading for IP address discovery?
- What happens when the user clicks the 'Invite' button?
- How is the IP address displayed in the GUI?
- What error handling is implemented in this chunk?
- How are resources managed when the window is closed?

*Source: unknown | chunk_id: codebase_src_gui_windows_invite.zig_chunk_0*
