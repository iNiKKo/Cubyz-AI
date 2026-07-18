# [issues/issue_611.md] - Issue #611 discussion

**Type:** review
**Keywords:** ores, stone types, texture generation, shader recalculations, block breaking animation, resource usage
**Concepts:** texture generation, shader recalculations, resource management

## Summary
Discussion on handling ores on different stone types with options for texture generation or shader recalculations.

## Explanation
The issue revolves around how to manage the visual representation of ores placed on various stone types without causing excessive resource usage. The maintainer suggests drawing the overlay in a separate face, similar to the block breaking animation, to avoid generating numerous textures and simplify the shader complexity.

## Related Questions
- What are the potential performance impacts of generating textures for each ore and stone combination?
- How does drawing overlays in a separate face compare to recalculating textures in a shader in terms of resource usage?
- Can you explain the benefits of using rotation mode and storing source block information in the 16-bit data section?
- What are the trade-offs between allowing addon creators to handle ore textures versus centralizing texture management?
- How does the block breaking animation's approach to overlays influence the decision-making process for handling ores on different stone types?
- What architectural considerations should be taken into account when deciding how to manage ore textures in Cubyz?

*Source: unknown | chunk_id: github_issue_611_discussion*
