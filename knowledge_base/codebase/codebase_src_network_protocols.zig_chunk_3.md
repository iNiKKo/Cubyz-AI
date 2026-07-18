# [hard/codebase_src_network_protocols.zig] - Chunk 3

**Type:** networking
**Keywords:** networking, serialization, deserialization, binary data, position updates, velocity handling
**Symbols:** playerPosition, playerPosition.id, playerPosition.serverReceive, playerPosition.lastPositionSent, playerPosition.send, entityPosition, entityPosition.id, entityPosition.type_entity, entityPosition.type_item, entityPosition.Type, entityPosition.clientReceive, entityPosition.send, blockUpdate, blockUpdate.id, blockUpdate.clientReceive, blockUpdate.send
**Concepts:** networking protocol, player position updates, entity positions, block updates

## Summary
This chunk defines network protocols for player position updates, entity positions, and block updates.

## Explanation
The chunk contains three main structs: `playerPosition`, `entityPosition`, and `blockUpdate`. Each struct represents a different type of network protocol. The `playerPosition` struct handles sending and receiving player position data, ensuring that updates are sent no more than once every 50 milliseconds. The `entityPosition` struct manages the serialization and deserialization of entity and item positions, including their velocities and types. The `blockUpdate` struct is responsible for updating block states in the game world, both on the client side and server side.

## Code Example
```zig
pub fn send(conn: *Connection, playerPos: Vec3d, playerVel: Vec3d, time: u16) void {
	if (time -% lastPositionSent < 50) {
		return; // Only send at most once every 50 ms.
	}
	lastPositionSent = time;
	var writer = utils.BinaryWriter.initCapacity(main.stackAllocator, 62);
	defer writer.deinit();
	writer.writeInt(u64, @bitCast(playerPos[0]));
	writer.writeInt(u64, @bitCast(playerPos[1]));
	writer.writeInt(u64, @bitCast(playerPos[2]));
	writer.writeInt(u64, @bitCast(playerVel[0]));
	writer.writeInt(u64, @bitCast(playerVel[1]));
	writer.writeInt(u64, @bitCast(playerVel[2]));
	writer.writeInt(u32, @bitCast(game.camera.rotation[0]));
	writer.writeInt(u32, @bitCast(game.camera.rotation[1]));
	writer.writeInt(u32, @bitCast(game.camera.rotation[2]));
	writer.writeInt(u16, time);
	conn.send(.lossy, id, writer.data.items);
}
```

## Related Questions
- What is the purpose of the `playerPosition` struct?
- How often does the player position data get sent according to the code?
- What types of entities and items are handled by the `entityPosition` struct?
- How is block update data serialized in the `blockUpdate` struct?
- What happens if the velocity magnitude of an entity is less than 1e-6*1e-6 in the `entityPosition` struct?
- How does the `clientReceive` function in the `entityPosition` struct handle different types of entities and items?
- What is the role of the `blockEntityData` field in the block update process?
- How is the connection type specified when sending data in these network protocols?
- What is the maximum capacity initialized for the binary writer in the `playerPosition` struct?
- How does the `clientReceive` function in the `blockUpdate` struct handle incoming block updates?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_3*
