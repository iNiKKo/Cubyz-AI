# [hard/codebase_src_network_protocols.zig] - Chunk 6

**Type:** networking
**Keywords:** network protocols, UTF-8 validation, message length checks, binary data handling, server-client communication
**Symbols:** chat, chat.id, chat.clientReceive, chat.serverReceive, chat.send, lightMapRequest, lightMapRequest.id, lightMapRequest.serverReceive, lightMapRequest.sendRequest
**Concepts:** networking, chat system, light map generation

## Summary
Defines network protocols for chat and light map requests.

## Explanation
This chunk defines two network protocols: 'chat' and 'lightMapRequest'. The 'chat' protocol handles sending and receiving chat messages, ensuring they are valid UTF-8 and within length limits. Specifically, client-received messages must be valid UTF-8, and server-received messages must not exceed 10,000 bytes or 1,000 visible characters. The 'lightMapRequest' protocol manages requests for light maps, validating input data and queuing tasks for the server to process. The ID for the chat protocol is 10, and the ID for the light map request protocol is 11.

The `send` function in the 'chat' protocol sends a message over a connection with a specified reliability mode and message ID.

The `clientReceive` function in the 'chat' protocol reads a message from the reader, validates its UTF-8 encoding, and adds it to the chat window if valid.

The `serverReceive` function in the 'chat' protocol reads a message from the reader, validates its UTF-8 encoding and length, logs an error if invalid, and forwards the message to the server with the user information.

The `sendRequest` function in the 'lightMapRequest' protocol sends multiple light map requests over a connection. It initializes a binary writer, writes each request's world coordinates and voxel size shift, and sends the data securely.

The `serverReceive` function in the 'lightMapRequest' protocol processes incoming light map requests. It reads the world coordinates and voxel size shift for each request, creates a map fragment position, and queues the task for the server to process with the user's reference count increased.

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
