# [hard/codebase_src_network.zig] - Chunk 15

**Type:** networking
**Keywords:** networking, atomic operations, mutex, packet loss, disconnection, bandwidth estimation, congestion control
**Symbols:** Connection, Connection.connectionState, Connection.nextPacketTimestamp, Connection.manager, Connection.remoteAddress, Connection.connectionIdentifier, Connection.lossyChannel, Connection.secureChannel, Connection.slowChannel, Connection.handlePacketLoss, Connection.sendConfirmationPacket, Connection.mutex, Connection.relativeIdleTime, Connection.relativeSendTime, Connection.rttEstimate, Connection.queuedConfirmations, Connection.isServerSide, Connection.user, Connection.handShakeWaiting, ChannelId.keepalive, ChannelId.init, ChannelId.disconnect, utils.BinaryWriter, main.stackAllocator, internalMessageOverhead, headerOverhead, main.random, main.seed, main.io.sleep, main.server.world, main.exitToMenu, std.log.info
**Concepts:** networking, packet management, connection states, thread safety, mutex locking

## Summary
Handles network connection states and packet management.

## Explanation
This chunk manages the lifecycle of a network connection, including sending packets based on connection state, handling packet loss, adjusting send timing, and disconnecting. It uses atomic operations for thread-safe state transitions and employs a mutex to synchronize access to shared resources.

### Connection States
The `Connection` struct has several states managed by `connectionState`, such as `.awaitingClientConnection`, `.awaitingServerResponse`, `.awaitingClientAcknowledgement`, `.connected`, `.disconnected`, and `.paused`. Depending on the state, different actions are taken:
- **.awaitingClientConnection**: Sends a keepalive packet every 100 ms.
- **.awaitingServerResponse** and **.awaitingClientAcknowledgement**: Sends an initialization packet with connection details (identifier, fully confirmed indices) every 100 ms.
- **.connected**: No action is taken.
- **.disconnected** and **.paused**: The function returns immediately without further processing.

### Packet Management
Packets are sent based on the current state and timing:
- **Packet Loss Handling**: Calls `handlePacketLoss` for each channel (`lossyChannel`, `secureChannel`, `slowChannel`) to check for packet losses.
- **Idle Time Calculation**: Adjusts `relativeIdleTime` if there is a period of no traffic.
- **Confirmation Packets**: Sends confirmation packets based on the difference between `relativeIdleTime` and `relativeSendTime` compared to `rttEstimate`.

### Bandwidth Estimation and Congestion Control
The chunk manages bandwidth estimation and congestion control by:
- Calculating packet time based on network length (`dataLen + headerOverhead`) divided by the estimated bandwidth (`bandwidthEstimateInBytesPerRtt`) multiplied by `rttEstimate`.
- Updating `nextPacketTimestamp` and `relativeSendTime` accordingly.

### Disconnection Process
The `disconnect` function sends a disconnection message, updates the connection state to `.disconnected`, and cleans up resources. If the operating system is Windows, it introduces a delay to prevent immediate socket closure, which can cause a `ConnectionResetByPeer` error on the other side.

### Thread Safety
Thread safety is ensured using atomic operations for state transitions and a mutex (`mutex`) to synchronize access to shared resources.

## Code Example
```zig
pub fn disconnect(self: *Connection) void {
		self.manager.send(&.{@intFromEnum(ChannelId.disconnect)}, self.remoteAddress, null);
		self.connectionState.store(.disconnected, .monotonic);
		if (builtin.os.tag == .windows and !self.isServerSide() and main.server.world != null) {
			main.io.sleep(.fromMilliseconds(10), .awake) catch {}; // Windows is too eager to close the socket, without waiting here we get a ConnectionResetByPeer on the other side.
		}
		self.manager.removeConnection(self);
		if (self.user) |user| {
			main.server.disconnect(user);
		} else {
			self.handShakeWaiting.broadcast();
			main.exitToMenu();
		}
		std.log.info("Disconnected", .{});
	}
```

## Related Questions
- What is the purpose of the `disconnect` function in this chunk?
- How does the chunk handle packet loss for different channels?
- What mechanism ensures thread safety when accessing shared resources?
- How is the next packet timestamp calculated and updated?
- What conditions trigger the sending of a confirmation packet?
- How does the chunk manage bandwidth estimation and congestion control?
- What is the role of the `relativeIdleTime` and `relativeSendTime` variables?
- How are packets sent based on the connection state?
- What happens if the operating system is Windows during disconnection?
- How does the chunk handle the removal of a connection from the manager?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_15*
