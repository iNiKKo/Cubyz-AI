# [issues/issue_182.md] - Issue #182 discussion

**Type:** review
**Keywords:** out-of-memory error, Linux, chunk allocation, mesh loadlist, memory pools, palette compression
**Concepts:** memory management, render distance, palette compression

## Summary
The issue involves an out-of-memory error on Linux when too many chunks are allocated, likely due to the mesh loadlist growing indefinitely without removal.

## Explanation
The issue involves an out-of-memory error on Linux when too many chunks are allocated, likely due to the mesh loadlist growing indefinitely without removal. The problem stems from the lack of a mechanism for removing meshes from memory once they fall out of render distance. This is exacerbated by increasing base render distances and the discontinuation of memory pools since the introduction of palette compression, which previously helped manage memory usage more efficiently.

## Related Questions
- What is the current mechanism for removing meshes from memory when they fall out of render distance?
- How does increasing base render distance contribute to the out-of-memory error?
- Can reverting to memory pools help mitigate the issue with palette compression?
- Are there any plans to implement a cleanup mechanism for the mesh loadlist?
- What is the impact of palette compression on memory usage in Cubyz?
- How can we optimize memory management to prevent out-of-memory errors on Linux?

*Source: unknown | chunk_id: github_issue_182_discussion*
