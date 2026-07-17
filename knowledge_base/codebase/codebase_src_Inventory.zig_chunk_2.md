# [hard/codebase_src_Inventory.zig] - Chunk 2

**Type:** api
**Keywords:** mutex locking, user permissions, inventory sources, thread safety, command execution
**Symbols:** inventoryCreationMutex, createInventory, closeInventory, getInventory, getInventoryFromSource, getInventoryFromId, getServerInventory, clearPlayerInventory, tryCollectingToPlayerInventory
**Concepts:** entity ECS, inventory management, multiplayer synchronization

## Summary
Handles inventory creation, management, and access control in a multiplayer environment.

## Explanation
This chunk manages the lifecycle of inventories in a Cubyz server. It includes functions for creating, closing, and accessing inventories based on user permissions and inventory sources. The `createInventory` function initializes new inventories with appropriate callbacks and ensures that only authorized users can access certain types of inventories. The `closeInventory` function removes users from an inventory when they disconnect or close it. The `getInventory` and related functions retrieve inventory instances by various identifiers, ensuring thread safety with mutex locks. Additional functions like `clearPlayerInventory` and `tryCollectingToPlayerInventory` handle specific inventory operations such as clearing all items for a player or collecting dropped items into a player's inventory.

## Code Example
```zig
pub fn closeInventory(user: *main.server.User, clientId: InventoryId) !void {
	sync.threadContext.assertCorrectContext(.server);
	const serverId = user.inventoryClientToServerIdMap.get(clientId) orelse return error.InventoryNotFound;
	inventories.items()[@intFromEnum(serverId)].removeUser(user, clientId);
}
```

## Related Questions
- How does the `createInventory` function ensure that only authorized users can access certain types of inventories?
- What is the purpose of the `inventoryCreationMutex` in this chunk?
- How does the `getInventoryFromSource` function retrieve an inventory by its source?
- What operations are performed when a player's inventory is cleared using `clearPlayerInventory`?
- How does the `tryCollectingToPlayerInventory` function handle item collection into a player's inventory?
- What is the role of the `getInventory` function in this chunk?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_2*
