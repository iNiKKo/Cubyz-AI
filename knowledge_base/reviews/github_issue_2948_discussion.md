# [issues/issue_2948.md] - Issue #2948 discussion

**Type:** review
**Keywords:** structures, 32x32x32, large structures, generation model, height map, cave biomes, SDFs, terrain information, fitting terrain
**Concepts:** terrain generation, Signed Distance Functions (SDFs), performance

## Summary
The issue discusses the limitation of structures being limited to 32x32x32 in size and proposes a change to the generation model to support larger structures.

## Explanation
The current structure size limit is insufficient for generating large-scale features like dungeons or giant trees. The maintainer suggests modifying the generation model to allow large structures to either rely solely on height maps for surface biomes or have no terrain information at all for cave biomes. For structures that need to fit the surrounding terrain, the use of Signed Distance Functions (SDFs) is proposed to adjust the terrain instead of checking if the structure fits.

## Related Questions
- What is the current limitation on structure size in Cubyz?
- How does the maintainer propose to support larger structures?
- What are the two main options for large structures according to the maintainer's comment?
- Why is using SDFs suggested for fitting structures to the terrain?
- What is the performance implication of changing the generation model as proposed?
- Can you explain how height maps and SDFs contribute to generating larger structures?

*Source: unknown | chunk_id: github_issue_2948_discussion*
