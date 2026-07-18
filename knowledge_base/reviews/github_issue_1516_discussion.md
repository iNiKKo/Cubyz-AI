# [issues/issue_1516.md] - Issue #1516 discussion

**Type:** review
**Keywords:** scatter, direction, particle system, cone, spawn mode, anchor, point spawn, plane spawn, spread, attachment point
**Concepts:** particle system, direction mode, scatter parameter, cone shape, spawn mode, attachment point

## Summary
Discussion about adding a scatter parameter to the .direction in the particle system, with concerns over extending the direction mode and maintaining clarity.

## Explanation
The discussion revolves around enhancing the particle system by introducing a scatter parameter to the .direction feature. The maintainer initially suggests that this might be similar to spawning particles within a cone shape but clarifies that the user is looking for a 'spread' effect where particles are directed outward from a central point with some angular variance. The maintainer expresses reluctance to add more parameters to the direction mode, preferring instead to introduce a new spawn mode called 'Anchor DirectionMode' that would ensure particles spawn at the emitter's attachment point and spread outward. The user argues that an anchor is not suitable for point spawns and provides a visual example of how they envision the scatter effect working. There is also mention of wanting this feature for plane spawn types to allow particles to be directed in a specific direction while spreading slightly.

## Related Questions
- How does the scatter parameter differ from spawning particles within a cone shape?
- What is the maintainer's concern about adding more parameters to the direction mode?
- Why does the user argue that an anchor is not suitable for point spawns?
- Can you explain how the 'Anchor DirectionMode' would work in detail?
- How would the scatter feature be implemented for plane spawn types?
- What are the potential performance implications of adding a new spawn mode?

*Source: unknown | chunk_id: github_issue_1516_discussion*
