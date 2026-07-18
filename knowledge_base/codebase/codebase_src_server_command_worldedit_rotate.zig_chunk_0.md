# [easy/codebase_src_server_command_worldedit_rotate.zig] - Chunk 0

**Type:** api
**Keywords:** command execution, argument parsing, error handling, clipboard rotation, user feedback
**Symbols:** description, usage, execute
**Concepts:** world edit, clipboard manipulation, server command handling

## Summary
Handles the server command for rotating clipboard content around the Z axis.

## Explanation
This chunk defines a server command that allows users to rotate the contents of their world edit clipboard. The `execute` function processes the command arguments, validates the rotation angle, checks if there is any clipboard content, and then performs the rotation using the specified angle. If the angle is invalid or no clipboard content exists, it sends an error message back to the user.

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
- What is the description of the rotate command?
- How does the execute function handle invalid angles?
- What error message is sent if there is no clipboard content?
- Which allocator is used for rotating the clipboard content?
- What are the valid rotation angles accepted by this command?
- How is the clipboard content rotated in this chunk?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_rotate.zig_chunk_0*
