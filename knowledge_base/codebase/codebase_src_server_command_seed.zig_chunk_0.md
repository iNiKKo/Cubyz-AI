# [easy/codebase_src_server_command_seed.zig] - Chunk 0

**Type:** api
**Keywords:** server command, argument validation, world settings, user messaging, error handling
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command handling, argument parsing, world seed retrieval, user communication

## Summary
Handles the '/seed' command to retrieve and display the world seed.

## Explanation
This chunk defines a server command handler for the '/seed' command. It uses an argument parser to validate the command input, retrieves the world seed from the server settings, and sends it back to the user. If there's an error in parsing the arguments, it sends an error message instead.

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
- What happens if there's an error in parsing the arguments?
- Where does the chunk retrieve the world seed from?
- How does the chunk communicate the world seed back to the user?
- What is the purpose of the 'errorMessage' variable in the execute function?

*Source: unknown | chunk_id: codebase_src_server_command_seed.zig_chunk_0*
