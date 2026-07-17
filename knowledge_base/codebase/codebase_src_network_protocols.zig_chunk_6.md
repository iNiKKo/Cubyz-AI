# [hard/codebase_src_network_protocols.zig] - Chunk 6

**Type:** networking
**Keywords:** binary serialization, networking, error handling, UTF-8 validation, message routing, world state updates
**Symbols:** chat, chat.id, chat.clientReceive, chat.serverReceive, chat.send, lightMapRequest, lightMapRequest.id, lightMapRequest.serverReceive, lightMapRequest.sendRequest, lightMapTransmission, lightMapTransmission.id, lightMapTransmission.LightMapTask
**Concepts:** networking protocol, world editing, gamemodes, teleportation, biomes, particles, time synchronization, chat messages, light map requests, light map transmissions

## Summary
This chunk defines several network protocols for sending and receiving various types of updates, including world edits, gamemodes, teleport coordinates, biome information, particles, time updates, chat messages, light map requests, and light map transmissions.

## Explanation
The chunk contains multiple struct definitions, each representing a different type of network protocol. Each protocol has methods for receiving data from the client or server (`clientReceive` or `serverReceive`) and sending data to the client or server (`send`, `sendGamemode`, `sendTPCoordinates`, etc.). The protocols handle various game mechanics such as world editing, gamemodes, teleportation, biomes, particles, time synchronization, chat messages, light map requests, and light map transmissions. Each protocol uses a unique identifier (`id`) for routing messages over the network. The chunk also defines utility functions for writing binary data using `utils.BinaryWriter` and reading binary data using `utils.BinaryReader`. Error handling is implemented to validate UTF-8 characters in chat messages and ensure that message lengths do not exceed specified limits.

## Code Example
```zig
pub fn sendGamemode(conn: *Connection, gamemode: main.game.Gamemode) void {
	conn.send(.secure, id, &.{@intFromEnum(UpdateType.gamemode), @intFromEnum(gamemode)});
}
```

## Related Questions
- What is the purpose of the `sendGamemode` function?
- How does the chunk handle chat messages with invalid UTF-8 characters?
- What is the role of the `lightMapRequest` protocol in the network communication?
- How are binary data packets written and read in this chunk?
- What types of world state updates can be sent over the network using this chunk?
- How does the chunk ensure that chat messages do not exceed a certain length?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_6*
