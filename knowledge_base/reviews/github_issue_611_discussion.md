# [issues/issue_611.md] - Issue #611 discussion

**Type:** review
**Keywords:** ores, stone types, texture generation, shader recalculations, block breaking animation, resource usage
**Concepts:** texture generation, shader recalculations, resource management

## Summary
Discussion on handling ores on different stone types with three main options: letting addon creators handle it (with duplicate work), generating new block types during startup (costing index space), or using rotation mode to store source blocks in the data section. The maintainer suggests drawing overlays separately for efficiency.

## Explanation
The issue revolves around how to manage ores on different stone types without causing excessive resource usage. There are three main options discussed:

1. **Don't handle it**: Let addon creators deal with each ore and stone combination individually, which would result in a lot of duplicate work but allow for unique textures.
2. **Generate new block types during startup**: Create numerous new block types for all combinations of ores and stones, which would consume significant index space and reduce the maximum number of possible blocks.
3. **Use rotation mode**: Store the source block information in the 16-bit data section to manage different ore-stone combinations efficiently.

The maintainer suggests drawing overlays in a separate face similar to the block breaking animation approach, which avoids generating numerous textures and simplifies shader complexity.

## Related Questions
- What are the potential performance impacts of generating textures for each ore and stone combination?
- How does drawing overlays in a separate face compare to recalculating textures in a shader in terms of resource usage?
- Can you explain the benefits of using rotation mode and storing source block information in the 16-bit data section?
- What are the trade-offs between allowing addon creators to handle ore textures versus centralizing texture management?
- How does the block breaking animation's approach to overlays influence the decision-making process for handling ores on different stone types?

*Source: unknown | chunk_id: github_issue_611_discussion*
