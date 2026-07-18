# [easy/codebase_src_gui_windows_debug_network.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, Network stats, Players connected, Packet loss, Overhead, Protocols
**Symbols:** graphics, draw, Texture, network, Vec2f, GuiWindow, GuiComponent, window, render
**Concepts:** GUI, Network statistics display, Player connection, Packet loss, Internal message overhead, Header overhead, Protocol-specific data

## Summary
Network statistics display

## Explanation
This chunk displays network-related statistics in the GUI. It retrieves and renders information about players connected, packet loss, internal message overhead, header overhead, and protocol-specific data sent/received.

## Code Example
```zig
render() void {
	var y: f32 = 0;
	if (main.game.world != null) {
		if (main.server.world != null) {
			const userList = main.server.getUserListAndIncreaseRefCount(main.stackAllocator);
			defer main.server.freeUserListAndDecreaseRefCount(main.stackAllocator, userList);
			draw.print("Players Connected: {}", .{userList.len}, 0, y, 8);
			y += 8;
		}
		const sent = network.Connection.packetsSent.load(.monotonic);
		const resent = network.Connection.packetsResent.load(.monotonic);
		const loss = @as(f64, @floatFromInt(resent))/@as(f64, @floatFromInt(sent))*100;
		draw.print("Packet loss: {d:.1}% ({}/{})", .{loss, resent, sent}, 0, y, 8);
		y += 8;
		draw.print("Internal message overhead: {}kiB", .{network.Connection.internalMessageOverhead.load(.monotonic) >> 10}, 0, y, 8);
		y += 8;
		draw.print("Internal header overhead: {}kiB", .{network.Connection.internalHeaderOverhead.load(.monotonic) >> 10}, 0, y, 8);
		y += 8;
		draw.print("External header overhead: {}kiB", .{network.Connection.externalHeaderOverhead.load(.monotonic) >> 10}, 0, y, 8);
		y += 8;
		inline for (@typeInfo(network.protocols).@"struct".decls) |decl| {
			if (@TypeOf(@field(network.protocols, decl.name)) == type) {
				const id = @field(network.protocols, decl.name).id;
				draw.print("{s}: received {}kiB sent {}kiB", .{decl.name, network.protocols.bytesReceived[id].load(.monotonic) >> 10, network.protocols.bytesSent[id].load(.monotonic) >> 10}, 0, y, 8);
				y += 8;
			}
		}
	}
	if (window.contentSize[1] != y) {
		window.contentSize[1] = y;
		window.updateWindowPosition();
	}
}
```

## Related Questions
- How many lines of code are in the render function?
- What is the purpose of the `render` function?
- Which module does the `render` function belong to?
- What data structures are used in the `render` function?
- What algorithms are implemented in the `render` function?
- What error handling mechanisms are present in the `render` function?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug_network.zig_chunk_0*
