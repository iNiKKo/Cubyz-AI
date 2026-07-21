# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 3

**Type:** documentation
**Keywords:** recipes.zig, parseRecipe, reversible, symbolic pattern matching, InvalidReversibleRecipe
**Symbols:** parseRecipe()

## Summary
Engine-side recipe parsing details not exposed by the Addon Creator website, read directly from `items/recipes.zig: parseRecipe()`.

## Explanation
The website's simple `.inputs = .{...}, .output = "..."` format maps directly and works as-is. Two things the website doesn't expose: `.reversible` (bool, default `false`) -- if true, auto-generates the reverse recipe (output becomes an input and vice versa), but requires the recipe have exactly 2 items total (1 input + 1 output) or parsing fails with `error.InvalidReversibleRecipe`. And a much more powerful symbolic pattern-matching system (`{symbol}` wildcards in item ids, e.g. `"foo:{bar}/{baz}"`) for recipes that match families of items rather than one exact item -- entirely hand-edit only.

## Related Questions
- What does the .reversible field do on a Cubyz recipe, and what's its default?
- What's the limitation on a reversible Cubyz recipe?
- What symbolic pattern-matching feature does Cubyz's recipe system support that the website doesn't expose?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_3*
