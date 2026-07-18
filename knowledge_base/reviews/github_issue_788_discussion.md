# [issues/issue_788.md] - Issue #788 discussion

**Type:** review
**Keywords:** cloth z-fights, side pixels, same color, visual artifacts, rendering issue
**Concepts:** z-fighting, rendering

## Summary
The maintainer suggests fixing cloth z-fighting by making side pixels have the same color.

## Explanation
The issue involves visual artifacts where cloth textures meet at corners, causing z-fighting. The maintainer proposes a simple solution to address this by ensuring that all side pixels of the cloth have the same color, which should mitigate the visual issues without requiring complex changes to the rendering logic.

## Related Questions
- What is the current implementation of cloth rendering that causes z-fighting?
- How can making side pixels have the same color resolve z-fighting issues?
- Are there any potential performance implications of changing pixel colors in this way?
- Could this solution introduce new visual artifacts or other rendering issues?
- Is there a more comprehensive fix for z-fighting that could be considered?
- What are the trade-offs between simplicity and effectiveness in resolving z-fighting?

*Source: unknown | chunk_id: github_issue_788_discussion*
