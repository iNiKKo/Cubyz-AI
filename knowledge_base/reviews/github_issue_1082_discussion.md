# [issues/issue_1082.md] - Issue #1082 discussion

**Type:** review
**Keywords:** opaque blocks, drawing backfaces, fog effects, void blocks, commit #1324
**Symbols:** lava, void
**Concepts:** rendering, backface culling, visual effects

## Summary
The issue requires rendering backfaces of opaque blocks like lava and void to ensure correct visual effects.

## Explanation
The discussion indicates that the requirement for drawing backfaces extends beyond just lava to include void blocks introduced in a previous commit (#1324). This change is necessary to achieve the desired visual appearance, particularly for fog effects around opaque blocks. The maintainer's comment suggests that this fix should be applied uniformly across similar block types to maintain consistency and correctness in rendering.

## Related Questions
- What is the impact of enabling backface rendering on performance?
- How does this change affect the visual appearance of other opaque blocks?
- Are there any potential regressions in rendering quality with this fix?
- What are the implications for memory usage when drawing additional backfaces?
- How can we ensure that this fix is compatible with existing rendering pipelines?
- Is there a need to update shader code to handle backface rendering correctly?

*Source: unknown | chunk_id: github_issue_1082_discussion*
