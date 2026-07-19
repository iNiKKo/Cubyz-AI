# [issues/issue_482.md] - Issue #482 discussion

**Type:** review
**Keywords:** LOD leaves, texture optimization, culling performance, replacement block, torches, air in LOD
**Concepts:** Level of Detail (LOD), Texture Optimization, Rendering Efficiency

## Summary
Discussion on optimizing LOD (Level of Detail) for leaves blocks by using a different texture and potentially replacing certain blocks like torches with air.

## Explanation
Discussion on optimizing LOD (Level of Detail) for leaves blocks by using a different texture and potentially replacing certain blocks like torches with air. The maintainer suggests using an opaque texture for LOD leaves to enhance culling performance, which can be configured via the JSON format if it is not too expensive. Specifically, the JSON format properties that could be used include 'texture' and 'properties'. Additionally, there is a proposal to define a separate LOD replacement block that could replace base blocks like torches with air in LOD states, aiming to improve visual quality by removing unnecessary details and making LOD torches look better.

## Related Questions
- What specific JSON format properties are used for setting the texture and properties of LOD leaves?

*Source: unknown | chunk_id: github_issue_482_discussion*
