# [issues/issue_1093.md] - Issue #1093 discussion

**Type:** review
**Keywords:** spawnpoint, radial check, random spots, origin point, 0, 0, efficiency, predictable, consistent
**Concepts:** performance, predictability

## Summary
Discussion about improving the spawnpoint selection method to use a radial check around (0, 0) instead of random spots.

## Explanation
The maintainer suggests that the current spawnpoint selection method, which checks random spots in the world, should be replaced with a more efficient approach. The proposed change is to perform a radial check around the origin point (0, 0). This would likely improve performance by reducing the number of random checks needed and potentially making the spawnpoint selection process more predictable and consistent.

## Related Questions
- What is the current method for selecting spawnpoints in Cubyz?
- How does the proposed radial check around (0, 0) improve performance compared to random spot checks?
- Are there any potential drawbacks to using a radial check for spawnpoint selection?
- How would implementing this change affect the overall user experience of spawning in the game?
- What is the expected impact on the codebase if this change is implemented?
- Is there a risk of introducing new bugs with this change, and how can they be mitigated?

*Source: unknown | chunk_id: github_issue_1093_discussion*
