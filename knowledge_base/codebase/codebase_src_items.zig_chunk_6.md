# [hard/codebase_src_items.zig] - Chunk 6

**Type:** serialization
**Keywords:** binary serialization, inventory handling, texture generation, property evaluation, item retrieval
**Symbols:** initFromCraftingGrid, initFromInventory, initFromZon, extractItemsFromZon, save, fromBytes, toBytes, hashCode, getItemAt, getProperty, setProperty, getTexture, getTooltip
**Concepts:** item initialization, serialization, property management

## Summary
Handles procedural item initialization, serialization, and property management.

## Explanation
This chunk defines methods for initializing procedural items from different sources such as crafting grids, inventories, and serialized data. It includes functions to save and load procedural items in both Zon and binary formats. The code also manages properties of procedural items, ensuring they are correctly evaluated and updated. Additionally, it provides utility functions for accessing item details and generating textures.

## Code Example
```zig
fn hashCode(self: ProceduralItem) u32 {
    var hash: u32 = 0;
    for (self.craftingGrid) |nullItem| {
        if (nullItem) |item| {
            hash = 33*%hash +% item.material().?.hashCode();
        }
    }
    return hash;
}
```

## Related Questions
- How is a procedural item initialized from a crafting grid?
- What methods are available for serializing and deserializing procedural items?
- How does the code handle properties of procedural items?
- What steps are involved in generating textures for procedural items?
- How are procedural items retrieved from an inventory?
- What is the process for saving procedural item data to a Zon file?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_6*
