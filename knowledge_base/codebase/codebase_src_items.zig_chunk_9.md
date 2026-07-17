# [hard/codebase_src_items.zig] - Chunk 9

**Type:** api
**Keywords:** binary serialization, Zon elements, item stacks, crafting recipes, global registries, hash maps
**Symbols:** ItemStack, ItemStack.item, ItemStack.amount, ItemStack.load, ItemStack.deinit, ItemStack.clone, ItemStack.empty, ItemStack.storeToZon, ItemStack.fromBytes, ItemStack.toBytes, Recipe, Recipe.sourceItems, Recipe.sourceAmounts, Recipe.resultItem, Recipe.resultAmount, Recipe.getValidRecipe, Recipe.toBytes, Recipe.fromBytes, proceduralItemTypeList, proceduralItemTypeIdToIndex, reverseIndices, modifiers, modifierRestrictions, itemList, itemListSize, itemDeduplicationMap, recipeList, hasRegistered, hasRegisteredProceduralItem, iterator
**Concepts:** inventory management, crafting recipes, item serialization, global item registry

## Summary
This chunk defines the `ItemStack` and `Recipe` structs, along with their associated methods for loading, storing, and serialization. It also manages item lists and procedural item types.

## Explanation
The `ItemStack` struct represents a stack of items in the game, containing an `item` and an `amount`. It provides methods for loading from and storing to Zon elements, as well as binary serialization (`fromBytes` and `toBytes`). The `Recipe` struct defines crafting recipes with source items, amounts, result item, and amount. It includes a method to validate recipes against a list of registered recipes and supports binary serialization. The chunk also manages global lists and maps for procedural item types, base items, modifiers, and recipe lists. Functions are provided to check if an item or procedural item is registered and to iterate over the base item indices.

## Code Example
```zig
pub fn empty(self: *const ItemStack) bool {
	return self.amount == 0;
}
```

## Related Questions
- How does the `ItemStack` struct handle item serialization?
- What methods are available for managing `Recipe` objects?
- How is the global item list structured and accessed?
- What role do procedural item types play in the game?
- How are duplicate items handled during inventory loading?
- How are recipes validated against registered recipes?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_9*
