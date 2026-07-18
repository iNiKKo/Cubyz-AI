# [hard/codebase_src_server_server.zig] - Chunk 0

**Type:** implementation
**Keywords:** circular buffer, history management, clipboard operations, blueprint storage, selection tracking
**Symbols:** WorldEditData, WorldEditData.maxWorldEditHistoryCapacity, WorldEditData.selectionPosition1, WorldEditData.selectionPosition2, WorldEditData.clipboard, WorldEditData.undoHistory, WorldEditData.redoHistory, WorldEditData.mask, WorldEditData.History, WorldEditData.History.changes, WorldEditData.History.Value, WorldEditData.History.Value.blueprint, WorldEditData.History.Value.position, WorldEditData.History.Value.message, WorldEditData.History.Value.init, WorldEditData.History.Value.deinit, WorldEditData.History.Value.selection, WorldEditData.History.init, WorldEditData.History.deinit, WorldEditData.History.clear, WorldEditData.History.push, WorldEditData.History.pop, WorldEditData.init, WorldEditData.deinit, BlockUpdateSystem, world_zig, terrain, Entity, SimulationChunk, storage, permission, command
**Concepts:** world editing, undo/redo history, clipboard management, blueprint application, mask handling

## Summary
Defines the WorldEditData structure and its associated History struct for managing world editing operations in a server environment.

## Explanation
Defines the `WorldEditData` structure and its associated `History` struct for managing world editing operations in a server environment. The `maxWorldEditHistoryCapacity` is set to 1024, which limits the capacity of the circular buffer queue used by the history management system. The `WorldEditData` structure includes fields such as `selectionPosition1`, `selectionPosition2`, `clipboard`, `undoHistory`, and `redoHistory`. Each change in the undo/redo history is represented by a `Value` struct containing a blueprint, position, and message. Functions like `init`, `deinit`, `clear`, `push`, and `pop` are provided for managing clipboard operations, memory management within the History struct, and handling selection positions. The chunk also imports various modules necessary for network connections, entity management, world simulation, storage, permissions, commands, blueprints, masks, and utility functions.

## Code Example
```zig
pub fn init(blueprint: Blueprint, position: Vec3i, message: []const u8) Value {
	return .{.blueprint = blueprint, .position = position, .message = main.globalAllocator.dupe(u8, message)};
}
```

## Related Questions
- What is the maximum capacity of the world edit history?
- How does the WorldEditData structure manage clipboard operations?
- What functions are available for managing the undo/redo history in WorldEditData?
- How is memory managed within the History struct of WorldEditData?
- What is the purpose of the selectionPosition1 and selectionPosition2 fields in WorldEditData?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_0*
