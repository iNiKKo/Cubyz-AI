# [hard/codebase_src_items.zig] - Chunk 8

**Type:** api
**Keywords:** union, serialization, deserialization, rendering, cloning, resource management
**Symbols:** Item, Item.baseItem, Item.proceduralItem, Item.null, Item.init, Item.deinit, Item.clone, Item.stackSize, Item.insertIntoZon, Item.fromBytes, Item.toBytes, Item.getTexture, Item.id, Item.getTooltip, Item.getImage, Item.hashCode, Item.render
**Concepts:** item management, serialization, rendering

## Summary
The `Item` union represents different types of items in the game, including base items and procedural items. It provides methods for initialization, deinitialization, cloning, serialization, deserialization, rendering, and managing item properties such as durability and textures.

## Explanation
The `Item` union is defined with three variants: `baseItem`, `proceduralItem`, and `null`. Each variant has associated functions that handle specific operations related to the item type. The `init` function initializes an item from a ZonElement, while `deinit` cleans up resources if necessary. The `clone` method creates a copy of the item. Serialization and deserialization are handled by `toBytes` and `fromBytes`, respectively. The `render` method draws the item on the screen, including its durability bar for procedural items. Here are more detailed explanations of each function:

- **init**: Initializes an item from a ZonElement. If the item is a base item, it retrieves the base item index. If it's a procedural item, it initializes the procedural item from the child object in the ZonElement.
- **deinit**: Cleans up resources if necessary. For procedural items, this involves calling `deinit` on the procedural item itself.
- **clone**: Creates a copy of the item. Base items and null are copied directly, while procedural items involve cloning the procedural item.
- **stackSize**: Returns the stack size for the item. Base items return their specific stack size, procedural items have a stack size of 1, and null returns 0.
- **insertIntoZon**: Inserts the item into a ZonElement. For base items, it sets the `item` field with the base item index. For procedural items, it sets the `tool` field with the serialized procedural item.
- **fromBytes**: Deserializes an item from bytes. It reads the type of the item and then either retrieves the base item or initializes a procedural item based on the read data.
- **toBytes**: Serializes an item to bytes. It writes the type of the item, followed by the specific details for base items or procedural items.
- **getTexture**: Returns the texture associated with the item. Base items and procedural items have their own methods to retrieve textures.
- **id**: Returns the ID of the item if it's a procedural item or base item; returns null for null items.
- **getTooltip**: Returns the tooltip text for the item, which is specific to each type of item.
- **getImage**: Returns the image associated with the item. Base items and procedural items have their own methods to retrieve images.
- **hashCode**: Computes a hash code for the item based on its properties.
- **render**: Draws the item on the screen. For procedural items, it also renders a durability bar based on the current durability percentage of the item.

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
