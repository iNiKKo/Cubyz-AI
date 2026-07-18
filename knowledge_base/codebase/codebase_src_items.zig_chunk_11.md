# [hard/codebase_src_items.zig] - Chunk 11

**Type:** api
**Keywords:** ZonElement, ItemStack, BaseItemIndex, parseRecipe, recipeList, main.stackAllocator
**Symbols:** parseRecipeItem, registerRecipes
**Concepts:** item recipes, Zon element parsing, error handling, recipe registration

## Summary
This chunk defines functions for parsing item recipes from Zon elements and registering them into a global list.

## Explanation
The `parseRecipeItem` function takes a ZonElement, extracts an item ID and amount, trims whitespace, parses the amount if present, and then looks up the base item by ID. If the item is not found, it returns an error. The `registerRecipes` function iterates over a slice of recipe Zon elements, attempts to parse each one into a recipe using `recipes.parseRecipe`, and logs an error message if parsing fails, skipping that recipe.

## Code Example
```zig
pub fn registerRecipes(zon: ZonElement) void {
	for (zon.toSlice()) |recipeZon| {
		recipes.parseRecipe(recipeZon, &recipeList) catch |err| {
			const recipeString = recipeZon.toString(main.stackAllocator);
			defer main.stackAllocator.free(recipeString);
			std.log.err("Skipping recipe with error {s}:\n{s}", .{@errorName(err), recipeString});
			continue;
		};
	}
}
```

## Related Questions
- How does the `parseRecipeItem` function handle whitespace in item IDs?
- What error is returned if an item is not found during parsing?
- Where does the `registerRecipes` function log error messages?
- How does the `registerRecipes` function handle multiple recipes?
- What is the purpose of the `main.stackAllocator` in this chunk?
- How does the `parseRecipeItem` function determine the amount of an item?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_11*
