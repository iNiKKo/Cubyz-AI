# [hard/codebase_src_server_server.zig] - Chunk 6

**Type:** implementation
**Keywords:** thread management, user list, network protocols, entity synchronization, biome data
**Symbols:** update, startFromNewThread, startFromExistingThread, StopType, stop, disconnect
**Concepts:** server management, user connection handling, network communication, world updates

## Summary
Handles server updates, user management, and network communication.

## Explanation
This chunk contains the main logic for updating the server state, managing connected users, and sending/receiving network data. The `update` function processes world updates, entity positions, and biome changes. It also handles user connection and disconnection events. The `startFromNewThread` and `startFromExistingThread` functions initialize the server on a new or existing thread, respectively. The `stop` function stops the server, optionally restarting it. The `disconnect` function disconnects a user from the server.

## Code Example
```zig
fn update() void { // MARK: update()
	world.?.update();
	main.entity.server.update();

	while (userConnectList.popFront()) |user| {
		connectInternal(user);
		user.decreaseRefCount();
	}

	const userList = getUserListAndIncreaseRefCount(main.stackAllocator);
	defer freeUserListAndDecreaseRefCount(main.stackAllocator, userList);
	for (userList) |user| {
		user.update();
	}

	// Send the entity data:
	const itemData = world.?.itemDropManager.getPositionAndVelocityData(main.stackAllocator);
	defer main.stackAllocator.free(itemData);

	var entityData: main.ListManaged(main.entity.EntityNetworkData) = .init(main.stackAllocator);
	defer entityData.deinit();

	for (userList) |user| {
		const id = user.id; // TODO
		entityData.append(.{
			.id = id,
			.pos = user.player().pos,
			.vel = user.player().vel,
			.rot = user.player().rot,
		});
	}
	for (userList) |user| {
		main.network.protocols.entityPosition.send(user.conn, user.player().pos, entityData.items, itemData);
	}

	for (userList) |user| {
		const pos = @as(Vec3i, @trunc(user.player().pos));
		const biomeId = world.?.getBiome(pos[0], pos[1], pos[2]).paletteId;
		if (biomeId != user.lastSentBiomeId) {
			user.lastSentBiomeId = biomeId;
			main.network.protocols.genericUpdate.sendBiome(user.conn, biomeId);
		}
	}

	while (userDeinitList.popFront()) |user| {
		if (user.refCount.load(.monotonic) == 1) {
			user.decreaseRefCount();
		} else {
			userDeinitList.pushBack(user);
			break;
		}
	}
}
```

## Related Questions
- What is the primary function of the `update` method?
- How does the server handle user connections and disconnections?
- What network protocols are used for communication in this chunk?
- How is the server initialized on a new thread?
- What steps are taken to ensure proper cleanup when stopping the server?
- How is entity position data synchronized across users?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_6*
