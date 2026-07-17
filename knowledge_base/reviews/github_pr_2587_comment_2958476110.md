# [src/server/permission.zig] - PR #2587 review comment

**Type:** review
**Keywords:** PermissionGroup, StringHashMapUnmanaged, NeverFailingAllocator, threadContext, hasPermission, fromZon, toZon, createGroup, getGroup, stable pointers
**Symbols:** Permissions, PermissionGroup, groups, groupsArena, currentId, init, deinit, hasPermission, fromZon, toZon, createGroup, getGroup
**Concepts:** thread safety, memory management, stable pointers, serialization, deserialization

## Summary
The change updates the permission group management system by switching from a `StringHashMapUnmanaged(PermissionGroup)` to a `StringHashMapUnmanaged(*PermissionGroup)`, aiming to resolve issues related to stable pointers.

## Explanation
The reviewer has made significant changes to the permission management module in Cubyz. The primary modification is changing the data structure used to store permission groups from `StringHashMapUnmanaged(PermissionGroup)` to `StringHashMapUnmanaged(*PermissionGroup)`. This change is intended to address problems with stable pointers, which likely involve issues related to memory management and pointer validity over time. The reviewer emphasizes that this architectural adjustment should resolve these stability concerns. Additionally, the code includes functions for initializing and deinitializing permission groups, checking permissions, serializing and deserializing group data, creating new groups, and retrieving existing ones. The use of `NeverFailingAllocator` and assertions for thread context correctness ensures robust memory management and thread safety.

## Related Questions
- What is the purpose of changing from `StringHashMapUnmanaged(PermissionGroup)` to `StringHashMapUnmanaged(*PermissionGroup)`?
- How does the use of `NeverFailingAllocator` contribute to memory management in this module?
- What are the implications of using thread context assertions in the permission group functions?
- Can you explain the role of `fromZon` and `toZon` methods in the permission group serialization process?
- How does the `createGroup` function handle duplicate group names?
- What is the significance of the `currentId` variable in this module?
- How does the `deinit` function ensure proper cleanup of resources?
- Can you describe the structure and purpose of the `groupsToZon` method?
- What are the potential performance impacts of using pointers in the permission group hashmap?
- How does the reviewer's change address issues with stable pointers?

*Source: unknown | chunk_id: github_pr_2587_comment_2958476110*
