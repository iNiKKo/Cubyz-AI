# [hard/codebase_src_server_permission.zig] - Chunk 0

**Type:** api
**Keywords:** string hash map, ZonElement, thread context assertion, memory allocation, permission checking
**Symbols:** PermissionMap, PermissionMap.map, PermissionMap.fromZon, PermissionMap.toZon, PermissionMap.put, Permissions, Permissions.ListType, Permissions.arena, Permissions.whitelist, Permissions.blacklist, Permissions.init, Permissions.deinit, Permissions.PermissionResult, Permissions.list, Permissions.fromZon, Permissions.toZon, Permissions.addPermission, Permissions.removePermission, Permissions.hasPermission
**Concepts:** permission management, whitelist/blacklist, serialization/deserialization

## Summary
The chunk implements permission management for server operations, handling whitelist and blacklist permissions.

## Explanation
This chunk defines a `PermissionMap` struct to manage individual permissions using a string hash map. It includes methods to convert between ZonElement format and the internal representation, as well as adding and removing permissions. The `Permissions` struct manages both whitelists and blacklists using `PermissionMap`, providing initialization, deinitialization, and methods to add/remove permissions, check permission status, and serialize/deserialize from/to ZonElement.

The `PermissionMap` struct uses a `std.StringHashMapUnmanaged(void)` to store permissions internally. Memory allocation is handled by the `NeverFailingAllocator` and `NeverFailingArenaAllocator`. The `fromZon` method converts a `ZonElement` to a string hash map by iterating over its items and adding them to the internal map. The `toZon` method converts the internal representation back to a `ZonElement` by appending each key from the internal map to the ZonElement. Permissions are added using the `put` method, which ensures that each key is duplicated in the arena allocator. The `hasPermission` method returns `.no` if a permission path is found in the blacklist, `.yes` if it is found in the whitelist, and `.neutral` otherwise. Thread context assertion is performed using `sync.threadContext.assertCorrectContext(.server)` in various methods.

The `fromZon` method converts a `ZonElement` to a string hash map by iterating over its items and adding them to the internal map. The `toZon` method converts the internal representation back to a `ZonElement` by appending each key from the internal map to the ZonElement. Permissions are added using the `put` method, which ensures that each key is duplicated in the arena allocator. The `hasPermission` method returns `.no` if a permission path is found in the blacklist, `.yes` if it is found in the whitelist, and `.neutral` otherwise.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator) Permissions {
	return .{
		.arena = .init(allocator),
	};
}
```

## Related Questions
- How does the `fromZon` method convert a `ZonElement` to a string hash map?
- What specific fields are handled during the conversion process in the `fromZon` method?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_0*
