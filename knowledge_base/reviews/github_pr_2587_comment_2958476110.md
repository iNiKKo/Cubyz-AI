# [src/server/permission.zig] - PR #2587 review diff

**Type:** review
**Keywords:** PermissionGroup, StringHashMapUnmanaged, stable pointers, threadContext, allocator, ZonElement, permissions, groupsToZon
**Symbols:** PermissionGroup, Permissions, groups, groupsArena, currentId, init, deinit, hasPermission, createGroup, getGroup
**Concepts:** thread safety, memory management, stable pointers

## Summary
The change updates the PermissionGroup storage from a direct HashMap to a HashMap of pointers, aiming to resolve issues with stable pointers.

## Explanation
The reviewer has modified the storage mechanism for PermissionGroups by changing from `StringHashMapUnmanaged(PermissionGroup)` to `StringHashMapUnmanaged(*PermissionGroup)`. This change is intended to address problems related to stable pointers. The review indicates that this modification should ensure that the pointers remain valid even if the underlying data structure changes, which is crucial for maintaining consistent access and preventing potential bugs or crashes.

## Related Questions
- What was the previous storage mechanism for PermissionGroups?
- Why was the change from `StringHashMapUnmanaged(PermissionGroup)` to `StringHashMapUnmanaged(*PermissionGroup)` necessary?
- How does the new storage mechanism ensure stable pointers?
- What are the potential benefits of using a HashMap of pointers instead of direct objects?
- Are there any performance implications associated with this change?
- How does the reviewer ensure thread safety in these changes?
- What is the role of `groupsArena` in this implementation?
- How does the `createGroup` function handle existing group names?
- What error handling is implemented for the `getGroup` function?
- How are PermissionGroups serialized and deserialized in this code?
- What is the purpose of the `sync.threadContext.assertCorrectContext(.server);` calls?
- How does the change impact memory management in the server module?

*Source: unknown | chunk_id: github_pr_2587_comment_2958476110*
