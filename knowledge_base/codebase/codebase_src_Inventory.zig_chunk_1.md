# [hard/codebase_src_Inventory.zig] - Chunk 1

**Type:** api
**Keywords:** ServerInventory, addUser, removeUser, inventoryCreationMutex, VirtualList, externallyManaged, onFirstOpenCallback, onLastCloseCallback, disconnectUser, nextId, freeIdList
**Symbols:** ServerInventory, addUser, removeUser, inventories, maxId, freeIdList, inventoryCreationMutex, init, deinit, disconnectUser, nextId, freeId, createExternallyManagedInventory, destroyExternallyManagedInventory, destroyAndDropExternallyManagedInventory, createInventory
**Concepts:** inventory management, user association, ID allocation, mutex protection, callbacks, serialization, thread context assertions, virtual list storage

## Summary
Server-side inventory management system handling user association, ID allocation, creation/destruction of inventories with callbacks and mutex protection.

## Explanation
This chunk defines ServerInventory struct methods addUser and removeUser which manage the mapping between users and inventory IDs using a threadContext assertion for server context. The addUser method appends to self.users list, updates user.inventoryClientToServerIdMap, and triggers onFirstOpenCallback when first user is added. The removeUser method searches for matching user, swaps removes from list, asserts map consistency, triggers onLastCloseCallback when last user removed, and if internallyManaged calls deinit under mutex lock. Global state includes inventories VirtualList, maxId enum counter, freeIdList for recycling IDs, and inventoryCreationMutex protecting ID operations. init() initializes the inventories list. deinit() iterates all inventories logging leaks if source != alreadyFreed, asserts freeIdList is empty, clears it, deinits inventories, resets maxId. disconnectUser loops over user.inventoryClientToServerIdMap keyIterator closing each associated inventory via closeInventory (unreachable on failure). nextId acquires mutex, pops from freeIdList or increments maxId and adds to inventories list, returning the new ID. freeId appends an ID to freeIdList under mutex. createExternallyManagedInventory locks mutex, calls ServerInventory.init with externallyManaged flag, stores in inventories array by ID, deserializes data via fromBytes, returns ID. destroyExternallyManagedInventory switches on threadContext allowing server or chunkDeiniting (asserting no users remain), asserts managed == externallyManaged, locks mutex, deinits inventory. destroyAndDropExternallyManagedInventory asserts server context and externallyManaged, iterates inv.inv._items dropping zero-amount stacks to world via main.server.world.drop with random offset, clears itemStack, deinits under mutex. createInventory asserts server context, initializes empty callbacks, handles blockInventory/playerInventory/hand sources by checking user.id against id for playerInventory/hand logging error.Invalid if mismatch, locks mutex and searches inventories for matching source adding user or returning error.Invalid; workbench case is incomplete in this chunk.

## Related Questions
- What thread context does addUser assert and why?
- How is the first user added to an inventory detected?
- Which callback fires when a server inventory has exactly one user?
- What happens to internallyManaged inventories when all users are removed?
- How does disconnectUser iterate over a user's inventory associations?
- Where are new inventory IDs sourced from before allocation?
- What invariant is checked in destroyExternallyManagedInventory for thread context?
- Why does createInventory return error.Invalid for blockInventory sources?
- How is data deserialized into an externally managed inventory?
- What world operation drops items when destroying an externally managed inventory at a position?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_1*
