# [hard/codebase_src_network.zig] - Chunk 5

**Type:** networking
**Keywords:** mutex locking, socket communication, packet sending, connection tracking, data processing
**Symbols:** ConnectionManager, ConnectionManager.mutex, ConnectionManager.requests, ConnectionManager.connections, ConnectionManager.threadId, ConnectionManager.running, ConnectionManager.receiveBuffer, ConnectionManager.socket, ConnectionManager.packetSendRequests, ConnectionManager.online, ConnectionManager.externalAddress, ConnectionManager.allowNewConnections
**Concepts:** networking, connection management, packet handling, thread safety

## Summary
The chunk implements network connection management and packet handling for the Cubyz engine.

## Explanation
This chunk defines a `ConnectionManager` struct that manages network connections, handles incoming data, and processes outgoing packets. It uses mutexes to ensure thread safety when accessing shared resources like request lists and connection lists. The `addConnection`, `removeConnection`, and `finishCurrentReceive` methods manage the list of active connections. The `onReceive` method processes incoming data, either by forwarding it to an existing connection or handling a new connection attempt. The `run` method continuously listens for incoming packets, processes them, and sends outgoing packets at regular intervals.

## Code Example
```zig
pub fn addConnection(self: *ConnectionManager, conn: *Connection) error{AlreadyConnected}!void {
	self.mutex.lock();
	defer self.mutex.unlock();
	for (self.connections.items) |other| {
		if (other.remoteAddress.ip == conn.remoteAddress.ip and other.remoteAddress.port == conn.remoteAddress.port) return error.AlreadyConnected;
	}
	self.connections.append(main.globalAllocator, conn);
}
```

## Related Questions
- How does the ConnectionManager handle incoming data?
- What is the purpose of the mutex in the ConnectionManager?
- How are connections added and removed from the ConnectionManager?
- What happens when a connection reset error occurs during receive?
- How does the ConnectionManager manage outgoing packets?
- What is the role of the packetSendRequests queue in the ConnectionManager?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_5*
