# [hard/codebase_src_server_permission.zig] - Chunk 3

**Type:** implementation
**Keywords:** unit testing, error handling, Zon format, permissions, groups
**Concepts:** permission management, group creation, serialization

## Summary
This chunk contains unit tests for permission management in the Cubyz server.

## Explanation
This chunk contains unit tests for permission management in the Cubyz server. The tests cover scenarios related to creating groups, managing permissions within those groups, and serializing/deserializing permission data using binary format. The tests use Zig's standard testing library (`std.testing`) to assert expected outcomes.

- **`invalidGroupCreation` Test**: This test checks for error handling when attempting to create a duplicate group. It initializes the heap allocator, creates a group named 'test', and then tries to create the same group again, expecting an `error.AlreadyExists` error.

  ```zig
  init(main.heap.testingAllocator, 0);
  defer deinit();

  try createGroup("test");
  try std.testing.expectError(error.AlreadyExists, createGroup("test"));
  ```

- **`permissionListToFromBytes` Test**: This test verifies the serialization and deserialization of permission lists using binary format. It initializes a `Permissions` object, adds two permissions (`/command/test` and `/command/spawn`), converts the list to bytes using `BinaryWriter`, and then reconstructs the permissions from the bytes using `BinaryReader`. The test checks that the reconstructed list contains the same number of permissions as the original.

  ```zig
  var permissions: Permissions = .init(main.heap.testingAllocator);
  defer permissions.deinit();

  permissions.addPermission(.white, "/command/test");
  permissions.addPermission(.white, "/command/spawn");

  var writer = main.utils.BinaryWriter.init(main.heap.testingAllocator);
  defer writer.deinit();
  permissions.toBytes(&writer);

  var testPermissions: Permissions = .init(main.heap.testingAllocator);
  defer testPermissions.deinit();

  var reader: main.utils.BinaryReader = .init(writer.data.items);
  try testPermissions.fromBytes(&reader);

  try std.testing.expectEqual(2, testPermissions.whitelist.map.size);

  var it = testPermissions.whitelist.map.keyIterator();
  while (it.next()) |item| {
      try std.testing.expectEqual(true, permissions.whitelist.map.contains(item.*));
  }
  ```

- **`permissionGroupToFromBytes` Test**: This test checks the serialization and deserialization of entire permission groups using binary format. It initializes a group named 'test', adds two permissions, serializes the group to bytes using `BinaryWriter`, and then reconstructs the group from the bytes using `BinaryReader`. The test verifies that the reconstructed group contains the same number of permissions as the original.

  ```zig
  init(main.heap.testingAllocator, 0);
  defer deinit();

  try createGroup("test");
  const group = try getGroup("test");

  group.addPermission(main.heap.testingAllocator, .white, "/command/test");
  group.addPermission(main.heap.testingAllocator, .white, "/command/spawn");

  var writer: main.utils.BinaryWriter = .init(main.heap.testingAllocator);
  defer writer.deinit();
  group.toBytes(&writer);

  var reader: main.utils.BinaryReader = .init(writer.data.items);
  var testGroup: *Group = try .fromBytes(main.heap.testingAllocator, &reader, 0);
  defer testGroup.deinit(main.heap.testingAllocator);

  try std.testing.expectEqual(2, testGroup.permissions.whitelist.map.size);

  var it = testGroup.permissions.whitelist.map.keyIterator();
  while (it.next()) |item| {
      try std.testing.expectEqual(true, group.permissions.whitelist.map.contains(item.*));
  }
  ```

In all tests, memory allocation is handled using `main.heap.testingAllocator`, and resources are properly deallocated using `defer` statements.

## Related Questions
- How does the `invalidGroupCreation` test handle duplicate group creation?
- What permissions are added in the `permissionListToFromBytes` test?
- How are permissions serialized and deserialized in the `permissionGroupToFromBytes` test?
- What Zig standard library functions are used for testing in this chunk?
- How does the code handle memory allocation and deallocation in these tests?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_3*
