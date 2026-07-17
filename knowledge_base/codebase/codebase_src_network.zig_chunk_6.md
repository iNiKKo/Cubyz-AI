# [hard/codebase_src_network.zig] - Chunk 6

**Type:** networking
**Keywords:** networking, socket communication, packet queue, mutex locking, error logging
**Symbols:** UnconfirmedPacket, Connection, Connection.maxMtu, Connection.importantHeaderSize, Connection.minMtu, Connection.headerOverhead, Connection.congestionControl_historySize, Connection.congestionControl_historyMask, Connection.minimumBandWidth, Connection.receiveBufferSize, Connection.packetsSent, Connection.packetsResent, Connection.internalMessageOverhead, Connection.internalHeaderOverhead, Connection.externalHeaderOverhead, Connection.SequenceIndex, Connection.LossStatus, Connection.RangeBuffer, Connection.RangeBuffer.Range, Connection.RangeBuffer.init, Connection.RangeBuffer.clear, Connection.RangeBuffer.deinit, Connection.RangeBuffer.addRange, Connection.RangeBuffer.hasRange, Connection.RangeBuffer.extractFirstRange
**Concepts:** networking, packet processing, error handling, connection management

## Summary
The chunk handles network packet processing, including error handling and sending packets with timing control.

## Explanation
The chunk processes incoming errors by logging them appropriately based on the type of error. It manages outgoing packets by checking a queue for packets that are due to be sent and sending them using a socket. The chunk also ensures that packets are sent roughly every millisecond, processing each connection's next packets and keeping external connections alive with periodic messages if no activity is detected.

## Related Questions
- How does the chunk handle errors received during packet processing?
- What is the maximum UDP packet size defined in the Connection struct?
- How are packets managed for sending, and what controls their timing?
- What statistics are maintained by the Connection struct?
- How does the chunk ensure that external connections remain active?
- What is the purpose of the RangeBuffer structure within the Connection?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_6*
