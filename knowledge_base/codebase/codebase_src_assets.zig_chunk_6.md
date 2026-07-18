# [hard/codebase_src_assets.zig] - Chunk 6

**Type:** implementation
**Keywords:** asset management, migrations, palette registration, hot reloading, iterator usage
**Symbols:** loadWorldAssets, worldAssetFolder
**Concepts:** asset loading, entity ECS, world generation, hot reloading

## Summary
Handles loading and registering world assets including blocks, items, biomes, and entity models.

## Explanation
The `loadWorldAssets` function orchestrates the loading of various game assets such as blocks, items, biomes, and entity models from specified folders. It uses a series of iterators to process each type of asset, applying migrations if necessary and registering them into their respective palettes. The function also handles procedural items, recipes, blueprints, particles, cave layers, and entity components. Additionally, it sets up hot reloading for asset directories.

## Code Example
```zig
pub fn loadWorldAssets(assetFolder: []const u8, blockPalette: *Palette, itemPalette: *Palette, proceduralItemPalette: *Palette, biomePalette: *Palette, entityModelPalette: *Palette, entityComponentPalette: *Palette) !void { // MARK: loadWorldAssets()
	const prevVal = refCount.fetchAdd(1, .monotonic);
	if (prevVal != 0) return; // The assets already got loaded by the server.

	worldAssetFolder = main.worldArena.dupe(u8, assetFolder);

	main.Tag.initTags();

	const worldArena = main.stackAllocator.createArena();
	defer main.stackAllocator.destroyArena(worldArena);

	var worldAssets = common.clone(worldArena);
	worldAssets.read(worldArena, main.files.cubyzDir(), assetFolder);

	errdefer unloadAssets();

	migrations.registerAll(.block, &worldAssets.blockMigrations);
	migrations.apply(.block, blockPalette);

	migrations.registerAll(.item, &worldAssets.itemMigrations);
	migrations.apply(.item, itemPalette);

	migrations.registerAll(.biome, &worldAssets.biomeMigrations);
	migrations.apply(.biome, biomePalette);

	migrations.registerAll(.entityModel, &worldAssets.entityModelMigrations);
	migrations.apply(.entityModel, entityModelPalette);

	migrations.registerAll(.entityComponent, &worldAssets.entityComponentMigrations);
	migrations.apply(.entityComponent, entityComponentPalette);

	// models (block optimized):
	{
		var modelIterator = worldAssets.blockModels.iterator();
		while (modelIterator.next()) |entry| {
			const zon = worldAssets.blockModelsZon.get(entry.key_ptr.*);
			_ = main.models.registerModel(entry.key_ptr.*, entry.value_ptr.*, zon);
		}
	}

	// EntityModels:
	{
		// First models from the palette to enforce ID values.
		for (entityModelPalette.palette.items) |entityModelId| {
			std.log.debug("Registering entity model {s}", .{entityModelId});
			_ = main.entityModel.register(assetFolder, entityModelId, worldAssets.entityModelDescriptions.get(entityModelId) orelse .null);
		}
		// Then all the models that were missing in palette but are present in the game.
		var entModelIterator = worldAssets.entityModelDescriptions.iterator();
		while (entModelIterator.next()) |entry| {
			const entityModelId = entry.key_ptr.*;
			const zon = entry.value_ptr.*;

			if (main.entityModel.getById(entityModelId) != null) continue;

			std.log.debug("Registering entity model {s}", .{entry.key_ptr.*});
			_ = main.entityModel.register(assetFolder, entityModelId, zon);
			entityModelPalette.add(entityModelId);
		}
	}

	if (!main.settings.launchConfig.headlessServer) blocks.meshes.registerBlockBreakingAnimation(assetFolder);

	// Blocks:
	// First blocks from the palette to enforce ID values.
	for (blockPalette.palette.items) |stringId| {
		try registerBlock(assetFolder, stringId, worldAssets.blocks.get(stringId) orelse .null);
	}

	// Then all the blocks that were missing in palette but are present in the game.
	var iterator = worldAssets.blocks.iterator();
	while (iterator.next()) |entry| {
		const stringId = entry.key_ptr.*;
		const zon = entry.value_ptr.*;

		if (blocks.hasRegistered(stringId)) continue;

		try registerBlock(assetFolder, stringId, zon);
		blockPalette.add(stringId);
	}

	// Items:
	// First from the palette to enforce ID values.
	for (itemPalette.palette.items) |stringId| {
		// Some items are created automatically from blocks.
		if (worldAssets.blocks.get(stringId)) |zon| {
			if (!(zon.get(bool, "hasItem") orelse true)) continue;
			try registerItem(assetFolder, stringId, zon.getChild("item"));
			if (worldAssets.items.get(stringId) != null) {
				std.log.err("Item {s} appears as standalone item and as block item.", .{stringId});
			}
			continue;
		}
		// Items not related to blocks should appear in items hash map.
		if (worldAssets.items.get(stringId)) |zon| {
			try registerItem(assetFolder, stringId, zon);
			continue;
		}
		std.log.err("Missing item: {s}. Replacing it with default item.", .{stringId});
		try registerItem(assetFolder, stringId, .null);
	}

	// Then missing block-items to keep backwards compatibility of ID order.
	for (blockPalette.palette.items) |stringId| {
		const zon = worldAssets.blocks.get(stringId) orelse .null;

		if (!(zon.get(bool, "hasItem") orelse true)) continue;
		if (items.hasRegistered(stringId)) continue;

		try registerItem(assetFolder, stringId, zon.getChild("item"));
		itemPalette.add(stringId);
	}

	// And finally normal items.
	iterator = worldAssets.items.iterator();
	while (iterator.next()) |entry| {
		const stringId = entry.key_ptr.*;
		const zon = entry.value_ptr.*;

		if (items.hasRegistered(stringId)) continue;
		std.debug.assert(zon != .null);

		try registerItem(assetFolder, stringId, zon);
		itemPalette.add(stringId);
	}

	// After we have registered all items and all blocks, we can assign block references to those that come from blocks.
	for (blockPalette.palette.items) |stringId| {
		const zon = worldAssets.blocks.get(stringId) orelse .null;

		if (!(zon.get(bool, "hasItem") orelse true)) continue;
		std.debug.assert(items.hasRegistered(stringId));

		try assignBlockItem(stringId);
	}

	for (proceduralItemPalette.palette.items) |id| {
		registerProceduralItem(assetFolder, id, worldAssets.proceduralItems.get(id) orelse .null);
	}

	// procedural items:
	iterator = worldAssets.proceduralItems.iterator();
	while (iterator.next()) |entry| {
		const id = entry.key_ptr.*;
		if (items.hasRegisteredProceduralItem(id)) continue;
		registerProceduralItem(assetFolder, id, entry.value_ptr.*);
		proceduralItemPalette.add(id);
	}

	// block drops:
	blocks.finishBlocks(worldAssets.blocks);

	iterator = worldAssets.recipes.iterator();
	while (iterator.next()) |entry| {
		registerRecipesFromZon(entry.value_ptr.*);
	}

	try sbb.registerBlueprints(&worldAssets.blueprints);
	try sbb.registerSBB(&worldAssets.structureBuildingBlocks);
	try main.server.terrain.structures.registerStructureTables(&worldAssets.structureTables);

	iterator = worldAssets.particles.iterator();
	while (iterator.next()) |entry| {
		particles.ParticleManager.register(assetFolder, entry.key_ptr.*, entry.value_ptr.*);
	}

	// Biomes:
	var nextBiomeNumericId: u32 = 0;
	for (biomePalette.palette.items) |id| {
		registerBiome(nextBiomeNumericId, id, worldAssets.biomes.get(id) orelse .null);
		nextBiomeNumericId += 1;
	}
	iterator = worldAssets.biomes.iterator();
	while (iterator.next()) |entry| {
		if (biomes.hasRegistered(entry.key_ptr.*)) continue;
		registerBiome(nextBiomeNumericId, entry.key_ptr.*, entry.value_ptr.*);
		biomePalette.add(entry.key_ptr.*);
		nextBiomeNumericId += 1;
	}
	biomes.finishLoading();

	// Cave layers:
	try main.server.terrain.cave_layers.registerCaveLayers(&worldAssets.caveLayers);

	// EntityComponents
	{
		var map: std.StringHashMap(u32) = .init(main.stackAllocator.allocator);
		defer map.deinit();
		var index: u32 = 0;

		// the already exisiting ones:
		for (entityComponentPalette.palette.items) |value| {
			map.put(value, index) catch unreachable;
			index += 1;
		}

		// now give each component it's id:
		inline for (@typeInfo(main.entity.components).@"struct".decls) |decl| {
			const name = decl.name;
			if (map.get(name)) |id| {
				@field(main.entity.components, decl.name).entityComponentID = id;
			} else {
				entityComponentPalette.add(name);
				@field(main.entity.components, decl.name).entityComponentID = index;
				index += 1;
			}
		}
		main.entity.initComponents();
	}

	// Register paths for asset hot reloading:
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
			main.utils.file_monitor.listenToPath(path, main.blocks.meshes.reloadTextures, 0);
		}
	}

	worldAssets.log(.world);
}
```

## Related Questions
- What is the purpose of the `loadWorldAssets` function?
- How does the function handle asset migrations?
- Which assets are loaded and registered by this function?
- What steps are taken to ensure that all blocks and items are correctly registered?
- How does the function manage hot reloading for asset directories?
- What is the role of `refCount` in this function?
- How are procedural items handled during the loading process?
- What error handling mechanisms are present in the asset loading process?
- How does the function ensure that entity component IDs are correctly assigned?
- What is the sequence of operations for registering biomes?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_6*
