# [issues/issue_696.md] - Issue #696 discussion

**Type:** review
**Keywords:** z-fighting, chiseled blocks, glass, complete blocks, canSeeNeighbor, glPolygonOffsetClamp, OpenGL 4.6, transparent backfaces, opaque terrain, walls
**Symbols:** canSeeNeighbor, glPolygonOffsetClamp, glPolygonOffset
**Concepts:** z-fighting, OpenGL, transparent backfaces, opaque terrain

## Summary
Discussion about z-fighting issues between chiseled blocks and glass, with potential solutions involving OpenGL functions.

## Explanation
Discussion about z-fighting issues between chiseled blocks and glass, with potential solutions involving OpenGL functions. The issue revolves around z-fighting occurring when glass is placed adjacent to a chiseled block. The maintainer explains that complete blocks have the `canSeeNeighbor` bits set to false, which prevents drawing transparent backfaces towards opaque terrain. This setting ensures that only necessary faces are rendered for complete blocks, avoiding unnecessary rendering of transparent backfaces toward opaque terrain. Similar problems are noted for walls, where z-fighting also occurs due to the same underlying issue with block adjacency and transparency. The maintainer mentions that there is a `glPolygonOffsetClamp` function in the OpenGL 4.6 specification, which allows limiting the maximum offset and could help avoid the troubles of `glPolygonOffset`. This function could potentially mitigate z-fighting issues by providing more control over polygon offsets.

## Related Questions
- What is the purpose of the `canSeeNeighbor` bits in block rendering?
- How does `glPolygonOffsetClamp` differ from `glPolygonOffset`?
- Are there any other OpenGL functions that could help mitigate z-fighting issues?
- Can you explain why complete blocks have `canSeeNeighbor` set to false?
- What are the potential performance implications of using `glPolygonOffsetClamp`?
- How does the current block rendering logic handle adjacent transparent and opaque blocks?
- Are there any plans to update the block rendering logic to prevent z-fighting in future versions?

*Source: unknown | chunk_id: github_issue_696_discussion*
