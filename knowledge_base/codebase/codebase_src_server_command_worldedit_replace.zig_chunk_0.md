# [easy/codebase_src_server_command_worldedit_replace.zig] - Chunk 0

**Type:** implementation
**Keywords:** world edit command, block replacement, blueprint capture, undo history, error handling
**Symbols:** command, Vec3i, User, Block, Blueprint, Pattern, Mask, description, usage, execute, argsSplit, oldMaskString, newPatternString, selection, oldMask, newPattern, capture, success, failure, err, source.sendMessage
**Concepts:** world edit, block replacement, blueprint manipulation, undo/redo history

## Summary
World edit command to replace blocks in the selected area.

## Explanation
This function executes a world edit command that replaces blocks based on specified old and new patterns. It captures the current selection, parses the old mask and new pattern strings, and then applies the replacement operation to the captured blueprint. The modified blueprint is then pasted back into the world at the original selection position.

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
- What is the purpose of the `replace` function in this code?
- How does the `capture` function work in this context?
- What error handling is implemented for the `capture` function?
- What is the role of the `undoHistory` and `redoHistory` in this code?
- How are the old mask and new pattern parsed from strings?
- What is the purpose of the `clone` method on the modified blueprint?
- What is the effect of the `.preserveVoid = true` option when pasting the modified blueprint back into the world?
- What is the difference between `success` and `failure` in the capture result?
- How are errors reported to the user in this code?
- What is the purpose of the `Vec3i` type in this context?
- What is the role of the `User` struct in this code?
- What is the purpose of the `Block` and `Blueprint` types in this code?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_replace.zig_chunk_0*
