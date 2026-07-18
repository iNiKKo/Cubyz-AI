# [hard/codebase_src_items.zig] - Chunk 2

**Type:** implementation
**Keywords:** struct, initialization, hashing, textures, tooltips
**Symbols:** BaseItem, BaseItem.image, BaseItem.texture, BaseItem.id, BaseItem.name, BaseItem.tags, BaseItem.tooltip, BaseItem.stackSize, BaseItem.material, BaseItem.block, BaseItem.foodValue, BaseItem.init, BaseItem.hashCode, BaseItem.getTexture, BaseItem.getTooltip, BaseItem.hasTag
**Concepts:** item management, texture handling, tooltip generation

## Summary
Defines the `BaseItem` struct with methods for initialization, texture handling, and tooltip generation.

## Explanation
The `BaseItem` struct encapsulates properties of an item in the game, including its image, ID, name, tags, stack size, material, block type, food value, and tooltip. The `init` method initializes these fields using provided data and allocator. The `hashCode` method computes a hash for the item's ID. The `getTexture` method generates or retrieves the texture associated with the item. The `getTooltip` method returns the item's tooltip text. The `hasTag` method checks if the item has a specific tag.

## Code Example
```zig
fn hashCode(self: BaseItem) u32 {
	var hash: u32 = 0;
	for (self.id) |char| {
		hash = hash*%33 +% char;
	}
	return hash;
}
```

## Related Questions
- What is the purpose of the `init` method in the `BaseItem` struct?
- How does the `hashCode` method compute the hash for an item's ID?
- What steps are involved in generating or retrieving the texture for an item using the `getTexture` method?
- How is the tooltip text generated and returned by the `getTooltip` method?
- What does the `hasTag` method check for in an item?
- How is memory allocated for string fields like `id`, `name`, and `tooltip` in the `BaseItem` struct?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_2*
