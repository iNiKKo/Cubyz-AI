# [src/server/permission.zig] - PR #2530 review comment

**Type:** review
**Keywords:** permissions, string hash map, zon element, add permission, remove permission, has permission, permission group, world init, world deinit, resource persistence
**Symbols:** mapFromZon, mapToZon, Permissions, ListType, NeverFailingAllocator, NeverFailingArenaAllocator, ZonElement, sync, PermissionResult, PermissionGroup
**Concepts:** thread safety, memory management, data serialization, resource lifecycle

## Summary
The `permission.zig` file introduces a new module for managing permissions using string hash maps and ZonElement serialization/deserialization. It includes structs like `Permissions` and `PermissionGroup`, and functions for adding, removing, and checking permissions.

## Explanation
This code defines a permission management system within the Cubyz server. The `Permissions` struct manages two lists (white and black) of permissions using `std.StringHashMapUnmanaged`. Functions like `addPermission`, `removePermission`, and `hasPermission` allow for modifying and querying these lists. The `PermissionGroup` struct encapsulates a set of permissions with an ID, providing methods to initialize, deinitialize, and check permissions. The review highlights a potential issue where the `groups` variable is not initialized or reset, suggesting tying its lifecycle to world initialization and deinitialization to prevent resource persistence issues.

## Related Questions
- What is the purpose of the `mapFromZon` function?
- How does the `Permissions` struct manage white and black lists?
- What are the potential issues with the current implementation of `groups`?
- How does the `PermissionGroup` struct ensure thread safety?
- What happens if a permission is added to both white and black lists?
- How is memory managed in the `Permissions` module?
- What is the role of `NeverFailingAllocator` in this code?
- How does the `hasPermission` function determine the result?
- What are the implications of not resetting the `groups` variable?
- How can the lifecycle of `groups` be tied to world initialization and deinitialization?

*Source: unknown | chunk_id: github_pr_2530_comment_2775500350*
