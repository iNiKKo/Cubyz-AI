# [hard/codebase_src_block_entity.zig] - Chunk 0

**Type:** implementation
**Keywords:** vtable, mutex locking, enum, struct, thread safety, lifecycle callbacks
**Symbols:** UpdateEvent, ErrorSet, BlockEntityType, BlockEntityType.id, BlockEntityType.vtable, BlockEntityType.VTable.onLoadClient, BlockEntityType.VTable.onUnloadClient, BlockEntityType.VTable.onLoadServer, BlockEntityType.VTable.onUnloadServer, BlockEntityType.VTable.onStoreServerToDisk, BlockEntityType.VTable.onStoreServerToClient, BlockEntityType.VTable.updateClientData, BlockEntityType.VTable.updateServerData, BlockEntityType.VTable.getServerToClientData, BlockEntityType.VTable.getClientToServerData, BlockEntity, BlockEntity.noValue, BlockEntity.freeIndexList, BlockEntity.nextIndex, BlockEntity.mutex, BlockEntity.globalDeinit, BlockEntity.reset, BlockEntity.create, BlockEntity.destroy, BlockEntityDataStorage
**Concepts:** entity ECS, block entity management

## Summary
Defines block entity types and their lifecycle management in the Cubyz engine.

## Explanation
This chunk defines the `BlockEntityType` struct, which represents different types of block entities with a vtable for various lifecycle callbacks. It also defines the `BlockEntity` enum to manage unique identifiers for block entities, including methods for creating and destroying them. Additionally, it provides a generic `BlockEntityDataStorage` template for storing data associated with block entities, ensuring thread safety with mutexes.

## Code Example
```zig
pub inline fn onLoadClient(self: *const BlockEntityType, pos: Vec3i, chunk: *Chunk, reader: *BinaryReader) ErrorSet!void {
	return self.vtable.onLoadClient(pos, chunk, reader);
}
```

## Related Questions
- What is the purpose of the `BlockEntityType` struct?
- How are block entities created and destroyed in this code?
- What methods are available for handling block entity data storage?
- How does the code ensure thread safety when managing block entities?
- What lifecycle callbacks are defined for block entities?
- How is the `UpdateEvent` union used in the code?

*Source: unknown | chunk_id: codebase_src_block_entity.zig_chunk_0*
