# [issues/issue_2235.md] - Issue #2235 discussion

**Type:** review
**Keywords:** crash, colors, tool materials, lighting, threshold
**Concepts:** lighting calculations, game stability

## Summary
The game crashes when specifying less than 5 colors for tool materials. The discussion suggests that the issue might be related to lighting calculations.

## Explanation
The game crashes when specifying fewer than 5 colors for tool materials. According to a user comment, if the number of colors is reduced below 4, it causes unexpected behavior or a crash. This indicates a potential bug in the logic handling color thresholds and lighting calculations. The current logic appears to reduce the number of colors to 4 if it falls below this threshold. The user provided an image showing that reducing the number of colors below 4 results in unexpected behavior, suggesting that the game might be defaulting to a hardcoded value of 4 colors for lighting calculations.

## Related Questions
- What is the current logic for handling fewer than 5 colors in tool materials?
- Is there a specific function or module responsible for lighting calculations?
- How does the game handle cases where the number of colors is less than 4?
- Are there any existing tests that cover scenarios with fewer than 5 colors?
- What changes are needed to allow an arbitrary number of colors without crashing?
- Is there a risk of introducing new bugs by modifying the lighting calculation logic?

*Source: unknown | chunk_id: github_issue_2235_discussion*
