# [hard/codebase_src_items.zig] - Chunk 8

**Type:** api
**Keywords:** union, serialization, deserialization, rendering, cloning, resource management
**Symbols:** Item, Item.baseItem, Item.proceduralItem, Item.null, Item.init, Item.deinit, Item.clone, Item.stackSize, Item.insertIntoZon, Item.fromBytes, Item.toBytes, Item.getTexture, Item.id, Item.getTooltip, Item.getImage, Item.hashCode, Item.render
**Concepts:** item management, serialization, rendering

## Summary
The `Item` union represents different types of items in the game, including base items and procedural items. It provides methods for initialization, deinitialization, cloning, serialization, deserialization, and rendering.

## Explanation
The `Item` union is defined with three variants: `baseItem`, `proceduralItem`, and `null`. Each variant has associated functions that handle specific operations related to the item type. The `init` function initializes an item from a ZonElement, while `deinit` cleans up resources if necessary. The `clone` method creates a copy of the item. Serialization and deserialization are handled by `toBytes` and `fromBytes`, respectively. The `render` method draws the item on the screen, including its durability bar for procedural items.

## Code Example
```zig
pub fn deinit(self: Item) void {
	switch (self) {
		.baseItem, .null => {},
		.proceduralItem => |_proceduralItem| {
			_proceduralItem.deinit();
		},
	}
}
```

## Related Questions
- How is an `Item` initialized from a ZonElement?
- What methods are available for cloning an `Item`?
- How does the `Item` union handle serialization and deserialization?
- What is the purpose of the `deinit` method in the `Item` union?
- How is the durability bar rendered for procedural items?
- What types of textures can be retrieved from an `Item`?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_8*
