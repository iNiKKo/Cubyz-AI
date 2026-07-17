# [hard/codebase_src_network.zig] - Chunk 7

**Type:** networking
**Keywords:** buffer management, range merging, header parsing, protocol execution, secure channel
**Symbols:** ReceiveBuffer, ReceiveBuffer.Range, ReceiveBuffer.Header, ReceiveBuffer.ranges, ReceiveBuffer.availablePosition, ReceiveBuffer.currentReadPosition, ReceiveBuffer.decryptedBuffer, ReceiveBuffer.buffer, ReceiveBuffer.header, ReceiveBuffer.protocolBuffer, ReceiveBuffer.channelId, ReceiveBuffer.init, ReceiveBuffer.deinit, ReceiveBuffer.applyRanges, ReceiveBuffer.getHeaderInformation, ReceiveBuffer.collectRangesAndExecuteProtocols, ReceiveBuffer.ReceiveStatus, ReceiveBuffer.receive, ReceiveBuffer.receiveSecure, SendBuffer
**Concepts:** networking, data buffering, protocol handling, secure communication

## Summary
The chunk defines the `ReceiveBuffer` and `SendBuffer` structures for handling network data reception and transmission.

## Explanation
The `ReceiveBuffer` structure manages incoming network data, including merging ranges, checking for existing ranges, extracting the first range, initializing and deinitializing resources, applying ranges with secure channel support, retrieving header information, collecting ranges and executing protocols, and receiving data securely. The `SendBuffer` structure is defined but not fully implemented in this chunk.

## Code Example
```zig
pub fn hasRange(self: *RangeBuffer, range: Range) bool {
	for (self.ranges.items) |other| {
		if (range.start -% other.start >= 0 and range.end() -% other.end() <= 0) {
			return true;
		}
	}
	return false;
}
```

## Related Questions
- How does the `ReceiveBuffer` handle incoming data ranges?
- What is the purpose of the `applyRanges` method in `ReceiveBuffer`?
- How does the `ReceiveBuffer` manage header information?
- What steps are involved in collecting and executing protocols in `ReceiveBuffer`?
- How does the `SendBuffer` structure relate to network communication?
- What conditions lead to a data range being accepted or rejected?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_7*
