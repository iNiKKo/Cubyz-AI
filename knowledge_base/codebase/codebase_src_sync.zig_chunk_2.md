# [hard/codebase_src_sync.zig] - Chunk 2

**Type:** api
**Keywords:** gamemode setting, payload types, base operations, sync operations, inventory manipulation
**Symbols:** setGamemode, Command, Command.PayloadType, Command.Payload, BaseOperationType, BaseOperation, SyncOperationType, SyncOperation
**Concepts:** command handling, inventory management, server-client synchronization

## Summary
Defines functions and data structures for handling game commands and inventory operations.

## Explanation
The chunk defines a function `setGamemode` that sets the gamemode for either a client or a server user based on the provided `user` parameter. It also declares several structs and enums related to command payloads, base operations, and sync operations.

The `Command.PayloadType` enum lists various types of commands, each associated with a specific payload structure:
- open
- close
- depositOrSwap
- deposit
- takeHalf
- drop
- fillFromCreative
- fillAnyFromCreative
- depositOrDrop
- depositToAny
- moveToPlayerBag
- takeFromPlayerBag
- craftFrom
- craftProceduralItem
- clear
- updateBlock
- addHealth
- chatCommand

The `BaseOperationType` enum defines different types of inventory operations, such as move, swap, delete, create, etc., with corresponding struct fields for each operation type:
- move: struct { dest: InventoryAndSlot, source: InventoryAndSlot, amount: u16 }
- swap: struct { dest: InventoryAndSlot, source: InventoryAndSlot }
- delete: struct { source: InventoryAndSlot, item: Item = undefined, amount: u16 }
- create: struct { dest: InventoryAndSlot, item: Item, amount: u16 }
- moveToBag: struct { dest: *Inventory.BagInventory, source: InventoryAndSlot, amount: u16 }
- takeFromBag: struct { dest: InventoryAndSlot, source: *Inventory.BagInventory, amount: u16 }
- useDurability: struct { source: InventoryAndSlot, item: main.items.Item = undefined, durability: u31, previousDurability: u32 = undefined }
- addHealth: struct { target: ?*main.server.User, health: f32, cause: main.game.DamageType, previous: f32 }
- addEnergy: struct { target: ?*main.server.User, energy: f32, previous: f32 }

The `SyncOperationType` enum and its associated union define server-side synchronization operations, including creating or deleting items, using durability, updating health, killing entities, and managing energy:
- create: struct { inv: InventoryAndSlot, amount: u16, item: Item }
- delete: struct { inv: InventoryAndSlot, amount: u16 }
- useDurability: struct { inv: InventoryAndSlot, durability: u32 }
- health: struct { target: ?*main.server.User, health: f32 }
- kill: struct { target: ?*main.server.User, spawnPoint: Vec3d }
- energy: struct { target: ?*main.server.User, energy: f32 }

## Code Example
```zig
pub fn setGamemode(user: ?*main.server.User, gamemode: Gamemode) void {
	if (user == null) {
		client.setGamemode(gamemode);
	} else {
		server.setGamemode(user.?, gamemode);
	}
}
```

## Related Questions
- What is the purpose of the `setGamemode` function?
- How are different types of commands represented in this chunk?
- What operations can be performed using the `BaseOperationType` enum?
- How does the `SyncOperation` handle server-side updates?
- What is the structure of a `create` operation in `SyncOperation`?
- How are payloads for different command types defined?
- What is the role of the `PayloadType` enum in the command system?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_2*
