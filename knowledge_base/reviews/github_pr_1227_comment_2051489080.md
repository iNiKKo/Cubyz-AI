# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint, pasteInGeneration, substitutions, hashmap, performance, optimization, palette, compression, caching, ServerChunk, Vec3i
**Symbols:** Blueprint, PasteMode, pasteInGeneration, ServerChunk, Vec3i, SubstitutionMap
**Concepts:** performance optimization, hashmap lookup efficiency, palette compression, caching

## Summary
The code introduces a new `pasteInGeneration` function to paste blueprints into the game world with different modes and optional substitutions. However, it is noted that performing a hashmap lookup for every block could be inefficient.

## Explanation
The code introduces a new `pasteInGeneration` function to paste blueprints into the game world with different modes (`all`, `degradable`, `noAir`, `replaceAir`) and optional substitutions. The function iterates over each block in the blueprint, checking if it lies within the chunk boundaries and whether it is an origin or child block. If substitutions are provided, it checks for a substitution entry for each block type using a hashmap lookup. However, this approach can lead to performance issues, especially when dealing with large structures.

The review points out that the current implementation of the `pasteInGeneration` function involves checking each block against a substitution map using a hashmap lookup. This approach can lead to performance issues, especially when dealing with large structures. The reviewer suggests two potential improvements: palette-compressing the blueprint and caching palette entries. These suggestions are considered out of scope for the current PR. Instead, the reviewer recommends adding substitutions as a whole in a future PR to focus on optimizing the core system first.

## Related Questions
- How can we implement palette-compression for the blueprint?
- What are the potential benefits of caching palette entries?
- Can you provide a code example of how to add substitutions as a whole in a future PR?
- How does the current implementation affect performance with large structures?
- What are the trade-offs between hashmap lookups and palette compression?
- How can we ensure that the core system is optimized before adding new features?

*Source: unknown | chunk_id: github_pr_1227_comment_2051489080*
