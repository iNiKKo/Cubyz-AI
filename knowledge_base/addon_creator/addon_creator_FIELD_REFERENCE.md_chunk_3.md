# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 3

**Type:** documentation
**Keywords:** recipes.html, saveRecipeToProject, recipeOutputSearch, recipeInputSearch
**Symbols:** recipeFilename, recipeOutputCount, recipeInputCount1-4

## Summary
Cubyz Addon Creator: Recipes form (`recipes.html`) field-to-export mapping.

## Explanation
Recipe ID/Filename (`recipeFilename`) is the key in `projectData.recipes{}` and becomes the output filename -- multiple recipes can share a file (array per filename). What item does this craft + Amount Made (`recipeOutputSearch`/`recipeOutputCount`) export as `.output = "{count} {item}"`, auto-namespaced -- **the count prefix is omitted if the count is 1**. Ingredient slots 1-4 plus counts (`recipeInputSearch1-4`/`recipeInputCount1-4`) export as `.inputs = .{"{count} {item}", ...}` -- empty slots are skipped, and the form supports **up to 4 ingredients**.

## Related Questions
- How many ingredient slots does the Cubyz Addon Creator's recipe form support?
- How does the Cubyz Addon Creator handle a recipe output count of exactly 1 in its export?
- Can multiple Cubyz recipes share the same output filename?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_3*
