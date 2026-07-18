# [easy/codebase_src_gui_windows_invite.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, threading, IP address, error logging, memory management
**Symbols:** window, ipAddressLabel, ipAddressEntry, padding, ipAddress, gotIpAddress, thread, width, discoverIpAddress, discoverIpAddressFromNewThread, invite, copyIp, onOpen, onClose, update
**Concepts:** GUI window management, IP address sharing, multi-threading, error handling, resource management

## Summary
This chunk defines the logic for a GUI window that allows users to invite others by sharing their IP address.

## Explanation
The chunk contains a `GuiWindow` instance named `window` and several components like `Label`, `TextInput`, and `Button`. It includes functions for discovering the local IP address (`discoverIpAddress`), inviting a user (`invite`), copying the IP address to the clipboard (`copyIp`), handling window open and close events (`onOpen`, `onClose`), and updating the GUI (`update`). The chunk uses threading to discover the IP address in a separate thread, ensuring the main thread remains responsive. It also handles error logging and resource management, such as freeing allocated memory when the window closes.

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
