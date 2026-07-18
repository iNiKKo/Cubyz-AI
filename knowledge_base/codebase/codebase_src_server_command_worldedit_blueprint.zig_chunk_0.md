# [medium/codebase_src_server_command_worldedit_blueprint.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, filesystem interaction, user messaging, blueprint management, directory traversal
**Symbols:** description, usage, Args, ArgParser, execute, blueprintSave, sendWarningAndLog, sendInfoAndLog, openBlueprintsDir, blueprintDelete, blueprintList
**Concepts:** command-line interface, file system operations, user feedback, error handling

## Summary
Handles blueprint-related commands for saving, deleting, loading, and listing blueprints. The `execute` function parses input arguments using an argument parser and delegates to handler functions like `blueprintSave`, `blueprintDelete`, `blueprintLoad`, and `blueprintList`. These handlers perform file operations on the 'blueprints' directory and provide user feedback through messaging.

## Explanation
This chunk defines a set of functions to manage blueprints via command-line inputs. The commands include `/blueprint save <filePath>`, `/blueprint delete <filePath>`, `/blueprint load <filePath>`, and `/blueprint list`. Each command is parsed by the `ArgParser` which maps to specific handler functions (`execute`). For example, `blueprintSave` saves the clipboard content to a specified file path in the 'blueprints' directory. If successful, it sends an info message back to the user; otherwise, it logs and sends a warning message. Similarly, `blueprintDelete` deletes a blueprint file from the 'blueprints' directory with appropriate error handling. The `blueprintList` function lists all blueprint files in the directory, sending their paths to the user. Error handling is centralized in helper functions like `sendWarningAndLog` and `sendInfoAndLog`, which log errors and send feedback messages.

## Code Example
```zig
fn deinit(self: Args, allocator: NeverFailingAllocator) void {
	switch (self) {
		inline else => |field| field.deinit(allocator),
	}
}
```

## Related Questions
- What are the exact commands for saving, deleting, loading, and listing blueprints?
- How does each command interact with the filesystem?
- What specific error handling mechanisms are used in this chunk?
- Which functions manage file operations and how do they handle errors?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_blueprint.zig_chunk_0*
