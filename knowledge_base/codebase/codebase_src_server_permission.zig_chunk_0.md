# [hard/codebase_src_server_permission.zig] - Chunk 0

**Type:** api
**Keywords:** string hash map, ZonElement, thread context assertion, memory allocation, permission checking
**Symbols:** PermissionMap, PermissionMap.map, PermissionMap.fromZon, PermissionMap.toZon, PermissionMap.put, Permissions, Permissions.ListType, Permissions.arena, Permissions.whitelist, Permissions.blacklist, Permissions.init, Permissions.deinit, Permissions.PermissionResult, Permissions.list, Permissions.fromZon, Permissions.toZon, Permissions.addPermission, Permissions.removePermission, Permissions.hasPermission
**Concepts:** permission management, whitelist/blacklist, serialization/deserialization

## Summary
The chunk implements permission management for server operations, handling whitelist and blacklist permissions.

## Explanation
This chunk defines a `PermissionMap` struct to manage individual permissions using a string hash map. It includes methods to convert between ZonElement format and the internal representation, as well as adding and removing permissions. The `Permissions` struct manages both whitelists and blacklists using `PermissionMap`, providing initialization, deinitialization, and methods to add/remove permissions, check permission status, and serialize/deserialize from/to ZonElement.

The `PermissionMap` struct uses a `std.StringHashMapUnmanaged(void)` to store permissions internally. Memory allocation is handled by the `NeverFailingAllocator` and `NeverFailingArenaAllocator`. The `fromZon` method converts a `ZonElement` to a string hash map, while the `toZon` method converts the internal representation back to a `ZonElement`. Permissions are added using the `put` method, which ensures that each key is duplicated in the arena allocator. The `hasPermission` method returns `.no` if a permission path is found in the blacklist, `.yes` if it is found in the whitelist, and `.neutral` otherwise. Thread context assertion is performed using `sync.threadContext.assertCorrectContext(.server)` in various methods.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator) Permissions {
	return .{
		.arena = .init(allocator),
	};
}
```

## Related Questions
- How does the `PermissionMap` struct handle memory allocation?
- What is the purpose of the `fromZon` method in the `PermissionMap` struct?
- How are permissions added to a `Permissions` instance?
- What does the `hasPermission` method return if a permission path is not found in either list?
- How is the thread context asserted in methods of the `Permissions` struct?
- What data structure is used internally by `PermissionMap` to store permissions?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_0*
