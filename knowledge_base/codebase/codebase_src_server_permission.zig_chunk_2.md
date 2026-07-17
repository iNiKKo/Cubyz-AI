# [hard/codebase_src_server_permission.zig] - Chunk 2

**Type:** api
**Keywords:** AlreadyExists, GroupNotFound, Permissions, addPermission, hasPermission, removePermission, white, black, threadContext, cubyzDir
**Symbols:** createGroup, getGroup, deleteGroup
**Concepts:** group management, permission system, white/blacklist, prefix matching, thread context assertion, file deletion, hash map storage

## Summary
This chunk defines the public API for server-side group management (create/get/delete) and permission handling via a Permissions struct with white/blacklist semantics.

## Explanation
The chunk declares pub fn createGroup(name: []const u8) error{AlreadyExists}!void which asserts correct thread context, inserts the name into a hash map using groupsArena.allocator().allocator(), returns AlreadyExists if found, and stores a newly allocated Group struct (initialized with an empty Permissions). It also declares pub fn getGroup(name: []const u8) error{GroupNotFound}!*Group returning nil on missing entry or error.GroupNotFound. pub fn deleteGroup(allocator: NeverFailingAllocator, name: []const u8) bool fetches the group from the map, constructs a path under saves/{worldPath}/groups/{id}.zon, attempts to delete the file via main.files.cubyzDir().deleteFile(path), logs an error if deletion fails, and returns true on success. The Permissions struct (imported elsewhere) provides addPermission(.white/.black, []const u8) void and hasPermission([]const u8) PermissionResult enum; it also exposes removePermission(.white/.black, []const u8) bool. All public functions assert sync.threadContext.assertCorrectContext(.server). The chunk includes multiple test cases: whitePermission, blacklist, deepPermission (prefix matching), rootPermission, rootBlackPermission, addRemovePermission, removeNonExistentPermission, groupCreation, groupPermissions, groupRemovePermissions, and invalidGroup.

## Related Questions
- What error is returned when createGroup receives a name that already exists in the groups map?
- How does getGroup signal that a requested group name was not found?
- Which thread context must be active for all public group functions to proceed without assertion failure?
- Does deleteGroup guarantee removal of the underlying file, and how is failure reported?
- What PermissionResult enum values can hasPermission return and what do they mean?
- How does the Permissions struct handle prefix matching when checking a command path?
- Can removePermission be called on a permission that was never added, and what does it return in that case?
- Where are group files stored relative to main.server.world.path after creation or deletion?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_2*
