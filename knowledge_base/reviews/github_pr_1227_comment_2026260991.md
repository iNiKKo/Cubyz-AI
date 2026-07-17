# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint, generation, substitution, optimization, modes, chunk, blocks
**Symbols:** Blueprint, PasteMode, pasteInGeneration, ServerChunk, SubstitutionMap
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a new `pasteInGeneration` function to the Blueprint struct, allowing pasting with different modes and substitutions.

## Explanation
The change introduces a new method `pasteInGeneration` in the Blueprint struct, which enables pasting blueprints into a server chunk with specified modes (all, noAir, replaceAir) and optional substitutions. The reviewer suggests optimizing this functionality by creating a copy of the blueprint with substitution tables applied, which could simplify handling child and origin blocks during loading. However, they recommend deferring these optimizations for future development due to potential complexity.

## Related Questions
- What are the possible modes for pasting a blueprint?
- How does the `pasteInGeneration` function handle substitutions?
- Why is optimization of substitution handling deferred?
- What changes would be needed to implement the suggested future optimizations?
- How does the function ensure that blocks outside the chunk are not processed?
- Can you explain how the switch statement handles different paste modes?
- What potential issues might arise from deferring optimizations?
- How does the function determine if a block is an origin or child block?
- What is the purpose of the `liesInChunk` method in the ServerChunk struct?
- How would you modify the code to handle additional paste modes like 'noWater'?

*Source: unknown | chunk_id: github_pr_1227_comment_2026260991*
