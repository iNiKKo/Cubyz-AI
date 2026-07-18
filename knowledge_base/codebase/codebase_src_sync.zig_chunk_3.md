# [hard/codebase_src_sync.zig] - Chunk 3

**Type:** serialization
**Keywords:** binary serialization, inventory operations, player health, synchronization, deserialization
**Symbols:** create, delete, useDurability, health, kill, energy, executeFromData, getUsers, ignoreSource, deserialize
**Concepts:** inventory management, player state synchronization

## Summary
Handles synchronization operations for inventory and player state updates.

## Explanation
This chunk defines various synchronization operations such as creating, deleting, and using durability of items in inventories. It also handles health, kill, and energy updates for players. The `executeFromData` function processes these operations based on data read from a binary reader. The `getUsers` function retrieves affected users for each operation type, and the `ignoreSource` function determines if an operation should ignore its source. The `deserialize` function reads synchronization operations from a binary format, while the `serialize` function (incomplete in this snippet) would write them to a binary format.

## Code Example
```zig
pub fn executeFromData(reader: *BinaryReader) !void {
	switch (try deserialize(reader)) {
		.create => |create| {
			if (create.item != .null) {
				create.inv.ref().item = create.item;
			} else if (create.inv.ref().item == .null) {
				return error.Invalid;
			}

			if (create.inv.ref().amount +| create.amount > create.inv.ref().item.stackSize()) {
				return error.Invalid;
			}
			create.inv.ref().amount += create.amount;

			create.inv.inv.update();
		},
		.delete => |delete| {
			if (delete.inv.ref().amount < delete.amount) {
				return error.Invalid;
			}
			delete.inv.ref().amount -= delete.amount;
			if (delete.inv.ref().amount == 0) {
				delete.inv.ref().item = .null;
			}

			delete.inv.inv.update();
		},
		.useDurability => |durability| {
			durability.inv.ref().item.proceduralItem.durability -|= durability.durability;
			if (durability.inv.ref().item.proceduralItem.durability == 0) {
				durability.inv.ref().item = .null;
				durability.inv.ref().amount = 0;
			}

			durability.inv.inv.update();
		},
		.health => |health| {
			main.game.Player.super.health = std.math.clamp(main.game.Player.super.health + health.health, 0, main.game.Player.super.maxHealth);
		},
		.kill => |kill| {
			main.game.Player.kill(kill.spawnPoint);
		},
		.energy => |energy| {
			main.game.Player.super.energy = std.math.clamp(main.game.Player.super.energy + energy.energy, 0, main.game.Player.super.maxEnergy);
		},
	}
}
```

## Related Questions
- What operations are defined for inventory synchronization?
- How does the `executeFromData` function process synchronization data?
- Which users are affected by each type of synchronization operation?
- What conditions can cause an error during synchronization execution?
- How is a synchronization operation deserialized from binary data?
- What is the purpose of the `ignoreSource` method in synchronization operations?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_3*
