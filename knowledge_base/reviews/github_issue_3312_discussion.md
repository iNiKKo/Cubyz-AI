# [issues/issue_3312.md] - Issue #3312 discussion

**Type:** review
**Keywords:** arbitrary tags, runtime known, hardcoded climate properties, world file, vertically-stacked biomes, barren/balanced/overgrown
**Concepts:** performance, use-cases, climate properties, transition biomes

## Summary
Discussion about allowing arbitrary tags for transition biomes in Cubyz, with maintainer concerns over performance and use-cases.

## Explanation
The discussion revolves around the proposal to allow transition biomes in Cubyz to accept arbitrary tags instead of just properties. The maintainer raises concerns about the potential performance impact and questions the necessity, suggesting that more hardcoded climate properties might be a better solution. The user proposes storing the number and types of transition biomes in the world file to limit runtime checks but acknowledges that this could lead to inconsistent transitions between addons. The maintainer clarifies that transition biomes are intended for smoothing transitions between climate zones rather than specific biomes, and suggests exploring other solutions for vertically-stacked biomes.

## Related Questions
- What are the potential performance implications of allowing arbitrary tags for transition biomes?
- How could hardcoded climate properties address the user's needs better than arbitrary tags?
- Why is it important to maintain consistent transitions between addons in Cubyz?
- Can you explain the intended use of transition biomes in smoothing climate zone transitions?
- What alternative solutions are being considered for vertically-stacked biomes in Cubyz?
- How might storing transition biome information in the world file impact runtime performance?

*Source: unknown | chunk_id: github_issue_3312_discussion*
