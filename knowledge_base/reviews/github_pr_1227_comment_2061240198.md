# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint, paste, generation, mode, degradable, origin block, child block, void block, optimization, comparison, hashmap lookup
**Symbols:** Blueprint, PasteMode, pasteInGeneration, _pasteInGeneration, Vec3i, ServerChunk
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a new `pasteInGeneration` function to the Blueprint struct with modes 'all' and 'degradable'. The `_pasteInGeneration` helper function handles the actual pasting logic based on the mode.

## Explanation
The change introduces a new method `pasteInGeneration` in the Blueprint struct, which allows for different paste modes ('all' and 'degradable'). This method delegates to the `_pasteInGeneration` helper function, which iterates over the blueprint's blocks and pastes them into the server chunk based on the specified mode. The reviewer suggests replacing origin and child blocks with void blocks during loading to optimize block placement checks by reducing comparisons from two to one.

## Related Questions
- What is the purpose of the `pasteInGeneration` function in the Blueprint struct?
- How does the `_pasteInGeneration` helper function determine where to paste blocks?
- What are the two modes available for pasting blocks, and how do they differ?
- Why does the reviewer suggest replacing origin and child blocks with void blocks?
- How would optimizing block placement checks by reducing comparisons from two to one improve performance?
- Can you explain the role of the `Vec3i` and `ServerChunk` types in this code?

*Source: unknown | chunk_id: github_pr_1227_comment_2061240198*
