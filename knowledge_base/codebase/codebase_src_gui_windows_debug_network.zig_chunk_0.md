# [easy/codebase_src_gui_windows_debug_network.zig] - Chunk 0

**Type:** api
**Keywords:** atomic operations, GUI rendering, network metrics, player list, packet loss
**Symbols:** window, render
**Concepts:** network debugging, GUI window management, statistics display

## Summary
The chunk defines a debug network window for displaying network statistics and user list.

## Explanation
This chunk initializes a GUI window named 'window' with specific properties such as relative position, content size, and visibility settings. The `render` function updates the window's content by drawing various network-related statistics, including player count, packet loss, message overheads, and protocol-specific data transfer rates. It uses atomic operations to safely read network metrics and formats them for display using a drawing API.

## Code Example
```zig
pub fn render() void {
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
- What is the purpose of the 'window' variable?
- How does the 'render' function update the GUI window?
- What network metrics are displayed in the debug window?
- How is packet loss calculated and displayed?
- What role do atomic operations play in this chunk?
- How is the user list retrieved and managed within the render function?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug_network.zig_chunk_0*
