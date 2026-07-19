# [issues/issue_188.md] - Issue #188 discussion

**Type:** review
**Keywords:** mountain biomes, LOD transitions, texturing, block painting, visual detail, algorithm improvement
**Symbols:** LOD, Ground_structure
**Concepts:** Level of Detail (LOD), Block painting, Visual noise

## Summary
Discussion about improving mountain biome texturing and LOD transitions, with suggestions for more intelligent block painting.

## Explanation
The issue revolves around improving the texturing and Level of Detail (LOD) transitions in Cubyz's mountain biomes. The current implementation results in visually noisy textures, even at lower LODs. The proposed changes aim to make LOD transitions less noticeable by using a more uniform texturing approach. However, this leads to a loss of detail. Reviewers suggest that improving the ground structure's block painting algorithm could help reintroduce detail while maintaining better LOD performance. Specifically, the proposal includes using ground patches or tiny sub-biomes to add back the lost detail. There is also mention of potential issues with the LOD algorithm itself, as it may have gotten worse after a previous change (#1699). The maintainer asks for further investigation and possible fixes to the LOD chunk algorithm.

## Related Questions
- What changes were made to the LOD algorithm in #1699?
- How does the current block painting algorithm work in Cubyz?
- Can you provide a comparison of the old and new mountain biome textures?
- What specific improvements are suggested for the ground structure's block painting?
- Are there any plans to implement tiny sub-biomes to add detail back to the mountains?
- How does the LOD performance compare before and after the proposed changes?
- What potential issues might arise from changing the texturing approach in mountain biomes?
- Is there a way to balance uniform texturing with visual detail in LOD transitions?
- Can you explain the impact of the LOD algorithm on overall game performance?
- How does the current implementation handle ground patches in mountain biomes?

*Source: unknown | chunk_id: github_issue_188_discussion*
