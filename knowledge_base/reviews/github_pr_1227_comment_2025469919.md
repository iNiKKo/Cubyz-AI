# [src/blueprint.zig] - PR #1227 review diff

**Type:** review
**Keywords:** blueprint pasting, generation, modes, substitutions, performance, comptime
**Symbols:** Blueprint, PasteMode, pasteInGeneration, ServerChunk, SubstitutionMap
**Concepts:** performance optimization, compile-time evaluation

## Summary
Added a new function `pasteInGeneration` to handle blueprint pasting with different modes and substitutions.

## Explanation
The change introduces a new function `pasteInGeneration` in the `Blueprint` struct, which allows for pasting blueprints into a server chunk with different modes (`all`, `noAir`, `replaceAir`) and optional substitutions. The reviewer highlights potential performance concerns due to runtime checks during generation, suggesting that these could be optimized using compile-time evaluation if necessary.

The `pasteInGeneration` function iterates over the blocks in the blueprint and updates them in the server chunk based on the specified mode. If a substitution map is provided, it replaces the block type accordingly. The function skips origin and child blocks during this process. It also checks if the block lies within the target chunk before updating it.

The `PasteMode` enum has three values: `all`, `noAir`, and `replaceAir`. In `all` mode, all blocks are pasted. In `noAir` mode, air blocks are not pasted. In `replaceAir` mode, existing air blocks in the chunk are replaced with the blocks from the blueprint.

The function ensures that only valid world coordinates are updated by checking if the block lies within the target chunk using the `liesInChunk` method of the `ServerChunk` struct.

## Related Questions
- What are the potential performance implications of using runtime checks during blueprint generation?
- How can the `pasteInGeneration` function be optimized for better performance?
- Can the switch statement in `pasteInGeneration` be migrated to comptime evaluation?
- What is the purpose of the `SubstitutionMap` parameter in `pasteInGeneration`?
- How does the `pasteInGeneration` function handle blocks that are origins or children?
- What is the role of the `PasteMode` enum in the blueprint pasting process?
- How does the function ensure that only valid world coordinates are updated in the chunk?
- What changes were made to the `Blueprint` struct to support the new `pasteInGeneration` function?
- Can you explain the logic for handling substitutions in the `pasteInGeneration` function?
- How does the function determine if a block lies within the target chunk?

*Source: unknown | chunk_id: github_pr_1227_comment_2025469919*
