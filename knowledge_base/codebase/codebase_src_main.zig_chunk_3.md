# [hard/codebase_src_main.zig] - Chunk 3

**Type:** implementation
**Keywords:** main function, thread pool, initialization sequence, command line arguments, configuration file, GUI setup, networking, entity management
**Symbols:** main, heap.allocators.deinit, heap.GarbageCollection.assertAllThreadsStopped, initThreadLocals, deinitThreadLocals, threadedIo.init, threadedIo.deinit, log.init, log.deinit, argCheck, args.args.iterateAllocator, std.log.err, std.process.exit, settings.version.version, builtin.os.tag, settings.environment.init, settings.launchConfig.init, headless, gui.initWindowList, gui.deinitWindowList, args.environ.getAlloc, stackAllocator.allocator, files.init, files.deinit, settings.init, settings.deinit, utils.ThreadPool.init, threadPool.deinit, file_monitor.init, file_monitor.deinit, Window.init, Window.deinit, graphics.init, graphics.deinit, audio.init, audio.deinit, utils.initDynamicIntArrayStorage, utils.deinitDynamicIntArrayStorage, rotation.init, rotation.deinit, callbacks.init, block_entity.init, block_entity.deinit, models.init, models.deinit, items.globalInit, items.globalDeinit, sync.client.init, sync.client.deinit, itemdrop.ItemDropRenderer.init, itemdrop.ItemDropRenderer.deinit, assets.init, blocks.meshes.init, blocks.meshes.deinit, renderer.init, renderer.deinit, network.init, network.deinit, entity.client.init, entity.client.deinit, gui.init, particles.ParticleManager.init, particles.ParticleManager.deinit, server.terrain.globalInit, server.startFromExistingThread, heap.GarbageCollection.waitForFreeCompletion, clientMain
**Concepts:** game initialization, thread management, subsystem initialization, configuration handling, headless mode

## Summary
The main function initializes and deinitializes various components of the Cubyz game engine based on command-line arguments and configuration settings.

## Explanation
The main function starts by setting up thread-local storage, logging, and argument checking. It ensures that no command line arguments are provided, directing users to use a configuration file instead. The function initializes global settings, environment variables, and file handling systems. It sets up a thread pool for concurrent operations and initializes various subsystems such as GUI, graphics, audio, models, items, network communication, entity management, and rendering. Depending on whether the game is running in headless mode or not, it initializes additional components like window management, synchronization, item drop rendering, asset loading, block meshing, and particle systems. Finally, it starts either a server or client based on the configuration.

## Code Example
```zig
pub fn main(args: std.process.Init.Minimal) void { // MARK: main()
	defer heap.allocators.deinit();
	defer heap.GarbageCollection.assertAllThreadsStopped();
	initThreadLocals();
	defer deinitThreadLocals();
	threadedIo = .init(globalAllocator.allocator, .{});
	defer threadedIo.deinit();

	log.init();
	defer log.deinit();

	argCheck: {
		var argIterator = args.args.iterateAllocator(stackAllocator.allocator) catch |err| {
			std.log.err("Failed to read command line arguments: {s}", .{@errorName(err)});
			break :argCheck;
		};
		defer argIterator.deinit();
		_ = argIterator.skip();
		if (argIterator.next() != null) {
			std.log.info(
				\\Cubyz does not accept any command line arguments.
				\\All launch-time configuration is done through the "launchConfig.zon" file in the game's working directory. See that file for the available options.
			, .{});
			std.process.exit(0);
		}
	}

	std.log.info("Starting game with version {s}", .{settings.version.version});

	if (builtin.os.tag == .windows) {
		std.log.warn("Cubyz detected it's running on Windows. For optimal performance and reduced power usage please install Linux.", .{});
	}

	settings.environment.init(args.environ);
	settings.launchConfig.init();

	const headless = settings.launchConfig.headlessServer;

	if (!headless) gui.initWindowList();
	defer if (!headless) gui.deinitWindowList();

	{
		const homePath = args.environ.getAlloc(stackAllocator.allocator, if (builtin.os.tag == .windows) "USERPROFILE" else "HOME") catch |err| {
			std.log.err("Failed to get environment variable for home path: {s}", .{@errorName(err)});
			@panic("Failed to get environment variable for home path");
		};
		defer stackAllocator.free(homePath);
		files.init(homePath);
	}
	defer files.deinit();

	settings.init();
	defer settings.deinit();

	threadPool = utils.ThreadPool.init(globalAllocator, settings.cpuThreads orelse @max(1, (std.Thread.getCpuCount() catch 4) -| 1));
	defer threadPool.deinit();

	file_monitor.init();
	defer file_monitor.deinit();

	if (!headless) Window.init();
	defer if (!headless) Window.deinit();

	if (!headless) graphics.init();
	defer if (!headless) graphics.deinit();

	if (!headless) audio.init() catch std.log.err("Failed to initialize audio. Continuing the game without sounds.", .{});
	defer if (!headless) audio.deinit();

	utils.initDynamicIntArrayStorage();
	defer utils.deinitDynamicIntArrayStorage();

	rotation.init();
	defer rotation.deinit();

	callbacks.init();

	block_entity.init();
	defer block_entity.deinit();

	models.init();
	defer models.deinit();

	items.globalInit();
	defer items.globalDeinit();

	if (!headless) sync.client.init();
	defer if (!headless) sync.client.deinit();

	if (!headless) itemdrop.ItemDropRenderer.init();
	defer if (!headless) itemdrop.ItemDropRenderer.deinit();

	assets.init();

	if (!headless) blocks.meshes.init();
	defer if (!headless) blocks.meshes.deinit();

	if (!headless) renderer.init();
	defer if (!headless) renderer.deinit();

	network.init() catch @panic("Failed to initialize network");
	defer network.deinit();

	if (!headless) entity.client.init();
	defer if (!headless) entity.client.deinit();

	if (!headless) gui.init();
	defer if (!headless) gui.deinit();

	if (!headless) particles.ParticleManager.init();
	defer if (!headless) particles.ParticleManager.deinit();

	server.terrain.globalInit();

	if (headless) {
		server.startFromExistingThread(settings.launchConfig.autoEnterWorld, null, .multiplayer);
		heap.GarbageCollection.waitForFreeCompletion();
	} else {
		clientMain();
	}
}
```

## Related Questions
- What is the first step in the game initialization process?
- How does the main function handle command line arguments?
- Which subsystems are initialized when the game runs in headless mode?
- What happens if there is an error getting the environment variable for the home path?
- How many threads are used by default for the thread pool?
- What is the purpose of the `argCheck` block in the main function?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_3*
