# [issues/issue_2235.md] - Issue #2235 discussion

**Type:** review
**Keywords:** crash, colors, tool materials, lighting, threshold
**Concepts:** lighting calculations, game stability

## Summary
The game crashes when specifying less than 5 colors for tool materials. The discussion suggests that the issue might be related to lighting calculations.

## Explanation
The user reported that the game crashes when fewer than 5 colors are specified for tool materials. The discussion indicates a potential bug in the lighting calculation logic, where the number of colors is being reduced to 4 if it falls below this threshold. This could lead to an unexpected behavior or crash.

## Related Questions
- What is the current logic for handling fewer than 5 colors in tool materials?
- Is there a specific function or module responsible for lighting calculations?
- How does the game handle cases where the number of colors is less than 4?
- Are there any existing tests that cover scenarios with fewer than 5 colors?
- What changes are needed to allow an arbitrary number of colors without crashing?
- Is there a risk of introducing new bugs by modifying the lighting calculation logic?

*Source: unknown | chunk_id: github_issue_2235_discussion*
