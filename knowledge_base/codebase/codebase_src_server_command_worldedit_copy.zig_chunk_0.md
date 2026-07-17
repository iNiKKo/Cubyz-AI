# [easy/codebase_src_server_command_worldedit_copy.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, selection retrieval, blueprint capturing, error handling, clipboard management
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, user selection, clipboard functionality, blueprint capture

## Summary
Handles the '/copy' command for copying a selection to the clipboard.

## Explanation
This chunk defines the logic for executing the '/copy' command in the server. It uses an argument parser to validate the command, retrieves the current user's selection, captures the blueprint of the selected area, and stores it in the user's world edit data. If there is already a clipboard entry, it deinitializes the old one before storing the new one. Error handling is implemented for both parsing errors and capture failures, with appropriate messages sent to the user and logged.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	_ = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	const selection = command.getCurrentSelection(source) catch return;
	source.sendMessage("Copying: {f}", .{selection});

	const result = Blueprint.capture(main.globalAllocator, selection);
	switch (result) {
		.success => {
			if (source.worldEditData.clipboard != null) {
				source.worldEditData.clipboard.?.deinit(main.globalAllocator);
			}
			source.worldEditData.clipboard = result.success;

			source.sendMessage("Copied selection to clipboard.", .{});
		},
		.failure => |e| {
			source.sendMessage("#ff0000Error while copying block {}: {s}", .{e.pos, e.message});
			std.log.warn("Error while copying block {}: {s}", .{e.pos, e.message});
		},
	}
}
```

## Related Questions
- What is the description of the '/copy' command?
- How does the chunk handle argument parsing for the '/copy' command?
- What happens if there is an error during argument parsing?
- How does the chunk retrieve the current user's selection?
- What is the process for capturing a blueprint in this chunk?
- How does the chunk manage the clipboard data for the user?
- What kind of errors are handled in this chunk and how are they reported?
- Where is the error message logged if there is an issue during the copy operation?
- What is the structure of the Args union used in this chunk?
- How does the chunk ensure proper memory management with the errorMessage variable?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_copy.zig_chunk_0*
