# [medium/codebase_src_server_command_worldedit_blueprint.zig] - Chunk 1

**Type:** implementation
**Keywords:** directory traversal, file I/O, error handling, string manipulation, memory allocation
**Symbols:** sendWarningAndLog, blueprintList, blueprintLoad, FilePath, FilePath.path, FilePath.deinit, FilePath.parse, ensureBlueprintExtension
**Concepts:** world edit, blueprint management, file handling

## Summary
Handles world edit blueprint commands including listing, loading, and deleting blueprints.

## Explanation
This chunk defines functions to manage blueprint files for the world editor. It includes `blueprintList` to list all blueprint files in the 'blueprints' directory, `blueprintLoad` to load a specific blueprint file into the clipboard, and an implicit delete function (not shown here) that sends a warning and logs the deletion. The `FilePath` struct manages blueprint file paths, ensuring they have the correct '.blp' extension.

## Code Example
```zig
fn ensureBlueprintExtension(allocator: NeverFailingAllocator, fileName: []const u8) []const u8 {
	if (!std.ascii.endsWithIgnoreCase(fileName, ".blp")) {
		return std.fmt.allocPrint(allocator.allocator, "{s}.blp", .{fileName}) catch unreachable;
	} else {
		return allocator.dupe(u8, fileName);
	}
}
```

## Related Questions
- How does the `blueprintList` function handle directory traversal?
- What error handling is implemented in the `blueprintLoad` function?
- What is the purpose of the `FilePath` struct in this code?
- How does the `ensureBlueprintExtension` function ensure file extensions are correct?
- What happens if a blueprint file cannot be read during loading?
- How is memory managed for blueprint files in this implementation?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_blueprint.zig_chunk_1*
