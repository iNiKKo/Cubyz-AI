# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint, generation, substitutions, palette-compression, hashmap lookup, optimization
**Symbols:** Blueprint, PasteMode, pasteInGeneration, ServerChunk, SubstitutionMap
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a new `pasteInGeneration` function to the Blueprint struct, allowing pasting with different modes and optional substitutions.

## Explanation
The change introduces a new method `pasteInGeneration` in the Blueprint struct, which enables pasting blueprints into a generation context with various modes (all, degradable, noAir, replaceAir) and optional substitutions. The reviewer points out that performing a hashmap lookup for every block is inefficient and suggests palette-compression as an optimization. They recommend handling substitutions in a future PR to focus on the core system first.

## Related Questions
- What is the purpose of the `pasteInGeneration` function?
- How does the new `PasteMode` enum affect the pasting process?
- Why is hashmap lookup considered inefficient in this context?
- What are the benefits of palette-compression for blueprints?
- When will substitutions be handled according to the reviewer's suggestion?
- How can we implement palette-compression efficiently?

*Source: unknown | chunk_id: github_pr_1227_comment_2051489080*
