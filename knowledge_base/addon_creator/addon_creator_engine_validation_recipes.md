# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk recipes

**Type:** reference
**Keywords:** reversible, InvalidReversibleRecipe, recipe-defaults, symbolic-pattern-matching
**Symbols:** items/recipes.zig, parseRecipe
**Concepts:** engine-default-values, validation-errors

## Summary
Exact engine-side behavior for Cubyz recipe fields not exposed by the Addon Creator website,
read directly from `items/recipes.zig: parseRecipe()`.

## Explanation
The website's simple `.inputs = .{...}, .output = "..."` format maps directly and works as-is.
Two things the website doesn't expose at all:

- `.reversible` (bool, default `false`): if true, the engine auto-generates the reverse recipe
  (output becomes an input and vice versa). This requires the recipe have exactly 2 items total
  (1 input + 1 output) -- on any other combination, parsing fails with
  `error.InvalidReversibleRecipe`.
- A much more powerful symbolic pattern-matching system (`{symbol}` wildcards in item ids, e.g.
  `"foo:{bar}/{baz}"`) for recipes that match families of items rather than one exact item.
  Entirely hand-edit only, not exposed by the website.

## Related Questions
- What does the .reversible field do on a Cubyz recipe, and what's its default?
- What's the limitation on a reversible Cubyz recipe?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_recipes*
