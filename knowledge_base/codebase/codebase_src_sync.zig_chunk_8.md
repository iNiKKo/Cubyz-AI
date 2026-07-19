# [hard/codebase_src_sync.zig] - Chunk 8

**Type:** api
**Keywords:** inventory actions, binary serialization, item transfer, server-side logic, world interaction
**Symbols:** DepositOrSwap, DepositOrSwap.dest, DepositOrSwap.source, DepositOrSwap.run, DepositOrSwap.serialize, DepositOrSwap.deserialize, Deposit, Deposit.dest, Deposit.source, Deposit.amount, Deposit.run, Deposit.serialize, Deposit.deserialize, TakeHalf, TakeHalf.dest, TakeHalf.source, TakeHalf.run, TakeHalf.serialize, TakeHalf.deserialize, Drop, Drop.source, Drop.desiredAmount, Drop.run, Drop.serialize, Drop.deserialize
**Concepts:** inventory system, item manipulation, serialization, deserialization

## Summary
Defines actions for depositing, swapping, taking half, and dropping items in an inventory system.

## Explanation
This chunk defines several structs representing different item manipulation actions within an inventory system. Each struct has methods to execute the action (`run`), serialize the action to a binary format (`serialize`), and deserialize the action from a binary format (`deserialize`). The `DepositOrSwap` struct handles depositing or swapping items between two slots, considering stack sizes and permissions. Specifically, it checks if both source and destination slots have non-null items and if they are of the same type. If so, it calculates the amount to transfer based on the available space in the destination slot and the amount in the source slot. The `Deposit` struct specifically handles depositing a specified amount of an item into another slot, ensuring that the destination can accept the item and calculating the actual amount to move based on stack size limits. The `TakeHalf` struct takes half of the items from one slot and places them in another, calculating the desired amount as `(1 + self.source.ref().amount)/2`. The `Drop` struct drops items from the inventory into the world, with server-side handling for position and direction. It calculates the drop direction based on the player's rotation and uses a cooldown to prevent excessive item dropping.

## Code Example
```zig
fn run(self: Deposit, ctx: Context) error{serverFailure}!void {
			if (self.dest.inv.callbacks.canPutInto) |c| if (!c(self.dest.inv.source, self.source.ref().item, self.dest.slot)) return;
			const itemSource = self.source.ref().item;
			if (itemSource == .null) return;
			const itemDest = self.dest.ref().item;
			if (itemDest != .null) {
				if (std.meta.eql(itemDest, itemSource)) {
					if (self.dest.ref().amount >= itemDest.stackSize()) return;
					const amount = @min(itemDest.stackSize() - self.dest.ref().amount, self.source.ref().amount, self.amount);
					ctx.execute(.{.move = .{
						.dest = self.dest,
						.source = self.source,
						.amount = amount,
					}});
				}
			} else {
				const amount = @min(self.amount, self.source.ref().amount);
				ctx.execute(.{.move = .{
					.dest = self.dest,
					.source = self.source,
					.amount = amount,
				}});
			}
		}
```

## Related Questions
- What are the different actions defined in this chunk?
- How does the `DepositOrSwap` struct handle item transfer between slots?
- What is the purpose of the `serialize` method in each struct?
- How does the `Drop` action interact with the server and world?
- What conditions must be met for an item to be swapped using `DepositOrSwap`?
- How is the amount of items determined when performing a 'take half' action?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_8*
