# [issues/issue_2037.md] - Issue #2037 discussion

**Type:** review
**Keywords:** addons, recipes, identifiers, disable, overwrite, modify, behavior, flags
**Symbols:** cubyz:recipe_marble_tile, inputs, output, mode, overwrite, disable, modify
**Concepts:** uniqueness, modularity, compatibility

## Summary
Discussion on allowing addons to disable or block recipes in Cubyz, focusing on unique recipe identifiers and different modes of handling existing recipes.

## Explanation
Discussion on allowing addons to disable or block recipes in Cubyz, focusing on unique recipe identifiers and different modes of handling existing recipes. The user proposes assigning unique identifiers to recipes to manage them effectively. The maintainer suggests that recipes can already be uniquely identified by their behavior and provides concrete examples for disabling and modifying recipes using specific syntax:

To disable a recipe:
```zig.zon
{
    .disable = true,
    .inputs = .{"cubyz:marble"},
    .output = "cubyz:marble_tile",
}
```

To modify an existing recipe:
```zig.zon
{
    .inputs = .{"cubyz:marble", "cubyz:chisel"},
    .output = "cubyz:marble_tile",
}
```
The maintainer's approach addresses these concerns by providing clear syntax for disabling and modifying recipes without needing new modes like 'overwrite' or 'modify'. The discussion highlights potential issues with managing recipe IDs and the complexity of handling different addon interactions. The maintainer's approach aims to simplify this process by focusing on behavior-based identification and clear syntax for modification.

**Modes of Handling Existing Recipes:*

1. **Overwrite:** Allows an addon to overwrite what currently is loaded if it exists.
   ```zig.zon
{
    .mode = .overwrite,
    .identifier = "cubyz:recipe_marble_tile",
    .inputs = .{"cubyz:marble"},
    .output = "cubyz:marble_tile",
}
```

2. **Disable:** Lets an addon disable the recipe without questions asked, but does not account for a different addon overwriting it.
   ```zig.zon
{
    .mode = .disable,
    .identifier = "cubyz:recipe_marble_tile",
}
```

3. **Modify:** Cubyz will try to join the original recipe with the new one based on modifications without needing to overwrite the whole recipe, but this is not allowed if the recipe is disabled.
   ```zig.zon
{
    .mode = .modify,
    .identifier = "cubyz:recipe_marble_tile",
    .inputs = .{"3 cubyz:marble"},
}
```

## Related Questions
- How does the current system handle recipe conflicts between addons?
- What are the potential performance implications of adding unique identifiers to recipes?
- Can the 'disable' flag be used to prevent other addons from overwriting a recipe?
- How would the 'modify' mode work in practice, and what are its limitations?
- What is the impact on backwards compatibility with existing addons when introducing new recipe handling modes?

*Source: unknown | chunk_id: github_issue_2037_discussion*
