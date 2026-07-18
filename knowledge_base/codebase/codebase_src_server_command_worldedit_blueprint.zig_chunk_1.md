# [medium/codebase_src_server_command_worldedit_blueprint.zig] - Chunk 1

**Type:** implementation
**Keywords:** blueprint loading, file path parsing, extension checking, memory allocation, error logging
**Symbols:** blueprintLoad, FilePath, FilePath.path, FilePath.deinit, FilePath.parse, ensureBlueprintExtension
**Concepts:** world editing, file I/O, memory management, error handling

## Summary
Handles loading blueprint files for world editing.

## Explanation
The chunk defines a function `blueprintLoad` that loads a blueprint file from a specified path and assigns it to the user's clipboard. It opens the blueprints directory, reads the file content, and handles errors by sending warnings and logs. The `FilePath` struct manages file paths, including parsing and ensuring the correct file extension. The chunk also includes utility functions for error handling and memory management.

## Code Example
```zig
fn blueprintLoad(filePath: FilePath, source: *User) void {
	var blueprintsDir = openBlueprintsDir(source) orelse return;
	defer blueprintsDir.close();

	const storedBlueprint = blueprintsDir.read(main.stackAllocator, filePath.path) catch |err| {
		sendWarningAndLog("Failed to read blueprint file '{s}' ({s})", .{filePath.path, @errorName(err)}, source);
		return;
	};
	defer main.stackAllocator.free(storedBlueprint);

	if (source.worldEditData.clipboard) |oldClipboard| {
		oldClipboard.deinit(main.globalAllocator);
	}
	source.worldEditData.clipboard = Blueprint.load(main.globalAllocator, storedBlueprint) catch |err| {
		return sendWarningAndLog("Failed to load blueprint file '{s}' ({s})", .{filePath.path, @errorName(err)}, source);
	};

	sendInfoAndLog("Loaded blueprint file: {s}", .{filePath.path}, source);
}
```

## Related Questions
- What function loads a blueprint file?
- How does the chunk handle errors when reading a blueprint file?
- What is the purpose of the `FilePath` struct?
- How does the chunk ensure the correct file extension for blueprints?
- What happens if there is an existing clipboard when loading a new blueprint?
- How is memory managed in this chunk?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_blueprint.zig_chunk_1*
