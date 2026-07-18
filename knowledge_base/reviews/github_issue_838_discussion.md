# [issues/issue_838.md] - Issue #838 discussion

**Type:** review
**Keywords:** Rainbow Forest LODs, world gen slows, separate processing, gasses don't need to be precise, render distance
**Concepts:** performance optimization, world generation, LOD (Level of Detail), fog processing

## Summary
Discussion about performance issues with Rainbow Forest LOD generation and potential separation of fog processing.

## Explanation
The discussion revolves around a performance issue where the world generation slows down significantly when Rainbow Forest LODs are in render distance. The maintainer suggests separating fog processing from block processing to improve performance, as gasses do not need precise calculations.

## Related Questions
- What is the current performance impact of Rainbow Forest LOD generation?
- Why does separating fog processing from block processing potentially improve performance?
- Are there any other LODs that experience similar performance issues?
- How can the separation of fog processing be implemented without affecting visual quality?
- What are the potential trade-offs of separating fog and block processing?
- Is there a way to optimize the current fog processing algorithm for better performance?

*Source: unknown | chunk_id: github_issue_838_discussion*
