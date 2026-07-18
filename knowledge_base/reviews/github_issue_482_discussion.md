# [issues/issue_482.md] - Issue #482 discussion

**Type:** review
**Keywords:** LOD leaves, texture optimization, culling performance, replacement block, torches, air in LOD
**Concepts:** Level of Detail (LOD), Texture Optimization, Rendering Efficiency

## Summary
Discussion on optimizing LOD (Level of Detail) for leaves blocks by using a different texture and potentially replacing certain blocks like torches with air.

## Explanation
The discussion revolves around improving the rendering efficiency of leaves in lower levels of detail (LOD). The maintainer suggests using an opaque texture for LOD leaves to enhance culling performance. Additionally, there is a proposal to define a separate LOD replacement block that could replace base blocks like torches with air in LOD states, aiming to improve visual quality by removing unnecessary details.

## Related Questions
- What is the proposed method for optimizing LOD leaves?
- How does using an opaque texture improve culling performance?
- Why is there a suggestion to replace torches with air in LOD states?
- What are the potential benefits of defining a separate LOD replacement block?
- How might this optimization affect the visual quality of the game?
- Are there any considerations for backwards compatibility with existing block definitions?

*Source: unknown | chunk_id: github_issue_482_discussion*
