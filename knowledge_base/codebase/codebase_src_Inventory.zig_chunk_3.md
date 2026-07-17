# [hard/codebase_src_Inventory.zig] - Chunk 3

**Type:** api
**Keywords:** inventory operations, client-server interaction, item handling, synchronization, callbacks
**Symbols:** ClientInventory, ClientInventory.ClientType, ClientInventory.init, ClientInventory.deinit, ClientInventory.depositOrSwap, ClientInventory.deposit, ClientInventory.takeHalf, ClientInventory.distribute, ClientInventory.depositOrDrop, ClientInventory.depositToAny, ClientInventory.dropStack, ClientInventory.depositToBag, ClientInventory.dropOne, ClientInventory.fillFromCreative, Callbacks, Callbacks.onUpdateCallback, Callbacks.onFirstOpenCallback, Callbacks.onLastCloseCallback, Callbacks.canPutInto, SourceType, Source, Source.alreadyFreed, Source.playerInventory, Source.hand, Source.blockInventory, Source.workbench, Source.other
**Concepts:** inventory management, client-server synchronization, item depositing, slot swapping

## Summary
Handles inventory operations such as depositing items, swapping slots, and managing client-server synchronization.

## Explanation
This chunk defines the `ClientInventory` struct and its associated methods for managing inventory operations in a client-server context. It includes methods for initializing and deinitializing inventories, handling deposits, swaps, and other interactions with server-shared or creative inventories. The chunk also defines enums and structs for representing different types of inventory sources and callbacks for inventory updates.

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
- How does the `ClientInventory` struct initialize itself?
- What methods are available for managing inventory operations in a client-server context?
- How does the `depositOrSwap` method work in the `ClientInventory` struct?
- What is the purpose of the `Callbacks` struct in this chunk?
- How does the `fillFromCreative` method interact with the server?
- What types of inventory sources are defined in the `SourceType` enum?
- How does the `deinit` method handle deinitialization of a client inventory?
- What is the role of the `depositToBag` method in managing inventory items?
- How does the `takeHalf` method work in the context of inventory management?
- What are the different types of inventory operations supported by this chunk?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_3*
