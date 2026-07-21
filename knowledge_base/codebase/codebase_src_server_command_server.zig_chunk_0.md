# [easy/codebase_src_server_command_server.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, server stop, headless server, user messaging, error handling
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command handling, server management

## Summary
Handles the '/server' command for stopping or restarting the server.

## Explanation
This chunk defines a command handler for the '/server' command, which can stop or restart the server. The `description` field specifies that the command is used to 'Stop the server.' The `usage` field provides the syntax \/server <stop/restart>. The `Args` union enum defines the possible actions as `main.server.StopType`, with specific options like `.restart` and `.stop`. The `execute` function takes arguments of type `Args` and a pointer to a `User`. It checks if a headful restart is supported based on the server's configuration (`main.settings.launchConfig.headlessServer`). If the command is valid, it stops the server with the specified action. If an error occurs during argument parsing, it sends an error message to the user.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	const result = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};
	if (result.@"/server <action>".action == .restart and !main.settings.launchConfig.headlessServer) {
		source.sendMessage("#ff0000Headfull restart isn't supported yet.", .{});
		return;
	}

	main.server.stop(result.@"/server <action>".action);
}
```

## Related Questions
- What is the description of the '/server' command?
- How does the chunk parse arguments for the '/server' command?
- What actions can be performed with the '/server' command?
- How does the chunk handle errors in argument parsing?
- What condition prevents a headful restart from being executed?
- What function is called to stop the server?

*Source: unknown | chunk_id: codebase_src_server_command_server.zig_chunk_0*
