# [src/server/server.zig] - PR #2864 review diff

**Type:** review
**Keywords:** update function, entity iteration, freeId TODO, active entities, dynamic entity handling
**Symbols:** update, entityData, userList, entity_manager, getAll, used, id
**Concepts:** architectural review, iteration, entity management

## Summary
Replaced user iteration with entity iteration in the update function.

## Explanation
The change replaces the iteration over a userList with an iteration over entities managed by the entity_manager. This addresses a critical architectural issue where the previous method might have missed or incorrectly processed entities, especially those that were dynamically added or removed. The reviewer confirms that this resolves the TODO related to freeId, ensuring that all active entities are correctly processed during updates.

## Related Questions
- What was the previous method of iterating over users?
- How does the new iteration over entities improve the update process?
- Why is the check for 'ent.used' necessary in the entity iteration?
- Does this change affect the performance of the update function?
- Is there any potential risk of missing entities with this new approach?
- What was the purpose of the TODO comment related to freeId?
- How does this change ensure that all active entities are processed correctly?
- Are there any other parts of the codebase that might be affected by this architectural change?
- Does this update require any changes in other modules or files?
- How can we verify that this change has resolved the issue with freeId?

*Source: unknown | chunk_id: github_pr_2864_comment_3443862313*
