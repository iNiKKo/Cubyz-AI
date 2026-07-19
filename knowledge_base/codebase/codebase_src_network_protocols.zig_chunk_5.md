# [hard/codebase_src_network_protocols.zig] - Chunk 5

**Type:** networking
**Keywords:** binary serialization, network messages, state synchronization, gamemode change, teleportation, world editing, biome update, particle effects, time synchronization, chat clearing
**Symbols:** genericUpdate, genericUpdate.id, genericUpdate.UpdateType, genericUpdate.WorldEditPosition, genericUpdate.ClearType, genericUpdate.clientReceive, genericUpdate.serverReceive, genericUpdate.sendGamemode, genericUpdate.sendTPCoordinates, genericUpdate.sendWorldEditPos, genericUpdate.sendBiome, genericUpdate.sendParticles, genericUpdate.sendTime, genericUpdate.sendClear
**Concepts:** networking, client-server communication, game state updates

## Summary
Handles generic update messages for client-server communication in the Cubyz voxel engine.

## Explanation
This chunk defines a `genericUpdate` struct that manages various types of network updates between clients and servers. It includes enums for different update types (`gamemode`, `teleport`, `worldEditPos`, `time`, `biome`, `particles`, `clear`), world edit positions (`selectedPos1`, `selectedPos2`, `clear`), and clear types (`chat`). The `clientReceive` function processes incoming messages from the client, updating game state based on the message type (e.g., changing gamemode, teleporting player, editing world). The `serverReceive` function handles server-specific updates like setting world edit positions. Additionally, there are public functions to send different types of updates from either the client or server, such as sending gamemode changes, teleport coordinates, world edit positions, biomes, particles, time, and clear commands. Each send function initializes a binary writer, writes the appropriate data, and sends it over the network connection.

**Enums and Values:**
- `UpdateType` enum includes: `gamemode`, `teleport`, `worldEditPos`, `time`, `biome`, `particles`, `clear`
- `WorldEditPosition` enum includes: `selectedPos1`, `selectedPos2`, `clear`
- `ClearType` enum includes: `chat`

**ClientReceive Function:**
- Handles different update types based on the message type.
  - For `gamemode`: Changes the player's gamemode.
  - For `teleport`: Sets the player's position to a new coordinate.
  - For `worldEditPos`: Updates the selected positions for world editing.
  - For `time`: Adjusts the game time based on the received value.
  - For `biome`: Changes the player's biome and updates music accordingly.
  - For `particles`: Adds particles to the game with specific properties.
  - For `clear`: Clears chat messages if the type is `chat`.

**ServerReceive Function:**
- Handles server-specific updates like setting world edit positions.
- Returns an error for invalid message types (`gamemode`, `teleport`, `time`, `biome`, `particles`, `clear`).

**Send Functions:**
- Each send function initializes a binary writer, writes the appropriate data, and sends it over the network connection.
  - `sendGamemode`: Sends the gamemode change message.
  - `sendTPCoordinates`: Sends the teleport coordinates message.
  - `sendWorldEditPos`: Sends the world edit position message.
  - `sendBiome`: Sends the biome update message.
  - `sendParticles`: Sends the particle effects message.
  - `sendTime`: Sends the time synchronization message.
  - `sendClear`: Sends the clear command message.

**Related Questions:**
- **What is the purpose of the `genericUpdate` struct?**
  The `genericUpdate` struct manages various types of network updates between clients and servers, handling different update types like gamemode changes, teleportation, world editing, biome updates, particle effects, time synchronization, and chat clearing.

- **How does the `clientReceive` function handle different update types?**
  The `clientReceive` function processes incoming messages from the client based on the message type. It updates game state accordingly, such as changing gamemode, teleporting player, editing world, adjusting time, updating biome, adding particles, and clearing chat.

- **What data is sent when a client sends a gamemode change?**
  When a client sends a gamemode change, the `sendGamemode` function initializes a binary writer, writes the message type (`gamemode`) and the new gamemode value, and sends it over the network connection.

- **How are world edit positions handled in server messages?**
  In server messages, world edit positions are handled by the `serverReceive` function. It updates the selected positions for world editing based on the received message type (`selectedPos1`, `selectedPos2`, or `clear`).

- **What is the role of the `sendParticles` function?**
  The `sendParticles` function initializes a binary writer, writes the particle effects message with specific properties like particle ID, position, collision flag, count, and spawn zone string, and sends it over the network connection.

- **How is time synchronization managed between clients and servers?**
  Time synchronization is managed by the `sendTime` function. It initializes a binary writer, writes the message type (`time`) and the current game time value, and sends it over the network connection.

- **What happens if an invalid message type is received by the server?**
  If an invalid message type is received by the server, the `serverReceive` function returns an error for message types like `gamemode`, `teleport`, `time`, `biome`, `particles`, and `clear`.

- **How does the code handle missing biomes when updating them?**
  The code handles missing biomes by checking if the biome index is valid before updating it. If the biome index is invalid, it will not update the biome.

- **What is the difference between secure and lossy channels in sending messages?**
  Secure channels ensure that messages are delivered reliably, while lossy channels allow for faster transmission but may result in message loss. The `sendClear` function currently uses a lossy channel (`conn.send(.lossy, ...)`), which should be changed after issue #1879 is resolved.

- **How are particle effects initialized from a spawn zone string?**
  Particle effects are initialized by the `clientReceive` function when handling the `particles` message type. It reads the spawn zone string and uses it to initialize the particle effects with specific properties like position, collision flag, count, and other relevant data.

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
