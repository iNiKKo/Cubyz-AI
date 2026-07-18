# [hard/codebase_src_network.zig] - Chunk 6

**Type:** networking
**Keywords:** MTU, header overhead, range buffer, receive buffer, circular buffer, sequence index, congestion control
**Symbols:** Connection, Connection.maxMtu, Connection.importantHeaderSize, Connection.minMtu, Connection.headerOverhead, Connection.congestionControl_historySize, Connection.congestionControl_historyMask, Connection.minimumBandWidth, Connection.receiveBufferSize, Connection.packetsSent, Connection.packetsResent, Connection.internalMessageOverhead, Connection.internalHeaderOverhead, Connection.externalHeaderOverhead, Connection.SequenceIndex, Connection.LossStatus, Connection.RangeBuffer, Connection.RangeBuffer.Range, Connection.RangeBuffer.Range.start, Connection.RangeBuffer.Range.len, Connection.RangeBuffer.Range.end, Connection.RangeBuffer.ranges, Connection.RangeBuffer.init, Connection.RangeBuffer.clear, Connection.RangeBuffer.deinit, Connection.RangeBuffer.addRange, Connection.RangeBuffer.hasRange, Connection.RangeBuffer.extractFirstRange, Connection.ReceiveBuffer, Connection.ReceiveBuffer.Range, Connection.ReceiveBuffer.Range.start, Connection.ReceiveBuffer.Range.len, Connection.ReceiveBuffer.Header, Connection.ReceiveBuffer.Header.protocolIndex, Connection.ReceiveBuffer.Header.size, Connection.ReceiveBuffer.ranges, Connection.ReceiveBuffer.availablePosition, Connection.ReceiveBuffer.currentReadPosition, Connection.ReceiveBuffer.decryptedBuffer, Connection.ReceiveBuffer.buffer, Connection.ReceiveBuffer.header, Connection.ReceiveBuffer.protocolBuffer, Connection.ReceiveBuffer.channelId, Connection.ReceiveBuffer.init, Connection.ReceiveBuffer.deinit, Connection.ReceiveBuffer.applyRanges
**Concepts:** networking, buffer management, packet handling, sequence index tracking

## Summary
Defines network connection structures and buffer management for packet handling.

## Explanation
This chunk defines the `Connection` struct, which includes constants for MTU sizes, header overheads, and congestion control parameters. It also contains nested structs like `RangeBuffer` and `ReceiveBuffer`, each with their own methods for managing ranges of sequence indices and buffers for receiving data. The `RangeBuffer` manages non-overlapping ranges and supports adding, checking, and extracting ranges. The `ReceiveBuffer` handles incoming data, including decryption and buffer management, using fixed-size circular buffers.

## Code Example
```zig
pub fn init() RangeBuffer {
	return .{
		.ranges = .empty,
	};
}
```

## Related Questions
- What is the maximum MTU size defined in the Connection struct?
- How does the RangeBuffer handle overlapping ranges?
- What methods are available for managing the ReceiveBuffer?
- How is data extracted from the ReceiveBuffer?
- What is the purpose of the congestion control parameters in the Connection struct?
- How does the RangeBuffer ensure non-overlapping ranges?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_6*
