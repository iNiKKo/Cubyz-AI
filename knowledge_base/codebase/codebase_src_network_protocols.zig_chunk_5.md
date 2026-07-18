# [hard/codebase_src_network_protocols.zig] - Chunk 5

**Type:** networking
**Keywords:** binary serialization, network messages, state synchronization, gamemode change, teleportation, world editing, biome update, particle effects, time synchronization, chat clearing
**Symbols:** genericUpdate, genericUpdate.id, genericUpdate.UpdateType, genericUpdate.WorldEditPosition, genericUpdate.ClearType, genericUpdate.clientReceive, genericUpdate.serverReceive, genericUpdate.sendGamemode, genericUpdate.sendTPCoordinates, genericUpdate.sendWorldEditPos, genericUpdate.sendBiome, genericUpdate.sendParticles, genericUpdate.sendTime, genericUpdate.sendClear
**Concepts:** networking, client-server communication, game state updates

## Summary
Handles generic update messages for client-server communication in the Cubyz voxel engine.

## Explanation
This chunk defines a `genericUpdate` struct that manages various types of network updates between clients and servers. It includes enums for different update types, world edit positions, and clear types. The `clientReceive` function processes incoming messages from the client, updating game state based on the message type (e.g., changing gamemode, teleporting player, editing world). The `serverReceive` function handles server-specific updates like setting world edit positions. Additionally, there are public functions to send different types of updates from either the client or server, such as sending gamemode changes, teleport coordinates, world edit positions, biomes, particles, time, and clear commands. Each send function initializes a binary writer, writes the appropriate data, and sends it over the network connection.

## Code Example
```zig
pub fn sendGamemode(conn: *Connection, gamemode: main.game.Gamemode) void {
	conn.send(.secure, id, &.{@intFromEnum(UpdateType.gamemode), @intFromEnum(gamemode)});
}
```

## Related Questions
- What is the purpose of the `genericUpdate` struct?
- How does the `clientReceive` function handle different update types?
- What data is sent when a client sends a gamemode change?
- How are world edit positions handled in server messages?
- What is the role of the `sendParticles` function?
- How is time synchronization managed between clients and servers?
- What happens if an invalid message type is received by the server?
- How does the code handle missing biomes when updating them?
- What is the difference between secure and lossy channels in sending messages?
- How are particle effects initialized from a spawn zone string?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_5*
