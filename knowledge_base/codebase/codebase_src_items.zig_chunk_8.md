# [hard/codebase_src_items.zig] - Chunk 8

**Type:** api
**Keywords:** cloning, binary serialization, texture retrieval, rendering, stack management
**Symbols:** Item, Item.clone, Item.stackSize, Item.insertIntoZon, Item.fromBytes, Item.toBytes, Item.getTexture, Item.id, Item.getTooltip, Item.getImage, Item.hashCode, Item.render, ItemStack, ItemStack.item, ItemStack.amount, ItemStack.load
**Concepts:** item management, serialization, rendering

## Summary
This chunk defines the `Item` and `ItemStack` structures, handling item cloning, serialization, texture retrieval, and rendering.

## Explanation
The `Item` struct represents different types of items in the game, including base items and procedural items. It provides methods for cloning, determining stack size, inserting into a Zon object, reading from and writing to binary formats, retrieving textures, IDs, tooltips, images, hash codes, and rendering. The `ItemStack` struct manages stacks of items, with methods for loading from a Zon element.

## Code Example
```zig
pub fn stackSize(self: Item) u16 {
	switch (self) {
		.baseItem => |_baseItem| {
			return _baseItem.stackSize();
		},
		.proceduralItem => {
			return 1;
		},
		.null => {
			return 0;
		},
	}
}
```

## Related Questions
- How does the `Item` struct handle cloning?
- What methods are available for serializing and deserializing items?
- How is the texture retrieved for an item?
- What is the process for rendering an item with durability information?
- How does the `ItemStack` struct manage item amounts?
- What error handling is implemented when loading an `ItemStack`?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_8*
