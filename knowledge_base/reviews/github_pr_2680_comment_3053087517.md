# [src/entityModel.zig] - PR #2680 review diff

**Type:** review
**Keywords:** refactor, memory allocation, global allocator, stack allocator, worldArena, entity model initialization, zon parameter
**Symbols:** EntityModel, initFromObj, init, assetFolder, id, zon, worldArena
**Concepts:** memory management, architectural consistency, lifetime management

## Summary
Refactored `initFromObj` to `init`, changed memory allocation strategy from stack to global allocator, and added a new parameter `zon`.

## Explanation
The change refactors the initialization function for `EntityModel` by renaming it to `init` and modifying its parameters. The original function used the stack allocator for temporary storage of model data, which is now replaced with the global allocator to ensure that the entity model persists for the lifetime of the world. This aligns with the architectural recommendation to use the worldArena for long-lived objects. The addition of a `zon` parameter suggests an integration with zone-specific data or configuration.

## Related Questions
- What is the purpose of changing from stack to global allocator in this refactoring?
- How does the addition of the `zon` parameter affect the functionality of the `EntityModel` initialization?
- Can you explain the architectural recommendation mentioned in the review comment?
- What potential issues might arise from using the global allocator instead of the stack allocator?
- How does the new `init` function differ from the old `initFromObj` function?
- Is there any impact on performance or memory usage due to this change?

*Source: unknown | chunk_id: github_pr_2680_comment_3053087517*
