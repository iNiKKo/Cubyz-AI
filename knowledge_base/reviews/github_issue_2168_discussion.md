# [issues/issue_2168.md] - Issue #2168 discussion

**Type:** review
**Keywords:** rendering, air, biome, fog, colors, models, stairs, performance, feasibility
**Concepts:** greedy mesher, biome rendering, fog colors, raymarching

## Summary
Discussion about rendering air differently based on biome, focusing on fog colors and feasibility.

## Explanation
The issue discusses the possibility of modifying the greedy mesher to render air faces differently depending on the biome. The main focus is on implementing biome-specific fog colors. The maintainers note that while biome fog colors already exist, extending this effect to models that don't fill their cubes (like stairs) would require complex raymarching, which is not feasible due to performance constraints.

## Related Questions
- What is the current implementation of biome fog colors in Cubyz?
- How does the greedy mesher currently handle air faces between biomes?
- What are the performance implications of implementing raymarching for non-cube models?
- Are there any existing solutions or workarounds for rendering air differently based on biome?
- Can the current fog block system be adapted to achieve the desired effect without raymarching?
- How would extending fog colors to non-cube models impact the overall rendering pipeline?

*Source: unknown | chunk_id: github_issue_2168_discussion*
