# [easy/codebase_src_server_command_worldedit_undo.zig] - Chunk 0

**Type:** implementation
**Keywords:** undo command, world edit, history restore, blueprint capture, undo history
**Symbols:** description, usage, Args, ArgParser, execute, User, Block, Blueprint, worldEditData
**Concepts:** undo, redo, world editing, command handling, history management

## Summary
Handles the '/undo' command for world editing, restoring the previous state of the world.

## Explanation
The function `execute` handles the '/undo' command in the server's world editing system. It parses the input arguments, checks if there is an undo history entry to restore, captures the redo history from the undone action, pastes it back into the world at the original position, and updates the redo history with the captured redo data. If no undo history exists, it sends a message indicating that nothing can be undone.

## Code Example
```zig
fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	_ = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};
	if (source.worldEditData.undoHistory.pop()) |action| {
		defer action.deinit();

		const redo = Blueprint.capture(main.globalAllocator, action.selection());
		action.blueprint.paste(action.position, .{.preserveVoid = true});

		switch (redo) {
			.success => |blueprint| {
				source.worldEditData.redoHistory.push(.init(blueprint, action.position, action.message));
			},
			.failure => {
				source.sendMessage("#ff0000Error: Could not capture redo history.", .{});
			},
		}
		source.sendMessage("#00ff00Un-done last {s}.", .{action.message});
	} else {
		source.sendMessage("#ccccccNothing to undo.", .{});
	}
}
```

## Related Questions
- What is the purpose of the 'undo' command in the world editing system?
- How does the function `execute` handle the '/undo' command?
- What data structures are used for storing undo and redo history in the world editing system?
- What error handling is implemented when restoring the previous state of the world?
- How is the redo history captured after an undo action?
- What message is sent to the user if there is nothing to undo?
- What is the purpose of the 'preserveVoid' option when pasting a blueprint back into the world?
- What is the difference between 'success' and 'failure' in the redo capture process?
- How are the undo and redo history entries managed in the world editing system?
- What is the role of the `ArgParser` in handling command arguments for the '/undo' command?
- What is the purpose of the `List(u8)` used to store error messages in the function `execute`?
- How does the function `execute` handle errors during argument parsing?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_undo.zig_chunk_0*
