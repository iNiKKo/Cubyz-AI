# [hard/codebase_src_server_permission.zig] - Chunk 2

**Type:** api
**Keywords:** thread safety, group creation, permission checking, error handling, testing
**Symbols:** createGroup, getGroup, deleteGroup
**Concepts:** group management, permission system

## Summary
This chunk manages group creation, retrieval, and deletion, as well as permission handling within those groups.

## Explanation
The chunk provides functions to create, retrieve, and delete groups, ensuring thread safety with context assertions. It also includes methods for adding and removing permissions from groups and checking if a path has a specific permission status. The tests cover various scenarios including white and blacklisting, deep permissions, root permissions, and group-specific operations.

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
