# [hard/codebase_src_network_protocols.zig] - Chunk 9

**Type:** networking
**Keywords:** binary serialization, network communication, entity components, secure connection, action handling
**Symbols:** clientReceive, unload, load
**Concepts:** networking, entity ECS

## Summary
Handles network communication for loading and unloading entity components.

## Explanation
This chunk defines functions to handle the reception of component load and unload actions from a client. The `clientReceive` function reads data from a binary reader, determines the action type (load or unload), and processes it accordingly by either loading or unloading the specified component for the given entity. The `unload` and `load` functions prepare binary data to send component unload and load requests over a secure connection, respectively.

## Code Example
```zig
fn clientReceive(_: *Connection, reader: *utils.BinaryReader) !void {
	const entityId: main.entity.Entity = @enumFromInt(try reader.readVarInt(u32));
	const componentId = try reader.readVarInt(u32);
	const actionType: ActionType = try reader.readEnum(ActionType);

	if (actionType == .load) {
		const componentVersion = try reader.readVarInt(u32);
		try main.entity.loadComponent(.client, componentId, entityId, reader.remaining, componentVersion);
	} else if (actionType == .unload) {
		try main.entity.unloadComponent(.client, componentId, entityId);
	}
}
```

## Related Questions
- What does the `clientReceive` function do?
- How is data sent over a secure connection in this chunk?
- What are the possible action types handled by this code?
- Where is the binary writer initialized and deinitialized?
- What specific actions are taken when an unload request is received?
- How does the `load` function differ from the `unload` function?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_9*
