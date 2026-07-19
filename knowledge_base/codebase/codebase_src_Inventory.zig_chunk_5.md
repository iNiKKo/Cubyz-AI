# [hard/codebase_src_Inventory.zig] - Chunk 5

**Type:** api
**Keywords:** inventory, stacking, serialization, binary format, allocator
**Symbols:** BagInventory, BagInventory.sizeLimit, BagInventory.slots, BagInventory.init, BagInventory.deinit, BagInventory.fromBytes, BagInventory.toBytes, BagInventory.push, BagInventory.pop, BagInventory.peek
**Concepts:** inventory management, item stacking, serialization

## Summary
Defines the BagInventory struct for managing an inventory with a size limit and item slots.

## Explanation
The BagInventory struct manages an inventory system with a specified size limit (`sizeLimit`) and a list of item stacks (`slots`). It includes methods for initialization (`init`), deinitialization (`deinit`), serialization (from/to bytes) using `fromBytes` and `toBytes`, adding items (`push`), removing items (`pop`), and peeking at items without removing them (`peek`).

The `init` method initializes a BagInventory instance with a given size limit and allocator. The `deinit` method deinitializes the BagInventory by deallocating all item stacks and the slots list.

Serialization is handled by the `fromBytes` and `toBytes` methods. `fromBytes` reads a variable-length integer representing the number of items, followed by each item's data. `toBytes` writes the number of items as a variable-length integer, followed by each item's serialized data.

The `push` method adds an item stack to the inventory. If the last item in the slots list is the same type as the new item, it combines them up to the maximum stack size (`stackSize`). If the inventory is full or the item cannot be combined, the remaining amount is returned.

The `pop` method removes and returns the top item from the inventory. The `peek` method returns the item at a specified offset from the top without removing it.

## Code Example
```zig
pub fn deinit(self: BagInventory) void {
	for (self.slots.items) |*item| {
		item.deinit();
	}
	self.slots.deinit();
}
```

## Related Questions
- What is the purpose of the `BagInventory` struct?
- How does the `push` method handle item stacking?
- What does the `deinit` method do for a BagInventory instance?
- How are items serialized and deserialized in BagInventory?
- What is the role of the `sizeLimit` field in BagInventory?
- How does the `peek` method work in BagInventory?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_5*
