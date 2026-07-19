# [hard/codebase_src_network.zig] - Chunk 13

**Type:** networking
**Keywords:** mutex locking, thread safety, RTT estimation, packet loss, bandwidth adjustment
**Symbols:** send, isConnected, isServerSide, handlePacketLoss, increaseCongestionBandwidth, receiveConfirmationPacket, sendConfirmationPacket, receive, tryReceive
**Concepts:** networking, connection management, packet handling, congestion control

## Summary
Handles network connections, including sending and receiving packets, managing connection states, and adjusting congestion control parameters.

## Explanation
This chunk defines the `Connection` struct with methods for sending and receiving data over different channels. It includes logic for handling packet loss, increasing congestion bandwidth, and processing confirmation packets to estimate round-trip times (RTT). The code also manages connection states and ensures thread safety using mutexes.

### Detailed Explanation:
- **send Method**: Sends data over a specified channel with a given protocol index. It asserts that the handshake state is complete or the protocol index matches specific IDs. It increments the bytes sent counter for the protocol, locks the mutex, and sends the data through the appropriate channel (lossy, secure, slow). If sending fails, it logs an error and disconnects.

- **isConnected Method**: Checks if the connection state is `connected` by locking the mutex and loading the connection state atomically.

- **isServerSide Method**: Determines if a connection is server-side by checking if the user field is not null.

- **handlePacketLoss Method**: Adjusts congestion control parameters based on packet loss status. If there is no loss, it returns immediately. For double loss, it increases the RTT estimate and halves the bandwidth estimate, ensuring it does not drop below a minimum MTU value.

- **increaseCongestionBandwidth Method**: Increases the bandwidth estimate based on whether the connection is in slow start mode or not. In slow start, it adds the full packet length to the estimate; otherwise, it uses a more complex calculation involving the packet length, current bandwidth estimate, and MTU estimate.

- **receiveConfirmationPacket Method**: Processes confirmation packets by reading channel IDs, time offsets, and sequence indices from the reader. It calculates RTT for each confirmed packet and updates congestion control parameters if necessary. It also adjusts the RTT estimate using a formula based on RFC 6298 with minor changes.

- **sendConfirmationPacket Method**: Sends confirmation packets containing information about received packets. It writes channel IDs, time offsets, and sequence indices to a binary writer and sends the data through the network manager.

- **receive Method**: Receives data and processes it using `tryReceive`. If an error occurs, it logs the error, prints the stack trace if available, and disconnects.

- **tryReceive Method**: Processes incoming packets by reading channel IDs and handling initialization packets. It updates connection states and connects channels based on received sequence indices.

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
