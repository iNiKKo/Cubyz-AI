# [hard/codebase_src_items.zig] - Chunk 10

**Type:** api
**Keywords:** global initialization, deinitialization, item registration, texture loading, procedural items
**Symbols:** globalInit, globalDeinit, reset, register, loadPixelSources, registerProceduralItem
**Concepts:** item management, texture handling, procedural content generation

## Summary
Handles initialization, deinitialization, and registration of items in the game.

## Explanation
This chunk contains functions for initializing and deinitializing global item systems, resetting item states, registering new items with textures and IDs, and loading procedural item data from assets. It manages item lists, procedural item types, and their associated properties and pixel sources. The code includes error handling for file reading and ensures that images are correctly sized.

## Code Example
```zig
pub fn globalDeinit() void {
	Inventory.client.deinit();
}
```

## Related Questions
- What is the purpose of the `globalInit` function?
- How does the `registerProceduralItem` function handle errors during image loading?
- What data structure is used to store procedural item types?
- How are pixel sources loaded for procedural items?
- What is the role of the `reset` function in the item management system?
- How does the code ensure that images have the correct dimensions?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_10*
