# [easy/codebase_src_server_command_gamemode.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, user interaction, gamemode setting, error handling, server command
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command handling, player management, gamemode control

## Summary
Handles the /gamemode command for setting or getting a player's gamemode.

## Explanation
The chunk defines the logic for the /gamemode server command, which allows users to set or retrieve the gamemode of a specified player. The command can be used with different syntaxes: `/gamemode <survival/creative>`, `/gamemode @playerIndex <survival/creative>`, `/gamemode`, and `/gamemode @playerIndex`. The `Args` union enum defines the possible argument structures for the command, where `@"/gamemode <playerIndex> <mode>"` contains a player index and a mode. The `execute` function handles the execution of the command based on the parsed arguments. If setting, it updates the player's gamemode; if getting, it sends the current gamemode back to the user. If there is an error during argument parsing, an error message is sent back to the user.

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
		.@"/gamemode <playerIndex> <mode>" => |params| {
			const target = command.Target.fromPlayerIndex(params.playerIndex, source) catch return;
			defer target.deinit();

			if (params.mode) |mode| {
				main.sync.setGamemode(target.user, mode);
			} else {
				source.sendMessage("#ffff00{s}", .{@tagName(target.user.gamemode.load(.monotonic))});
			}
		},
	}
}
```

## Related Questions
- What is the description of the /gamemode command?
- How does the chunk handle parsing arguments for the /gamemode command?
- What are the possible usages of the /gamemode command?
- How does the chunk determine whether to set or get a player's gamemode?
- What happens if there is an error during argument parsing?
- How does the chunk update a player's gamemode?
- What message is sent back to the user when retrieving their current gamemode?
- What type of allocator is used for error messages in this chunk?

*Source: unknown | chunk_id: codebase_src_server_command_gamemode.zig_chunk_0*
