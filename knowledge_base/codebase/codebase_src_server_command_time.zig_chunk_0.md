# [easy/codebase_src_server_command_time.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, user input handling, game time control, error messaging, state updating
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, server management, time manipulation

## Summary
Handles server time-related commands, including getting and setting the game time.

## Explanation
Handles server time-related commands, including getting and setting the game time. The `execute` function processes different forms of input related to time settings using an argument parser (`ArgParser`). It supports four types of inputs: `/time`, `/time <number>`, `/time <phase>`, and `/time <subcommand>`. For each type, it performs specific actions:
- `/time`: Retrieves the current game time and sends a message with this value.
- `/time <number>`: Sets the game time to the specified number.
- `/time <phase>`: Sets the game time to either `dayStart` or `nightStart` based on whether the phase is day or night, respectively. These values are defined in `main.game.World.DayTime.dayStart` and `main.game.World.DayTime.nightStart`.
- `/time <subcommand>`: Toggles time cycling (`start`/`stop`) by setting `doGameTimeCycle` to true or false, sending a message confirming the action. Error handling is implemented to send feedback if the input is invalid.

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
- What specific values are used for day and night phases?
- How does the command handle toggling time cycling?

*Source: unknown | chunk_id: codebase_src_server_command_time.zig_chunk_0*
