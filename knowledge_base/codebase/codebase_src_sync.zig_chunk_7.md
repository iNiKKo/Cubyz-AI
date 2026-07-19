# [hard/codebase_src_sync.zig] - Chunk 7

**Type:** implementation
**Keywords:** inventory serialization, client-server synchronization, item manipulation, binary data handling, operation execution
**Symbols:** Command, Inventory, Side, main.server.User, Gamemode, BaseOperation, Context, Open, Close, DepositOrSwap, InventoryId, Inventory.Source, Inventory.SourceType, main.entity.Entity, Vec3i, BinaryReader, BinaryWriter
**Concepts:** inventory management, server-client communication, item operations

## Summary
This chunk defines structures and functions for handling inventory operations in a game server, including opening, closing, and depositing/swapping items.

## Explanation
**Explanation**

This chunk defines structures and functions for handling inventory operations in a game server, including opening, closing, and depositing/swapping items. The `Command` struct manages base operations, while the `Inventory` struct represents an inventory with methods for adding and removing items. The `Side` enum distinguishes between client and server operations.

The `Context` struct provides an execution context for these operations, including an allocator, command reference, side (client/server), user information, and gamemode. It has a method `execute` that executes base operations using the provided context.

The `Open` struct represents opening an inventory. It has methods for running the operation (`run`), finalizing it (`finalize`), serializing its data (`serialize`), and deserializing from a reader (`deserialize`). The `run` method currently does nothing, while the `finalize` method maps server IDs to client IDs if the side is the client.

The `Close` struct represents closing an inventory. It has methods for running the operation (`run`), finalizing it (`finalize`), serializing its data (`serialize`), and deserializing from a reader (`deserialize`). The `run` method currently does nothing, while the `finalize` method deinitializes the inventory on the client side and unmaps server IDs by client IDs.

The `DepositOrSwap` struct represents depositing or swapping items between two inventories. It has methods for running the operation (`run`), serializing its data (`serialize`), and deserializing from a reader (`deserialize`). The `run` method checks if the destination inventory can accept the item, then either moves or swaps the item based on the conditions.

The `removeProceduralItemCraftingIngredients` function removes crafting ingredients from a workbench by executing base operations to delete items from the inventory.

## Code Example
```zig
fn run(_: Open, _: Context) error{serverFailure}!void {}

fn finalize(self: Open, side: Side, reader: *BinaryReader) !void {
	if (side != .client) return;
	if (reader.remaining.len != 0) {
		const serverId = try reader.readEnum(InventoryId);
		Inventory.client.mapServerId(serverId, self.inv);
	}
}
```

## Related Questions
- What is the purpose of the `Context` struct in this chunk?
- How does the `DepositOrSwap` struct handle item swapping or depositing?
- What methods are available for serializing and deserializing inventory operations?
- How does the `Open` struct manage client-server synchronization?
- What error handling is implemented in the `run` method of the `Close` struct?
- How does the `removeProceduralItemCraftingIngredients` function interact with the inventory?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_7*
