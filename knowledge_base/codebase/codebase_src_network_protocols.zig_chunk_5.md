# [hard/codebase_src_network_protocols.zig] - Chunk 5

**Type:** networking
**Keywords:** network protocols, binary serialization, connection handling, update types, state updates
**Symbols:** Connection, genericUpdate, genericUpdate.id, genericUpdate.UpdateType, genericUpdate.WorldEditPosition, genericUpdate.ClearType, genericUpdate.clientReceive, genericUpdate.serverReceive, genericUpdate.sendGamemode, genericUpdate.sendTPCoordinates, genericUpdate.sendWorldEditPos
**Concepts:** networking, client-server communication, game state synchronization

## Summary
Handles network communication for generic updates in the Cubyz engine.

## Explanation
This chunk defines functions and data structures for sending and receiving generic updates over a secure connection. It includes methods to send various types of updates such as gamemode changes, teleportation coordinates, world edit positions, time synchronization, biome changes, particle effects, and chat clearing. The `clientReceive` function processes incoming messages on the client side, updating game state accordingly. Conversely, the `serverReceive` function handles server-specific logic for certain update types. The chunk also provides utility functions like `sendGamemode`, `sendTPCoordinates`, and `sendWorldEditPos` to facilitate sending specific updates.

## Code Example
```zig
pub fn send(conn: *Connection, msg: []const u8) void {
	conn.send(.secure, id, msg);
}
```

## Related Questions
- How does the `send` function work in this chunk?
- What types of updates are handled by `clientReceive`?
- What is the purpose of the `serverReceive` function?
- How are gamemode changes sent over the network?
- What happens when a client receives a world edit position update?
- How does the engine handle time synchronization between client and server?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_5*
