# [medium/codebase_src_items_recipes.zig] - Chunk 1

**Type:** api
**Keywords:** recipe generation, pattern matching, Zon elements, item combinations, reversible recipes
**Symbols:** ItemWithAmount, ItemKeyPair, findRecipeItemOptions, generateItemCombos, addRecipe, parseRecipe
**Concepts:** item recipes, pattern matching, Zon parsing

## Summary
Handles item recipes and their parsing from Zon elements.

## Explanation
This chunk defines structures for items with amounts and key pairs. It includes functions to find recipe item options, generate item combinations from a recipe, add recipes to a list, and parse recipes from Zon elements. The `findRecipeItemOptions` function matches patterns and keys to find suitable items. `generateItemCombos` creates all possible combinations of input items for a given recipe. `addRecipe` constructs a Recipe struct and appends it to a list. `parseRecipe` parses a Zon element into recipes, handling reversible recipes if specified. Tests are provided for pattern parsing and matching.

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
- How do you find recipe item options?
- What does the generateItemCombos function do?
- How are recipes added to a list?
- How is a Zon element parsed into recipes?
- What error can occur during pattern parsing?
- How is pattern matching with keys handled?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_1*
