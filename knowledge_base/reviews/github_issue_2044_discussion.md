# [issues/issue_2044.md] - Issue #2044 discussion

**Type:** review
**Keywords:** secondary child biome, primary child biome, spawn outside, intended parent biome, chance of 0, biome generation bug
**Concepts:** biome generation, hierarchical relationships, spawn chance

## Summary
The issue involves a secondary child biome spawning outside of its intended parent biome despite having a chance of 0.

## Explanation
The problem arises when a secondary child biome is nested inside a primary child biome. Despite both biomes having a spawn chance of 0, the secondary child biome frequently spawns directly inside the parent biome or even spills into neighboring biomes. This behavior suggests a bug in the biome generation algorithm that fails to properly enforce the hierarchical relationship between biomes.

## Related Questions
- What is the current algorithm for determining the spawn location of child biomes?
- Are there any known issues with biome generation in Cubyz that could cause this behavior?
- How does the spawn chance setting interact with the hierarchy of biomes during generation?
- Is there a specific condition or edge case where the secondary child biome might spawn outside its intended parent?
- What changes need to be made to ensure that child biomes respect their parent's boundaries during generation?
- Are there any existing tests for biome generation that could help identify and fix this issue?

*Source: unknown | chunk_id: github_issue_2044_discussion*
