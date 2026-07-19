# [hard/codebase_src_network.zig] - Chunk 11

**Type:** networking
**Keywords:** mbedtls_ssl_read, mbedtls_ssl_write, mutex locking, thread safety, handshaking, reconnection logic
**Symbols:** Connection, Connection.manager, Connection.user, Connection.remoteAddress, Connection.bruteforcingPort, Connection.bruteForcedPortRange, Connection.lossyChannel, Connection.secureChannel, Connection.slowChannel, Connection.restartChannelCounter, Connection.restartCounter, Connection.hasRttEstimate, Connection.rttEstimate, Connection.rttUncertainty, Connection.lastRttSampleTime, Connection.nextPacketTimestamp, Connection.nextConfirmationTimestamp, Connection.queuedConfirmations, Connection.mtuEstimate, Connection.bandwidthEstimateInBytesPerRtt, Connection.slowStart, Connection.relativeSendTime, Connection.relativeIdleTime, Connection.connectionState, Connection.handShakeState, Connection.handShakeWaiting, Connection.lastConnectionTime, Connection.connectionIdentifier, Connection.remoteConnectionIdentifier, Connection.mutex, SecureChannel, SecureChannel.sslContext, SecureChannel.super, SecureChannel.mutex, SecureChannel.receiveThroughTls, SecureChannel.sendThroughTls, SecureChannel.receive, SecureChannel.send, SecureChannel.receiveConfirmationAndGetTimestamp, SecureChannel.checkForLosses, SecureChannel.sendNextPacketAndGetSize, SecureChannel.getStatistics, ChannelId, ChannelId.lossy, ChannelId.secure, ChannelId.slow, ChannelId.confirmation, ChannelId.init, ChannelId.keepalive, ChannelId.disconnect, ConfirmationData, ConfirmationData.channel, ConfirmationData.start, ConfirmationData.receiveTimeStamp, ConnectionState, ConnectionState.awaitingClientConnection, ConnectionState.awaitingServerResponse, ConnectionState.awaitingClientAcknowledgement, ConnectionState.connected, ConnectionState.disconnected, ConnectionState.paused, HandShakeState, HandShakeState.start, HandShakeState.userData, HandShakeState.signatureRequest, HandShakeState.signatureResponse, HandShakeState.reload, HandShakeState.assets, HandShakeState.serverData, HandShakeState.complete
**Concepts:** networking, TLS encryption, connection management, data transmission channels

## Summary
The `Connection` struct manages secure and lossy data transmission channels for a network connection, handling TLS encryption, packet sending/receiving, and state management.

## Explanation
**Explanation**

The `Connection` struct is central to managing network connections in the Cubyz engine. It includes fields for various channels (lossy, secure, slow) and their respective states. The struct provides methods for initializing a connection, sending and receiving data through these channels, and managing TLS encryption using the `SecureChannel`. It also handles connection state transitions, such as handshaking and reconnection logic. The `Connection` struct uses mutexes for thread safety during concurrent operations on shared resources like buffers and states.

**Fields of Connection Struct:**
- **manager**: Pointer to the `ConnectionManager`.
- **user**: Optional pointer to the user associated with the connection.
- **remoteAddress**: Address of the remote endpoint.
- **bruteforcingPort**: Boolean indicating if port bruteforcing is active.
- **bruteForcedPortRange**: Range of ports being brute forced.
- **lossyChannel**: Channel for lossy data transmission.
- **secureChannel**: Secure channel for encrypted data transmission.
- **slowChannel**: Channel for slow data transmission.
- **restartChannelCounter**: Array to count restarts for different channels.
- **restartCounter**: Counter for total restarts.
- **hasRttEstimate**: Boolean indicating if RTT estimate is available.
- **rttEstimate**: Estimated round-trip time in milliseconds.
- **rttUncertainty**: Uncertainty of the RTT estimate.
- **lastRttSampleTime**: Timestamp of the last RTT sample.
- **nextPacketTimestamp**: Timestamp for the next packet to be sent.
- **nextConfirmationTimestamp**: Timestamp for the next confirmation to be sent.
- **queuedConfirmations**: Circular buffer queue for queued confirmations.
- **mtuEstimate**: Estimated maximum transmission unit in bytes.
- **bandwidthEstimateInBytesPerRtt**: Bandwidth estimate in bytes per RTT.
- **slowStart**: Boolean indicating if slow start is active.
- **relativeSendTime**: Relative send time for congestion control.
- **relativeIdleTime**: Relative idle time for connection management.
- **connectionState**: Atomic variable representing the current state of the connection (e.g., `awaitingClientConnection`, `connected`).
- **handShakeState**: Atomic variable representing the current state of the handshake process (e.g., `start`, `complete`).
- **handShakeWaiting**: Condition for waiting during the handshake process.
- **lastConnectionTime**: Timestamp of the last connection attempt.
- **connectionIdentifier**: Unique identifier for the connection from the local side.
- **remoteConnectionIdentifier**: Unique identifier for the connection from the remote side.
- **mutex**: Mutex for thread safety during concurrent operations.

**Methods of Connection Struct:**
- **init**: Initializes a new `Connection` instance with default values and sets up channels.

**SecureChannel Struct Methods:**
- **receiveThroughTls**: Reads data from the TLS context into an output buffer, handling errors and unlocking the mutex after use.
- **sendThroughTls**: Writes data to the TLS context, handling errors and unlocking the mutex after use.
- **receive**: Receives secure data through the `SecureChannel` using the superclass method.
- **send**: Sends secure data through the `SecureChannel` using the superclass method, asserting that the handshake is over before sending.
- **receiveConfirmationAndGetTimestamp**: Retrieves a confirmation result for a given start index.
- **checkForLosses**: Checks for packet losses in the connection and returns the loss status.
- **sendNextPacketAndGetSize**: Sends the next packet in the connection, considering congestion control, and returns its size if sent.
- **getStatistics**: Retrieves statistics about unconfirmed and queued packets.

**Enumerations:**
- **ChannelId**: Enumerates different types of channels (e.g., `lossy`, `secure`).
- **ConnectionState**: Enumerates possible states of a connection (e.g., `awaitingClientConnection`, `connected`).
- **HandShakeState**: Enumerates stages of the handshake process (e.g., `start`, `complete`).

## Code Example
```zig
pub fn receive(self: *SecureChannel, conn: *Connection, start: SequenceIndex, data: []const u8) !ReceiveBuffer.ReceiveStatus {
			return self.super.receiveBuffer.receiveSecure(self, conn, start, data);
		}
```

## Related Questions
- What is the purpose of the `SecureChannel` struct in the `Connection` module?
- How does the `Connection` struct handle TLS encryption for data transmission?
- What are the different states a connection can be in according to the `ConnectionState` enum?
- How does the `Connection` struct manage concurrent operations on shared resources?
- What is the role of the `HandShakeState` enum in the connection process?
- How does the `Connection` struct initialize its various channels and states?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_11*
