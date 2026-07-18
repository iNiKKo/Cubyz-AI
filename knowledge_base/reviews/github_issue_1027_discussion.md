# [issues/issue_1027.md] - Issue #1027 discussion

**Type:** review
**Keywords:** sub-biomes, spawn, center bias, #1026, #917
**Concepts:** biome generation, parameter tuning

## Summary
The issue discusses sub-biomes spawning only next to each other, with a bias towards the center of the parent biome.

## Explanation
The discussion revolves around an issue where sub-biomes are not evenly distributed but tend to cluster together near the center of their parent biomes. The maintainer suggests that this might be due to incorrect parameter settings and indicates that it should have been resolved by a previous change (#917). However, there is uncertainty about whether the parameters have been correctly adjusted.

## Related Questions
- What changes were made in #917 to address the sub-biome generation issue?
- Are there any specific parameters that control the distribution of sub-biomes?
- How can we verify if the parameters are correctly set for even sub-biome distribution?
- Is there a way to test the sub-biome generation algorithm in isolation?
- What is the expected behavior of sub-biomes in relation to their parent biomes?
- Are there any known limitations or edge cases with the current biome generation system?

*Source: unknown | chunk_id: github_issue_1027_discussion*
