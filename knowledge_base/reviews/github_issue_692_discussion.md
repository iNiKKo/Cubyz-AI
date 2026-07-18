# [issues/issue_692.md] - Issue #692 discussion

**Type:** review
**Keywords:** physics, fixed rate, vsync, input lag, collision margin, catch-up mechanic, GPU rendering time
**Concepts:** framerate independence, physics update separation, input lag, collision detection

## Summary
Discussion on separating update loops in Cubyz to make physics updates independent of the render frame rate, addressing issues like #599 and #533.

## Explanation
The issue proposes fixing physics to run at a fixed rate to avoid inconsistencies. The maintainer highlights potential drawbacks such as increased input lag for players without vsync. The user suggests separating player-driven actions from the physics loop to mitigate this. There's also discussion on refining collision detection and implementing a catch-up mechanic for #533, with considerations around GPU rendering times.

## Related Questions
- What are the potential benefits of separating physics updates from rendering in Cubyz?
- How might increasing input lag for players without vsync be mitigated?
- What is the proposed solution to issue #599 regarding player movement and collision margins?
- Can the catch-up mechanic effectively solve issue #533, and why or why not?
- How does separating player-driven actions from physics updates impact performance in Cubyz?
- What are the implications of making vsync only affect rendering on the overall game experience?

*Source: unknown | chunk_id: github_issue_692_discussion*
