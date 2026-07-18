# [issues/issue_696.md] - Issue #696 discussion

**Type:** review
**Keywords:** z-fighting, chiseled blocks, glass, complete blocks, canSeeNeighbor, glPolygonOffsetClamp, OpenGL 4.6, transparent backfaces, opaque terrain, walls
**Symbols:** canSeeNeighbor, glPolygonOffsetClamp, glPolygonOffset
**Concepts:** z-fighting, OpenGL, transparent backfaces, opaque terrain

## Summary
Discussion about z-fighting issues between chiseled blocks and glass, with potential solutions involving OpenGL functions.

## Explanation
The issue revolves around z-fighting occurring when glass is placed adjacent to a chiseled block. The maintainer explains that complete blocks have the `canSeeNeighbor` bits set to false, which prevents drawing transparent backfaces towards opaque terrain. The maintainer also suggests using the `glPolygonOffsetClamp` function from OpenGL 4.6 specification as a potential solution to avoid issues with `glPolygonOffset`. Similar problems are noted for walls.

## Related Questions
- What is the purpose of the `canSeeNeighbor` bits in block rendering?
- How does `glPolygonOffsetClamp` differ from `glPolygonOffset`?
- Are there any other OpenGL functions that could help mitigate z-fighting issues?
- Can you explain why complete blocks have `canSeeNeighbor` set to false?
- What are the potential performance implications of using `glPolygonOffsetClamp`?
- How does the current block rendering logic handle adjacent transparent and opaque blocks?
- Are there any plans to update the block rendering logic to prevent z-fighting in future versions?
- Can you provide a code example demonstrating how to use `glPolygonOffsetClamp` to resolve z-fighting?
- What are the compatibility considerations for using `glPolygonOffsetClamp` across different hardware and drivers?
- How does the issue of z-fighting between chiseled blocks and glass affect user experience in Cubyz?

*Source: unknown | chunk_id: github_issue_696_discussion*
