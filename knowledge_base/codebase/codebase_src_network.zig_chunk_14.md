# [hard/codebase_src_network.zig] - Chunk 14

**Type:** networking
**Keywords:** networkTimestamp, BinaryReader, BinaryWriter, cmpxchgStrong, fetchAdd, sendBuffer, fullyConfirmedIndex
**Symbols:** tryReceive, processNextPackets
**Concepts:** networking, packet handling, connection management

## Summary
Handles packet reception and processing for network connections.

## Explanation
The chunk defines functions to receive and process packets in a network connection. `tryReceive` processes incoming data, handling different channels like lossy, secure, slow, confirmation, init, keepalive, and disconnect. It updates the connection state and handles acknowledgments. `processNextPackets` manages sending periodic keepalive or initial packets based on the connection state and checks for packet losses.

### Handling Different Packet Channels
- **Lossy Channel**: Handles lossy data transmission with specific sequence indices for start positions.
- **Secure Channel**: Manages secure data transmission using similar sequence indices.
- **Slow Channel**: Processes slow data transmissions with designated sequence indices.
- **Confirmation Channel**: Used to acknowledge received packets and track their timestamps.
- **Init Channel**: Initializes the connection, setting up channels and remote identifiers.
- **Keepalive Channel**: Sends periodic keepalive messages to maintain connection status.
- **Disconnect Channel**: Handles disconnection requests from the other side of the connection.

### Acknowledgment Handling
Acknowledgments are handled by checking if the received packet is an acknowledgment. If it is, and the connection state is `awaitingClientAcknowledgement`, the state transitions to `connected`. For non-handshake packets, acknowledgments are sent back to the client using a BinaryWriter that writes the channel ID and connection identifier.

### Conditions for Sending Keepalive or Initial Packets
- **Initial Packets**: Sent once every 100 milliseconds when the connection is in states like `awaitingServerResponse` or `awaitingClientAcknowledgement`.
- **Keepalive Packets**: Periodically sent to maintain connection status, based on the time elapsed since the last packet was sent and the relative idle time compared to the estimated round-trip time (RTT).

### Packet Loss Detection and Management
Packet loss is detected by checking if the time elapsed since the last packet was sent exceeds a certain threshold. If so, the relative idle time is updated, and the next confirmation timestamp is adjusted accordingly.

## Code Example
```zig
fn tryReceive(self: *Connection, data: []const u8) !void {
		std.debug.assert(self.manager.threadId == std.Thread.getCurrentId());
		self.lastConnectionTime = networkTimestamp();
		var reader = utils.BinaryReader.init(data);
		const channel = try reader.readEnum(ChannelId);
		if (channel == .init) {
			const remoteConnectionIdentifier = try reader.readInt(i64);
			const isAcknowledgement = reader.remaining.len == 0;
			if (isAcknowledgement) {
				switch (self.connectionState.load(.monotonic)) {
					.awaitingClientAcknowledgement => {
						if (self.remoteConnectionIdentifier == remoteConnectionIdentifier) {
							_ = self.connectionState.cmpxchgStrong(.awaitingClientAcknowledgement, .connected, .monotonic, .monotonic);
						}
					},
					else => {},
				}
				return;
			}
			const lossyStart = try reader.readInt(SequenceIndex);
			const secureStart = try reader.readInt(SequenceIndex);
			const slowStart = try reader.readInt(SequenceIndex);
			switch (self.connectionState.load(.monotonic)) {
				.awaitingClientConnection => {
					self.lossyChannel.connect(lossyStart);
					self.secureChannel.connect(secureStart);
					self.slowChannel.connect(slowStart);
					_ = self.connectionState.cmpxchgStrong(.awaitingClientConnection, .awaitingClientAcknowledgement, .monotonic, .monotonic);
					self.remoteConnectionIdentifier = remoteConnectionIdentifier;
				},
				.awaitingServerResponse => {
					self.lossyChannel.connect(lossyStart);
					self.secureChannel.connect(secureStart);
					self.slowChannel.connect(slowStart);
					_ = self.connectionState.cmpxchgStrong(.awaitingServerResponse, .connected, .monotonic, .monotonic);
					self.remoteConnectionIdentifier = remoteConnectionIdentifier;
				},
				.awaitingClientAcknowledgement => {},
				.connected => {
					if (self.remoteConnectionIdentifier != remoteConnectionIdentifier) { // Reconnection attempt
						if (self.user) |user| {
							self.manager.removeConnection(self);
							main.server.disconnect(user);
						} else {
							std.log.err("Server reconnected?", .{});
							self.disconnect();
						}
						return;
					}
				},
				.disconnected, .paused => {},
			}
			// Acknowledge the packet on the client:
			if (self.user == null) {
				var writer = utils.BinaryWriter.initCapacity(main.stackAllocator, 1 + @sizeOf(i64));
				defer writer.deinit();

				writer.writeEnum(ChannelId, .init);
				writer.writeInt(i64, self.connectionIdentifier);

				_ = internalMessageOverhead.fetchAdd(writer.data.items.len + headerOverhead, .monotonic);
				self.manager.send(writer.data.items, self.remoteAddress, null);
			}
			return;
		}
		if (self.connectionState.load(.monotonic) != .connected) return; // Reject all non-handshake packets until the handshake is done.
		if (self.handShakeState.load(.monotonic) != .complete and (channel == .lossy or channel == .slow)) return; // Reject all non-handshake packets from other channels.
		switch (channel) {
			.lossy => {
				const start = try reader.readInt(SequenceIndex);
				if (try self.lossyChannel.receive(self, start, reader.remaining) == .accepted) {
					self.queuedConfirmations.pushBack(.{
						.channel = channel,
						.start = start,
						.receiveTimeStamp = networkTimestamp(),
					});
				}
			},
			.secure => {
				const start = try reader.readInt(SequenceIndex);
				if (try self.secureChannel.receive(self, start, reader.remaining) == .accepted) {
					self.queuedConfirmations.pushBack(.{
						.channel = channel,
						.start = start,
						.receiveTimeStamp = networkTimestamp(),
					});
				}
			},
			.slow => {
				const start = try reader.readInt(SequenceIndex);
				if (try self.slowChannel.receive(self, start, reader.remaining) == .accepted) {
					self.queuedConfirmations.pushBack(.{
						.channel = channel,
						.start = start,
						.receiveTimeStamp = networkTimestamp(),
					});
				}
			},
			.confirmation => {
				try self.receiveConfirmationPacket(&reader, networkTimestamp());
			},
			.init => unreachable,
			.keepalive => {},
			.disconnect => {
				self.disconnect();
			},
		}

		// TODO: Packet statistics
	}
```

## Related Questions
- What are the specific sequence indices used for each channel in handling packets?
- How does the chunk handle acknowledgments based on the connection state?
- Under what conditions are initial or keepalive packets sent to maintain the connection?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_14*
