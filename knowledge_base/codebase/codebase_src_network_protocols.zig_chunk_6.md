# [hard/codebase_src_network_protocols.zig] - Chunk 6

**Type:** networking
**Keywords:** network protocols, UTF-8 validation, message length checks, binary data handling, server-client communication
**Symbols:** chat, chat.id, chat.clientReceive, chat.serverReceive, chat.send, lightMapRequest, lightMapRequest.id, lightMapRequest.serverReceive, lightMapRequest.sendRequest
**Concepts:** networking, chat system, light map generation

## Summary
Defines network protocols for chat and light map requests.

## Explanation
This chunk defines two network protocols: 'chat' and 'lightMapRequest'. The 'chat' protocol handles sending and receiving chat messages, ensuring they are valid UTF-8 and within length limits. The 'lightMapRequest' protocol manages requests for light maps, validating input data and queuing tasks for the server to process.

## Code Example
```zig
pub fn send(conn: *Connection, msg: []const u8) void {
	conn.send(.lossy, id, msg);
}
```

## Related Questions
- What is the ID for the chat protocol?
- How does the client handle received chat messages?
- What validation checks are performed on server-received chat messages?
- What is the purpose of the 'sendRequest' function in lightMapRequest?
- How are invalid UTF-8 characters handled in chat messages?
- What data structure is used to queue light map requests on the server?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_6*
