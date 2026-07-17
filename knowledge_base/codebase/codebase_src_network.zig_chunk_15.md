# [hard/codebase_src_network.zig] - Chunk 15

**Type:** networking
**Keywords:** monotonic timestamp, connection timeout, keepalive packet, fully confirmed index, packet loss check, congestion bandwidth, RTT estimate, mutex lock defer unlock
**Symbols:** Connection, processNextPackets, disconnect
**Concepts:** packet processing loop, timeout handling, keepalive exchange, sequence acknowledgements, channel management, congestion control, bandwidth estimation, mutex locking, BinaryWriter serialization

## Summary
This chunk implements the Connection struct's packet processing loop, handling timeouts, keepalive exchanges, sequence acknowledgements across lossy/secure/slow channels, and congestion control with bandwidth estimation.

## Explanation
The processNextPackets method first checks for connection timeout using a monotonic timestamp comparison; if exceeded it logs 'timeout' and disconnects. It then switches on self.connectionState: awaitingClientConnection sends keepalive packets every 100ms after the nextPacketTimestamp threshold; awaitingServerResponse or awaitingClientAcknowledgement constructs an init packet containing the connectionIdentifier and fullyConfirmedIndex values from each channel's sendBuffer, writes it via a BinaryWriter with capacity calculated as 1 + sizeOf(i64) + 3*sizeOf(SequenceIndex), sends through manager.send, and returns early. The connected state does nothing; disconnected/paused also return immediately. After handling the switch, processPacketLoss is called for each of lossyChannel, secureChannel, and slowChannel with their respective checkForLosses methods passing self and timestamp. Idle time tracking accumulates relativeIdleTime when timestamps exceed nextPacketTimestamp by more than 10ms; if combined idle plus send time exceeds rttEstimate it halves both counters. Confirmation packets are sent in a while loop as long as the timestamp is past nextConfirmationTimestamp and queuedConfirmations is not empty, invoking sendConfirmationPacket. Congestion control attempts to increase bandwidth only when relativeSendTime/2 > relativeIdleTime; inside a block that acquires self.mutex (defer unlock), it iterates twice with permutation incrementing modulo 2 to alternate between lossyChannel.sendNextPacketAndGetSize and secureChannel.sendNextPacketAndGetSize, or continues if slowChannel.sendNextPacketAndGetSize returns null. The returned dataLen is converted to networkLen as f32 by adding headerOverhead, then packetTime is computed using bandwidthEstimateInBytesPerRtt and rttEstimate with a floor division and max of 1; nextPacketTimestamp is advanced by packetTime and relativeSendTime incremented accordingly.

## Related Questions
- How does the timeout detection logic determine when to disconnect a Connection?
- What exact fields are written into the init packet for awaitingServerResponse and awaitingClientAcknowledgement states?
- In what order do processPacketLoss calls occur across the three channel types inside processNextPackets?
- Under which condition is relativeIdleTime accumulated versus reset in the idle time tracking block?
- How does the permutation variable ensure alternating send attempts between lossy and secure channels within a single iteration of the congestion control loop?
- What happens to nextPacketTimestamp when a confirmation packet is sent via sendConfirmationPacket?
- Does processNextPackets ever modify self.connectionState directly, or only through disconnect?
- How is headerOverhead incorporated into networkLen before computing packetTime?
- What is the purpose of the defer self.mutex.unlock() inside the congestion control block?
- If queuedConfirmations becomes empty while timestamp exceeds nextConfirmationTimestamp, does sendConfirmationPacket still execute?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_15*
