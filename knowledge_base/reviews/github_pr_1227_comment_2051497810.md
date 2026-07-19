# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** palette compression, degradation, air blocks, substitutions, WorldEdit commands, instantiation time, blueprint modifications
**Symbols:** Blueprint, PasteMode, pasteInGeneration, ServerChunk, SubstitutionMap
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added `PasteMode` enum and `pasteInGeneration` method to handle different paste modes in blueprint generation.

## Explanation
The change introduces a new `PasteMode` enum with specific options: 'all', 'degradable', 'noAir', and 'replaceAir'. These options control how blocks are pasted into the world. The `pasteInGeneration` method iterates over the blueprint's blocks, checks if they lie within the target chunk, and applies substitutions if provided. Specifically, for each block in the blueprint, it calculates its position in the world, skips origin and child blocks, and applies any substitutions from the `SubstitutionMap`. If a substitution is found, it replaces the block type accordingly. The reviewer suggests optimizing palette compression and decompression by applying replacements at instantiation time, which would allow for more complex operations like using masks and patterns. They also propose making WorldEdit (WE) functions methods on the `Blueprint` struct to standardize command patterns and enable programmatic use of WE commands.

## Related Questions
- How does the `pasteInGeneration` method handle block substitutions?
- What are the potential performance implications of applying substitutions at instantiation time?
- How does the new `PasteMode` enum affect the pasting process?
- Can you explain the proposed optimization for palette compression and decompression?
- Why should WorldEdit functions be methods on the `Blueprint` struct?
- How would the standardized command pattern improve programmability of WE commands?

*Source: unknown | chunk_id: github_pr_1227_comment_2051497810*
