# [hard/codebase_src_items.zig] - Chunk 5

**Type:** api
**Keywords:** enum reading, iterator, ID to index conversion, property access, image handling, texture generation, cloning
**Symbols:** ProceduralItemTypeIndex, ProceduralItemTypeIterator, fromId, id, tags, properties, slotInfos, pixelSources, pixelSourcesOverlay, ProceduralItemType, ProceduralItemProperty, ProceduralItem, craftingGridSize, CraftingGridMask, init, deinit, clone, initFromCraftingGrid, initFromInventory
**Concepts:** item management, procedural item generation

## Summary
This chunk defines the procedural item system, including reading from a reader, iterating over items, and managing properties and textures.

## Explanation
The chunk contains definitions for procedural item types and their properties. It includes functions to read an enum from a reader, iterate over items, convert IDs to indices, and access various properties of procedural items such as tags, properties, slot information, and pixel sources. The `ProceduralItem` struct manages crafting grids, material grids, modifiers, tooltips, images, textures, seed, type, durability, handle position, inertia, center of mass, and moment of inertia. It provides methods for initialization, deinitialization, cloning, and creating items from a crafting grid or inventory.

## Code Example
```zig
pub fn iterator() ProceduralItemTypeIterator {
	return .{};
}
```

## Related Questions
- How do you read an enum from a reader?
- What is the function to convert an ID to a procedural item index?
- How do you access the tags of a procedural item?
- What methods are available for managing procedural item properties?
- How does the `ProceduralItem` struct handle initialization and deinitialization?
- What steps are involved in cloning a procedural item?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_5*
