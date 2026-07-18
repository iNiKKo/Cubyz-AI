# [easy/codebase_src_server_command_worldedit_undo.zig] - Chunk 0

**Type:** implementation
**Keywords:** undo command, world edit, redo history, blueprint capture, world paste
**Symbols:** description, usage, Args, ArgParser, execute, User, Block, Blueprint, source, worldEditData, undoHistory, pop, action, deinit, capture, globalAllocator, redo, success, failure, message, sendMessage
**Concepts:** world editing, undo, redo history, blueprint capture, world paste

## Summary
Handles the '/undo' command for world editing, restoring the previous state of the world.

## Explanation
The function `execute` handles the '/undo' command in the server's world editing system. It parses the input arguments, checks if there is an undo history entry to restore, captures the redo history from the undone action, pastes it back into the world at the original position, and updates the redo history with the new state. If no undo history exists, it sends a message indicating that nothing can be undone.

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
- What error handling is implemented when capturing or pasting blueprints during an undo operation?
- What message is sent to the user if there is nothing to undo?
- How does the function `execute` handle the restoration of a blueprint after an undo operation?
- What information is stored in the redo history entry for each undone action?
- What is the purpose of the 'capture' function used during an undo operation?
- What is the purpose of the 'paste' function used during an undo operation?
- How does the function `execute` handle the message associated with the undone action?
- What is the purpose of the 'sendMessage' function used to communicate with users in the world editing system?
- What are the possible outcomes when restoring a blueprint after an undo operation?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_undo.zig_chunk_0*
