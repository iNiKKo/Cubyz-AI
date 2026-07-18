# [hard/codebase_src_network.zig] - Chunk 7

**Type:** networking
**Keywords:** circular buffer, priority queue, header parsing, message insertion, sequence index
**Symbols:** ReceiveBuffer, ReceiveBuffer.currentReadPosition, ReceiveBuffer.decryptedBuffer, ReceiveBuffer.buffer, ReceiveBuffer.header, ReceiveBuffer.protocolBuffer, ReceiveBuffer.channelId, ReceiveBuffer.init, ReceiveBuffer.deinit, ReceiveBuffer.applyRanges, ReceiveBuffer.getHeaderInformation, ReceiveBuffer.collectRangesAndExecuteProtocols, ReceiveBuffer.ReceiveStatus, ReceiveBuffer.receive, ReceiveBuffer.receiveSecure, SendBuffer, SendBuffer.Range, SendBuffer.Range.start, SendBuffer.Range.len, SendBuffer.Range.timestamp, SendBuffer.Range.wasResent, SendBuffer.Range.wasResentAsFirstPacket, SendBuffer.Range.considerForCongestionControl, SendBuffer.Range.compareTime, SendBuffer.unconfirmedRanges, SendBuffer.lostRanges, SendBuffer.buffer, SendBuffer.fullyConfirmedIndex, SendBuffer.highestSentIndex, SendBuffer.nextIndex, SendBuffer.lastUnsentTime, SendBuffer.init, SendBuffer.deinit, SendBuffer.insertMessage, SendBuffer.insertMessageSecure
**Concepts:** networking, data buffering, protocol handling, message confirmation

## Summary
The chunk defines the `ReceiveBuffer` and `SendBuffer` structs for handling network data reception and transmission, including initialization, deinitialization, and core processing methods.

## Explanation
The `ReceiveBuffer` struct manages incoming network data, using circular buffers to store decrypted and raw data. It includes methods like `init`, `deinit`, `applyRanges`, `getHeaderInformation`, and `collectRangesAndExecuteProtocols` for managing data ranges, extracting headers, and executing protocols based on received data. The `SendBuffer` struct handles outgoing data with similar circular buffers and priority queues for unconfirmed and lost ranges. It includes methods like `init`, `deinit`, and `insertMessage` for managing sent messages and their confirmation status.

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

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_7*
