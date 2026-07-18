# [issues/issue_570.md] - Issue #570 discussion

**Type:** review
**Keywords:** ocean height, liquid block, biome properties, base height, cave biomes, stone blocks, world-gen
**Concepts:** biome customization, world generation, liquid block specification

## Summary
Discussion on allowing biomes to specify different water heights and liquid blocks, considering varying base heights and cave biomes.

## Explanation
The discussion revolves around enabling biomes to have customizable ocean heights and liquid blocks. The user proposes features such as setting individual ocean heights and liquid blocks for each biome, with the addition of stone blocks at boundaries between biomes with different properties. The maintainer points out that a fixed height might not suffice for biomes with varying base heights and suggests considering cave biomes like the mantle.

## Related Questions
- How can the system handle varying base heights between biomes?
- What are the implications of allowing different liquid blocks in adjacent biomes?
- How should cave biomes like the mantle be integrated into this feature?
- What changes need to be made to the world generation algorithm to support these new biome properties?
- How can we ensure that stone blocks at boundaries between biomes with different properties are generated correctly?
- What performance optimizations can be implemented for handling multiple liquid block types in the game?

*Source: unknown | chunk_id: github_issue_570_discussion*
