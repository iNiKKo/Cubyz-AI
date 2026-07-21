# [easy/codebase_src_server_command_entity_avatar.zig] - Chunk 0

**Type:** implementation
**Keywords:** command parser, avatar update, entity model change, user interface logic, server command execution
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, user interaction, entity management

## Summary
Handles avatar lookup or change commands

## Explanation
This chunk defines the logic for handling avatar-related commands in the Cubyz server. It includes parsing arguments, executing commands based on user input, and updating the user's entity model.

The `description` constant provides a brief description of the command: 'Lookup or change your avatar'. The `usage` string specifies the syntax for the command:
```
/avatar
/avatar <entityModel>
```
The `Args` union defines two possible argument structures for the command. The first variant, `@"/avatar"`, does not require any arguments. The second variant, `@"/avatar <entityModel>"`, requires an `entityModel` parameter of type `command.EntityModel`.

The `execute` function handles the execution of the avatar-related commands based on the parsed arguments. It uses a switch statement to determine which command was issued and performs the corresponding action. If the `/avatar <entityModel>` command is issued, it updates the user's entity model using the `model.server.put` function and sends a message to the user confirming the change. If the `/avatar` command is issued without any arguments, it checks if the user has an entity model assigned using the `model.server.get` function. If an entity model is found, it sends a message indicating that the user is visible with their entity model ID. If no entity model is found, it sends a message indicating that the user is invisible.

The code example provided in the kb_content is incorrect and does not match the actual implementation. The correct `execute` function should be:
```zig
pub fn execute(args: Args, source: *User) void {
    switch (args) {
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

The `ArgParser.parse` function is not used in the actual implementation. Instead, the `execute` function directly processes the `Args` union based on the parsed arguments.

The `model.server.put` and `model.server.get` functions are used to store and retrieve user entity models from the server's model storage system.

Messages sent to users from the server in response to commands are formatted using the `source.sendMessage` function. The messages include color codes (e.g., `#00ff00` for green, `#ff00ff` for pink) and placeholders for dynamic content (e.g., `{s}` for strings).

The logic behind determining if a user is visible or invisible based on their entity model is implemented in the `/avatar` command handler. If an entity model is found using `model.server.get`, the user is considered visible, and a message with the entity model ID is sent to the user. If no entity model is found, the user is considered invisible, and a corresponding message is sent.

The `errorMessage` variable is used to store error messages that may occur during command parsing. The `defer errorMessage.deinit(main.stackAllocator)` statement ensures that the error message list is properly deallocated after use.

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
