# [hard/codebase_src_assets.zig] - Chunk 3

**Type:** implementation
**Keywords:** BytesHashMap, file reading, error handling, directory traversal, migration files
**Symbols:** readAllAssets, readAllBlueprints, readAllModels
**Concepts:** asset management, file I/O, data storage

## Summary
This chunk handles reading assets from addon directories and storing them in a BytesHashMap.

## Explanation
The chunk contains three public functions: readAllAssets, readAllBlueprints, and readAllModels. Each function reads files from specified subdirectories of an addon, processes them, and stores the results in a BytesHashMap. The readAllAssets function also handles migration files separately. Error handling is included for file operations, with appropriate logging on failure.

## Code Example
```zig
pub fn readAllModels(addon: Addon, allocator: NeverFailingAllocator, subPath: []const u8, fileEnding: []const u8, output: *BytesHashMap) void {
			var assetsDirectory = addon.dir.openIterableDir(subPath) catch |err| {
				if (err != error.FileNotFound) {
					std.log.err("Could not open addon directory {s}: {s}", .{subPath, @errorName(err)});
				}
				return;
			};
			defer assetsDirectory.close();
			var walker = assetsDirectory.walk(main.stackAllocator);
			defer walker.deinit();

			while (walker.next(main.io) catch |err| blk: {
				std.log.err("Got error while iterating addon directory {s}: {s}", .{subPath, @errorName(err)});
				break :blk null;
			}) |entry| {
				if (entry.kind != .file) continue;
				if (!std.ascii.endsWithIgnoreCase(entry.basename, fileEnding)) continue;

				const id = createAssetStringID(allocator, addon.name, "model", entry.path) catch continue;

				const string = assetsDirectory.read(allocator, entry.path) catch |err| {
					std.log.err("Could not open {s}/{s}: {s}", .{subPath, entry.path, @errorName(err)});
					continue;
				};
				output.put(allocator.allocator, id, string) catch unreachable;
			}
		}
```

## Related Questions
- What is the purpose of the readAllAssets function?
- How does the chunk handle migration files?
- What types of errors are logged during file operations?
- Where does the chunk store the read assets?
- How does the chunk determine if a file should be skipped?
- What is the role of the BytesHashMap in this chunk?
- How does the chunk ensure that only specific file endings are processed?
- What happens if an error occurs while iterating through the directory?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_3*
