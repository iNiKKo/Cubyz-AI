# [hard/codebase_src_network_protocols.zig] - Chunk 8

**Type:** networking
**Keywords:** binary serialization, mutex locking, reference counting, secure connections, entity components
**Symbols:** blockEntityUpdate, blockEntityUpdate.id, blockEntityUpdate.serverReceive, blockEntityUpdate.sendClientDataUpdateToServer, blockEntityUpdate.sendServerDataUpdateToClientsInternal, blockEntityUpdate.sendServerDataUpdateToClients, EntityComponentUpdate, EntityComponentUpdate.id, EntityComponentUpdate.ActionType, EntityComponentUpdate.clientReceive, EntityComponentUpdate.unload, EntityComponentUpdate.load
**Concepts:** networking protocol, block entity updates, entity component management

## Summary
Defines network protocols for block entity and entity component updates.

## Explanation
This chunk defines two main network protocols: `blockEntityUpdate` and `EntityComponentUpdate`. The `blockEntityUpdate` protocol handles updates to block entities, including receiving updates from the server and sending client data to the server. It involves reading and writing binary data using `utils.BinaryReader` and `utils.BinaryWriter`, managing chunk references with reference counting, and locking mutexes for thread safety. The `EntityComponentUpdate` protocol manages loading and unloading of entity components, also involving binary data serialization and deserialization, and sending messages over secure connections.

### Detailed Explanation
- **blockEntityUpdate Protocol**
  - **ID**: The ID for block entity updates is `14`.
  - **Server Receive**: The server receives block entity updates by reading a position vector (`Vec3i`) and a block type (`u16`). It then retrieves the simulation chunk, locks the mutex, and updates the block entity data if the block type matches. Finally, it sends the updated data to clients.
  - **Send Client Data Update**: The client sends block entity data updates by writing the position vector, block type, and block entity data to a binary writer and sending it over a secure connection.
  - **Send Server Data Update**: The server sends block entity data updates to clients by writing the block entity data to a binary writer and broadcasting it to all connected users.

- **EntityComponentUpdate Protocol**
  - **ID**: The ID for entity component updates is `15`.
  - **Action Types**: The protocol supports two action types: `unload` (0) and `load` (1).
  - **Client Receive**: The client receives entity component updates by reading the entity ID, component ID, action type, and additional data if the action type is `load`. It then loads or unloads the component accordingly.
  - **Unload**: The client sends an unload message for an entity component by writing the entity ID, component ID, and action type to a binary writer and sending it over a secure connection.
  - **Load**: The client sends a load message for an entity component by writing the entity ID, component ID, version, and component data to a binary writer and sending it over a secure connection.

## Code Example
```zig
const ActionType = enum(u8) {
		unload = 0,
		load = 1,
	}
```

## Related Questions
- What is the ID for block entity updates?
- How does the server handle receiving block entity updates?
- What actions can be performed on entity components via network messages?
- How are binary data packets written and read in these protocols?
- What role do mutexes play in ensuring thread safety?
- How are references to chunks managed during network operations?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_8*
