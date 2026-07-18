# [easy/codebase_src_server_command_help.zig] - Chunk 0

**Type:** api
**Keywords:** command execution, error handling, string manipulation, user feedback, argument parsing
**Symbols:** description, usage, Args, ArgParser, execute, Cmd
**Concepts:** server command processing, argument parsing, command help system

## Summary
Handles the /help server command to display information about available commands.

## Explanation
This chunk defines the logic for processing the '/help' command in a server context. It uses an argument parser to handle different forms of the command, such as listing all commands or providing usage details for a specific command. The `execute` function parses the input arguments and constructs a response message accordingly. If there's an error during parsing, it sends an error message back to the user. The `Cmd` struct is responsible for parsing individual command names and handling errors if the command is not recognized.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	const result = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	var msg: main.ListManaged(u8) = .init(main.stackAllocator);
	defer msg.deinit();
	msg.appendSlice("#ffff00");
	switch (result) {
		.@"/help" => {
			var iterator = command.commands.valueIterator();
			while (iterator.next()) |cmd| {
				msg.append('/');
				msg.appendSlice(cmd.name);
				msg.appendSlice(": ");
				msg.appendSlice(cmd.description);
				msg.append('\n');
			}
			msg.appendSlice("\nUse /help <command> for usage of a specific command.\n");
		},
		.@"/help <command>" => |params| {
			const cmd = params.command.cmd;
			msg.append('/');
			msg.appendSlice(cmd.name);
			msg.appendSlice(": ");
			msg.appendSlice(cmd.description);
			msg.append('\n');
			msg.appendSlice(cmd.usage);
			msg.append('\n');
		},
		.@"/help <bobik>" => {
			msg.appendSlice("Even Bobik can't help you anymore ");
		},
	}
	if (msg.items[msg.items.len - 1] == '\n') _ = msg.pop();
	source.sendMessage("{s}", .{msg.items});
}
```

## Related Questions
- What is the purpose of the 'description' constant in this chunk?
- How does the 'execute' function handle different forms of the '/help' command?
- What error handling is implemented for unrecognized commands?
- What is the role of the 'Cmd' struct in this code?
- How are messages constructed and sent back to the user?
- What is the structure of the 'Args' union(enum)?
- How does the argument parser work in this chunk?
- What is the function of the 'NeverFailingAllocator'?
- How are command descriptions retrieved and displayed?
- What happens if there's an error during argument parsing?

*Source: unknown | chunk_id: codebase_src_server_command_help.zig_chunk_0*
