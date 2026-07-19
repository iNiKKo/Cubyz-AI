# [hard/codebase_src_network.zig] - Chunk 8

**Type:** networking
**Keywords:** sequence index, message insertion, secure transmission, acknowledgment processing, packet retrieval, memory allocation
**Symbols:** SendBuffer, SendBuffer.fullyConfirmedIndex, SendBuffer.highestSentIndex, SendBuffer.nextIndex, SendBuffer.lastUnsentTime, SendBuffer.init, SendBuffer.deinit, SendBuffer.insertMessage, SendBuffer.insertMessageSecure, ReceiveConfirmationResult, SendBuffer.receiveConfirmationAndGetTimestamp, SendBuffer.checkForLosses, SendBuffer.getNextPacketToSend
**Concepts:** networking, packet management, loss detection, retransmission, buffer handling

## Summary
The SendBuffer struct manages the sending and confirmation of network packets, handling message insertion, loss detection, and packet retrieval for transmission.

## Explanation
**Explanation**
The `SendBuffer` struct is responsible for managing the sending and confirmation of network packets. It maintains several fields including:

- **fullyConfirmedIndex**: Tracks the index of the last fully confirmed packet.
- **highestSentIndex**: Tracks the index of the highest sent packet.
- **nextIndex**: Tracks the next available index for new messages.
- **lastUnsentTime**: Records the timestamp of the last unsent message.

The `init` function initializes these fields and allocates memory for internal buffers. The `deinit` function frees allocated resources. The `insertMessage` and `insertMessageSecure` methods add messages to the buffer, with the latter also handling secure transmission through a TLS channel. The `receiveConfirmationAndGetTimestamp` method processes acknowledgments from the network, updating internal state based on received confirmations. The `checkForLosses` method detects packet loss and marks packets for retransmission if necessary. The `getNextPacketToSend` method retrieves the next packet to send, either resending lost packets or sending new ones based on buffer availability and allowed delay.

**Code Example**
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

**Related Questions**
- What is the purpose of the `init` function in `SendBuffer`?
  - The `init` function initializes the `SendBuffer` struct, setting up internal buffers and initializing fields like `fullyConfirmedIndex`, `highestSentIndex`, `nextIndex`, and `lastUnsentTime` with the provided index.

- How does `SendBuffer` handle secure message transmission?
  - The `insertMessageSecure` method handles secure message transmission by sending data through a TLS channel if a secure channel is provided. Otherwise, it adds the message to the buffer for regular transmission.

- What information does `receiveConfirmationAndGetTimestamp` update?
  - This method updates internal state based on received confirmations, including marking packets as confirmed and updating timestamps.

- How does `checkForLosses` detect packet loss?
  - The `checkForLosses` method detects packet loss by checking the timestamp of unconfirmed packets against the current time and retransmission timeout. It marks packets for retransmission if they have not been acknowledged within the timeout period.

- What conditions determine when a new packet is sent in `getNextPacketToSend`?
  - A new packet is sent if there are no lost packets to resend, the buffer has space available, and the allowed delay condition is met. The method also ensures that the highest sent index does not exceed the receive buffer size.

- How does `SendBuffer` manage memory allocation and deallocation?
  - Memory allocation is handled during initialization with `.init(main.globalAllocator, 1 << 10)` for lost ranges and `.init(main.globalAllocator, 1 << 20)` for the main buffer. Deallocation is managed by the `deinit` function, which frees resources using `main.globalAllocator.allocator`.

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
