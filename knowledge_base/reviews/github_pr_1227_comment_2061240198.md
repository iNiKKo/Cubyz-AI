# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** Blueprint, pasteInGeneration, PasteMode, all, degradable, _pasteInGeneration, ServerChunk, Vec3i, blocks, width, depth, height, liesInChunk, get, isOriginBlock
**Symbols:** Blueprint, PasteMode, pasteInGeneration, _pasteInGeneration, ServerChunk, Vec3i, blocks, width, depth, height, liesInChunk, get, isOriginBlock, isChildBlock, voidType
**Concepts:** thread safety, backwards compatibility, memory leak, performance optimization

## Summary
Added a new `pasteInGeneration` function to the Blueprint struct with modes 'all' and 'degradable'. The `_pasteInGeneration` helper function handles the actual pasting logic based on the mode.

## Explanation
The change introduces a new method `pasteInGeneration` in the Blueprint struct, which allows for different paste modes ('all' and 'degradable'). This method delegates to the helper function `_pasteInGeneration`, which iterates over the blueprint's blocks and pastes them into the server chunk based on the specified mode. The `_pasteInGeneration` function uses nested loops to iterate through the width, depth, and height of the blueprint's blocks. For each block, it calculates its world position and checks if it lies within the server chunk's boundaries using the `liesInChunk` method. If the block is an origin block, a child block, or has a type of `voidType`, it is skipped. Otherwise, the block is pasted into the chunk. The reviewer suggests optimizing block handling by replacing origin and child blocks with void blocks during loading, reducing comparisons from two to one and eliminating a hashmap lookup.

## Related Questions
- What is the purpose of the `pasteInGeneration` function in the Blueprint struct?
- How does the `_pasteInGeneration` helper function handle block pasting based on the mode?
- What optimization suggestion is made by the reviewer regarding block handling?
- How does the code ensure that blocks are only pasted within the server chunk's boundaries?
- What conditions are checked before a block is pasted into the chunk?
- Can you explain the difference between 'all' and 'degradable' paste modes in the Blueprint struct?

*Source: unknown | chunk_id: github_pr_1227_comment_2061240198*
