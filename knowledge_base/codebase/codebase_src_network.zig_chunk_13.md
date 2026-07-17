# [hard/codebase_src_network.zig] - Chunk 13

**Type:** networking
**Keywords:** networking, connection states, user interactions, packet loss, congestion control, mutex locking, binary serialization, timestamp handling
**Symbols:** Connection, Connection.restartCounter, Connection.user, Connection.connectionState, Connection.handShakeState, Connection.mutex, Connection.lossyChannel, Connection.secureChannel, Connection.slowChannel, Connection.restartChannelCounter, Connection.rttEstimate, Connection.bandwidthEstimateInBytesPerRtt, Connection.mtuEstimate, Connection.slowStart, Connection.queuedConfirmations, Connection.lastRttSampleTime, Connection.nextPacketTimestamp, Connection.hasRttEstimate
**Concepts:** networking, connection management, packet processing, congestion control

## Summary
Handles network connection management and packet processing for Cubyz.

## Explanation
This chunk defines the `Connection` struct and its methods for managing network connections in Cubyz. It includes functions for restarting connections, sending packets, checking restart counters, handling packet loss, increasing congestion bandwidth, receiving confirmation packets, and sending confirmation packets. The code also manages connection states, user interactions, and congestion control mechanisms.

## Code Example
```zig
fn isConnected(self: *Connection) bool {
	self.mutex.lock();
	defer self.mutex.unlock();

	return self.connectionState.load(.monotonic) == .connected;
}
```

## Related Questions
- How does the `Connection` struct manage its connection state?
- What is the role of the `restartCounter` in the `Connection` struct?
- How does the `send` method handle different types of channels?
- What steps are taken to handle packet loss in a connection?
- How is congestion bandwidth increased in a connection?
- How does the `receiveConfirmationPacket` method update RTT estimates?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_13*
