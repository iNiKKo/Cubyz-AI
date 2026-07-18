# [issues/issue_845.md] - Issue #845 discussion

**Type:** review
**Keywords:** cross-shaped vegetation, billboard rendering, LOD0.5, backface culling, swamps, jungles, dense environments, mesh replacement
**Concepts:** backface culling, level of detail (LOD), rendering optimization

## Summary
Discussion about optimizing cross-shaped vegetation rendering by replacing them with billboards at 0.5 LOD to reduce face count.

## Explanation
The issue discusses the potential optimization of rendering cross-shaped vegetation like grass, ferns, and vines in Cubyz. The current implementation excludes these from backface culling and draws both sides of the block separately, resulting in four times more faces than necessary. However, the LOD0.5 system is currently unable to handle replacing mesh components with different ones, such as billboards. The maintainers predict this could become a significant issue in dense environments like swamps and jungles.

## Related Questions
- How does the current LOD0.5 system handle mesh replacements?
- What is the impact of backface culling on vegetation rendering performance?
- Can the LOD0.5 system be modified to support billboard rendering for vegetation?
- What are the potential performance improvements from using billboards in dense environments?
- How does excluding grass from backface culling affect rendering efficiency?
- Are there any architectural limitations preventing mesh replacement in LOD0.5?
- What is the expected impact of this optimization on memory usage?
- How can the prediction about swamps and jungles becoming an issue be verified?
- What are the potential trade-offs between visual fidelity and performance in vegetation rendering?
- How does the current implementation handle dense vegetation like vines and ferns?

*Source: unknown | chunk_id: github_issue_845_discussion*
