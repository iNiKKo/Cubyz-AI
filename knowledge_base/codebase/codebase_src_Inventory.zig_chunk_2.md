# [hard/codebase_src_Inventory.zig] - Chunk 2

**Type:** api
**Keywords:** inventory retrieval, callbacks, client-server context, union types, enum types
**Symbols:** getInventory, Callbacks, Callbacks.onUpdateCallback, Callbacks.onFirstOpenCallback, Callbacks.onLastCloseCallback, Callbacks.canPutInto, SourceType, SourceType.alreadyFreed, SourceType.playerInventory, SourceType.hand, SourceType.blockInventory, SourceType.workbench, SourceType.other, Source, Source.alreadyFreed, Source.playerInventory, Source.hand, Source.blockInventory, Source.workbench, Source.other
**Concepts:** inventory management, callback mechanisms, context-based retrieval

## Summary
Defines inventory retrieval and callback mechanisms for different contexts.

## Explanation
This chunk defines functions and structures related to inventory management. The `getInventory` function retrieves an inventory based on the context (client or server) and user information. The `Callbacks` struct contains optional callbacks for various inventory events like updates, first open, last close, and item placement checks. The `SourceType` enum categorizes different types of inventory sources, and the `Source` union holds specific data corresponding to each source type.

## Code Example
```zig
pub fn getInventory(id: InventoryId, side: sync.Side, user: ?*main.server.User) ?Inventory {
	sync.threadContext.assertCorrectContext(side);
	return switch (side) {
		.client => client.getInventory(id),
		.server => server.getInventory(user.?, id),
	};
}
```

## Related Questions
- How does the `getInventory` function determine which inventory to retrieve?
- What are the possible values for the `SourceType` enum?
- What is the purpose of the `Callbacks` struct in this code?
- Can you explain how the `Source` union works with different source types?
- What does the `onUpdateCallback` callback do in the `Callbacks` struct?
- How is the client-server context handled in the `getInventory` function?

*Source: unknown | chunk_id: codebase_src_Inventory.zig_chunk_2*
