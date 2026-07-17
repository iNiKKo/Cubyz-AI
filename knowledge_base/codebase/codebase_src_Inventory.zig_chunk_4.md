# [hard/codebase_src_Inventory.zig] - Chunk 4

**Type:** api
**Keywords:** inventory, ItemStack, allocator, freeId, source, callbacks, union, enum, deinit, size, getItem, getStack, canHold, remainingAmount
**Symbols:** Inventory, CanHoldReturn, _init, _deinit, size, getItem, getStack, getAmount, canHold
**Concepts:** inventory management, item stack handling, client server ID allocation, memory allocation deallocation, capacity checking

## Summary
Inventory module defines the core inventory data structure and public API for depositing items, crafting, placing/breaking blocks, and querying stack contents.

## Explanation
The chunk declares a top-level struct Inventory with fields id (InventoryId), _items ([]ItemStack), source (Source), and callbacks (Callbacks). It provides an initializer _init that allocates the item array via allocator.alloc(ItemStack, _size) and assigns an ID based on sync.Side (client.nextId() or server.nextId()). The deinitializer _deinit frees IDs back to client.freeId/server.freeId, calls deinit on each ItemStack, and releases the allocated array. Accessor methods size, getItem, getStack, and getAmount delegate to self._items.len and self._items[slot].item/amount respectively. A union CanHoldReturn is defined with variants yes (void) and remainingAmount (u16). The canHold function checks if sourceStack.amount == 0 returning .yes; otherwise it computes remaining amount by subtracting the inventory's current capacity from sourceStack.amount, clamping to zero if negative.

## Related Questions
- What is the type of Inventory.id and how are client versus server IDs allocated?
- How does _init allocate the internal item array and what happens to each ItemStack element after allocation?
- What is the purpose of the callbacks field in Inventory and when is it invoked?
- Describe the behavior of canHold when sourceStack.amount equals zero.
- If sourceStack.amount exceeds remaining capacity, how is remainingAmount computed and clamped?
- What does _deinit do for each item in self._items before freeing the array?
- How are IDs freed back to the client or server during deinitialization?
- Which accessor methods delegate directly to self._items without additional logic?
- Is CanHoldReturn a public union and what variants does it expose?
- What is the signature of Inventory.size and how does it relate to _items.len?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_4*
