# [issues/issue_692.md] - Issue #692 discussion

**Type:** review
**Keywords:** physics, fixed rate, vsync, input lag, collision margin, catch-up mechanic, GPU rendering time
**Concepts:** framerate independence, physics update separation, input lag, collision detection

## Summary
Discussion on separating update loops in Cubyz to make physics updates independent of the render frame rate, addressing issues like #599 and #533.

## Explanation
Discussion on separating update loops in Cubyz to make physics updates independent of the render frame rate, addressing issues like #599 and #533. The issue proposes fixing physics to run at a fixed rate (e.g., 60 or 120fps) with a catch-up mechanic if rendering is slow. Benefits include resolving inconsistencies in player movement (#599) by ensuring updates don't happen too frequently, and alleviating input lag issues (#533) through multiple physics frames per render frame. Drawbacks involve requiring interpolation of physics for rendering (already implemented for networking), increased input lag without vsync due to one physics tick delay, and additional work splitting physics from non-physics updates. The maintainer notes that #599 is caused by player movement smaller than a collision margin of 0.1 units; a solution involves storing exact collision results without margins. For #533, implementing the catch-up mechanic alone might not suffice if GPU rendering time significantly exceeds physics update time (e.g., if the GPU takes 16ms to render and physics only take 0.1ms).

## Related Questions
- What are the potential benefits of separating physics updates from rendering in Cubyz?
- How might increasing input lag for players without vsync be mitigated?
- What is the proposed solution to issue #599 regarding player movement and collision margins?
- Can the catch-up mechanic effectively solve issue #533, and why or why not?
- How does separating player-driven actions from physics updates impact performance in Cubyz?
- What are the implications of making vsync only affect rendering on the overall game experience?

*Source: unknown | chunk_id: github_issue_692_discussion*
