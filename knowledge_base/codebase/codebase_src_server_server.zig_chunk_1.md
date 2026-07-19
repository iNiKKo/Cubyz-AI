# [hard/codebase_src_server_server.zig] - Chunk 1

**Type:** implementation
**Keywords:** reference counting, user state, connection management, inventory, permissions
**Symbols:** User, User.maxSimulationDistance, User.simulationSize, User.simulationMask, User.conn, User.innerPlayer, User.timeDifference, User.interpolation, User.lastTime, User.lastSaveTime, User.name, User.renderDistance, User.clientUpdatePos, User.receivedFirstEntityData, User.isLocal, User.id, User.loadedChunks, User.lastRenderDistance, User.lastPos, User.gamemode, User.spawnPos, User.worldEditData, User.playerIndex, User.jobQueue, User.jobQueueScheduled, User.jobQueueLastUpdate, User.lastSentBiomeId, User.newKeyString, User.key, User.legacyKey, User.inventoryClientToServerIdMap, User.inventory, User.handInventory, User.connected, User.state, User.refCount, User.mutex, User.inventoryCommands, User.permissions, User.State, User.player, User.initAndIncreaseRefCount, User.@continue, User.deinit, User.pause, User.increaseRefCount, User.decreaseRefCount, User.identifyFromKeysAndName
**Concepts:** player management, connection handling, inventory system, permissions, job scheduling

## Summary
The `User` struct manages player state and interactions within the server, including initialization, deinitialization, reference counting, and state transitions.

## Explanation
The `User` struct manages player state and interactions within the server, including initialization, deinitialization, reference counting, and state transitions. It contains several important fields such as connection details (`conn`), player attributes (`innerPlayer`, `timeDifference`, etc.), inventory management (`inventoryClientToServerIdMap`, `inventory`, `handInventory`), permissions (`permissions`), job scheduling (`jobQueue`, `jobQueueLastUpdate`), and more. The struct provides methods for initializing (`initAndIncreaseRefCount`), continuing (`@continue`), deinitializing (`deinit`), pausing (`pause`), increasing (`increaseRefCount`), and decreasing (`decreaseRefCount`) reference counts. It also handles key identification (`identifyFromKeysAndName`). Constants like `maxSimulationDistance`, `simulationSize`, and `simulationMask` are defined as follows: `const maxSimulationDistance = 8; const simulationSize = 2 * maxSimulationDistance; const simulationMask = simulationSize - 1;`. The `User` struct interacts with various components like the connection manager, inventory system, permissions, and world data. The jobQueueScheduled field is a boolean indicating whether the job queue has been scheduled. The User.State enum includes states such as awaitingKeyVerification, connectedVerified, and awaitingReloadVerified.

## Code Example
```zig
pub fn player(self: *User) *Entity {
	return &self.innerPlayer;
}
```

## Related Questions
- What are the values of constants such as maxSimulationDistance, simulationSize, and simulationMask?
- How does the User struct handle reference counting?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_1*
