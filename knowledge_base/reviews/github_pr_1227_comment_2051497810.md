# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** palette compression, decompression, substitutions, WorldEdit, command patterns, programmatic use, blueprint modifications
**Symbols:** Blueprint, PasteMode, pasteInGeneration, ServerChunk, Vec3i, SubstitutionMap
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a new `pasteInGeneration` method to the `Blueprint` struct, allowing for pasting with different modes and substitutions.

## Explanation
The change introduces a new method `pasteInGeneration` in the `Blueprint` struct that enables pasting blueprints into a generation context with various modes such as 'all', 'degradable', 'noAir', and 'replaceAir'. The method iterates over the blueprint's blocks, checks if they lie within the target chunk, and applies substitutions if provided. The reviewer suggests optimizing palette compression and decompression by applying replacements at instantiation time to create modified copies of blueprints. This would facilitate more complex operations like using masks and patterns from commands like /set. Additionally, the reviewer proposes making WorldEdit (WE) functions methods on the `Blueprint` struct to standardize command patterns and allow for programmatic use of WE commands.

## Related Questions
- What are the different modes available for pasting blueprints?
- How does the method handle substitutions during the paste operation?
- What is the suggested optimization for palette compression and decompression?
- Why should WorldEdit functions be methods on the Blueprint struct?
- How would programmatic use of WE commands be facilitated by this change?
- What are the potential implications of storing blueprints globally with hash-based IDs?

*Source: unknown | chunk_id: github_pr_1227_comment_2051497810*
