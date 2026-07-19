# [issues/issue_1192.md] - Issue #1192 discussion

**Type:** review
**Keywords:** brightness, RGB, overexposure, repropagation, lighting, Cubyz, mushrooms, crystals
**Concepts:** flood-fill lighting, light mixing, performance optimization

## Summary
Discussion about improving light mixing and cascades in Cubyz, focusing on limitations of flood-fill lighting and potential performance issues.

## Explanation
Discussion about improving light mixing and cascades in Cubyz, focusing on limitations of flood-fill lighting. The inherent limitation is that multiple identical light sources do not increase brightness. Maintainers explore an alternative approach involving a 'brightness' value that multiplies with RGB values to create an overexposure effect but dismiss this idea due to potential performance issues. Specifically, adding a 'brightness' value would require repropagating all light sources in the area whenever a block is placed, which is computationally expensive. The radius of influence for each light source is 32 blocks, and this could lead to significant performance problems if there are many crystals or other light-emitting blocks in the area.

## Related Questions
- What is the current lighting technique used in Cubyz?
- Why does flood-fill lighting not allow brightness to add up from multiple sources?
- How would adding a 'brightness' value affect light propagation?
- What are the potential performance implications of repropagating all light sources?
- Can you explain the concept of overexposure in this context?
- Is there any alternative lighting technique that could be considered for Cubyz?

*Source: unknown | chunk_id: github_issue_1192_discussion*
