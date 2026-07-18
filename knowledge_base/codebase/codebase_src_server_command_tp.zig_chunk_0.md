# [easy/codebase_src_server_command_tp.zig] - Chunk 0

**Type:** api
**Keywords:** teleportation, command execution, argument parsing, spiral search, network protocol
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, teleportation mechanics, argument parsing, spiral search algorithm, network communication

## Summary
The chunk implements the teleportation command logic for the server.

## Explanation
This chunk defines the teleportation command (`/tp`) for the Cubyz server. It supports three types of arguments: teleporting to a biome, teleporting to specific coordinates, and teleporting to another player's position. The `Args` union enum categorizes these argument types. The `ArgParser` is used to parse the input arguments. The `execute` function handles the command execution based on the parsed arguments. For biomes, it searches for a suitable location within a specified radius using a spiral search algorithm. For coordinates and player indices, it resolves the target position and sends teleportation coordinates to the client via the network protocol.

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
