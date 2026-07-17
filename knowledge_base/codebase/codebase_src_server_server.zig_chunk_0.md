# [hard/codebase_src_server_server.zig] - Chunk 0

**Type:** implementation
**Keywords:** circular buffer, atomic operations, mutex locking, inventory mapping, permission handling
**Symbols:** WorldEditData, WorldEditData.maxWorldEditHistoryCapacity, WorldEditData.selectionPosition1, WorldEditData.selectionPosition2, WorldEditData.clipboard, WorldEditData.undoHistory, WorldEditData.redoHistory, WorldEditData.mask, WorldEditData.History, WorldEditData.History.changes, WorldEditData.History.Value, WorldEditData.History.Value.blueprint, WorldEditData.History.Value.position, WorldEditData.History.Value.message, WorldEditData.History.Value.init, WorldEditData.History.Value.deinit, WorldEditData.History.Value.selection, WorldEditData.History.init, WorldEditData.History.deinit, WorldEditData.History.clear, WorldEditData.History.push, WorldEditData.History.pop, WorldEditData.init, WorldEditData.deinit, User, User.maxSimulationDistance, User.simulationSize, User.simulationMask, User.conn, User.innerPlayer, User.timeDifference, User.interpolation, User.lastTime, User.lastSaveTime, User.name, User.renderDistance, User.clientUpdatePos, User.receivedFirstEntityData, User.isLocal, User.id, User.loadedChunks, User.lastRenderDistance, User.lastPos, User.gamemode, User.spawnPos, User.worldEditData, User.playerIndex, User.jobQueue, User.jobQueueScheduled, User.jobQueueLastUpdate, User.lastSentBiomeId, User.newKeyString, User.key, User.legacyKey, User.inventoryClientToServerIdMap, User.inventory, User.handInventory, User.connected, User.state, User.refCount, User.mutex, User.inventoryCommands, User.permissions, BlockUpdateSystem, world_zig, terrain, Entity, SimulationChunk, storage, permission, command
**Concepts:** world editing, user management, inventory system, permissions, concurrency control

## Summary
Defines the `WorldEditData` and `User` structs for server-side world editing and user management.

## Explanation
The chunk defines two main structures: `WorldEditData` and `User`. The `WorldEditData` struct manages world editing operations, including selection positions, clipboard content, undo/redo history, and a mask. It includes nested `History` and `Value` structs for managing changes with circular buffer queues. The `User` struct represents server-side user data, including connection details, player state, loaded chunks, gamemode, inventory management, and permissions. It also manages concurrency through job queues and synchronization using mutexes.

## Related Questions
- What is the maximum capacity of the world edit history?
- How does the `WorldEditData` struct manage clipboard content?
- What fields are included in the `User` struct?
- How is concurrency managed within the `User` struct?
- What is the purpose of the `simulationMask` constant in the `User` struct?
- How does the `History` struct handle memory management for stored changes?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_0*
