# [issues/issue_1038.md] - Issue #1038 discussion

**Type:** review
**Keywords:** inside faces, walls, culled, variant models, rendering problem
**Concepts:** rendering, culled

## Summary
The issue discusses inside faces of walls not being culled in Cubyz.

## Explanation
The discussion revolves around a rendering problem where the inside faces of walls are visible, which is undesirable. The maintainer suggests that there might be no solution other than manually creating all 16 variant models to address this issue.

## Related Questions
- What is the current state of the rendering engine in Cubyz?
- Are there any plans to implement automatic culling for inside faces?
- How does manual model creation impact performance and maintainability?
- Can the issue be resolved by adjusting the shader code?
- Is there a way to detect and remove inside faces during the mesh generation process?
- What are the potential side effects of hand-crafting all 16 variant models?

*Source: unknown | chunk_id: github_issue_1038_discussion*
