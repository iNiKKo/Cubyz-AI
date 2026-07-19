# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint, generation, paste mode, air blocks, degradable mode, void blocks
**Symbols:** Blueprint, pasteInGeneration, PasteMode, all, noAir, replaceAir, ServerChunk, SubstitutionMap
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a new `pasteInGeneration` function to the Blueprint struct, allowing for different paste modes including 'all', 'noAir', and 'replaceAir'.

## Explanation
The change introduces a new method `pasteInGeneration` in the Blueprint struct, which allows pasting blueprint blocks into a server chunk with various modes. The `.all` mode is intended to replace everything, but it should not be used for structures that can overlap. Instead, a `.degradable` mode is suggested for such cases. For now, the `.replaceAir` mode is used as a safer alternative, especially for small houses where air blocks prevent terrain destruction while walls replace existing terrain. The reviewer highlights the need for further polishing when void blocks are introduced.

The function handles block substitutions by checking if a substitution map is provided and replacing the block type accordingly. Origin and child blocks are skipped during pasting. The `liesInChunk` method is used to ensure that only blocks within the chunk bounds are updated.

## Related Questions
- What is the purpose of the `.all` paste mode in the `pasteInGeneration` function?
- How does the `.replaceAir` mode differ from `.all` in terms of functionality?
- When will the `.degradable` paste mode be introduced, and what is its intended use case?
- What are the implications of using void blocks with the current paste modes?
- How does the function handle block substitutions during pasting?
- Is there any potential for thread safety issues in the `pasteInGeneration` method?
- What changes need to be made when introducing void blocks to ensure compatibility?
- Can you explain how the `liesInChunk` method is used within the `pasteInGeneration` function?
- How does the function handle origin and child blocks during pasting?
- What are the performance considerations for iterating over large blueprint volumes in the `pasteInGeneration` method?

*Source: unknown | chunk_id: github_pr_1227_comment_2020184245*
