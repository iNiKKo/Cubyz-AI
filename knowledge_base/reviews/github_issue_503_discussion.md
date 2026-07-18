# [issues/issue_503.md] - Issue #503 discussion

**Type:** review
**Keywords:** fence hitbox, bounding box, cylinder-triangle intersection, collision issues, player movement
**Concepts:** collision detection, bounding box, intersection tests

## Summary
The discussion revolves around improving fence collision detection by using a separate bounding box for each model to avoid issues like getting caught between fence posts or bouncing up and down.

## Explanation
The user suggests that using a separate bounding box for each model would provide more accurate collision detection, addressing the problem of players getting stuck between fence posts or experiencing bouncy movements when walking on top of fences. The maintainer acknowledges this solution but expresses uncertainty about implementing cylinder-triangle intersection tests, which are necessary for precise collision detection with complex shapes like fences.

## Related Questions
- How can we implement cylinder-triangle intersection tests for better collision detection?
- What are the potential performance implications of using separate bounding boxes for each model?
- Are there any existing libraries or tools that can help with implementing complex intersection tests in Cubyz?
- How does the current collision detection system handle fences, and what specific issues arise?
- Can we optimize the collision detection algorithm to reduce computational overhead while maintaining accuracy?
- What are the trade-offs between using a single bounding box and multiple bounding boxes for collision detection?

*Source: unknown | chunk_id: github_issue_503_discussion*
