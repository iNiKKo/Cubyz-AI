# [hard/codebase_src_server_permission.zig] - Chunk 3

**Type:** api
**Keywords:** createGroup, getGroup, addPermission, removePermission, hasPermission, toZon, fromZon, Permissions, Group, error.GroupNotFound, error.AlreadyExists
**Symbols:** createGroup, getGroup, addPermission, hasPermission, removePermission, toZon, fromZon, Permissions, Group
**Concepts:** unit testing, permission management, group serialization, error handling, allocator initialization, defer cleanup

## Summary
This chunk contains unit tests for the server permission system, verifying group creation, permission addition/removal, error handling for invalid groups and duplicates, and serialization round-trips between Permissions/Group objects and ZonElement.

## Explanation
The chunk defines a series of test functions that exercise the permission subsystem. Each test initializes main.heap.testingAllocator with zero capacity (init(...,0)) and defers deinit() to clean up. The tests cover: createGroup/getGroup round-trips; group.addPermission and group.hasPermission for white permissions on /command/test; group.removePermission returning true after removal; error handling via expectError(error.GroupNotFound) when querying non-existent groups ('root') or empty groups, and expectError(error.AlreadyExists) when creating a duplicate group name. The permissionListToFromZon test constructs a Permissions object, adds two white permissions (/command/test, /command/spawn), serializes to Zon via whitelist.toZon, then deserializes into a new Permissions using fromZon on the arena allocator and verifies map.size equals 2 and that all keys are present. The permissionGroupToFromZon test creates a group with two white permissions, serializes it to a ZonElement via group.toZon (using initObject), then reconstructs a Group via fromZon with a new name 'test2', asserts the reconstructed map.size equals 2, and iterates keys to confirm presence. All tests use std.testing.expectEqual or expectError assertions; no production code is declared in this chunk.

## Related Questions
- What error is returned when querying a non-existent group name like 'root'?
- How does the test verify that adding a permission and then checking hasPermission returns true?
- Which allocator is used for all tests in this chunk and how is it initialized?
- What happens if createGroup is called with a name that already exists?
- How are permissions serialized to ZonElement and deserialized back into Permissions/Group objects?
- Does the permissionListToFromZon test verify map.size after round-trip serialization?
- Are both whitelist.toZon and fromZon used in the same test function?
- What is the expected return value of removePermission after successfully removing a permission?
- How does the chunk ensure cleanup of allocated memory across all tests?
- Which permissions are added to the Permissions object in permissionListToFromZon?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_3*
