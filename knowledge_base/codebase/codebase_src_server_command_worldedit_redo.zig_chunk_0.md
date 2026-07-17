# [easy/codebase_src_server_command_worldedit_redo.zig] - Chunk 0

**Type:** implementation
**Keywords:** undo, redo, world editing, blueprint, selection
**Symbols:** description, usage, Args, ArgParser, execute, errorMessage, source, User, Block, Blueprint, worldEditData, redoHistory, pop, action, deinit, capture, paste, undo, success, failure, message
**Concepts:** world editing, undo/redo history, block modification

## Summary
Redo last change done to world with world editing commands.

## Explanation
This function handles the '/redo' command, which re-applies the last block modification made by the user through world editing. It uses a stack-based redo history to store and apply the most recent action. The function captures the undo history of the previous action, pastes it back into the world at the same position, and then updates the undo history with the new action. If there is no redo history, it informs the user that there is nothing to redo.

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
- What is the purpose of the 'execute' function in this chunk?
- How does the 'redoHistory' stack work in this implementation?
- What happens if there is no redo history available?
- What is the role of the 'undo' variable in this code?
- How is the undo history stored and retrieved in this function?
- What is the purpose of the 'capture' function in this chunk?
- What does the 'paste' function do in this implementation?
- What is the difference between 'success' and 'failure' in the 'undo' result?
- How is the undo history updated after a redo operation?
- What is the format of the error message displayed to the user if an error occurs during the redo process?
- What does the 'message' variable represent in this code?
- How is the 'position' variable used in this function?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_redo.zig_chunk_0*
