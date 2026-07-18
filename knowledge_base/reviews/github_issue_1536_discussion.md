# [issues/issue_1536.md] - Issue #1536 discussion

**Type:** review
**Keywords:** optimization, 1x1 textures, pitch-black light, Terraria tile culling, dark caves
**Concepts:** occlusion culling, texture rendering

## Summary
The issue discusses a potential optimization for drawing 1x1 textures on blocks with pitch-black light values, comparing it to Terraria's tile culling method.

## Explanation
The maintainer suggests that existing occlusion culling already handles most dark caves and that the proposed optimization is likely unnecessary due to the small size of most textures. The discussion focuses on whether this new optimization would provide significant benefits given the current implementation.

## Related Questions
- What is the current implementation of occlusion culling in Cubyz?
- How does the size of textures affect rendering performance in Cubyz?
- Is there a way to measure the impact of texture size on rendering efficiency?
- Could implementing this optimization lead to any unintended side effects?
- How does the proposed optimization compare to existing culling methods?
- What are the potential benefits and drawbacks of drawing 1x1 textures with pitch-black light values?

*Source: unknown | chunk_id: github_issue_1536_discussion*
