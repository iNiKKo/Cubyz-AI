# [issues/issue_673.md] - Issue #673 discussion

**Type:** review
**Keywords:** OBJ tiles, hitbox, collision boxes, single block, gameplay flexibility, AABB bounding boxes
**Concepts:** hitbox, collision detection, performance optimization

## Summary
Discussion on fixing OBJ tiles with larger than one tile hitboxes.

## Explanation
The issue revolves around the broken hitbox for OBJ tiles that exceed the size of one tile. The maintainer considers this a trade-off between gameplay flexibility and performance optimization, as limiting hitboxes to single blocks reduces iteration overhead but may not be suitable for complex game mechanics like Minecraft's fences.

## Related Questions
- What is the current implementation of hitboxes in Cubyz?
- How does the use of AABB bounding boxes mitigate the impact of larger hitboxes?
- Are there any plans to implement larger hitboxes for gameplay purposes?
- What are the potential performance implications of allowing larger hitboxes?
- Can you provide examples of how Minecraft's fences handle collision detection?
- How might the current optimization strategy affect future game design?

*Source: unknown | chunk_id: github_issue_673_discussion*
