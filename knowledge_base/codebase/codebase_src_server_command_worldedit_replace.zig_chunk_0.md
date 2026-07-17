# [easy/codebase_src_server_command_worldedit_replace.zig] - Chunk 0

**Type:** implementation
**Keywords:** replace command, block replacement, selection retrieval, error handling, blueprint manipulation
**Symbols:** command, Vec3i, User, Block, Blueprint, Pattern, Mask
**Concepts:** world edit, command execution

## Summary
World edit replace command execution

## Explanation
This chunk defines the `execute` function for the `replace` command in the world edit system. It parses input arguments, retrieves the current selection, and performs a block replacement operation based on provided old mask and new pattern strings.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var argsSplit = std.mem.splitScalar(u8, args, ' ');
	const oldMaskString = argsSplit.next() orelse {
		return source.sendMessage("#ff0000Missing required <old> argument.", .{});
	};
	const newPatternString = argsSplit.next() orelse {
		return source.sendMessage("#ff0000Missing required <new> argument.", .{});
	};

	const selection = command.getCurrentSelection(source) catch return;

	const oldMask = Mask.initFromString(main.stackAllocator, oldMaskString) catch |err| {
		return source.sendMessage("#ff0000Error parsing mask: {s}", .{@errorName(err)});
	};
	defer oldMask.deinit(main.stackAllocator);

	const newPattern = Pattern.initFromString(main.stackAllocator, newPatternString) catch |err| {
		return source.sendMessage("#ff0000Error parsing pattern: {s}", .{@errorName(err)});
	};
	defer newPattern.deinit(main.stackAllocator);

	const capture = Blueprint.capture(main.globalAllocator, selection);

	switch (capture) {
		.success => |blueprint| {
			source.worldEditData.undoHistory.push(.init(blueprint, selection.minPos, "replace"));
			source.worldEditData.redoHistory.clear();

			var modifiedBlueprint = blueprint.clone(main.stackAllocator);
			defer modifiedBlueprint.deinit(main.stackAllocator);

			modifiedBlueprint.replace(oldMask, null, newPattern);
			modifiedBlueprint.paste(selection.minPos, .{.preserveVoid = true});
		},
		.failure => |err| {
			source.sendMessage("#ff0000Error: Could not capture selection. (at {}, {s})", .{err.pos, err.message});
		},
	}
}
```

## Related Questions
- What is the purpose of the `execute` function in this chunk?
- How does the `execute` function handle missing arguments?
- What error messages are displayed for parsing issues with masks or patterns?
- Which module contains the definition of the `User` struct?
- Describe the process of capturing and modifying a blueprint during the replace operation.
- What is the purpose of the `undoHistory` push in this function?
- How does the `replace` method on the `Blueprint` struct work?
- What is the significance of the `.preserveVoid = true` option in the `paste` method?
- Which module contains the definition of the `Mask` struct?
- Describe the process of initializing a mask from a string.
- How are masks and patterns initialized from strings using the `initFromString` methods?
- What is the purpose of the `undoHistory` and `redoHistory` in this function?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_replace.zig_chunk_0*
