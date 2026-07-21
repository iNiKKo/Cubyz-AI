# [easy/codebase_src_server_command_seed.zig] - Chunk 0

**Type:** api
**Keywords:** command handler, argument validation, error handling, world configuration, user communication
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** server command handling, argument parsing, world seed retrieval

## Summary
Handles the '/seed' server command to retrieve and display the world seed.

## Explanation
This chunk defines a server command handler for the '/seed' command. The `description` constant provides a brief description of the command, and the `usage` constant specifies the exact syntax for using the command. The `Args` union defines the possible arguments for the command, in this case, just the `/seed` argument. The `execute` function retrieves the world seed from the server's configuration and sends it back to the user with a specific color code (`#ffff00`). There is no error handling or argument parsing involved in this chunk.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	_ = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	source.sendMessage("#ffff00{}", .{main.server.world.?.settings.seed});
}
```

## Related Questions
- What is the description of the '/seed' command?
- How does the chunk handle argument parsing for the '/seed' command?
- What happens if there is an error in parsing the arguments?
- Where does the chunk retrieve the world seed from?
- How does the chunk send a message to the user?
- What is the purpose of the 'errorMessage' variable?

*Source: unknown | chunk_id: codebase_src_server_command_seed.zig_chunk_0*
