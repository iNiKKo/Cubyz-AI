# [hard/codebase_src_network.zig] - Chunk 3

**Type:** networking
**Keywords:** STUN, address resolution, mutex locking, priority queue, network connections
**Symbols:** ipServerList, MAPPED_ADDRESS, XOR_MAPPED_ADDRESS, MAGIC_COOKIE, requestAddress, findIPPort, verifyHeader, ConnectionManager, ConnectionManager.socket, ConnectionManager.thread, ConnectionManager.threadId, ConnectionManager.externalAddress, ConnectionManager.online, ConnectionManager.running, ConnectionManager.connections, ConnectionManager.requests, ConnectionManager.mutex, ConnectionManager.waitingToFinishReceive, ConnectionManager.allowNewConnections, ConnectionManager.receiveBuffer, ConnectionManager.world, ConnectionManager.localPort, ConnectionManager.packetSendRequests, ConnectionManager.PacketSendRequest, ConnectionManager.PacketSendRequest.data, ConnectionManager.PacketSendRequest.target, ConnectionManager.PacketSendRequest.time, ConnectionManager.init
**Concepts:** networking, STUN protocol, thread safety, packet management

## Summary
Handles network connections and address requests using STUN protocol.

## Explanation
The chunk defines a `ConnectionManager` struct responsible for managing network connections, sending and receiving packets, and handling address requests through the STUN protocol. It includes methods like `requestAddress` to query external addresses from STUN servers, `findIPPort` to parse IP and port information from STUN responses, and `verifyHeader` to validate STUN message headers. The struct uses a mutex for thread safety and manages lists of connections and requests. It also initializes a priority queue for packet send requests.

## Code Example
```zig
fn verifyHeader(data: []const u8, transactionID: []const u8) !void {
	if (data[0] != 0x01 or data[1] != 0x01) return error.NotABinding;
	if (@as(u16, @intCast(data[2] & 0xff))*256 + (data[3] & 0xff) != data.len - 20) return error.BadSize;
	for (MAGIC_COOKIE, 0..) |cookie, i| {
		if (data[i + 4] != cookie) return error.WrongCookie;
	}
	for (transactionID, 0..) |_, i| {
		if (data[i + 8] != transactionID[i]) return error.WrongTransaction;
	}
}
```

## Related Questions
- What is the purpose of the `requestAddress` function?
- How does the `findIPPort` function parse IP and port information from STUN responses?
- What checks are performed in the `verifyHeader` function to validate STUN message headers?
- What data structures are used for managing connections and requests in the `ConnectionManager` struct?
- How is thread safety ensured in the `ConnectionManager` struct?
- What is the role of the priority queue in packet management within the `ConnectionManager`?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_3*
