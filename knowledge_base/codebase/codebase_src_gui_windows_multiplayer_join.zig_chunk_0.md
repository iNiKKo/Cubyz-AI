# [easy/codebase_src_gui_windows_multiplayer_join.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, networking, threading, atomic operations, clipboard interaction, user input handling
**Symbols:** window, ipAddressLabel, ipAddressEntry, padding, connection, ipAddress, gotIpAddress, thread, width, discoverIpAddress, discoverIpAddressFromNewThread, join, copyIp, onOpen, onClose, update
**Concepts:** GUI window management, multiplayer connection, IP address discovery, threading for non-blocking operations

## Summary
Handles the multiplayer join window GUI logic, including IP address discovery and connection management.

## Explanation
This chunk defines the logic for a GUI window that allows players to join a multiplayer game. It includes functions for discovering the player's IP address in a separate thread, handling user input for joining a server, copying the IP address to the clipboard, initializing the window components, and cleaning up resources when the window is closed. The chunk uses threading for non-blocking IP discovery, manages connection states, and updates the GUI based on the discovered IP address.

## Code Example
```zig
fn join() void {
	if (thread) |_thread| {
		_thread.join();
		thread = null;
	}
	if (ipAddress.len != 0) {
		main.globalAllocator.free(ipAddress);
		ipAddress = "";
	}
	if (connection) |_connection| {
		_connection.world = &main.game.testWorld;
		main.game.world = &main.game.testWorld;
		std.log.info("Connecting to server: {s}", .{ipAddressEntry.currentString.items});
		main.game.testWorld.init(ipAddressEntry.currentString.items, _connection) catch |err| {
			std.log.err("Encountered error while opening world: {s}", .{@errorName(err)});
			main.gui.windowlist.notification.raiseNotification("Encountered error while opening world: {s}", .{@errorName(err)});
			main.game.world = null;
			_connection.world = null;
			return;
		};
		main.globalAllocator.free(settings.lastUsedIPAddress);
		settings.lastUsedIPAddress = main.globalAllocator.dupe(u8, ipAddressEntry.currentString.items);
		settings.save();
		connection = null;
	} else {
		std.log.err("No connection found. Cannot connect.", .{});
		main.gui.windowlist.notification.raiseNotification("No connection found. Cannot connect.", .{});
	}
	for (gui.openWindows.items) |openWindow| {
		gui.closeWindowFromRef(openWindow);
	}
	gui.openHud();
}
```

## Related Questions
- What is the purpose of the `discoverIpAddress` function?
- How does the chunk handle threading for IP address discovery?
- What components are added to the GUI window in the `onOpen` function?
- How does the chunk manage connection states during the join process?
- What happens when the user clicks the 'Copy IP' button?
- How is the discovered IP address displayed in the GUI?

*Source: unknown | chunk_id: codebase_src_gui_windows_multiplayer_join.zig_chunk_0*
