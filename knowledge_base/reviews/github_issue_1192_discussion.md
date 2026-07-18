# [issues/issue_1192.md] - Issue #1192 discussion

**Type:** review
**Keywords:** brightness, RGB, overexposure, repropagation, lighting, Cubyz, mushrooms, crystals
**Concepts:** flood-fill lighting, light mixing, performance optimization

## Summary
Discussion about improving light mixing and cascades in Cubyz, focusing on limitations of flood-fill lighting and potential performance issues.

## Explanation
The discussion revolves around the inherent limitation of flood-fill lighting in Cubyz, where multiple identical light sources do not increase brightness. The maintainers explore alternative approaches such as adding a 'brightness' value that multiplies with RGB values to create an overexposure effect. However, they quickly dismiss this idea due to potential performance issues, specifically the need to repropagate all light sources in the area whenever a block is placed, which would be computationally expensive.

## Related Questions
- What is the current lighting technique used in Cubyz?
- Why does flood-fill lighting not allow brightness to add up from multiple sources?
- How would adding a 'brightness' value affect light propagation?
- What are the potential performance implications of repropagating all light sources?
- Can you explain the concept of overexposure in this context?
- Is there any alternative lighting technique that could be considered for Cubyz?

*Source: unknown | chunk_id: github_issue_1192_discussion*
