# [easy/codebase_src_server_command_entity_avatar.zig] - Chunk 0

**Type:** implementation
**Keywords:** command parser, avatar update, entity model change, user interface logic, server command execution
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, user interaction, entity management

## Summary
Handles avatar lookup or change commands

## Explanation
This chunk defines the logic for handling avatar-related commands in the Cubyz server. It includes parsing arguments, executing commands based on user input, and updating the user's entity model.

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
		.@"/avatar <entityModel>" => |params| {
			model.server.put(source.id, .{
				.entityModel = params.entityModel.index,
			});
			source.sendMessage("#00ff00Your entity model was changed to {s}.", .{params.entityModel.index.get().entityModelId});
		},
		.@"/avatar" => {
			if (model.server.get(source.id)) |rc| {
				source.sendMessage("#00ff00You are a {s}", .{rc.entityModel.get().entityModelId});
			} else source.sendMessage("#ff00ffYou are invisible.", .{});
		},
	}
}
```

## Related Questions
- What is the purpose of the `execute` function in this chunk?
- How does the `ArgParser.parse` function work in relation to command processing?
- What data structures are used for storing and retrieving user entity models?
- What error handling mechanism is implemented when parsing command arguments?
- How are messages sent to users from the server in response to commands?
- What is the logic behind determining if a user is visible or invisible based on their entity model?
- What is the role of `model.server.put` and `model.server.get` functions in this chunk?
- Can you explain how the command parser handles different types of avatar-related commands?
- How are messages formatted for sending to users from the server?
- What is the significance of the `errorMessage` variable in this chunk?
- What is the purpose of the `defer errorMessage.deinit(main.stackAllocator)` statement?
- Can you describe how the switch statement handles different command types and their respective actions?

*Source: unknown | chunk_id: codebase_src_server_command_entity_avatar.zig_chunk_0*
