# [hard/codebase_src_server_server.zig] - Chunk 5

**Type:** implementation
**Keywords:** world generation, user references, connection manager, entity list, initialization, deinitialization
**Symbols:** updatesPerSec, updateTime, world, userMutex, users, userDeinitList, userConnectList, connectionManager, running, restart, lastTime, thread, init, deinit, getUserListAndIncreaseRefCount, freeUserListAndDecreaseRefCount, getInitialEntityList
**Concepts:** server world management, user management, connection handling, entity synchronization

## Summary
This chunk manages the initialization and deinitialization of a server world, including user management, connection handling, and entity synchronization.

## Explanation
This chunk manages the initialization and deinitialization of a server world, including user management, connection handling, and entity synchronization. It defines constants such as `updatesPerSec` which is set to 20 updates per second, and `updateTime`, which is calculated based on nanoseconds (1000000000/20). The chunk sets up essential components like the world generation, user management, and connection manager. It initializes the server world with specific configurations and handles deinitialization by pausing the connection manager and thread pool, clearing user lists, and freeing resources such as the world arena.

The `init` function creates a world using the provided name and mode, generates it, and starts the connection manager. The `deinit` function pauses all necessary components, clears user lists, deinitializes the world, and frees allocated memory. User references are managed through methods like `getUserListAndIncreaseRefCount`, which increases reference counts for users, and `freeUserListAndDecreaseRefCount`, which decreases them safely.

The `getInitialEntityList` function prepares an initial list of entities by appending null and item drop lists to a main.ZonElement array, then converting it into a string format suitable for synchronization.

## Code Example
```zig
fn deinit() void {
	connectionManager.pause();
	main.threadPool.pause();
	defer main.threadPool.@"continue"();

	main.threadPool.unschedulePlayers();

	users.clearAndFree();

	while (userDeinitList.popFront()) |user| {
		user.clearJobQueue();
		if (user.refCount.load(.monotonic) == 1) {
			user.decreaseRefCount();
		} else {
			std.log.err("Leaked user {f}", .{user});
			user.pause();
			user.deinit();
		}
	}

	if (world) |_world| {
		_world.deinit();
	}
	world = null;

	main.sync.server.deinit();
	main.items.Inventory.server.deinit();
	main.entity.server.deinit();

	command.deinit();

	main.heap.allocators.destroyWorldArena();
}
```

## Related Questions
- What is the value of updatesPerSec?
- How is updateTime calculated?
- How does the init function create and generate the world?
- What steps are involved in deinitializing the server world?
- How are user references managed during initialization and deinitialization?
- What role does the connection manager play in this code?
- How is the initial entity list prepared for synchronization?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_5*
