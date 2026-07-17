# [src/entityModel.zig] - PR #2680 review diff

**Type:** review
**Keywords:** refactor, memory efficiency, allocator, worldArena, entity initialization
**Symbols:** EntityModel, initFromObj, init, assetFolder, id, ZonElement
**Concepts:** memory management, allocator choice, worldArena

## Summary
Refactored `EntityModel` initialization to use a global allocator and introduced a new method signature.

## Explanation
The change refactors the `initFromObj` function into a more generic `init` function that accepts an asset folder, an ID, and a ZonElement. The reviewer emphasizes using the worldArena for memory management of entities that persist throughout the world's lifetime. This architectural decision aims to improve memory efficiency and potentially reduce fragmentation by ensuring consistent allocation strategies.

## Related Questions
- What is the purpose of using `main.globalAllocator` in the new `init` function?
- How does the use of `worldArena` impact memory management in Cubyz?
- Why was the method signature changed from `initFromObj` to `init`?
- Can you explain the benefits of using a global allocator for entity models?
- What is the role of `zon` in the new `init` function?
- How does this change affect the loading process of player models?
- Is there any potential risk of memory leaks with this new approach?
- How does this refactor align with Cubyz's overall memory management strategy?
- Can you provide an example of how to use the new `init` method?
- What are the implications of changing the allocator for existing entity models?

*Source: unknown | chunk_id: github_pr_2680_comment_3053087517*
