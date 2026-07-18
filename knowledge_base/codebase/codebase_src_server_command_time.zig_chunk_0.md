# [easy/codebase_src_server_command_time.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, user input handling, game time control, error messaging, state updating
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, server management, time manipulation

## Summary
Handles server time-related commands, including getting and setting the game time.

## Explanation
The chunk defines a command handler for server time management. It uses an argument parser to interpret different forms of input related to time settings. The `execute` function processes these inputs, updating the game time or toggling time cycling based on the user's command. Error handling is implemented to send feedback if the input is invalid.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	const result = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	const gameTime: i64 = switch (result) {
		.@"/time" => time: {
			source.sendMessage("#ffff00{}", .{main.server.world.?.gameTime});
			break :time main.server.world.?.gameTime;
		},
		.@"/time <number>" => |params| params.number,
		.@"/time <phase>" => |params| switch (params.phase) {
			.day => main.game.World.DayTime.dayStart,
			.night => main.game.World.DayTime.nightStart,
		},
		.@"/time <subcommand>" => |params| {
			switch (params.subcommand) {
				.start => {
					main.server.world.?.doGameTimeCycle = true;
					source.sendMessage("#ffff00Time started.", .{});
					return;
				},
				.stop => {
					main.server.world.?.doGameTimeCycle = false;
					source.sendMessage("#ffff00Time stopped.", .{});
					return;
				},
			}
		},
	};
	main.server.world.?.gameTime = gameTime;
}
```

## Related Questions
- What is the description of the server time command?
- How does the chunk handle invalid user input?
- What are the possible subcommands for setting the game time?
- Which function processes the user's time-related commands?
- How is the game time updated based on user input?
- What message is sent to the user if an error occurs in parsing arguments?

*Source: unknown | chunk_id: codebase_src_server_command_time.zig_chunk_0*
