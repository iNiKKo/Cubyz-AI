# [hard/codebase_src_Inventory.zig] - Chunk 0

**Type:** implementation
**Keywords:** inventory ID, mutex locking, hash map, callback handling, user tracking
**Symbols:** InventoryId, client, client.maxId, client.freeIdList, client.serverToClientMap, client.init, client.deinit, client.nextId, client.freeId, client.mapServerId, client.unmapServerId, client.unmapServerIdByClientId, client.getInventory, client.getInventoryByClientId, server, server.ServerInventory, server.ServerInventory.inv, server.ServerInventory.users, server.ServerInventory.source, server.ServerInventory.managed, server.ServerInventory.Managed, server.ServerInventory.init, server.ServerInventory.deinit, server.ServerInventory.addUser, server.ServerInventory.removeUser
**Concepts:** inventory management, client-server synchronization, user management

## Summary
The chunk defines inventory management logic for both client and server sides, including ID mapping, initialization, deinitialization, and user management.

## Explanation
This chunk contains the implementation of inventory management systems for both the client and server. It includes structures like `InventoryId`, `client`, and `server`. The `client` struct manages inventory IDs, maps server IDs to client inventories, and provides functions to initialize, deinitialize, and manage these mappings. The `server` struct defines a `ServerInventory` which holds an inventory, user information, and source details. It includes methods for initializing and deinitializing the server inventory, adding and removing users, and handling callbacks when the first or last user opens or closes the inventory.

## Code Example
```zig
pub fn init() void {
	serverToClientMap = .init(main.globalAllocator.allocator);
}
```

## Related Questions
- How does the client manage inventory IDs?
- What is the purpose of the `mapServerId` function in the client struct?
- How are users added and removed from a server inventory?
- What happens when the last user closes an inventory on the server side?
- How is the `serverToClientMap` initialized and deinitialized?
- What role does the `Managed` enum play in the `ServerInventory` struct?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_0*
