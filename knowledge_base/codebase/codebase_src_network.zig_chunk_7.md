# [hard/codebase_src_network.zig] - Chunk 7

**Type:** networking
**Keywords:** circular buffer, priority queue, header parsing, message insertion, sequence index
**Symbols:** ReceiveBuffer, ReceiveBuffer.currentReadPosition, ReceiveBuffer.decryptedBuffer, ReceiveBuffer.buffer, ReceiveBuffer.header, ReceiveBuffer.protocolBuffer, ReceiveBuffer.channelId, ReceiveBuffer.init, ReceiveBuffer.deinit, ReceiveBuffer.applyRanges, ReceiveBuffer.getHeaderInformation, ReceiveBuffer.collectRangesAndExecuteProtocols, ReceiveBuffer.ReceiveStatus, ReceiveBuffer.receive, ReceiveBuffer.receiveSecure, SendBuffer, SendBuffer.Range, SendBuffer.Range.start, SendBuffer.Range.len, SendBuffer.Range.timestamp, SendBuffer.Range.wasResent, SendBuffer.Range.wasResentAsFirstPacket, SendBuffer.Range.considerForCongestionControl, SendBuffer.Range.compareTime, SendBuffer.unconfirmedRanges, SendBuffer.lostRanges, SendBuffer.buffer, SendBuffer.fullyConfirmedIndex, SendBuffer.highestSentIndex, SendBuffer.nextIndex, SendBuffer.lastUnsentTime, SendBuffer.init, SendBuffer.deinit, SendBuffer.insertMessage, SendBuffer.insertMessageSecure
**Concepts:** networking, data buffering, protocol handling, message confirmation

## Summary
The chunk defines the `ReceiveBuffer` and `SendBuffer` structs for handling network data reception and transmission, including initialization, deinitialization, and core processing methods.

## Explanation
The chunk defines the `ReceiveBuffer` and `SendBuffer` structs for handling network data reception and transmission, including initialization, deinitialization, and core processing methods. The `ReceiveBuffer` struct manages incoming network data using circular buffers to store decrypted and raw data. It includes methods like `init`, which initializes the buffer with a given channel ID; `deinit`, which deallocates all resources; `applyRanges`, which processes received data ranges; `getHeaderInformation`, which extracts header information from the decrypted buffer; and `collectRangesAndExecuteProtocols`, which executes protocols based on received data. The `SendBuffer` struct handles outgoing data with similar circular buffers and priority queues for unconfirmed and lost ranges. It includes methods like `init`, which initializes the buffer with a given starting index (`1 << 10` for `lostRanges` and `1 << 20` for `buffer`); `deinit`, which deallocates all resources; `insertMessage`, which inserts messages into the buffer; and `insertMessageSecure`, which inserts messages securely through a secure channel. The `unconfirmedRanges` priority queue in `SendBuffer` manages ranges that have been sent but not yet confirmed, while `fullyConfirmedIndex` tracks the highest index of fully confirmed data. The `lostRanges` priority queue manages ranges that have been lost during transmission, `buffer` stores the actual data to be transmitted, and `highestSentIndex`, `nextIndex`, and `lastUnsentTime` track the state of message transmission. The `insertMessageSecure` method appends protocol index, header overhead, and data to a fullData list, which is then sent through TLS or added to the buffer. The `receiveConfirmationAndGetTimestamp` method processes confirmation packets and updates the buffer state accordingly. The `checkForLosses` method checks for packet losses and manages retransmissions. The `getNextPacketToSend` method retrieves the next packet to send, either from lost ranges or new data, ensuring that the MTU is respected.

## Code Example
```zig
pub fn init(channelId: ChannelId) ReceiveBuffer {
	return .{
		.ranges = .init(),
		.decryptedBuffer = .init(main.globalAllocator),
		.buffer = .init(main.globalAllocator),
		.channelId = channelId,
	};
}
```

## Related Questions
- How does the `ReceiveBuffer` initialize its buffers?
- What is the purpose of the `applyRanges` method in `ReceiveBuffer`?
- How does `SendBuffer` handle message insertion with a secure channel?
- What is the role of the `unconfirmedRanges` priority queue in `SendBuffer`?
- How does `ReceiveBuffer` manage header information extraction?
- What steps are involved in deinitializing both `ReceiveBuffer` and `SendBuffer`?
- How does `SendBuffer` determine if a message should be resent?
- What is the significance of the `fullyConfirmedIndex` in `SendBuffer`?
- What methods and properties are associated with the 'unconfirmedRanges' priority queue in `SendBuffer`?
- What methods and properties are associated with the 'lostRanges', 'buffer', 'fullyConfirmedIndex', 'highestSentIndex', 'nextIndex', and 'lastUnsentTime' properties of `SendBuffer`?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_7*
