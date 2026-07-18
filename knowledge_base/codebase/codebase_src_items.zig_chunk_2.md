# [hard/codebase_src_items.zig] - Chunk 2

**Type:** implementation
**Keywords:** struct, initialization, hashing, textures, tooltips
**Symbols:** BaseItem, BaseItem.image, BaseItem.texture, BaseItem.id, BaseItem.name, BaseItem.tags, BaseItem.tooltip, BaseItem.stackSize, BaseItem.material, BaseItem.block, BaseItem.foodValue, BaseItem.init, BaseItem.hashCode, BaseItem.getTexture, BaseItem.getTooltip, BaseItem.hasTag
**Concepts:** item management, texture handling, tooltip generation

## Summary
Defines the `BaseItem` struct with methods for initialization, texture handling, and tooltip generation.

## Explanation
The `BaseItem` struct encapsulates properties of an item in the game, including its image, ID, name, tags, stack size (default is 120), material, block type, food value (default is 0), and tooltip. The `init` method initializes these fields using provided data and allocator. If no texture path is specified, it defaults to a default image. Tags are loaded from the ZonElement's 'tags' child. Material initialization depends on the presence of a material object in the ZonElement. Block type is determined by the block ID in the ZonElement or null if not present. The `hashCode` method computes a hash for the item's ID using each character of the ID string. The `getTexture` method generates or retrieves the texture associated with the item, either from a default image or based on the block type if applicable. The `getTooltip` method returns the item's tooltip text which includes the name and any material-specific tooltips. The `hasTag` method checks if the item has a specific tag by iterating through its tags.

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
- What is the default stack size for an item?
- How is the food value of an item determined?
- Under what conditions does the `init` method set the material field?
- How are block types assigned to items during initialization?
- What happens if no texture path is specified in the `init` method?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_2*
