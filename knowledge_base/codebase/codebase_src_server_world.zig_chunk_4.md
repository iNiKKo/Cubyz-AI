# [hard/codebase_src_server_world.zig] - Chunk 4

**Type:** implementation
**Keywords:** NeverFailingAllocator, main.globalAllocator, files.cubyzDir, ZonElement, std.log.info, errdefer, chunkUpdateQueue, regionUpdateQueue, storeToZon, decreaseRefCount
**Symbols:** loadPalette, deinit, loadWorldConfig
**Concepts:** world initialization, palette loading, version migration, asset persistence, chunk manager setup, permission groups, resource cleanup

## Summary
This chunk implements the ServerWorld initialization sequence: loading and persisting palettes (block, item, procedural, biome, entity model/component), migrating world data across versioned formats, initializing ChunkManager and permission groups, and providing deinit with cleanup of all allocated resources.

## Explanation
The init method first initializes chunkUpdateQueue and regionUpdateQueue via .init(main.globalAllocator, 256). It then creates an arena on the stack allocator for temporary allocations. It opens the saves directory using files.cubyzDir().openDir with a formatted path 'saves/{path}'. The loadPalette function is called multiple times to load blockPalette, itemPalette, proceduralItemPalette, biomePalette, entityModelPalette, and entityComponentPalette; each call allocates a path string via std.fmt.allocPrint into the arena, reads the .zon file using files.cubyzDir().readToZon, then calls main.assets.Palette.init with main.globalAllocator. Each palette is errdefer'd to deinit on failure. After loading palettes, assets are unloaded (errdefer main.assets.unloadAssets()), then worldData is read via dir.readToZon('world.zig.zon'). loadWorldConfig is called with the arena and worldData; it handles version migrations: if version==2 it reads gamerules.zig.zon and generatorSettings.zig.zon, constructs a settings object copying defaultGamemode, allowCheats, testingMode, seed (error.NoSeed if missing), updates worldData.version to 3, writes world.zig.zon, deletes gamerules.zig.zon and generatorSettings.zig.zon. If version==3 it renames default_gamemode to defaultGamemode and cheats to allowCheats inside the settings child, then sets version to 4 and rewrites world.zig.zon. If version==4 it prepares a list of player files (only .zon) from dir.openIterableDir('players') for later migration to numerical names. After loadWorldConfig returns, main.assets.loadWorldAssets is called with a formatted assets path '{cubyzDirStr()}/{path}/assets/' and all palettes as arguments. Then the six palette zon files are written back to disk via dir.writeZon using each palette's storeToZon method. ChunkManager.init(self, worldData.getChild('generatorSettings')) is called; errdefer self.chunkManager.deinit(). permission.loadGroups(try dir.openIterableDir('groups')) loads group definitions. std.debug.assert ensures the missing entity model exists. The init returns self.

The loadPalette function (declared in this chunk) takes a NeverFailingAllocator, worldName, paletteName, and optional firstEntry; it allocates a path string 'saves/{worldName}/{paletteName}.zig.zon' into main.stackAllocator.allocator, reads the file via files.cubyzDir().readToZon (catching .null), then calls main.assets.Palette.init(main.globalAllocator, paletteZon, firstEntry) and logs with std.log.info.

The deinit method cleans up: it saves world config (saveWorldConfig) catching errors and logging via std.log.err; saves all players (saveAllPlayers); saves item drops (saveItemdrops). It then processes self.chunkUpdateQueue by popping front elements, calling updateRequest.ch.save(self) and decreaseRefCount(), then deinit the queue. Similarly for regionUpdateQueue: popFront, store() on updateRequest.region, decreaseRefCount(). Then it calls deinit on chunkManager, itemDropManager, all six palettes (blockPalette, itemPalette, proceduralItemPalette, biomePalette, entityModelPalette, entityComponentPalette), permission.deinit(), frees self.path and self.name from main.globalAllocator, and finally destroys self.

loadWorldConfig is declared as pub fn loadWorldConfig(self: *ServerWorld, arena: NeverFailingAllocator, dir: main.files.Dir, worldData: ZonElement) !void. It uses std.log.info for migration messages, constructs settings via ZonElement.initObject(arena), calls settings.put and settings.removeChild to rename keys, reads gamerules.zig.zon and generatorSettings.zig.zon via dir.readToZon, writes back with dir.writeZon('world.zig.zon'), deletes old files with dir.deleteFile. The function also opens playerDir = try dir.openIterableDir('players') and iterates using iterator.next(main.io) to collect .zon file names into a list (fileNames.append(arena, arena.dupe(u8, file.name))).

## Related Questions
- What palettes are loaded during ServerWorld init and how is each persisted to disk?
- How does loadPalette handle missing .zon files when reading a palette from the saves directory?
- Describe the exact steps performed inside deinit for cleaning up chunkUpdateQueue entries.
- Which version migrations are implemented in loadWorldConfig and what keys are renamed during migration 3→4?
- What error is returned if a world being migrated lacks a seed value, and how is it logged?
- How does the code ensure that the missing entity model exists before returning from init?
- Explain why main.assets.unloadAssets() is errdefer'd immediately after loading palettes.
- What is the purpose of opening dir.openIterableDir('groups') and calling permission.loadGroups on it?
- How are player file names collected in loadWorldConfig for later migration to numerical IDs?
- Which functions are declared as pub in this chunk and what are their signatures?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_4*
