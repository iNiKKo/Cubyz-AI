# [hard/codebase_src_block_entity.zig] - Chunk 0

**Type:** api
**Keywords:** vtable, mutex locking, enum management, error handling, thread safety
**Symbols:** UpdateEvent, ErrorSet, BlockEntityType, BlockEntityType.id, BlockEntityType.vtable, BlockEntityType.VTable.onLoadClient, BlockEntityType.VTable.onUnloadClient, BlockEntityType.VTable.onLoadServer, BlockEntityType.VTable.onUnloadServer, BlockEntityType.VTable.onStoreServerToDisk, BlockEntityType.VTable.onStoreServerToClient, BlockEntityType.VTable.updateClientData, BlockEntityType.VTable.updateServerData, BlockEntityType.VTable.getServerToClientData, BlockEntityType.VTable.getClientToServerData, BlockEntity, BlockEntity.noValue, BlockEntity.freeIndexList, BlockEntity.nextIndex, BlockEntity.mutex
**Concepts:** entity ECS, block entity management

## Summary
Defines block entity types and management in the Cubyz engine.

## Explanation
This chunk defines the `BlockEntityType` struct which represents different types of block entities with a vtable for various lifecycle methods. It also defines the `BlockEntity` enum for managing unique block entity indices, including functions for creating and destroying block entities. The code includes mutex locking for thread safety in index management.

## Code Example
```zig
pub inline fn onLoadClient(self: *const BlockEntityType, pos: Vec3i, chunk: *Chunk, reader: *BinaryReader) ErrorSet!void {
	return self.vtable.onLoadClient(pos, chunk, reader);
}
```

## Related Questions
- What is the purpose of the `BlockEntityType` struct?
- How are block entities managed in terms of creation and destruction?
- What methods does the `BlockEntity` enum provide for managing indices?
- How is thread safety ensured in block entity index management?
- What is the role of the vtable in `BlockEntityType`?
- How are errors handled in the lifecycle methods of `BlockEntityType`?

*Source: unknown | chunk_id: codebase_src_block_entity.zig_chunk_0*
