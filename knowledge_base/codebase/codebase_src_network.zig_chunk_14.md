# [hard/codebase_src_network.zig] - Chunk 14

**Type:** networking
**Keywords:** network packet processing, connection state, RTT calculation, error handling, thread synchronization
**Symbols:** increaseCongestionBandwidth, sendConfirmationPacket, receive, tryReceive, receiveConfirmationPacket
**Concepts:** networking, connection management, RTT estimation, packet confirmation

## Summary
Handles network packet processing and connection state management.

## Explanation
This chunk contains methods for managing network connections, including receiving packets, updating RTT estimates, sending confirmation packets, and handling different channel types. It maintains connection states such as awaiting client/server responses or being connected. The code also includes error handling for received data processing errors, logging the error and disconnecting if necessary.

## Code Example
```zig
fn sendConfirmationPacket(self: *Connection, timestamp: i64) void {
	std.debug.assert(self.manager.threadId == std.Thread.getCurrentId());
	var writer = utils.BinaryWriter.initCapacity(main.stackAllocator, self.mtuEstimate);
	defer writer.deinit();

	writer.writeEnum(ChannelId, .confirmation);

	while (self.queuedConfirmations.popFront()) |confirmation| {
		writer.writeEnum(ChannelId, confirmation.channel);
		writer.writeInt(u16, std.math.lossyCast(u16, @divTrunc(timestamp -% confirmation.receiveTimeStamp, 2)));
		writer.writeInt(SequenceIndex, confirmation.start);
		if (writer.data.capacity - writer.data.items.len < @sizeOf(ChannelId) + @sizeOf(u16) + @sizeOf(SequenceIndex)) break;
	}

	_ = internalMessageOverhead.fetchAdd(writer.data.items.len + headerOverhead, .monotonic);
	self.manager.send(writer.data.items, self.remoteAddress, null);
}
```

## Related Questions
- What method is responsible for sending confirmation packets?
- How does the chunk handle received data errors?
- What is the purpose of the `increaseCongestionBandwidth` method?
- Which connection states are managed in this chunk?
- How is RTT estimation updated in the chunk?
- What channels are handled by the `tryReceive` method?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_14*
