# [hard/codebase_src_network.zig] - Chunk 4

**Type:** networking
**Keywords:** ConnectionManager, socket, thread, mutex, packet, connection
**Symbols:** ConnectionManager, ConnectionManager.socket, ConnectionManager.thread, ConnectionManager.threadId, ConnectionManager.externalAddress, ConnectionManager.online, ConnectionManager.running, ConnectionManager.connections, ConnectionManager.requests, ConnectionManager.mutex, ConnectionManager.waitingToFinishReceive, ConnectionManager.allowNewConnections, ConnectionManager.receiveBuffer, ConnectionManager.world, ConnectionManager.localPort, ConnectionManager.packetSendRequests, ConnectionManager.PacketSendRequest, ConnectionManager.PacketSendRequest.data, ConnectionManager.PacketSendRequest.target, ConnectionManager.PacketSendRequest.time, ConnectionManager.init, ConnectionManager.@continue, ConnectionManager.deinit, ConnectionManager.pause, ConnectionManager.makeOnline, ConnectionManager.send, ConnectionManager.sendRequest, ConnectionManager.addConnection, ConnectionManager.finishCurrentReceive, ConnectionManager.removeConnection, ConnectionManager.onReceive, ConnectionManager.run
**Concepts:** networking, thread management, mutex synchronization, packet handling, connection management

## Summary
The ConnectionManager struct manages network connections, handles incoming and outgoing packets, and maintains a list of active connections.

## Explanation
The ConnectionManager struct manages network connections, handles incoming and outgoing packets, and maintains a list of active connections. It initializes a socket on a specified local port, manages threads for handling network operations, and uses mutexes to synchronize access to shared resources. The struct maintains lists of active connections and pending requests. It provides methods for sending data, handling incoming packets, adding and removing connections, and managing the lifecycle of the network thread.

The `init` method initializes the ConnectionManager with a local port and options, setting up the socket and starting the network thread. The `@continue` method resumes network operations if they are paused. The `deinit` method properly shuts down the network manager by disconnecting all connections and deinitializing resources. The `pause` method stops network operations and cleans up pending requests and packets.

The `makeOnline` method sets the external address using STUN and marks the connection as online. The `send` method sends data to a target address, either immediately or with a scheduled time. The `sendRequest` method sends a request and waits for a response within a specified timeout. The `addConnection` method adds a new connection if it is not already connected. The `finishCurrentReceive` method ensures that the current receive operation is completed before proceeding. The `removeConnection` method removes a connection from the list.

The `onReceive` method processes incoming packets, either by forwarding them to an existing connection or handling them as part of an active request. If the packet is unknown and new connections are allowed, it attempts to connect a new user. Otherwise, it logs a warning.

The `run` method is the main loop that processes incoming packets, sends queued packets, and handles connection management. It ensures that packets are sent at regular intervals and keeps the network port open by sending periodic messages if there is no activity.

## Code Example
```zig
fn compare(_: void, a: PacketSendRequest, b: PacketSendRequest) std.math.Order {
			return std.math.order(a.time, b.time);
		}
```

## Related Questions
-  How does the ConnectionManager handle incoming packets?
-  What is the purpose of the `packetSendRequests` priority queue in ConnectionManager?
-  Can you explain how the ConnectionManager manages multiple connections simultaneously?
-  How does the ConnectionManager ensure thread safety when accessing shared resources?
-  What mechanisms are used to keep the network port open after a period of inactivity?
-  How does the ConnectionManager handle errors during packet reception and transmission?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_4*
