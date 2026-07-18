# [hard/codebase_src_assets.zig] - Chunk 2

**Type:** implementation
**Keywords:** asset discovery, ZON file reading, blueprint processing, default configuration, directory iteration
**Symbols:** Addon, Addon.name, Addon.dir, Addon.discoverAll, Addon.deinit, Addon.Defaults, Addon.Defaults.localArena, Addon.Defaults.localAllocator, Addon.Defaults.defaults, Addon.Defaults.init, Addon.Defaults.deinit, Addon.Defaults.get, Addon.Defaults.read, Addon.readAllZon, Addon.readAllBlueprints
**Concepts:** asset management, addon system, file I/O, error handling

## Summary
Handles asset discovery and reading for Cubyz, including addons, defaults, and specific asset types like blueprints.

## Explanation
This chunk defines the `Addon` struct responsible for managing assets within an addon directory. It includes methods to discover all addons in a given path, read ZON files with optional default merging, and read blueprint files. The `Defaults` nested struct manages default asset configurations, reading from `_defaults.zig.zon` or `_defaults.zon` files. Error handling is implemented throughout for file operations, logging errors when assets cannot be opened or processed.

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
