# [hard/codebase_src_sync.zig] - Chunk 4

**Type:** serialization
**Keywords:** BinaryWriter, Inventory, deinit, popOrNull, assertCorrectContext, moveToBag, takeFromBag, useDurability, addHealth, addEnergy
**Symbols:** SyncOperation, serializePayload, do, undo, finalize
**Concepts:** binary serialization, inventory operations, thread context assertions, reverse undo iteration, player state updates

## Summary
Chunk defines the serialization and undo logic for SyncOperation types (create, delete, useDurability, health, kill, energy) and Command operations (move, swap, delete, create, moveToBag, takeFromBag, useDurability, addHealth, addEnergy), including binary writer usage and thread context assertions.

## Explanation
The chunk declares SyncOperation with a serialize method that writes the operation type enum then branches on each variant: .create writes an Inventory.write() call plus amount (u16) and optionally item bytes; .delete writes inventory write and amount u16; .useDurability writes inventory write and durability u32; .health writes f32 float; .kill writes Vec3d spawn point; .energy writes f32 energy. It also declares Command fields payload, baseOperations (empty list), syncOperations (empty list). The serializePayload method uses BinaryWriter.init with defer deinit and switches on self.payload to call payload.serialize(). The do method asserts threadContext is correct for side, asserts baseOperations items len == 0 (preventing double execution without cleanup), then runs payload.run with allocator/cmd/side/user/gamemode. The undo method asserts client context, iterates baseOperations in reverse via popOrNull, and switches on step: .move copies item from dest to source if amount != 0, updates amounts, nulls dest item when amount reaches 0, calls inv.update() on both; .swap swaps the full struct of source and dest items then updates inventories; .delete asserts source item matches or is null, sets source item and adds amount, updates inventory; .create asserts dest has enough space, subtracts amount, deinit/nulls dest item when empty, updates inventory; .moveToBag peeks dest stack 0, loops while remainingAmount != 0 popping stacks, adjusting amounts and pushing back the remainder, then sets source to a new item with remaining amount; .takeFromBag asserts amount <= dest amount, pushes from dest to source, decrements dest amount, nulls dest when empty; .useDurability asserts source matches or is null, sets source item, updates proceduralItem durability to previous value, updates inventory; .addHealth and .addEnergy assign directly to main.game.Player.super.health/energy. The finalize method iterates baseOperations items, switches on step: for most variants it does nothing (empty case), but for .delete it calls info.item.deinit().

## Code Example
```zig
pub fn serialize(self: SyncOperation, allocator: NeverFailingAllocator) []const u8 {
		var writer = BinaryWriter.initCapacity(allocator, 13);
		writer.writeEnum(SyncOperationType, self);
		switch (self) {
			.create => |create| {
				create.inv.write(&writer);
				writer.writeInt(u16, create.amount);
				if (create.item != .null) {
					create.item.toBytes(&writer);
				}
			},
			.delete => |delete| {
				delete.inv.write(&writer);
				writer.writeInt(u16, delete.amount);
			},
			.useDurability => |durability| {
				durability.inv.write(&writer);
				writer.writeInt(u32, durability.durability);
			},
			.health => |health| {
				writer.writeFloat(f32, health.health);
			},
			.kill => |kill| {
				writer.writeVec(Vec3d, kill.spawnPoint);
			},
			.energy => |energy| {
				writer.writeFloat(f32, energy.energy);
			},
		}
		return writer.data.toOwnedSlice();
	}
```

## Related Questions
- What SyncOperation variants are serialized and how does each write its data?
- How does serializePayload handle an inline payload versus other types?
- Which assertions guard the do method against double execution without cleanup?
- In undo, what is the purpose of iterating baseOperations in reverse order via popOrNull?
- How does moveToBag split a stack when remainingAmount is less than the top stack amount?
- What invariant checks are performed before modifying source or dest items in delete and create?
- Where is the player health/energy state updated during undo operations?
- Does finalize deinit any items, and for which operation types does it do so?
- How does useDurability preserve previous durability when applying a new item?
- What happens to dest.item in create when its amount reaches zero after subtraction?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_4*
