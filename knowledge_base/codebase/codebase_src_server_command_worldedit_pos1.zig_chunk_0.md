# [easy/codebase_src_server_command_worldedit_pos1.zig] - Chunk 0

**Type:** api
**Keywords:** command parsing, position selection, network update, world edit data, flooring coordinates
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** world editing, command handling, player position selection

## Summary
Handles the '/pos1' command to select player position as position 1 for world editing.

## Explanation
This chunk defines a command handler for the '/pos1' command, which selects the player's current position as the first selection point for world editing. The `Args` union enum specifies that the `/pos1` command does not take any arguments. When the command is executed, it retrieves the player's position using `source.player().pos`, floors it to integer coordinates using `@floor`, and stores it in the user's world edit data (`selectionPosition1`). It then sends the updated position over the network to clients using `main.network.protocols.genericUpdate.sendWorldEditPos`. If the argument parsing fails, an error message is sent to the user.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	_ = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	const pos: Vec3i = @floor(source.player().pos);

	source.worldEditData.selectionPosition1 = pos;
	main.network.protocols.genericUpdate.sendWorldEditPos(source.conn, .selectedPos1, pos);

	source.sendMessage("Position 1: {}", .{pos});
}
```

## Related Questions
- What is the description of the '/pos1' command?
- How does the chunk parse arguments for the '/pos1' command?
- What happens if the argument parsing fails in the '/pos1' command?
- Where is the player's position stored after executing the '/pos1' command?
- How is the updated position sent over the network?
- What message is sent to the user after successfully setting position 1?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_pos1.zig_chunk_0*
