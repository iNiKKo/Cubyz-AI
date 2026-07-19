# [hard/codebase_src_server_permission.zig] - Chunk 2

**Type:** api
**Keywords:** thread safety, group creation, permission checking, error handling, testing
**Symbols:** createGroup, getGroup, deleteGroup
**Concepts:** group management, permission system

## Summary
This chunk manages group creation, retrieval, and deletion, as well as permission handling within those groups.

## Explanation
This chunk manages group creation, retrieval, and deletion, ensuring thread safety with context assertions. It includes functions to create a new group (`createGroup`), retrieve an existing group (`getGroup`), and delete a group (`deleteGroup`). The `createGroup` function checks for the existence of a group and returns an error if it already exists. The `getGroup` function retrieves a group by name or returns an error if the group does not exist. The `deleteGroup` function deletes a group and its associated file, returning false if the group does not exist.

The chunk also includes methods for adding and removing permissions from groups (`addPermission`, `removePermission`) and checking if a path has a specific permission status (`hasPermission`). The tests cover various scenarios including white and blacklisting, deep permissions, root permissions, and group-specific operations. For example, the `whitePermission` test checks that a path with a white permission is accessible, while the `blacklist` test checks that a path with a blacklist permission is not accessible.

The structure of a test case for white permissions involves initializing a `Permissions` object, adding a white permission to a specific path, and then checking if the path has the expected permission status.

## Code Example
```zig
pub fn createGroup(name: []const u8) error{AlreadyExists}!void {
	sync.threadContext.assertCorrectContext(.server);
	const result = groups.getOrPut(groupsArena.allocator().allocator, name) catch unreachable;
	if (result.found_existing) return error.AlreadyExists;

	result.key_ptr.* = groupsArena.allocator().dupe(u8, name);
	result.value_ptr.* = .init(groupsArena.allocator(), result.key_ptr.*);
}
```

## Related Questions
- How do you create a new group?
- What error is returned if a group already exists?
- How do you retrieve an existing group?
- What happens if you try to delete a non-existent group?
- How are permissions added to a group?
- How do you check if a path has a specific permission?
- What is the structure of a test case for white permissions?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_2*
