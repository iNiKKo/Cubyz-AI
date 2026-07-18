# [issues/issue_942.md] - Issue #942 discussion

**Type:** review
**Keywords:** fogColor, sky color, biomes, volumetric fog, density gradient, cave fog
**Concepts:** fog, sky color, biome, rendering

## Summary
Discussion about separating sky color from fog color in biomes.

## Explanation
The issue discusses the current behavior where setting a biome's fogColor also changes the sky color, which is not ideal for surface biomes. Maintainers express concerns about the complexity of implementing different fog and sky colors due to rendering issues and potential hardware restrictions. They suggest a density gradient in the fog as an ideal solution but note that it could break cave fog.

## Related Questions
- What is the current behavior of setting a biome's fogColor?
- Why is separating sky and fog colors challenging?
- What are the potential hardware restrictions mentioned in the discussion?
- How does a density gradient in fog address the issue?
- What concerns are raised about breaking cave fog with changes to fog rendering?
- Are there any plans for rewriting the fog system?

*Source: unknown | chunk_id: github_issue_942_discussion*
