# [hard/codebase_src_Inventory.zig] - Chunk 7

**Type:** api
**Keywords:** inventory operations, item addition, item removal, stack size, callbacks
**Symbols:** putItemsInto, removeItems
**Concepts:** inventory management, item stacking, callback constraints

## Summary
Handles inventory operations such as adding and removing items.

## Explanation
The chunk defines methods for managing item inventories. The `putItemsInto` function attempts to add a specified amount of items from a provider into the available slots in the inventories, respecting constraints like stack sizes and callbacks. It returns the remaining amount that could not be added. The `removeItems` function removes a specified amount of a base item from the inventories, executing delete operations on the context for each removal.

## Code Example
```zig
pub fn putItemsInto(self: Inventories, ctx: sync.Command.Context, itemAmount: u16, provider: Provider) u16 {
	const item = provider.getItem();
	var remainingAmount = itemAmount;
	var selectedEmptySlot: ?u32 = null;
	var selectedEmptyInv: ?Inventory = null;

	outer: for (self.inventories) |dest| {
		var emptySlot: ?u32 = null;
		var hasItem = false;
		for (dest._items, 0..) |*destStack, destSlot| {
			if (dest.callbacks.canPutInto) |c| if (!c(dest.source, item, destSlot)) continue;
			if (destStack.item == .null and emptySlot == null) {
				emptySlot = @intCast(destSlot);
				if (selectedEmptySlot == null) {
					selectedEmptySlot = emptySlot;
					selectedEmptyInv = dest;
				}
			}
			if (std.meta.eql(destStack.item, item)) {
				hasItem = true;
				const amount = @min(item.stackSize() - destStack.amount, remainingAmount);
				if (amount == 0) continue;
				ctx.execute(provider.getBaseOperation(.{.inv = dest, .slot = @intCast(destSlot)}, amount));
				remainingAmount -= amount;
				if (remainingAmount == 0) break :outer;
			}
		}
		if (emptySlot != null and hasItem) {
			ctx.execute(provider.getBaseOperation(.{.inv = dest, .slot = emptySlot.?}, remainingAmount));
			remainingAmount = 0;
			break :outer;
		}
	}
	if (remainingAmount > 0 and selectedEmptySlot != null) {
		ctx.execute(provider.getBaseOperation(.{.inv = selectedEmptyInv.?, .slot = selectedEmptySlot.?}, remainingAmount));
		remainingAmount = 0;
	}
	return remainingAmount;
}
```

## Related Questions
- How does the `putItemsInto` function determine where to place items?
- What happens if there is not enough space for all items in the inventories?
- Can you explain how the `removeItems` function handles removing items from the inventory?
- What role do callbacks play in the inventory operations?
- How does the chunk handle partial item additions or removals?
- What is the purpose of the `selectedEmptySlot` and `selectedEmptyInv` variables?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_7*
