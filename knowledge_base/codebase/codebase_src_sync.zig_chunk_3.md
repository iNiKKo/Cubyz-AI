# [hard/codebase_src_sync.zig] - Chunk 3

**Type:** serialization
**Keywords:** SyncOperationType, InventoryAndSlot, NeverFailingAllocator, BinaryReader, BinaryWriter, Vec3d, f32, u16, u32, error.Invalid
**Symbols:** SyncOperation, deserialize, executeFromData, getUsers, ignoreSource, serialize
**Concepts:** binary serialization, enum tag dispatch, inventory slot updates, player state clamping, user retrieval, stack size validation, durability decrement, spawn point kill

## Summary
This chunk defines the SyncOperation enum and its binary serialization/deserialization logic, along with executeFromData to apply inventory changes or player state updates, getUsers to retrieve affected users, ignoreSource for filtering, and serialize to write compacted bytes.

## Explanation
The chunk declares a public enum SyncOperation (not shown in the snippet but implied by usage) with variants create, delete, useDurability, health, kill, energy. Each variant is deserialized via deserialize(reader: *BinaryReader) !SyncOperation which reads a SyncOperationType enum tag then branches: .create reads an InventoryAndSlot (via read), a u16 amount, and optionally an Item from bytes; .delete reads an InventoryAndSlot and a u16 amount; .useDurability reads an InventoryAndSlot and a u32 durability; .health reads a f32 health value with target null; .kill reads a Vec3d spawnPoint with target null; .energy reads a f32 energy value with target null. The deserialize function returns the constructed SyncOperation union field populated accordingly.

The executeFromData(reader: *BinaryReader) !void method first deserializes into a local variable, then pattern-matches on it. For .create it checks that create.item is not null; if so it assigns create.inv.ref().item = create.item, else returns error.Invalid if the slot already holds an item. It also validates that adding create.amount to the existing amount does not exceed the item's stackSize() (via +| operator), returning error.Invalid on overflow, otherwise adds the amount and calls create.inv.inv.update(). For .delete it ensures delete.inv.ref().amount >= delete.amount, subtracts the amount, and if the resulting amount is zero sets delete.inv.ref().item = .null. For .useDurability it decrements proceduralItem.durability via -|=; when durability reaches 0 it nullifies both item and amount fields. For .health it clamps main.game.Player.super.health with std.math.clamp, adding health.health between 0 and maxHealth. For .kill it calls main.game.Player.kill(kill.spawnPoint). For .energy it clamps main.game.Player.super.energy similarly.

The getUsers(self: SyncOperation, allocator: NeverFailingAllocator) []*main.server.User method pattern-matches on self. For create/delete/useDurability it retrieves the server inventory via Inventory.server.getServerInventory(data.inv.inv.id), accesses its users.items array, allocates a result slice of that length, and copies each user pointer into result[i]. For health/kill/energy it allocates a single-element User slice and returns data.target.? (the target user). The ignoreSource(self: SyncOperation) bool method returns true for create/delete/useDurability/health/energy and false for kill.

The serialize(self: SyncOperation, allocator: NeverFailingAllocator) []const u8 method initializes a BinaryWriter with capacity 13, writes the SyncOperationType enum tag, then branches on self. For .create it calls create.inv.write(&writer), writes the amount as u16, and if create.item != .null it calls create.item.toBytes(&writer). For .delete it writes inv and amount. For .useDurability it writes inv and durability as u32. For .health it writes health.health as f32. For .kill it writes kill.spawnPoint as Vec3d. The snippet ends mid-switch for .energy, implying a similar writeFloat call would follow.

## Related Questions
- How does deserialize handle the optional item field in SyncOperation.create?
- What error is returned when adding an amount would exceed stackSize() in executeFromData?
- Which variants of SyncOperation cause getUsers to return a single-element user array?
- Does ignoreSource treat kill as ignorable or not, and why might that matter for network filtering?
- How does serialize write the item bytes only when create.item is non-null?
- What is the fixed capacity used by BinaryWriter.initCapacity in serialize and why 13?
- In executeFromData.delete, under what condition is delete.inv.ref().item set to .null?
- Does deserialize ever return an error for missing bytes on a variant that has no optional fields?
- How does the code ensure thread-safety when multiple users share the same inventory slot via getUsers?
- What happens if serialize is called with a SyncOperation that was never deserialized from this file's format?
- Can executeFromData be safely called on a SyncOperation constructed manually without using deserialize?
- Where does main.game.Player.kill receive its spawn point argument in the serialized form?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_3*
