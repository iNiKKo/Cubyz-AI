# [easy/codebase_src_server_command_worldedit_pos1.zig] - Chunk 0

**Type:** implementation
**Keywords:** command parsing, position setting, world edit update, network packet sending, error handling
**Symbols:** description, usage, Args, ArgParser, execute, errorMessage, source, Vec3i, main.stackAllocator, source.player().pos, source.worldEditData.selectionPosition1, main.network.protocols.genericUpdate.sendWorldEditPos, source.conn, .selectedPos1, pos
**Concepts:** command handling, world edit data management, network communication

## Summary
Handles the /pos1 command to set the player's position as position 1.

## Explanation
The chunk defines a function `execute` that handles the '/pos1' command. It parses the arguments, retrieves the player's position, updates the world edit data with the selected position, and sends an update packet to the client. The function also sends a confirmation message to the user.

## Code Example
```zig
fn execute(args: []const u8, source: *User) void {
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
- What is the purpose of the 'execute' function in this chunk?
- How does the function handle command parsing errors?
- What data structure is used to store the selected position?
- Which network protocol is used to send updates to clients?
- What message format is used for error messages?
- How is the player's current position retrieved and floored?
- What is the purpose of the 'worldEditData' struct in this chunk?
- What function sends an update packet to the client?
- What is the format of the 'selectedPos1' message?
- What is the purpose of the 'Vec3i' type in this chunk?
- How does the function send a confirmation message to the user?
- What are the keywords used in the code snippet for error handling?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_pos1.zig_chunk_0*
