# [easy/codebase_src_server_command_tp.zig] - Chunk 0

**Type:** api
**Keywords:** teleportation, command execution, argument parsing, spiral search, network protocol
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, teleportation mechanics, argument parsing, spiral search algorithm, network communication

## Summary
The chunk implements the teleportation command logic for the server.

## Explanation
This chunk defines the teleportation command (`/tp`) for the Cubyz server. It supports three types of arguments: teleporting to a biome, teleporting to specific coordinates, and teleporting to another player's position. The `Args` union enum categorizes these argument types as follows:

- `/tp <biome>`: Teleports the user to a specified biome within a radius of 16384 blocks using a spiral search algorithm. If the biome is a cave, teleportation to the biome is not available.
- `/tp <x> <y> <z>`: Teleports the user to specific coordinates provided in the command. The coordinates are resolved using `command.resolveCoordinates`.
- `/tp @<playerIndex>`: Teleports the user to another player's position based on their index. The target player is identified using `command.Target.fromPlayerIndex`, and if successful, the user's position is retrieved and used for teleportation.

The `ArgParser` is used to parse the input arguments. The `execute` function handles the command execution based on the parsed arguments. For biomes, it searches for a suitable location within a specified radius using a spiral search algorithm that explores chunks in a spiral pattern from the center. If the biome is a cave, teleportation to the biome is not available. The algorithm iterates through chunks and samples within each chunk until a suitable biome is found or the entire area has been searched.

For coordinates and player indices, it resolves the target position and sends teleportation coordinates to the client via the network protocol using `main.network.protocols.genericUpdate.sendTPCoordinates`.

## Code Example
```zig
const Args = union(enum) {
	@"/tp <biome>": struct { biome: command.BiomeId },
	@"/tp <x> <y> <z>": struct {
		x: command.Coordinate,
		y: command.Coordinate,
		z: command.Coordinate,
	},
	@"/tp <playerIndex>": struct { playerIndex: command.PlayerIndex },
}
```

## Related Questions
- What is the description of the teleportation command?
- How many types of arguments does the teleportation command support?
- What is the purpose of the `Args` union enum?
- Which function handles the execution of the teleportation command?
- How does the chunk search for a suitable location in a biome?
- What network protocol is used to send teleportation coordinates?
- How are specific coordinates resolved during teleportation?

*Source: unknown | chunk_id: codebase_src_server_command_tp.zig_chunk_0*
