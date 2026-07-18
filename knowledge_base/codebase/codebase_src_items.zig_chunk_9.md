# [hard/codebase_src_items.zig] - Chunk 9

**Type:** api
**Keywords:** item stack, recipe validation, binary serialization, ZonElement, global item list
**Symbols:** ItemStack, ItemStack.item, ItemStack.amount, ItemStack.load, ItemStack.deinit, ItemStack.clone, ItemStack.empty, ItemStack.storeToZon, ItemStack.fromBytes, ItemStack.toBytes, Recipe, Recipe.sourceItems, Recipe.sourceAmounts, Recipe.resultItem, Recipe.resultAmount, Recipe.getValidRecipe, Recipe.toBytes, Recipe.fromBytes, proceduralItemTypeList, proceduralItemTypeIdToIndex, reverseIndices, modifiers, modifierRestrictions, itemList, itemListSize, itemDeduplicationMap, recipeList, hasRegistered, hasRegisteredProceduralItem, iterator, getRecipes
**Concepts:** inventory management, crafting recipes, serialization, deserialization

## Summary
Defines item stack and recipe structures with serialization, deserialization, and registration functionalities.

## Explanation
This chunk defines two primary structures: `ItemStack` and `Recipe`. The `ItemStack` structure manages an item and its quantity, providing methods for loading from a ZonElement, deinitializing resources, cloning the stack, checking if it's empty, storing to a ZonElement, and serializing/deserializing to/from binary formats. The `Recipe` structure represents crafting recipes, including methods for validating recipes, serializing to binary format, and deserializing from binary format. Additionally, the chunk declares several global variables related to item management, such as lists of procedural item types, reverse indices for items, modifiers, modifier restrictions, an array of base items, a deduplication map for items, and a list of recipes.

## Code Example
```zig
pub fn empty(self: *const ItemStack) bool {
	return self.amount == 0;
}
```

## Related Questions
- How does an `ItemStack` load data from a ZonElement?
- What methods are available for managing an `ItemStack`?
- How is a `Recipe` validated against existing recipes?
- What global variables are used for item management?
- How do you check if an item has been registered?
- How does the engine handle multiple indices mapping to the same item?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_9*
