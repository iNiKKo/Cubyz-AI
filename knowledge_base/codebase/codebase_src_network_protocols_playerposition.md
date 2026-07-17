# [medium/src/network/protocols.zig] - Chunk playerposition

**Type:** codebase
**Keywords:** playerPosition, network protocol, position sync, velocity, timestamp
**Symbols:** network.protocols.playerPosition, World.update, Player.getPosBlocking, Player.getVelBlocking
**Concepts:** networking, client-server sync, protocol struct

## Summary
The `playerPosition` protocol struct (`src/network/protocols.zig`, protocol id 4) is how Cubyz
sends a client's position, velocity, and a timestamp to the server over the network.

## Explanation
`network.protocols.playerPosition` is a protocol struct with `pub const id: u8 = 4`. It's sent via
`network.protocols.playerPosition.send(self.conn, Player.getPosBlocking(), Player.getVelBlocking(), @intCast(newTime & 65535))`,
called from `World.update()` -- so every world update tries to send the player's current
position, current velocity, and a truncated (16-bit) timestamp to the server. `send()` itself
throttles this: `if (time -% lastPositionSent < 50) { return; }` -- position updates are sent at
most once every 50 ms, not on every single call. The server side receives it via
`serverReceive(conn, reader)`, which calls `conn.user.?.receiveData(reader)`.

## Related Questions
- How does Cubyz store its player position data over the network?
- What protocol struct handles player position syncing in Cubyz?
- What data does the playerPosition network message contain?

*Source: raw_cubyz_dataset/codebase/src/network/protocols.zig | chunk_id: codebase_src_network_protocols_playerposition*
