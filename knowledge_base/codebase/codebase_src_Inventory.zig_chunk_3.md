# [hard/codebase_src_Inventory.zig] - Chunk 3

**Type:** api
**Keywords:** inventory operations, server-client communication, item transfer, crafting procedures, block placement
**Symbols:** ClientInventory, ClientInventory.ClientType, ClientInventory.init, ClientInventory.deinit, ClientInventory.depositOrSwap, ClientInventory.deposit, ClientInventory.takeHalf, ClientInventory.distribute, ClientInventory.depositOrDrop, ClientInventory.depositToAny, ClientInventory.dropStack, ClientInventory.depositToBag, ClientInventory.dropOne, ClientInventory.fillFromCreative, ClientInventory.fillAmountFromCreative, ClientInventory.fillAnyFromCreative, ClientInventory.craftFrom, ClientInventory.craftProceduralItem, ClientInventory.placeBlock, ClientInventory.breakBlock, ClientInventory.size, ClientInventory.getItem, ClientInventory.getStack, ClientInventory.getAmount
**Concepts:** inventory management, client-server synchronization, item manipulation, crafting system, block interaction

## Summary
The `ClientInventory` struct manages client-side inventory operations, including initialization, deinitialization, and various item manipulation methods.

## Explanation
The `ClientInventory` struct extends the base `Inventory` type with additional functionality specific to client-side inventories. It includes a union enum `ClientType` that categorizes different types of client inventories such as server-shared, creative, crafting, and workbench result inventories. The struct provides methods for initializing and deinitializing inventories, depositing or swapping items between inventories, handling item deposits, taking half of an item stack, distributing items across multiple inventories, dropping items, filling from the creative inventory, crafting items, placing and breaking blocks, and retrieving inventory size, items, stacks, and amounts. Each method interacts with the server through `main.sync.client.executeCommand` for operations that require synchronization with the server.

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
