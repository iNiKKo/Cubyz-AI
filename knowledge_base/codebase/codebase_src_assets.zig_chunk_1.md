# [hard/codebase_src_assets.zig] - Chunk 1

**Type:** api
**Keywords:** discoverAll, readAllZon, Defaults, join, walk, AssetStringID, FileNotFound, deinit, arena allocator, HashMap
**Symbols:** Addon, Addon.name, Addon.dir, Addon.discoverAll, Addon.deinit, Addon.Defaults, Addon.Defaults.localArena, Addon.Defaults.localAllocator, Addon.Defaults.defaults, Addon.Defaults.init, Addon.Defaults.deinit, Addon.Defaults.get, Addon.Defaults.read, Assets.log
**Concepts:** asset discovery, addon directory iteration, default file merging, ZON loading, left-prefer join, file filtering, error handling, resource cleanup

## Summary
This chunk defines the Assets module that discovers and reads all game assets from addon directories. It implements a public API to load ZON files for blocks, items, tools, structure tables, biomes, cave layers, recipes, SBBs, blueprints, models, particles, world presets, and entity model descriptions. The code handles default file merging via a Defaults struct that reads _defaults.zig.zon or _defaults.zon, applies left-prefer joins, and logs final counts.

## Explanation
The chunk declares the Addon struct with name and dir fields, plus discoverAll which iterates an assetDir, validates addon names (lowercase letters, digits, underscores), opens each subdirectory, and appends valid Addons to a list. It also defines deinit for Addon that closes the directory and frees the name string. The Defaults struct holds a localArena, localAllocator, and defaults HashMap; init creates an arena from stackAllocator, get looks up or inserts a path into the map (reading _defaults.zig.zon first, then _defaults.zon if missing), and read attempts to load those default files returning .null on FileNotFound. The public function readAllZon opens the addon's assetType directory, walks it, skips hidden defaults and migrations, creates an AssetStringID for each file, reads the ZON into zon, optionally joins with defaultsStorage.get (if hasDefaults is true), and continues processing remaining files.

## Related Questions
- What validation rules does discoverAll enforce on addon names?
- How does the Defaults struct handle missing default files?
- Which file patterns are skipped during readAllZon iteration?
- What happens when an addon directory cannot be opened?
- Is there any merging logic applied to ZON data in this chunk?
- Where is memory for addon names allocated and freed?
- How does the code ensure proper cleanup of directories on exit?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_1*
