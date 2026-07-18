# [easy/codebase_src_server_command_worldedit_rotate.zig] - Chunk 0

**Type:** api
**Keywords:** command execution, argument parsing, error handling, clipboard rotation, user feedback
**Symbols:** description, usage, execute
**Concepts:** world edit, clipboard manipulation, server command handling

## Summary
Handles the server command for rotating clipboard content around the Z axis.

## Explanation
This chunk defines a server command that allows users to rotate the contents of their world edit clipboard around the Z axis counterclockwise. The `execute` function processes the command arguments, sets a default angle of 90 degrees if no argument is provided, validates the rotation angle (which can be 0, 90, 180, or 270 degrees), checks if there is any clipboard content, and then performs the rotation using the specified angle. If the angle is invalid or no clipboard content exists, it sends an error message back to the user.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var angle: Degrees = .@"90";
	if (args.len != 0) {
		angle = std.meta.stringToEnum(Degrees, args) orelse {
			source.sendMessage("#ff0000Error: Invalid angle '{s}'. Use 0, 90, 180 or 270.", .{args});
			return;
		};
	}
	if (source.worldEditData.clipboard == null) {
		source.sendMessage("#ff0000Error: No clipboard content to rotate.", .{});
		return;
	}
	const current = source.worldEditData.clipboard.?;
	defer current.deinit(main.globalAllocator);
	source.worldEditData.clipboard = current.rotateZ(main.globalAllocator, angle);
}
```

## Related Questions
- What is the default angle when no argument is provided?
- Which angles are valid for this command?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_rotate.zig_chunk_0*
