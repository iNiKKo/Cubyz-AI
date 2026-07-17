# [easy/codebase_src_server_command_spawn.zig] - Chunk 0

**Type:** implementation
**Keywords:** command, parsing, player, world, spawn point
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command handling, argument parsing, player management, world management

## Summary
Handles the '/spawn' command to get or set a player's or the world's spawn point.

## Explanation
The function `execute` parses the command arguments using an argument parser and processes them based on the provided parameters. It handles different cases such as setting a player's spawn point, getting a player's spawn point, setting the world's spawn point, and getting the world's spawn point.

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
		.@"/spawn <playerIndex> <x> <y> <z>" => |params| {
			const target = command.Target.fromPlayerIndex(params.playerIndex, source) catch return;
			defer target.deinit();
			target.user.spawnPos = command.resolveCoordinates(params.x, params.y, params.z, source);
		},
		.@"/spawn <playerIndex>" => |params| {
			const target = command.Target.fromPlayerIndex(params.playerIndex, source) catch return;
			defer target.deinit();
			source.sendMessage("#ffff00{}", .{target.user.getSpawnPos()});
		},
		.@"/spawn <world> <x> <y> <z>" => |params| {
			const pos = command.resolveCoordinates(params.x, params.y, params.z, source);
			const world = main.server.world.?;
			world.spawn = @trunc(pos);
		},
		.@"/spawn <world>" => {
			const world = main.server.world.?;
			source.sendMessage("#ffff00World spawn: {}", .{world.spawn});
		},
	}
}
```

## Related Questions
- What does the '/spawn' command handle?
- How is argument parsing performed in this function?
- What happens if an error occurs during argument parsing?
- How are player and world spawn points updated based on the command arguments?
- What data structures are used to store spawn points?
- How is memory management handled for dynamically allocated resources?

*Source: unknown | chunk_id: codebase_src_server_command_spawn.zig_chunk_0*
