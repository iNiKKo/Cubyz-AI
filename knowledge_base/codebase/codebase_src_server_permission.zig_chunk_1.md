# [hard/codebase_src_server_permission.zig] - Chunk 1

**Type:** serialization
**Keywords:** permissions, unique ID, ZON files, memory allocation, error handling
**Symbols:** Group, Group.permissions, Group.id, Group.name, Group.init, Group.deinit, Group.fromZon, Group.toZon, Group.save, Group.addPermission, Group.removePermission, Group.hasPermission, groups, groupsArena, currentId
**Concepts:** permission management, group membership, file I/O, ZON serialization

## Summary
The `Group` struct manages permission groups with unique IDs and names. It handles initialization, deinitialization, saving to and loading from ZON files, adding/removing permissions, and checking permission status.

## Explanation
The `Group` struct manages permission groups with unique IDs and names, ensuring consistent user membership even after group deletions and recreations. Each group has a unique ID (`id`) to prevent stale membership issues, as demonstrated by the example scenario where User1 joins Group1, which is deleted and recreated while User1 is offline, leading to incorrect treatment upon reconnection. The struct provides methods for initialization (`init`), deinitialization (`deinit`), saving (`save`), and loading from ZON files (`fromBytes`, `toBytes`). It also includes functionality to add (`addPermission`) and remove (`removePermission`) permissions, as well as checking if a group has a specific permission (`hasPermission`). The `groups` variable is a `StringHashMapUnmanaged` that maps group names to their respective `Group` instances. The module manages the lifecycle of groups, including initialization (`init`), deinitialization (`deinit`), and loading all groups from a directory (`loadGroups`). It also handles saving metadata about groups (`saveMetaData`), which includes writing the current ID to a ZON file. The `groupsArena` allocator is used for memory management during group operations.

The `fromBytes` method reads a `Group` instance from a binary reader, checking the version and reading the necessary fields including permissions. The `toBytes` method writes a `Group` instance to a binary writer, including its version and permissions. The `loadGroups` function iterates over files in a directory, parsing their names to extract group IDs and loading the corresponding data using `fromBytes`. File names are expected to follow a specific format, with leading zeroes being invalid.

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
- How does the `Group` struct initialize a new group?
- What is the purpose of the `currentId` variable in this module?
- How are permissions added and removed from a group?
- What happens if there's an error saving metadata for permission groups?
- How does the module load all groups from a directory?
- What is the role of the `groupsArena` allocator in this module?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_1*
