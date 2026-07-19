# [src/server/world.zig] - PR #2587 review diff

**Type:** review
**Keywords:** ServerWorld, loadPermissionGroups, groups.zig.zon, memory, saves, permission groups, file reading, allocator, writeZon, allocPrint, stackAllocator
**Symbols:** ServerWorld, loadPermissionGroups, files.cubyzDir().writeZon, std.fmt.allocPrint, main.stackAllocator.allocator
**Concepts:** memory management, file I/O, data loading

## Summary
Added a function to load permission groups from disk into memory.

## Explanation
The change introduces a new function `loadPermissionGroups` in the `ServerWorld` struct. This function reads permission group data from a file named 'groups.zig.zon' located in the server's save directory and loads it into memory. The exact path is constructed using `std.fmt.allocPrint(main.stackAllocator.allocator, "saves/{s}/groups.zig.zon", .{self.path}) catch unreachable;`. After loading the data, it writes the world data to a file using `files.cubyzDir().writeZon(path, worldData);`. The reviewer suggests loading all permission groups into memory to simplify management, indicating that this approach is acceptable for current needs.

## Related Questions
- What is the purpose of the `loadPermissionGroups` function?
- Where does the function read permission group data from?
- How is memory allocated for storing the permission group data?
- Why was it decided to load all permission groups into memory?
- What potential issues could arise from loading all permission groups into memory?
- Is there any error handling in the `loadPermissionGroups` function?
- How does this change affect the overall architecture of the server world management?
- Are there any performance implications of loading all permission groups into memory?
- Can you explain the role of `main.stackAllocator.allocator` in this context?
- What is the format of the 'groups.zig.zon' file?
- How does this change impact backwards compatibility?

*Source: unknown | chunk_id: github_pr_2587_comment_2961265211*
