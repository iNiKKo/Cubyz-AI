# [medium/codebase_src_items_recipes.zig] - Chunk 1

**Type:** api
**Keywords:** NeverFailingAllocator, StringHashMap, ListManaged, ZonElement, ItemKeyPair, ItemWithAmount, Recipe
**Symbols:** findRecipeItemOptions, generateItemCombos, addRecipe, parseRecipe
**Concepts:** item recipes, pattern matching, recipe generation

## Summary
Handles item recipe parsing and generation.

## Explanation
This chunk contains functions for finding recipe item options, generating item combinations from a recipe, adding recipes to a list, and parsing recipes from Zon elements. It also includes tests for pattern parsing and matching. The primary data structures used are `ItemKeyPair`, `ItemWithAmount`, and `Recipe`. Functions like `findRecipeItemOptions` handle specific logic for finding items that match given patterns, while `generateItemCombos` creates all possible combinations of input items based on a recipe. The `addRecipe` function adds a parsed recipe to a list, and `parseRecipe` processes Zon elements to define recipes, including handling reversible recipes.

## Code Example
```zig
fn addRecipe(itemCombo: []const ItemWithAmount, list: *main.ListManaged(Recipe)) void {
	const inputs = itemCombo[0 .. itemCombo.len - 1];
	const output = itemCombo[itemCombo.len - 1];
	const recipe = Recipe{
		.sourceItems = main.worldArena.alloc(BaseItemIndex, inputs.len),
		.sourceAmounts = main.worldArena.alloc(u16, inputs.len),
		.resultItem = output.item,
		.resultAmount = output.amount,
	};
	for (inputs, 0..) |input, i| {
		recipe.sourceItems[i] = input.item;
		recipe.sourceAmounts[i] = input.amount;
	}
	list.append(recipe);
}
```

## Related Questions
- How does the `findRecipeItemOptions` function work?
- What is the purpose of the `generateItemCombos` function?
- How are recipes added to a list in this module?
- What error handling is implemented for parsing recipes?
- Can you explain how pattern matching works in this chunk?
- What data structures are used to store item combinations and recipes?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_1*
