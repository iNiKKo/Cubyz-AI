# [hard/codebase_src_network.zig] - Chunk 4

**Type:** api
**Keywords:** mutex locking, priority queue, thread spawning, socket initialization, error deferral, allocator ownership, atomic operations, signal notification
**Symbols:** ConnectionManager, PacketSendRequest, init, continue, deinit, pause, makeOnline, send, sendRequest, addConnection
**Concepts:** network connection management, threaded I/O loop, packet queuing with priority ordering, request-response timeout handling, STUN address resolution, mutex-protected state transitions, condition variable signaling, atomic online flag

## Summary
Chunk 4 defines the ConnectionManager struct and its public methods for managing network connections, including initialization with mutex/condition variables, thread spawning, pausing/resuming operations, STUN address resolution, packet sending (queued or direct), request handling with timeouts, and connection addition.

## Explanation
The chunk declares a ConnectionManager struct containing fields: mutex (Mutex), waitingToFinishReceive (Condition), allowNewConnections (bool), receiveBuffer ([Connection.maxMtu]u8), world (?*game.World), localPort (u16), packetSendRequests (PriorityQueue of PacketSendRequest). It defines PacketSendRequest as a struct with data ([]const u8), target (Address), time (i64) and a compare function ordering by time. The init function allocates ConnectionManager, sets allowNewConnections from options, initializes localPort, creates a Socket on the given port (with fallback to any port if AddressInUse), stores result.localPort after socket creation, calls continue(), then returns the pointer. The continue method checks running flag; if not running it returns early; otherwise it locks mutex, iterates connections calling each conn.continue(), clears requests and packetSendRequests, sets running true, spawns a thread named "Network Thread" in main.io namespace running run (not defined here), with errdefer logging on rename failure. The deinit method checks running flag and calls pause() if needed; then disconnects all connections via conn.disconnect(); deinitializes socket; deinitializes connections list using main.globalAllocator; finally destroys self from globalAllocator. The pause method asserts running is true, sets running false, joins the thread, locks mutex, signals all pending requests in self.requests (iterating items and calling request.requestNotifier.signal()), deinit requests queue, pops all packets from packetSendRequests freeing each packet.data, deinit packetSendRequests, then pauses all connections via conn.pause(). The makeOnline method checks online atomic flag; if false it calls stun.requestAddress(self) to resolve external address, stores true in online. The send method takes data, target, nanoTime; if nanoTime is provided it locks mutex, pushes a PacketSendRequest into packetSendRequests (duping data with main.globalAllocator.dupe), otherwise directly sends via self.socket.send(data, target). The sendRequest method sends immediately via socket, creates a Request struct with address and data, then within a block locks mutex, appends request to self.requests, calls request.requestNotifier.timedWait(&self.mutex, timeout) (catching any error), then iterates self.requests items swapping out the matching request; after unlocking it checks if request.data.ptr equals original data.ptr—if so returns null (no result); otherwise if allocator is main.globalAllocator it returns request.data directly, else duplicates request.data into a new allocation and frees request.data. The addConnection method signature begins but body not shown.

## Related Questions
- What happens if init is called with localPort == 0?
- How does continue handle the case when running is already false?
- Which allocator is used to free packet data in pause?
- Does sendRequest guarantee that request.data.ptr equals original data.ptr after a successful response?
- Can addConnection be called while another connection is being added?
- What error type does addConnection return if the target is already connected?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_4*
