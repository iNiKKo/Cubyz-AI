# [issues/issue_1516.md] - Issue #1516 discussion

**Type:** review
**Keywords:** scatter, direction, particle system, cone, spawn mode, anchor, point spawn, plane spawn, spread, attachment point
**Concepts:** particle system, direction mode, scatter parameter, cone shape, spawn mode, attachment point

## Summary
Discussion about adding a scatter parameter to the .direction in the particle system, with concerns over extending the direction mode and maintaining clarity.

## Explanation
The discussion revolves around enhancing the particle system by introducing a scatter parameter to the .direction feature. The maintainer initially suggests that this might be similar to spawning particles within a cone shape but clarifies that the user is looking for a 'spread' effect where particles are directed outward from a central point with an angular variance of pi/4 (for example, a semisphere). The maintainer expresses reluctance to add more parameters to the direction mode, preferring instead to introduce a new spawn mode called 'Anchor DirectionMode', which should work like spread but guarantee that the particle spawns in the center or attachment point of the spawn shape. The user argues that an anchor is not suitable for point spawns and provides a visual example of how they envision the scatter effect working: particles would be directed outward from a central point with some angular variance, forming a cone-like distribution. There is also mention of wanting this feature for plane spawn types to allow particles to be directed in a specific direction while spreading slightly around that direction.

## Related Questions
- What is the exact angle used as an example for spread?
- How does 'Anchor DirectionMode' guarantee particle spawning at the attachment point?
- Why is an anchor not suitable for point spawns?

*Source: unknown | chunk_id: github_issue_1516_discussion*
