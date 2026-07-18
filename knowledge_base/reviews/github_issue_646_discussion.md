# [issues/issue_646.md] - Issue #646 discussion

**Type:** review
**Keywords:** LOD5, render distance, memory usage, world loading speed, #647, heightmap based LOD
**Concepts:** Level of Detail (LOD), Render Distance, Memory Usage

## Summary
Discussion about reducing or removing LOD5 due to recent increases in render distance and potential replacement by heightmap-based LOD.

## Explanation
The issue discusses the current poor quality and resource cost of LOD5, which is the lowest level of detail. With increased base render distances, there's a suggestion to remove LOD5 to improve world loading speed and reduce memory usage. The maintainer comments that this could be addressed with the addition of another feature (#647), implying that rendering LOD5 would become less necessary.

## Related Questions
- What are the current issues with LOD5?
- How does increasing render distance affect LOD5?
- What is the proposed replacement for LOD5?
- Why might rendering LOD5 become less necessary with feature #647?
- How would removing LOD5 impact world loading speed?
- What are the potential memory usage benefits of removing LOD5?

*Source: unknown | chunk_id: github_issue_646_discussion*
