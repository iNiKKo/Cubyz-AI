# [issues/issue_2044.md] - Issue #2044 discussion

**Type:** review
**Keywords:** secondary child biome, primary child biome, spawn outside, intended parent biome, chance of 0, biome generation bug
**Concepts:** biome generation, hierarchical relationships, spawn chance

## Summary
The issue involves a secondary child biome spawning outside of its intended parent biome despite having a chance of 0.

## Explanation
The issue involves a secondary child biome spawning outside of its intended parent biome despite having a spawn chance of 0. When a secondary child biome is nested inside a primary child biome, it frequently spawns directly inside the parent biome or even spills into neighboring biomes. This behavior suggests a bug in the biome generation algorithm that fails to properly enforce the hierarchical relationship between biomes. Both biomes (oasis and oasis_water) have a chance of 0 but still spawn outside their intended parent biome. An attached test datapack (oasis_test.zip) demonstrates this issue in a simple addon containing two biomes - oasis and oasis_water. For enhanced visibility, the primary child biome has its ground block set to cyan chalk and the secondary child biome has its ground block set to red chalk, making it easier to see where each biome is supposed to spawn.

## Related Questions
- What specific ground blocks were used to make the problem more visible?
- Where can I find the attached test datapack for this issue?

*Source: unknown | chunk_id: github_issue_2044_discussion*
