# [easy/codebase_src_server_command_worldedit_redo.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, history management, blueprint capture, state reapplication, user feedback
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** world editing, command handling, redo/undo functionality

## Summary
Handles the execution of the '/redo' command for world editing, allowing users to reapply their last undone change.

## Explanation
The chunk defines a command handler for the '/redo' world editing command. It uses an argument parser to validate input and checks if there is any action available in the redo history. If an action exists, it captures the current state as an undo blueprint, reapplies the last change, and updates the undo history accordingly. If no action is available, it informs the user that there is nothing to redo.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	_ = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	if (source.worldEditData.redoHistory.pop()) |action| {
		defer action.deinit();

		const undo = Blueprint.capture(main.globalAllocator, action.selection());
		action.blueprint.paste(action.position, .{.preserveVoid = true});

		switch (undo) {
			.success => |blueprint| {
				source.worldEditData.undoHistory.push(.init(blueprint, action.position, action.message));
			},
			.failure => {
				source.sendMessage("#ff0000Error: Could not capture undo history.", .{});
			},
		}
		source.sendMessage("#00ff00Re-done last {s}.", .{action.message});
	} else {
		source.sendMessage("#ccccccNothing to redo.", .{});
	}
}
```

## Related Questions
- What is the description of the '/redo' command?
- How does the chunk handle argument parsing for the '/redo' command?
- What happens if there are no actions available in the redo history?
- How is the current state captured before reapplying the last change?
- What feedback is given to the user after successfully redone an action?
- How is the undo history updated when a redo operation is successful?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_redo.zig_chunk_0*
