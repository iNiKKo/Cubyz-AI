# [hard/codebase_src_network.zig] - Chunk 14

**Type:** networking
**Keywords:** networkTimestamp, BinaryReader, BinaryWriter, cmpxchgStrong, fetchAdd, sendBuffer, fullyConfirmedIndex
**Symbols:** tryReceive, processNextPackets
**Concepts:** networking, packet handling, connection management

## Summary
Handles packet reception and processing for network connections.

## Explanation
The chunk defines functions to receive and process packets in a network connection. `tryReceive` processes incoming data, handling different channels like lossy, secure, slow, confirmation, init, keepalive, and disconnect. It updates the connection state and handles acknowledgments. `processNextPackets` manages sending periodic keepalive or initial packets based on the connection state and checks for packet losses.

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
- What is the purpose of the `tryReceive` function?
- How does the chunk handle different packet channels?
- What state transitions occur in the connection based on received packets?
- How are acknowledgments handled in this chunk?
- What conditions trigger sending keepalive or initial packets?
- How is packet loss detected and managed?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_14*
