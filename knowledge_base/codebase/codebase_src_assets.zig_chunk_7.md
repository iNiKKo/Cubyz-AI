# [hard/codebase_src_assets.zig] - Chunk 7

**Type:** implementation
**Keywords:** asset unloading, file reading, reference count, hot reloading, directory iteration
**Symbols:** unloadAssets, readAsset, worldPresets
**Concepts:** asset management, file I/O, reference counting

## Summary
Handles asset unloading and reading.

## Explanation
This chunk contains functions for managing assets, including unloading them when they are no longer needed and reading specific assets from the file system. The `unloadAssets` function decrements a reference count and deinitializes various components if the count reaches zero. These components include `main.entity`, `sbb`, `blocks`, `items`, `migrations`, `biomes`, `main.server.terrain.cave_layers`, `main.server.terrain.structures`, `main.models`, `main.particles.ParticleManager`, `main.rotation`, and `main.Tag`. It also removes paths from asset hot reloading by iterating over the `assets` directory and removing paths for directories that contain block textures. The `readAsset` function constructs a path based on given parameters (`subPath`, `id`, and `fileEnding`). If the file does not exist in the first constructed path, it tries another path. It reads the contents of the file and returns them. The `worldPresets` function returns a pointer to a world presets map.

## Code Example
```zig
pub fn unloadAssets() void { // MARK: unloadAssets()
	const prevVal = refCount.fetchSub(1, .monotonic);
	std.debug.assert(prevVal != 0);
	if (prevVal != 1) return;

	main.entity.deinitComponents();
	sbb.reset();
	blocks.reset();
	items.reset();
	migrations.reset();
	biomes.reset();
	main.server.terrain.cave_layers.reset();
	main.server.terrain.structures.reset();
	main.models.reset();
	main.particles.ParticleManager.reset();
	main.rotation.reset();
	main.Tag.resetTags();
	main.entityModel.reset();

	// Remove paths from asset hot reloading:
	var dir = main.files.cwd().openIterableDir("assets") catch |err| {
		std.log.err("Can't open asset path {s}: {s}", .{"assets", @errorName(err)});
		return;
	};
	defer dir.close();
	var dirIterator = dir.iterate();
	while (dirIterator.next(main.io) catch |err| blk: {
		std.log.err("Got error while iterating over asset path {s}: {s}", .{"assets", @errorName(err)});
		break :blk null;
	}) |addon| {
		if (addon.kind == .directory) {
			const path = std.fmt.allocPrintSentinel(main.stackAllocator.allocator, "assets/{s}/blocks/textures", .{addon.name}, 0) catch unreachable;
			defer main.stackAllocator.free(path);
			// Check for access rights
			if (!main.files.cwd().hasDir(path)) continue;
			main.utils.file_monitor.removePath(path);
		}
	}
}
```

## Related Questions
- What does the `unloadAssets` function do?
- How does the `readAsset` function construct file paths?
- What is the purpose of the `worldPresets` function?
- How does the chunk handle errors when reading files?
- What components are deinitialized in the `unloadAssets` function?
- How does the chunk manage asset hot reloading paths?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_7*
