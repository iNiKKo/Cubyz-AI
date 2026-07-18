# [issues/issue_2037.md] - Issue #2037 discussion

**Type:** review
**Keywords:** addons, recipes, identifiers, disable, overwrite, modify, behavior, flags
**Symbols:** cubyz:recipe_marble_tile, inputs, output, mode, overwrite, disable, modify
**Concepts:** uniqueness, modularity, compatibility

## Summary
Discussion on allowing addons to disable or block recipes in Cubyz, focusing on unique recipe identifiers and different modes of handling existing recipes.

## Explanation
The issue revolves around enabling addons to remove or modify recipes from the base game. The user proposes assigning unique identifiers to recipes to manage them effectively. The maintainer suggests that recipes can already be uniquely identified by their behavior, and proposes using a 'disable' flag to block recipes without needing new modes like 'overwrite' or 'modify'. The discussion highlights potential issues with managing recipe IDs and the complexity of handling different addon interactions.

## Related Questions
- How does the current system handle recipe conflicts between addons?
- What are the potential performance implications of adding unique identifiers to recipes?
- Can the 'disable' flag be used to prevent other addons from overwriting a recipe?
- How would the 'modify' mode work in practice, and what are its limitations?
- What is the impact on backwards compatibility with existing addons when introducing new recipe handling modes?
- How does the maintainer's approach address the issue of managing recipe IDs effectively?

*Source: unknown | chunk_id: github_issue_2037_discussion*
