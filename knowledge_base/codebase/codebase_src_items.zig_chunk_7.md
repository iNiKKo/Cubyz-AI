# [hard/codebase_src_items.zig] - Chunk 7

**Type:** implementation
**Keywords:** item properties, texture rendering, tooltip formatting, durability decrement, inventory interaction
**Symbols:** ProceduralItem, ProceduralItem.getItemAt, ProceduralItem.getProperty, ProceduralItem.setProperty, ProceduralItem.getTexture, ProceduralItem.getTooltip, ProceduralItem.hasTag, ProceduralItem.isEffectiveOn, ProceduralItem.getBlockDamage, ProceduralItem.onUseReturnBroken, ItemType, Item, Item.init, Item.deinit, Item.clone, Item.stackSize, Item.insertIntoZon
**Concepts:** item management, property handling, texture generation, tooltip creation, durability tracking

## Summary
Defines the `ProceduralItem` struct and its methods, handling item properties, textures, tooltips, and interactions.

## Explanation
This chunk defines the `ProceduralItem` struct with various methods to manage item properties, generate textures, create tooltips, and handle durability. It also includes a union type `Item` that can represent different types of items, each with its own initialization, deinitialization, cloning, stack size calculation, and serialization logic.

## Code Example
```zig
pub fn getItemAt(self: *const ProceduralItem, x: i32, y: i32) ?BaseItemIndex {
	if (x < 0 or x >= 5) return null;
	if (y < 0 or y >= 5) return null;
	return self.craftingGrid[@intCast(x + y*5)];
}
```

## Related Questions
- How does the `ProceduralItem` struct manage item properties?
- What is the purpose of the `getTexture` method in `ProceduralItem`?
- How are tooltips generated for `ProceduralItem` instances?
- What conditions determine if a procedural item can be put into a workbench?
- How does the `Item` union handle different types of items during initialization?
- What is the role of the `deinit` method in the `Item` union?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_7*
