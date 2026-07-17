# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint, generation, paste, mode, replaceAir, degradable, void blocks
**Symbols:** Blueprint, pasteInGeneration, PasteMode, ServerChunk, SubstitutionMap
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a new `pasteInGeneration` function in the Blueprint struct to handle pasting blueprints into server chunks with different modes.

## Explanation
The change introduces a new function `pasteInGeneration` that allows for pasting blueprint blocks into a server chunk at a specified position. The function supports three paste modes: `all`, `noAir`, and `replaceAir`. The reviewer notes that the `.all` mode is intended to replace everything, which can be destructive if not used carefully, especially for overlapping structures. They suggest using a `.degradable` mode instead for such cases. The current implementation uses `.replaceAir` as a compromise, ensuring that air blocks are replaced while other terrain is preserved. The reviewer also mentions that this needs further polishing when void blocks are introduced.

## Related Questions
- What is the purpose of the `pasteInGeneration` function in the Blueprint struct?
- How does the `.all` mode differ from other paste modes in terms of functionality?
- Why was the `.replaceAir` mode chosen over `.all` for pasting blueprints?
- What are the potential issues with using the `.all` mode for overlapping structures?
- When will void blocks be introduced, and how will they affect the `pasteInGeneration` function?
- How does the function handle substitutions of block types during the paste operation?

*Source: unknown | chunk_id: github_pr_1227_comment_2020184245*
