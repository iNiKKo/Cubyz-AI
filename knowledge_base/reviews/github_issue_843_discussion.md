# [issues/issue_843.md] - Issue #843 discussion

**Type:** review
**Keywords:** ridges, cliffs, biomes, interpolation, post-processing, heightmap, smooth rounding
**Concepts:** terrain generation, biome customization, heightmap processing

## Summary
Discussion about adding a 'ridges/cliffs' parameter for biomes in Cubyz.

## Explanation
The discussion revolves around the idea of introducing a new parameter for biomes that would create ridge or cliff-like terrain within the biome boundaries, similar to setting interpolation to '.none' but confined to the biome. The suggestion involves allowing different post-processing functions on the heightmap and using a smooth rounding function to achieve cliff-like shapes.

## Related Questions
- How would the 'ridges/cliffs' parameter be implemented in Cubyz?
- What are the potential impacts on performance when adding this new terrain feature?
- Can you provide examples of other games that use similar biome customization techniques?
- How does the suggested smooth rounding function contribute to creating cliff-like shapes?
- Are there any backward compatibility concerns with introducing this new parameter?
- What kind of testing would be necessary to ensure the correctness of the new terrain feature?

*Source: unknown | chunk_id: github_issue_843_discussion*
