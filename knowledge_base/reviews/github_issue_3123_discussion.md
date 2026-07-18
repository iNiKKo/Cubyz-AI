# [issues/issue_3123.md] - Issue #3123 discussion

**Type:** review
**Keywords:** sub-biomes, song, parent biome, stone rock, main menu song, #732
**Concepts:** bug, inheritance, default behavior

## Summary
The issue discusses sub-biomes playing a default song instead of their parent biome's song, with maintainers noting that the behavior is expected due to multiple possible parent biomes and that it should have been resolved by a previous commit.

## Explanation
The discussion revolves around a bug report where sub-biomes are observed to play the main menu song instead of inheriting their parent biome's music. The maintainers clarify that this behavior is intentional because a single sub-biome can potentially spawn in multiple parent biomes, making it impossible for it to consistently play one specific song. Additionally, they mention that this issue should have been addressed by a previous commit (#732), suggesting that the fix might not have fully resolved the problem or there could be other underlying issues.

## Related Questions
- What changes were made in commit #732 to address the issue with sub-biomes playing the wrong song?
- How does Cubyz handle multiple parent biomes for a single sub-biome, and why is this relevant to the music playback issue?
- Is there a way to configure sub-biomes to play their parent biome's song even if they have multiple potential parents?
- What are the implications of having multiple parent biomes on the design of Cubyz's biome system?
- Can you provide more details on how the music playback is implemented in Cubyz and why it defaults to the main menu song for sub-biomes?
- Are there any plans to revisit or improve the handling of music playback in sub-biomes with multiple parent biomes?

*Source: unknown | chunk_id: github_issue_3123_discussion*
