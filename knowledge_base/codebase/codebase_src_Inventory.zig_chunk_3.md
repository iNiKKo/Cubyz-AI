# [hard/codebase_src_Inventory.zig] - Chunk 3

**Type:** api
**Keywords:** inventory operations, server-client communication, item transfer, crafting procedures, block placement
**Symbols:** ClientInventory, ClientInventory.ClientType, ClientInventory.init, ClientInventory.deinit, ClientInventory.depositOrSwap, ClientInventory.deposit, ClientInventory.takeHalf, ClientInventory.distribute, ClientInventory.depositOrDrop, ClientInventory.depositToAny, ClientInventory.dropStack, ClientInventory.depositToBag, ClientInventory.dropOne, ClientInventory.fillFromCreative, ClientInventory.fillAmountFromCreative, ClientInventory.fillAnyFromCreative, ClientInventory.craftFrom, ClientInventory.craftProceduralItem, ClientInventory.placeBlock, ClientInventory.breakBlock, ClientInventory.size, ClientInventory.getItem, ClientInventory.getStack, ClientInventory.getAmount
**Concepts:** inventory management, client-server synchronization, item manipulation, crafting system, block interaction

## Summary
The `ClientInventory` struct manages client-side inventory operations, including initialization, deinitialization, and various item manipulation methods.

## Explanation
The `ClientInventory` struct manages client-side inventory operations, including initialization, deinitialization, and various item manipulation methods. It extends the base `Inventory` type with additional functionality specific to client-side inventories. The struct includes a union enum `ClientType` that categorizes different types of client inventories such as server-shared (`serverShared`), creative (`creative`), crafting (`crafting`), and workbench result (`workbenchResult`) inventories.

The `init` method initializes a `ClientInventory` by creating an instance of the base `Inventory` type and setting its `type`. If the client type is server-shared, it sends an open command to the server. The `deinit` method deinitializes the inventory, sending a close command if connected to the server or manually deinitializing otherwise.

The `depositOrSwap` method deposits or swaps items between inventories. If the destination inventory is creative, it fills from the creative inventory; otherwise, it sends a deposit or swap command to the server. The `deposit` method handles item deposits, filling from the creative inventory if the source is creative, or sending a deposit command to the server otherwise.

The `takeHalf` method takes half of an item stack and places it in another inventory. If the destination inventory is creative, it fills from the creative inventory; otherwise, it sends a take half command to the server. The `distribute` method distributes items across multiple inventories by calculating the amount per inventory and sending deposit commands.

The `depositOrDrop` method deposits items into specified destinations or drops them if no destination is available. It sends a deposit or drop command to the server. The `depositToAny` method deposits items into any of the specified destinations, sending a deposit to any command to the server. The `dropStack` method drops an entire stack from an inventory by sending a drop command to the server. The `dropOne` method drops a single item by sending a drop command with a desired amount of 1.

The `fillFromCreative` and `fillAmountFromCreative` methods fill inventories with items from the creative inventory, either filling a specific slot or specifying an amount. The `fillAnyFromCreative` method fills any of the specified destinations with items from the creative inventory by sending a fill any command to the server.

The `craftFrom` method crafts items using a crafting inventory, sending a craft command to the server. The `craftProceduralItem` method crafts procedural items by interacting with the workbench inventory and sending a craft procedural item command to the server.

The `placeBlock` and `breakBlock` methods handle block placement and breaking, respectively, by interacting with the renderer's mesh selection system and sending place or break commands to the server.

The struct also provides methods for retrieving inventory size (`size`), items (`getItem`), stacks (`getStack`), and amounts (`getAmount`). These methods return the respective properties of the inventory without additional operations.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator, _size: usize, clientType: ClientType, source: Source, callbacks: Callbacks) ClientInventory {
	const self: ClientInventory = .{
		.super = Inventory._init(allocator, _size, source, .client, callbacks),
		.type = clientType,
	};
	if (clientType == .serverShared) {
		sync.client.executeCommand(.{.open = .{.inv = self.super, .source = source}});
	}
	return self;
}
```

## Related Questions
- What are the different types of client inventories defined in `ClientInventory`?
- How does the `init` method initialize a `ClientInventory`?
- What operations are performed when deinitializing a `ClientInventory`?
- How do items get deposited or swapped between inventories?
- What is the process for depositing items into another inventory?
- How does the `takeHalf` method work in `ClientInventory`?
- How are items distributed across multiple inventories?
- What steps are involved in dropping an item stack from an inventory?
- How do items get filled from the creative inventory?
- What is the procedure for crafting items using a crafting inventory?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_3*
