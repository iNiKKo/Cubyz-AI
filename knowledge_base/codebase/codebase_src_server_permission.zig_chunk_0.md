# [hard/codebase_src_server_permission.zig] - Chunk 0

**Type:** api
**Keywords:** StringHashMapUnmanaged, getOrPut, keyIterator, dupe, remove, lastIndexOfScalar, NeverFailingArenaAllocator, threadContext, assertCorrectContext
**Symbols:** PermissionMap, Permissions, Group
**Concepts:** permission management, whitelist blacklist, serialization, ZonElement, thread context assertion, arena allocator, group membership

## Summary
Defines server-side permission management with PermissionMap (whitelist/blacklist) and Permissions structs that serialize to/from ZonElement, plus Group struct for user group membership.

## Explanation
The chunk declares PermissionMap as a struct containing an unmanaged StringHashMapUnmanaged(void). Its fromZon method iterates zon.toSlice(), converts each item to []const u8 (skipping nulls), and puts them into the map. The toZon method asserts server context, creates an array ZonElement, appends all keys via keyIterator, and returns it. PermissionMap.put uses getOrPut with a catch unreachable; if not found_existing it dupe the key into the map.

Permissions is a struct holding an arena allocator, whitelist and blacklist PermissionMaps. Its init method returns a Permissions with an initialized NeverFailingArenaAllocator (the rest of fields default to empty maps). deinit asserts server context and calls self.arena.deinit().

The list helper returns either &self.whitelist or &self.blacklist based on ListType enum (.white/.black). fromZon asserts server context, then calls self.list(.white).fromZon with zon.getChild("permissionWhitelist") and similarly for blacklist.
toZon asserts server context, puts "permissionWhitelist" and "permissionBlacklist" into the provided ZonElement using self.list(...).toZon. addPermission asserts server context, gets the appropriate list via self.list(listType), then calls put with allocator.dupe of permissionPath. removePermission asserts server context, returns the result of map.remove on the selected list.

hasPermission walks a permission path by repeatedly finding the last '/' (std.mem.lastIndexOfScalar). At each segment it checks blacklist.map.contains; if found returns .no, else whitelist.map.contains; if found returns .yes. It descends to the parent segment (permissionPath[0..nextPos]). If no slash remains and whitelist contains "/" it returns .yes, otherwise .neutral.

Group is a struct with permissions field, an id u32, and name []const u8. The comment explains that each group must have a unique ID to avoid stale membership issues (User1 joins Group1, Group1 deleted while User1 offline, new Group1 created, User1 reconnects incorrectly treated as member of new Group1). init increments currentId, calls saveMetaData with error logging on failure, allocates Group via allocator.create, initializes permissions, sets id and name, then calls self.save. deinit asserts server context, calls self.permissions.deinit(), and destroys the group.

fromZon creates a Group, initializes its permissions, sets id and name from parameters (the snippet cuts off before completing the struct initialization).

## Related Questions
- How does PermissionMap.fromZon handle null items in zon.toSlice?
- What happens inside PermissionMap.put when a key already exists?
- Which fields are initialized by default in Permissions.init?
- How does hasPermission descend through a permission path like 'admin/chat'?
- Why is currentId incremented before creating a Group in init?
- What error message is logged if saveMetaData fails during Group.init?
- Does toZon write both whitelist and blacklist even if one is empty?
- How does fromZon for Permissions extract child nodes named 'permissionWhitelist' and 'permissionBlacklist'?
- Is the PermissionMap stored inside Permissions owned by the arena or unmanaged?

*Source: unknown | chunk_id: codebase_src_server_permission.zig_chunk_0*
