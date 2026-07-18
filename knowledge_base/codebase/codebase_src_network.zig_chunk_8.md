# [hard/codebase_src_network.zig] - Chunk 8

**Type:** networking
**Keywords:** sequence index, message insertion, secure transmission, acknowledgment processing, packet retrieval, memory allocation
**Symbols:** SendBuffer, SendBuffer.fullyConfirmedIndex, SendBuffer.highestSentIndex, SendBuffer.nextIndex, SendBuffer.lastUnsentTime, SendBuffer.init, SendBuffer.deinit, SendBuffer.insertMessage, SendBuffer.insertMessageSecure, ReceiveConfirmationResult, SendBuffer.receiveConfirmationAndGetTimestamp, SendBuffer.checkForLosses, SendBuffer.getNextPacketToSend
**Concepts:** networking, packet management, loss detection, retransmission, buffer handling

## Summary
The SendBuffer struct manages the sending and confirmation of network packets, handling message insertion, loss detection, and packet retrieval for transmission.

## Explanation
The SendBuffer struct is responsible for managing the sending and confirmation of network packets. It maintains several fields including fullyConfirmedIndex, highestSentIndex, nextIndex, and lastUnsentTime to track the state of sent packets. The init function initializes these fields and allocates memory for internal buffers. The deinit function frees allocated resources. The insertMessage and insertMessageSecure methods add messages to the buffer, with the latter also handling secure transmission through a TLS channel. The receiveConfirmationAndGetTimestamp method processes acknowledgments from the network, updating internal state based on received confirmations. The checkForLosses method detects packet loss and marks packets for retransmission if necessary. The getNextPacketToSend method retrieves the next packet to send, either resending lost packets or sending new ones based on buffer availability and allowed delay.

## Code Example
```zig
pub fn init(index: SequenceIndex) SendBuffer {
	return .{
		.lostRanges = .init(main.globalAllocator, 1 << 10),
		.buffer = .init(main.globalAllocator, 1 << 20),
		.fullyConfirmedIndex = index,
		.highestSentIndex = index,
		.nextIndex = index,
		.lastUnsentTime = networkTimestamp(),
	};
}
```

## Related Questions
- What is the purpose of the init function in SendBuffer?
- How does SendBuffer handle secure message transmission?
- What information does receiveConfirmationAndGetTimestamp update?
- How does checkForLosses detect packet loss?
- What conditions determine when a new packet is sent in getNextPacketToSend?
- How does SendBuffer manage memory allocation and deallocation?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_8*
