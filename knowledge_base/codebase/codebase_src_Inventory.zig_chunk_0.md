# [hard/codebase_src_Inventory.zig] - Chunk 0

**Type:** implementation
**Keywords:** mutex locking, ID management, map operations, resource cleanup, assertions
**Symbols:** InventoryId, client, client.maxId, client.freeIdList, client.serverToClientMap, client.init, client.deinit, client.nextId, client.freeId, client.mapServerId, client.unmapServerId, client.unmapServerIdByClientId, client.getInventory, client.getInventoryByClientId
**Concepts:** inventory management, ID allocation, thread safety, server-client mapping

## Summary
Manages client-side inventory mappings and ID allocation.

## Explanation
This chunk defines the client-side logic for managing inventories, including ID allocation, mapping between server and client IDs, and retrieving inventory instances. It uses a mutex to ensure thread safety during operations that modify shared state like `maxId`, `freeIdList`, and `serverToClientMap`. The `init` function initializes the map, while `deinit` ensures proper cleanup by asserting no leaks and freeing resources. The `nextId` function allocates new inventory IDs, either from a free list or by incrementing `maxId`. `freeId` returns an ID to the free list. `mapServerId` associates server IDs with client-side inventory instances, while `unmapServerId` removes this association. `getInventory` and `getInventoryByClientId` retrieve inventories based on server or client IDs, respectively.

## Code Example
```zig
pub fn init() void {
	serverToClientMap = .init(main.globalAllocator.allocator);
}
```

## Related Questions
- How is the `InventoryId` enum defined?
- What does the `client.init` function do?
- How are inventory IDs allocated in this chunk?
- What is the purpose of the `freeIdList` variable?
- How does the `mapServerId` function work?
- What assertion is made during the `deinit` process?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_0*
