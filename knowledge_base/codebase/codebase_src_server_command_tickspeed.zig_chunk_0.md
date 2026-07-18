# [easy/codebase_src_server_command_tickspeed.zig] - Chunk 0

**Type:** implementation
**Keywords:** command, argument parser, tick speed, world state, error handling
**Symbols:** description, usage, Args, ArgParser, execute, errorMessage, User, main.server.world, main.server.world.tickSpeed
**Concepts:** command handling, argument parsing, world state modification

## Summary
Handles server tick speed commands

## Explanation
The chunk defines a command to get or set the server's random tickrate, measured in blocks per chunk per tick. It uses an argument parser to handle different command formats and updates the world's tick speed accordingly.

## Code Example
```zig
fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	const result = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	switch (result) {
		.@"/tickspeed <rate>" => |tickSpeed| main.server.world.?.tickSpeed.store(tickSpeed.rate, .monotonic),
		.@"/tickspeed" => {},
	}
	source.sendMessage("#ffff00{}", .{main.server.world.?.tickSpeed.load(.monotonic)});
}
```

## Related Questions
- What is the purpose of the `execute` function?
- How does the command parser handle different arguments?
- What happens if an error occurs during parsing?
- What is the default behavior when no rate is provided?
- How is the world's tick speed updated?
- What message is sent to the user upon successful execution or error?

*Source: unknown | chunk_id: codebase_src_server_command_tickspeed.zig_chunk_0*
