# [hard/codebase_src_items.zig] - Chunk 10

**Type:** api
**Keywords:** global initialization, deinitialization, item registration, texture loading, procedural items
**Symbols:** globalInit, globalDeinit, reset, register, loadPixelSources, registerProceduralItem
**Concepts:** item management, texture handling, procedural content generation

## Summary
Handles initialization, deinitialization, resetting item states, registering new items with textures and IDs, loading procedural item data from assets, managing item lists, procedural item types, their properties, and pixel sources. Includes specific error handling for file reading and ensures images are correctly sized.

## Explanation
This chunk contains functions for initializing and deinitializing global item systems, resetting item states, registering new items with textures and IDs, and loading procedural item data from assets. It manages item lists (`itemList`), procedural item types (`proceduralItemTypeList`), and their associated properties and pixel sources. The code includes error handling for file reading using `std.log.err`, ensuring that images are correctly sized (16x16 pixels). Specific details include:

- **Initialization:**
  - `globalInit`: Initializes procedural item type IDs, modifiers, modifier restrictions, and client inventory.
  - `modifiers.put` initializes modifier structs from `modifierList`.
  - `modifierRestrictions.put` initializes restriction structs from `modifierRestrictionList`.

- **Deinitialization:**
  - `globalDeinit`: Deinitializes the client inventory (`Inventory.client.deinit()`).

- **Resetting Item States:**
  - `reset`: Resets procedural item type list, item ID to index mapping, reverse indices, recipe list, and item list size.

- **Registering New Items:**
  - `register`: Registers new items with textures (`texturePath`), replacement textures (`replacementTexturePath`), IDs (`id`), and Zon elements (`zon`). It also logs the registered item ID.

- **Loading Procedural Item Data:**
  - `loadPixelSources`: Loads pixel sources for procedural items from assets, handling file not found errors by providing a default path. Ensures images are correctly sized (16x16 pixels).
  - `registerProceduralItem`: Registers procedural items with disabled and optional slot information, parameter matrices, tags, properties, and pixel sources.

- **Error Handling:**
  - Logs errors for file not found issues during image loading (`std.log.err`). Ensures images are correctly sized (16x16 pixels) by truncating incorrect dimensions.

## Code Example
```zig
pub fn globalDeinit() void {
	Inventory.client.deinit();
}
```

## Related Questions
- What specific data structures are used to manage procedural item types and their properties?
- How does the `register` function handle texture paths and IDs for new items?
- Describe the process of loading pixel sources for procedural items, including error handling.

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_10*
