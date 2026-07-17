# [hard/codebase_src_network.zig] - Chunk 12

**Type:** implementation
**Keywords:** ConnectionManager, SecureChannel, lossyChannel, slowChannel, rttEstimate, bruteforcingPort, symmetricNAT, Atomic, CircularBufferQueue, handShakeState
**Symbols:** Connection, HandShakeState
**Concepts:** connection lifecycle, state machine, secure channel negotiation, RTT estimation, symmetric NAT handling, reconnect prevention, channel multiplexing, atomic state transitions

## Summary
This chunk defines the Connection struct and its lifecycle methods, including initialization with secure/lossy channels, state transitions (disconnected/paused/restarting), and partial implementation of the checkRestartCounter protocol handler.

## Explanation
The Connection struct holds a manager pointer, optional user reference, remote Address, multiple Channel instances (lossyChannel, secureChannel, slowChannel), restart counters, RTT estimation fields, atomic ConnectionState and HandShakeState enums, a Mutex, and a CircularBufferQueue for queued confirmations. The init function allocates the Connection via main.globalAllocator, sets default states (.awaitingClientConnection or .awaitingServerResponse depending on user presence), initializes lossyChannel as a random sequence with 1ms latency, slowChannel similarly with 100ms, and secureChannel with 10ms latency and client/server role determined by user. It parses the ipPort string using std.mem.splitScalar(u8, ':'), resolves the IP via Socket.resolveIP, handles symmetric NAT detection when port contains '?', and sets bruteforcingPort accordingly. If parsing fails it falls back to settings.defaultPort with an error log. After adding itself to the manager via result.manager.addConnection(result), init returns the pointer. The deinit method checks if still connected (not disconnected) and calls disconnect() then finishCurrentReceive(), then tears down all channels, clears queuedConfirmations, and frees memory. The pause function asserts not already paused, stores .paused only from .connected, increments restartCounter, and invokes user.pause(). The @

## Related Questions
- What are the possible values of ConnectionState and when is each used?
- How does Connection.init decide between awaiting a client connection or server response?
- In what order are the channels initialized during Connection creation?
- Which fields are cleaned up in deinit if the connection was already disconnected?
- What happens to restartCounter when pause() is called on an active connection?
- How does the code detect and handle symmetric NAT from the ipPort string?
- Where is the remoteAddress populated with IP and port values?
- What role does main.globalAllocator play in Connection memory management?
- Is there any synchronization around mutable fields besides the Mutex declaration?
- How are queuedConfirmations initialized and what determines their capacity?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_12*
