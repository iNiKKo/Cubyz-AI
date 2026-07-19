# [hard/codebase_src_assets.zig] - Chunk 2

**Type:** implementation
**Keywords:** asset discovery, ZON file reading, blueprint processing, default configuration, directory iteration
**Symbols:** Addon, Addon.name, Addon.dir, Addon.discoverAll, Addon.deinit, Addon.Defaults, Addon.Defaults.localArena, Addon.Defaults.localAllocator, Addon.Defaults.defaults, Addon.Defaults.init, Addon.Defaults.deinit, Addon.Defaults.get, Addon.Defaults.read, Addon.readAllZon, Addon.readAllBlueprints
**Concepts:** asset management, addon system, file I/O, error handling

## Summary
Handles asset discovery and reading for Cubyz, including addons, defaults, and specific asset types like blueprints.

## Explanation
This chunk defines the `Addon` struct responsible for managing assets within an addon directory. It includes methods to discover all addons in a given path, read ZON files with optional default merging, and read blueprint files. The `Defaults` nested struct manages default asset configurations, reading from `_defaults.zig.zon` or `_defaults.zon` files. Error handling is implemented throughout for file operations, logging errors when assets cannot be opened or processed.

The `Addon` struct has the following methods:
- `discoverAll`: Discovers all addons in a given path. It checks if the addon name contains only lowercase letters, numbers, and underscores. If not, it logs an error and skips the addon.
- `deinit`: Closes the directory and frees the addon's name.

The `Defaults` struct has the following methods:
- `init`: Initializes the local arena allocator and default hashmap.
- `deinit`: Deinitializes the local arena allocator.
- `get`: Retrieves or reads a default configuration for a given directory path.
- `read`: Reads a ZON file from the specified directory. If the `_defaults.zig.zon` file is not found, it attempts to read the `_defaults.zon` file.

The `Addon` struct also has methods for reading all ZON files and blueprints:
- `readAllZon`: Reads all ZON files in a given asset type directory. It merges defaults if specified and handles errors by logging them.
- `readAllBlueprints`: Reads all blueprint files in a given subpath directory and processes them.

## Code Example
```zig
fn deinit(self: *Defaults) void {
				self.localArena.deinit();
			}
```

## Related Questions
- How does the `Addon` struct discover all addons in a given path?
- What is the purpose of the `Defaults` nested struct within the `Addon` struct?
- How does the `readAllZon` method handle errors when reading ZON files?
- What specific checks are performed on addon names during discovery?
- How does the `readAllBlueprints` method process blueprint files?
- What is the role of the `localArena` and `localAllocator` in the `Defaults` struct?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_2*
