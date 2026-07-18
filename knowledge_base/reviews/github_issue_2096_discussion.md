# [issues/issue_2096.md] - Issue #2096 discussion

**Type:** review
**Keywords:** abrupt fog changes, interpolate fog colors, air as fog block, biome border, smooth transition
**Concepts:** fog interpolation, biome transitions, visual smoothness

## Summary
The discussion revolves around making cave biome fog transitions less abrupt by interpolating between fog colors or simulating air as a fog block that changes based on biome.

## Explanation
The issue highlights that the current implementation of fog color changes in cave biomes is too sudden, leading to a jarring experience. The proposed solutions include gradually transitioning between fog colors as one moves across biome borders, similar to Minecraft's approach, or treating air as a fog block whose properties change based on the surrounding biome. The maintainer suggests that simply increasing the time it takes for the fog to adjust could also mitigate the abruptness.

## Related Questions
- How can we implement gradual fog color interpolation between biomes?
- What are the potential performance impacts of simulating air as a fog block?
- Can increasing the fog adjustment time resolve abrupt transitions without affecting visual quality?
- How does Minecraft handle fog transitions across biome borders?
- Are there any existing code patterns in Cubyz that can be adapted for smoother fog transitions?
- What are the trade-offs between smooth transitions and performance optimization in this context?

*Source: unknown | chunk_id: github_issue_2096_discussion*
