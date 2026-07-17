# [easy/codebase_src_server_command_worldedit_rotate.zig] - Chunk 0

**Type:** api
**Keywords:** command parsing, angle conversion, error reporting, clipboard rotation, memory management
**Symbols:** description, usage, execute
**Concepts:** command handling, user input, error handling, world editing, clipboard manipulation

## Summary
Handles the 'rotate' command for world editing, rotating clipboard content around the Z axis.

## Explanation
The function `execute` processes the 'rotate' command. It takes arguments and a user object as input. If no angle is provided, it defaults to 90 degrees. It checks if there is clipboard content; if not, it sends an error message. Otherwise, it rotates the clipboard content around the Z axis by the specified angle using the `rotateZ` method of the clipboard object.

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
- What does the 'rotate' command do?
- How is user input handled in this function?
- What error messages are sent if invalid input is provided?
- How is clipboard content rotated?
- Who calls the `execute` function?
- What happens if there is no clipboard content to rotate?
- How does memory management work for clipboard objects?
- What is the default rotation angle if none is specified?
- How is the `rotateZ` method used in this function?
- What type of data structure is used for storing clipboard content?
- Who defines the `Degrees` enum?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_rotate.zig_chunk_0*
