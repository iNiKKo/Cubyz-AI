# [hard/codebase_src_Inventory.zig] - Chunk 6

**Type:** implementation
**Keywords:** binary serialization, varInt encoding, enum IDs, stack merging, size limit, callbacks, provider union, NeverFailingAllocator, sync.Command.BaseOperation, context execution
**Symbols:** Inventories, Inventories.init, Inventories.initFromClientInventories, Inventories.fromBytes, Inventories.deinit, Inventories.toBytes, Inventories.canHold, Inventories.Provider, Inventories.Provider.getBaseOperation, Inventories.Provider.getItem, Inventories.putItemsInto
**Concepts:** serialization, networking, api, implementation

## Summary
Implements the Inventory system with serialization, client-side inventory handling, provider-based item movement logic, and slot-level callbacks for custom put rules.

## Explanation
The chunk defines BagInventory as a stackable-slot container with toBytes/push/pop/peek methods; push merges matching stacks up to remaining space or sizeLimit. Inventories is an array of Inventory with init/initFromClientInventories/fromBytes/deinit/toBytes for binary serialization using varInt counts and enum IDs, returning error.Invalid on malformed data. canHold iterates inventories delegating to each dest.canHold and returns .yes/.remainingAmount. Provider is a union(enum) {move, create, bag} with getBaseOperation/getItem producing sync.Command.BaseOperation (move/create/takeFromBag). putItemsInto walks self.inventories, respects dest.callbacks.canPutInto, finds empty slots, merges matching items, executes provider operations via ctx.execute, and breaks when remainingAmount reaches zero. The code uses NeverFailingAllocator for dupe/alloc/free patterns.

## Related Questions
- How does Inventories.fromBytes handle malformed binary data?
- What error is returned when an inventory count exceeds remaining bytes?
- How are client inventories converted to server Inventory objects?
- What happens if dest.callbacks.canPutInto returns false for a slot?
- How does putItemsInto decide which provider operation to execute?
- Is the Provider union exhaustive or can it be extended?
- Where is memory allocated for Inventories.inventories and how is it freed?
- Does fromBytes use errdefer for cleanup on early return?
- What is the purpose of dest._items in putItemsInto?
- How does push handle merging when stack size limit is reached?
- Can canHold be called concurrently across multiple threads?
- Is Inventories.toBytes deterministic given identical input arrays?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_6*
