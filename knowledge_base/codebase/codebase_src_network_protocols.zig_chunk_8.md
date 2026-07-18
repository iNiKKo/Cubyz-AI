# [hard/codebase_src_network_protocols.zig] - Chunk 8

**Type:** networking
**Keywords:** binary serialization, mutex locking, reference counting, secure connections, entity components
**Symbols:** blockEntityUpdate, blockEntityUpdate.id, blockEntityUpdate.serverReceive, blockEntityUpdate.sendClientDataUpdateToServer, blockEntityUpdate.sendServerDataUpdateToClientsInternal, blockEntityUpdate.sendServerDataUpdateToClients, EntityComponentUpdate, EntityComponentUpdate.id, EntityComponentUpdate.ActionType, EntityComponentUpdate.clientReceive, EntityComponentUpdate.unload, EntityComponentUpdate.load
**Concepts:** networking protocol, block entity updates, entity component management

## Summary
Defines network protocols for block entity and entity component updates.

## Explanation
This chunk defines two main network protocols: `blockEntityUpdate` and `EntityComponentUpdate`. The `blockEntityUpdate` protocol handles updates to block entities, including receiving updates from the server and sending client data to the server. It involves reading and writing binary data using `utils.BinaryReader` and `utils.BinaryWriter`, managing chunk references with reference counting, and locking mutexes for thread safety. The `EntityComponentUpdate` protocol manages loading and unloading of entity components, also involving binary data serialization and deserialization, and sending messages over secure connections.

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
