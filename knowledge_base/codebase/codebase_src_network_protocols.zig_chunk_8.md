# [hard/codebase_src_network_protocols.zig] - Chunk 8

**Type:** networking
**Keywords:** BinaryReader, BinaryWriter, mutex locking, thread safety, network messages, component loading, component unloading
**Symbols:** inventory, inventory.id, inventory.clientReceive, inventory.serverReceive, inventory.sendCommand, inventory.sendConfirmation, inventory.sendFailure, inventory.sendSyncOperation, blockEntityUpdate, blockEntityUpdate.id, blockEntityUpdate.serverReceive, blockEntityUpdate.sendClientDataUpdateToServer, blockEntityUpdate.sendServerDataUpdateToClientsInternal, blockEntityUpdate.sendServerDataUpdateToClients, EntityComponentUpdate, EntityComponentUpdate.id, EntityComponentUpdate.ActionType, EntityComponentUpdate.clientReceive, EntityComponentUpdate.unload, EntityComponentUpdate.load
**Concepts:** networking, inventory management, block entity updates, entity component updates

## Summary
Defines network protocols for inventory management, block entity updates, and entity component updates.

## Explanation
This chunk defines three main network protocols: inventory, blockEntityUpdate, and EntityComponentUpdate. Each protocol has a unique ID and handles specific types of network messages between the client and server.

The inventory protocol manages commands, confirmations, failures, and synchronization operations. It uses a BinaryReader to parse incoming data and a BinaryWriter to construct outgoing messages. The server validates received commands and processes them accordingly.

The blockEntityUpdate protocol handles updates to block entities in the world. It reads position and type information from the network message, retrieves the corresponding simulation chunk, locks the mutex for thread safety, and updates the block entity's data. It also sends updated data to connected clients.

The EntityComponentUpdate protocol manages loading and unloading of entity components. It uses a BinaryReader to parse action types (load or unload) and handles each case by either loading component data from the network message or unloading it on the client side.

## Code Example
```zig
pub fn sendFailure(conn: *Connection) void {
	std.debug.assert(conn.isServerSide());
	conn.send(.secure, id, &.{0xfe});
}
```

## Related Questions
- What is the ID for the inventory protocol?
- How does the server handle a failure message in the inventory protocol?
- What actions are defined in the EntityComponentUpdate protocol?
- How does the blockEntityUpdate protocol send data to clients?
- What is the purpose of the ActionType enum in the EntityComponentUpdate protocol?
- How does the inventory protocol handle synchronization operations?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_8*
