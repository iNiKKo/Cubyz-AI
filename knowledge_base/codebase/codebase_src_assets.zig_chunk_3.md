# [hard/codebase_src_assets.zig] - Chunk 3

**Type:** implementation
**Keywords:** BytesHashMap, file reading, error handling, directory traversal, migration files
**Symbols:** readAllAssets, readAllBlueprints, readAllModels
**Concepts:** asset management, file I/O, data storage

## Summary
This chunk handles reading assets from addon directories and storing them in a BytesHashMap.

## Explanation
This chunk handles reading assets from addon directories and storing them in a BytesHashMap. It contains three public functions: `readAllAssets`, `readAllBlueprints`, and `readAllModels`. Each function reads files from specified subdirectories of an addon, processes them, and stores the results in a BytesHashMap. The `readAllAssets` function also handles migration files separately. Error handling is included for file operations, with appropriate logging on failure.

The `readAllAssets` function iterates over entries in the assets directory, skipping `_migrations.zig.zon` files. It creates an asset ID using `createAssetStringID`, reads the ZON file into a `zon` object, and merges it with default settings if available. The resulting `zon` object is then stored in the output map.

The `readAllBlueprints` function reads blueprint files (`.blp`) from the specified subdirectory, skipping `_defaults` and `_migrations` prefixed files. It creates an asset ID using `createAssetStringID`, reads the file data, and stores it in the output map.

The `readAllModels` function reads model files with a specific ending (e.g., `.obj`) from the specified subdirectory. It creates an asset ID using `createAssetStringID`, reads the file data, and stores it in the output map.

Migration files are handled separately by the `readAllAssets` function. If `_migrations.zig.zon` is found, it is read into a `zon` object and stored in the `_migrations` map. The chunk logs errors for file operations such as opening directories or reading files, using `std.log.err`. The chunk stores read assets in a BytesHashMap, where each asset is identified by a unique ID created using `createAssetStringID`. Files are skipped if they are not of type `.file`, do not match the specified file ending (for `readAllModels`), or have names prefixed with `_defaults` or `_migrations` (for `readAllBlueprints`). The BytesHashMap is used to efficiently store and retrieve asset data.

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
