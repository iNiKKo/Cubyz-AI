# [hard/codebase_src_network.zig] - Chunk 13

**Type:** networking
**Keywords:** mutex locking, thread safety, RTT estimation, packet loss, bandwidth adjustment
**Symbols:** send, isConnected, isServerSide, handlePacketLoss, increaseCongestionBandwidth, receiveConfirmationPacket, sendConfirmationPacket, receive, tryReceive
**Concepts:** networking, connection management, packet handling, congestion control

## Summary
Handles network connections, including sending and receiving packets, managing connection states, and adjusting congestion control parameters.

## Explanation
This chunk defines the `Connection` struct with methods for sending and receiving data over different channels. It includes logic for handling packet loss, increasing congestion bandwidth, and processing confirmation packets to estimate round-trip times (RTT). The code also manages connection states and ensures thread safety using mutexes.

## Code Example
```zig
pub fn isConnected(self: *Connection) bool {
	self.mutex.lock();
	defer self.mutex.unlock();

	return self.connectionState.load(.monotonic) == .connected;
}
```

## Related Questions
- What is the purpose of the `send` method in the Connection struct?
- How does the `handlePacketLoss` function adjust the bandwidth estimate?
- What state must a connection be in to send a handshake packet?
- How does the `receiveConfirmationPacket` method update RTT estimates?
- What ensures thread safety when managing connections?
- What is the role of the `sendConfirmationPacket` function?
- How does the `tryReceive` method handle initialization packets?
- What conditions trigger a disconnection in the receive methods?
- How are different channels (lossy, secure, slow) managed within the Connection struct?
- What is the significance of the `isServerSide` method in determining connection roles?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_13*
