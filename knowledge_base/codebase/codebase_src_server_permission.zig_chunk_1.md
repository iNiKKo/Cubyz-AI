# [hard/codebase_src_server_permission.zig] - Chunk 1

**Type:** serialization
**Keywords:** NeverFailingAllocator, ZonElement, thread context assertion, error handling, hashmap operations
**Symbols:** init, deinit, fromZon, toZon, save, addPermission, removePermission, hasPermission, groups, groupsArena, currentId
**Concepts:** permission management, group initialization, data persistence, Zon serialization

## Summary
This chunk manages permission group initialization, deinitialization, and persistence using Zon format. It also handles adding, removing, and checking permissions within groups.

## Explanation
The chunk defines a `Group` struct with methods for initialization (`init`), deinitialization (`deinit`), loading from Zon data (`fromZon`), saving to Zon data (`toZon`), saving the group to disk (`save`), adding permissions (`addPermission`), removing permissions (`removePermission`), and checking if a permission exists (`hasPermission`). It also manages a global `groups` hashmap and provides functions for initializing and deinitializing the groups system, loading groups from a directory (`loadGroups`), creating new groups (`createGroup`), retrieving existing groups (`getGroup`), and deleting groups (`deleteGroup`). The chunk ensures that all operations are performed in the server thread context using `sync.threadContext.assertCorrectContext(.server)`. It uses ZonElement for serialization and deserialization, and handles errors by logging them or returning appropriate error codes.

## Code Example
```zig
fn init(allocator: NeverFailingAllocator, name: []const u8) *Group {
	sync.threadContext.assertCorrectContext(.server);
	currentId += 1;
	saveMetaData(allocator) catch |err| {
		std.log.err("Couldn't save permission groups metadata: {t}", .{err});
	};
	const self = allocator.create(Group);
	self.* = .{
		.permissions = .init(allocator),
		.id = currentId,
		.name = name,
	};
	self.save(allocator);
	return self;
}
```

## Related Questions
- How does the `Group` struct initialize its permissions?
- What error handling is implemented in the `saveMetaData` function?
- How are groups loaded from a directory in this chunk?
- What is the purpose of the `currentId` variable in this chunk?
- How does the `createGroup` function handle duplicate group names?
- What methods are available for managing permissions within a group?
- How is thread context asserted in this chunk's functions?
- What role does the `groupsArena` allocator play in this chunk?
- How is data persisted to disk in this chunk?
- What is the structure of the Zon files used for serialization?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_1*
