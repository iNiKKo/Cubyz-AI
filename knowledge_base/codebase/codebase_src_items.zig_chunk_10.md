# [hard/codebase_src_items.zig] - Chunk 10

**Type:** api
**Keywords:** item registration, procedural items, texture loading, recipe handling, global initialization, memory management
**Symbols:** proceduralItemTypeList, proceduralItemTypeIdToIndex, reverseIndices, modifiers, modifierRestrictions, itemList, itemListSize, itemDeduplicationMap, recipeList, hasRegistered, hasRegisteredProceduralItem, iterator, getRecipes, globalInit, globalDeinit, reset, register, loadPixelSources, registerProceduralItem
**Concepts:** item registration, procedural item loading, recipe management

## Summary
Handles item registration, procedural item loading, and recipe management.

## Explanation
This chunk manages the registration of items and procedural items, including their textures and properties. It also handles the initialization and deinitialization of internal data structures used for these items. The `register` function adds a new item to the list, while `registerProceduralItem` processes procedural items from Zon files. The `loadPixelSources` function reads pixel data from images associated with procedural items. Recipes are managed through a list that can be retrieved using `getRecipes`. The chunk initializes and deinitializes various maps and lists during global setup and teardown.

## Code Example
```zig
pub fn hasRegistered(id: []const u8) bool {
	return reverseIndices.contains(id);
}
```

## Related Questions
- How do you check if an item is registered?
- What function registers a new procedural item?
- Where are the recipes stored and how can they be accessed?
- What happens during global initialization of items?
- How does the system handle multiple indices mapping to the same item?
- What is the purpose of the `loadPixelSources` function?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_10*
