# [issues/issue_3123.md] - Issue #3123 discussion

**Type:** review
**Keywords:** sub-biomes, song, parent biome, stone rock, main menu song, #732
**Concepts:** bug, inheritance, default behavior

## Summary
The issue discusses sub-biomes playing a default song instead of their parent biome's song, with maintainers noting that the behavior is expected due to multiple possible parent biomes and that it should have been resolved by a previous commit.

## Explanation
The discussion revolves around a bug report where sub-biomes are observed to play the main menu song instead of inheriting their parent biome's music. The maintainers clarify that this behavior is intentional because a single sub-biome, such as `decorative/stone_rock`, can potentially spawn in multiple parent biomes (e.g., different stone-related biomes), making it impossible for it to consistently play one specific song. Additionally, they mention that this issue should have been addressed by commit #732, which is expected to resolve the problem but does not provide further details on the exact changes made.

## Related Questions
- What changes were made in commit #732 to address the issue with sub-biomes playing the wrong song?
- How does Cubyz handle multiple parent biomes for a single sub-biome, and why is this relevant to the music playback issue?

*Source: unknown | chunk_id: github_issue_3123_discussion*
