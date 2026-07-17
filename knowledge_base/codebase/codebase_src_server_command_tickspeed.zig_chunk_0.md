# [easy/codebase_src_server_command_tickspeed.zig] - Chunk 0

**Type:** implementation
**Keywords:** tickspeed, command, tickrate, atomic, threadsafe
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** server command, random tickrate, atomic operations

## Summary
Server command to get or set the random tickrate.

## Explanation
This chunk defines a server command `/tickspeed` that allows users to retrieve or modify the server's random tick rate, measured in blocks per chunk per tick. The command can be used with or without an argument. If no argument is provided, it resets the tick rate to its default value. The tick rate is stored and retrieved using atomic operations for thread safety.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
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
- What is the purpose of the `description` variable in this chunk?
- How does the `ArgParser.parse` function work in this chunk?
- What is the default value for the tick rate if no argument is provided?
- What is the data structure used to store and retrieve the tick rate?
- What are the atomic operations performed on the tick rate?
- What happens if an error occurs during parsing of the command arguments?
- How is the user informed about any errors that occur during execution?
- What is the purpose of the `errorMessage` variable in this chunk?
- What is the data structure used to store error messages?

*Source: unknown | chunk_id: codebase_src_server_command_tickspeed.zig_chunk_0*
