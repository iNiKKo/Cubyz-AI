# [easy/codebase_src_server_command_worldedit_set.zig] - Chunk 0

**Type:** implementation
**Keywords:** command execution, selection handling, blueprint capture, undo history, worldedit
**Symbols:** description, usage, execute, server.command, Vec3i, User, Block, Blueprint, Pattern
**Concepts:** WorldEdit, Command Execution, Selection Handling, Blueprint Capture, Undo/Redo History

## Summary
Sets all blocks within a selection to a specified block pattern.

## Explanation
The `execute` function handles the '/set' command in the WorldEdit feature. It first checks if the required <pattern> argument is provided. If not, it sends an error message and returns. The current selection is retrieved using `command.getCurrentSelection`. A Pattern object is initialized from the provided arguments. After capturing the selection into a Blueprint, the function pushes the change to the undo history and clears the redo history. It then clones the captured blueprint, replaces blocks based on the mask and pattern, and pastes them back into the world at the original selection position.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	if (args.len == 0) {
		source.sendMessage("#ff0000Missing required <pattern> argument.", .{});
		return;
	}
	const selection = command.getCurrentSelection(source) catch return;

	const pattern = Pattern.initFromString(main.stackAllocator, args) catch |err| {
		source.sendMessage("#ff0000Error parsing pattern: {s}", .{@errorName(err)});
		return;
	};
	defer pattern.deinit(main.stackAllocator);

	const result = Blueprint.capture(main.globalAllocator, selection);

	switch (result) {
		.success => |blueprint| {
			source.worldEditData.undoHistory.push(.init(blueprint, selection.minPos, "set"));
			source.worldEditData.redoHistory.clear();

			var modifiedBlueprint = blueprint.clone(main.stackAllocator);
			defer modifiedBlueprint.deinit(main.stackAllocator);

			modifiedBlueprint.replace(null, source.worldEditData.mask, pattern);
			modifiedBlueprint.paste(selection.minPos, .{.preserveVoid = true});
		},
		.failure => |err| {
			source.sendMessage("#ff0000Error: Could not capture selection. (at {}, {s})", .{err.pos, err.message});
		},
	}
}
```

## Related Questions
- What is the purpose of the `execute` function in the WorldEdit command system?
- How does the `execute` function handle errors when parsing the pattern argument?
- What data structures are used to store and manipulate the selection and blueprint during the execution process?
- Describe the steps involved in capturing a selection into a Blueprint.
- What is the purpose of the undo/redo history system in this WorldEdit implementation?
- How does the `execute` function handle errors related to capturing the selection?
- What is the role of the mask and pattern in the block replacement process?
- Describe how the modified blueprint is pasted back into the world.
- What are the key data structures used to manage the WorldEdit command system's state?
- How does the `execute` function interact with other parts of the server codebase?
- What error messages are sent by the `execute` function when encountering issues during execution?
- Describe the process of cloning and modifying a blueprint in the context of the WorldEdit command.

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_set.zig_chunk_0*
