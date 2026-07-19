# [issues/issue_2612.md] - Issue #2612 discussion

**Type:** review
**Keywords:** subbiomes, music inheritance, parent biomes, arbitrary choice, future plans, per-biome music
**Symbols:** stone_pit.zig.zon
**Concepts:** inheritance, multiple parents, arbitrary choice, music inheritance

## Summary
Discussion on subbiome music inheritance, considering multiple parent biomes and potential arbitrary choices.

## Explanation
The issue revolves around ensuring that subbiomes inherit music from their parent biomes correctly. The complexity arises because a subbiome can have multiple parents, and determining which parent's music to use becomes non-trivial. There is a risk of playing incorrect music if the assumption that all parent biomes share the same music is not true. Additionally, future plans indicate that per-biome music will no longer be supported (see issue #732).

## Related Questions
- How does the current system determine which parent biome's music a subbiome should inherit?
- What are the potential issues if multiple parent biomes have different music tracks?
- Is there a mechanism to store which parent biome caused a subbiome to spawn?
- How will the removal of per-biome music affect the current implementation?
- Are there any plans to address the issue of arbitrary music selection for subbiomes?
- What changes are needed to ensure consistent music inheritance across different scenarios?

*Source: unknown | chunk_id: github_issue_2612_discussion*
