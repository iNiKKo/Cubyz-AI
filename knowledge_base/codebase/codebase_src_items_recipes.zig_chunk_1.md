# [medium/codebase_src_items_recipes.zig] - Chunk 1

**Type:** api
**Keywords:** NeverFailingAllocator, StringHashMap, ListManaged, ZonElement, ItemKeyPair, ItemWithAmount, Recipe
**Symbols:** findRecipeItemOptions, generateItemCombos, addRecipe, parseRecipe
**Concepts:** item recipes, pattern matching, recipe generation

## Summary
Handles item recipe parsing and generation.

## Explanation
This chunk contains several key functions for handling item recipe parsing and generation. The primary data structures used are `ItemKeyPair`, `ItemWithAmount`, and `Recipe`. Here's a detailed breakdown of each function:

1. **findRecipeItemOptions**: This function takes an allocator, an ItemStackPattern (which includes a pattern and amount), and keys to find matching items based on the provided pattern. If the pattern is a literal item ID, it returns that item directly with its associated keys. Otherwise, it iterates through all possible items to match the given pattern.

2. **generateItemCombos**: This function generates all possible combinations of input items for a recipe using an allocator and a list of Zon elements representing the recipe inputs and output. It uses nested loops to create combinations based on item patterns and keys, ensuring that each combination is valid according to the provided pattern.

3. **addRecipe**: Adds a parsed recipe to a list by extracting input items and their amounts from an `itemCombo` array and storing them in a `Recipe` struct. The function allocates memory for source items and amounts using the world arena, then populates these fields with data from the item combo.

4. **parseRecipe**: Parses recipes from Zon elements to define recipes, including handling reversible recipes. It checks if the recipe is reversible and ensures that it has exactly two parts (inputs and output) for reversibility. The function generates all possible combinations of input items based on the provided patterns and adds them to a list.

5. **Tests**: Includes tests for pattern parsing and matching, ensuring that ambiguous symbols, empty braces, unclosed braces, and no match errors are correctly handled. It also verifies that pattern matching produces expected key-value pairs for given inputs.

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
- Can you explain how pattern matching works in this chunk?
- What error handling is implemented for parsing recipes?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_1*
