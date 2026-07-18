# [hard/codebase_src_server_server.zig] - Chunk 0

**Type:** implementation
**Keywords:** circular buffer, history management, clipboard operations, blueprint storage, selection tracking
**Symbols:** WorldEditData, WorldEditData.maxWorldEditHistoryCapacity, WorldEditData.selectionPosition1, WorldEditData.selectionPosition2, WorldEditData.clipboard, WorldEditData.undoHistory, WorldEditData.redoHistory, WorldEditData.mask, WorldEditData.History, WorldEditData.History.changes, WorldEditData.History.Value, WorldEditData.History.Value.blueprint, WorldEditData.History.Value.position, WorldEditData.History.Value.message, WorldEditData.History.Value.init, WorldEditData.History.Value.deinit, WorldEditData.History.Value.selection, WorldEditData.History.init, WorldEditData.History.deinit, WorldEditData.History.clear, WorldEditData.History.push, WorldEditData.History.pop, WorldEditData.init, WorldEditData.deinit, BlockUpdateSystem, world_zig, terrain, Entity, SimulationChunk, storage, permission, command
**Concepts:** world editing, undo/redo history, clipboard management, blueprint application, mask handling

## Summary
Defines the WorldEditData structure and its associated History struct for managing world editing operations in a server environment.

## Explanation
The chunk defines the `WorldEditData` structure, which is used to manage world editing operations such as selection, clipboard storage, undo/redo history, and mask application. The `History` struct within `WorldEditData` manages a circular buffer queue of changes, each represented by a `Value` struct containing a blueprint, position, and message. Functions like `init`, `deinit`, `clear`, `push`, and `pop` are provided for managing the history and clipboard operations. The chunk also imports various modules necessary for handling network connections, entity management, world simulation, storage, permissions, commands, blueprints, masks, and utility functions.

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
- How does the WorldEditData structure handle blueprint storage and application?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_0*
