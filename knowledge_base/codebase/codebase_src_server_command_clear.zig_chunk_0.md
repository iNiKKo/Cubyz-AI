# [easy/codebase_src_server_command_clear.zig] - Chunk 0

**Type:** api
**Keywords:** server command, argument parser, error handling, inventory clear, chat clear
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command handling, argument parsing, inventory management, chat management

## Summary
Handles the '/clear' command to clear player inventory or chat.

## Explanation
This chunk defines a server-side command handler for the '/clear' command. It uses an argument parser to determine whether to clear the player's inventory or chat based on the provided target. The `execute` function parses the arguments, handles errors by sending error messages, and then performs the appropriate action using functions from other modules.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	const result = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	switch (result.@"/clear <target>".target) {
		.inventory => main.items.Inventory.server.clearPlayerInventory(source),
		.chat => main.network.protocols.genericUpdate.sendClear(source.conn, .chat),
	}
}
```

## Related Questions
- What is the description of the '/clear' command?
- How does the '/clear' command handle errors?
- Which modules are used to clear the player's inventory and chat?
- What is the structure of the Args union enum?
- How is the ArgParser initialized in this chunk?
- What is the purpose of the errorMessage variable in the execute function?

*Source: unknown | chunk_id: codebase_src_server_command_clear.zig_chunk_0*
