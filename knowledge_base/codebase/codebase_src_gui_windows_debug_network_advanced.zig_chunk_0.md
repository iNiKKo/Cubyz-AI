# [easy/codebase_src_gui_windows_debug_network_advanced.zig] - Chunk 0

**Type:** implementation
**Keywords:** renderConnectionData, render, network statistics, client/server connections, window size update
**Symbols:** graphics, draw, Texture, network, Vec2f, GuiWindow, GuiComponent, window, renderConnectionData, conn, name, y, unconfirmed, queued, lossyChannel, secureChannel, slowChannel, rttEstimate, bandwidthEstimateInBytesPerRtt
**Concepts:** networking, algorithm, gui rendering

## Summary
Network connection data rendering

## Explanation
This chunk defines the `renderConnectionData` function, which renders statistics for network connections. It also includes the `render` function that calls `renderConnectionData` for client and server connections and updates the window size based on rendered content.

## Code Example
```zig
fn renderConnectionData(conn: *main.network.Connection, name: []const u8, y: *f32) void {
	conn.mutex.lock();
	defer conn.mutex.unlock();
	var unconfirmed: [3]usize = @splat(0);
	var queued: [3]usize = @splat(0);
	conn.lossyChannel.getStatistics(&unconfirmed[0], &queued[0]);
	conn.secureChannel.getStatistics(&unconfirmed[1], &queued[1]);
	conn.slowChannel.getStatistics(&unconfirmed[2], &queued[2]);
	draw.print("{s} | RTT = {d:.1} ms | {d:.0} kiB/RTT", .{name, conn.rttEstimate/1000.0, conn.bandwidthEstimateInBytesPerRtt/1024.0}, 0, y.*, 8);
	y.* += 8;
	draw.print("Waiting in queue:      {: >6} kiB |{: >6} kiB |{: >6} kiB", .{queued[0] >> 10, queued[1] >> 10, queued[2] >> 10}, 0, y.*, 8);
	y.* += 8;
	draw.print("Sent but not confirmed:{: >6} kiB |{: >6} kiB |{: >6} kiB", .{unconfirmed[0] >> 10, unconfirmed[1] >> 10, unconfirmed[2] >> 10}, 0, y.*, 8);
	y.* += 8;
}
```

## Related Questions
- What is the purpose of the `renderConnectionData` function?
- How does `renderConnectionData` calculate and display network statistics for a connection?
- Where are the mutex locks used in `renderConnectionData`?
- What data structures are used to store unconfirmed and queued packets in `renderConnectionData`?
- How is the RTT estimate calculated in `renderConnectionData`?
- What is the bandwidth estimate per RTT in `renderConnectionData`?
- Where is the window size updated based on rendered content in `render`?
- How does `render` handle client and server connections?
- What data structures are used to store user lists in `render`?
- How is memory management handled for user lists in `render`?
- What is the purpose of the `GuiWindow` struct in this chunk?
- Where is the `window.contentSize[1]` updated based on rendered content in `render`?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug_network_advanced.zig_chunk_0*
