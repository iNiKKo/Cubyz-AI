# [hard/codebase_src_network_protocols.zig] - Chunk 4

**Type:** networking
**Keywords:** network protocols, Zon format, entity management, item drops, secure communication
**Symbols:** entity, entity.id, entity.clientReceive, entity.send
**Concepts:** networking, entity ECS, binary serialization

## Summary
Handles entity-related network protocols for client-server communication.

## Explanation
This chunk defines a struct `entity` with methods to receive and send entity data over a network connection. The `clientReceive` method processes incoming binary data using the Zon format, which can either remove or add entities based on the parsed elements. Specifically, if an element is of type `.int`, it removes the corresponding entity; if it's of type `.object`, it adds the entity. If an unrecognized zon parameter is encountered, it logs an error message. The method also handles item drops by removing existing ones or loading new ones from the received data. The `send` method sends messages securely with a specific protocol ID.

## Code Example
```zig
fn send(conn: *Connection, msg: []const u8) void {
	conn.send(.secure, id, msg);
}
```

## Related Questions
- How does the `clientReceive` method process incoming data?
- What is the purpose of the `send` method in this struct?
- How are entities managed based on the Zon elements received?
- What happens if an unrecognized zon parameter is encountered?
- How are item drops handled in the received data?
- What is the role of the `id` constant in this struct?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_4*
