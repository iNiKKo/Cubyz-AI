# [src/server/command/permission/perm.zig] - Chunk 3328982446

**Type:** review
**Keywords:** perm, whitelist, blacklist, add, remove, playerIndex, permissionPath, stackAllocator, NeverFailingAllocator, ListUnmanaged, union, enum, deinit
**Symbols:** Args, ArgParser, Path, NeverFailingAllocator, ListUnmanaged, User, permission.Permissions.ListType, command.Target, execute
**Concepts:** memory leak prevention, allocator correctness, union-based argument parsing, deferred cleanup, stack vs heap allocation semantics, error propagation, command-line interface parsing

## Summary
Refactored /perm command parsing from a manual split-based approach using an incorrect stack-allocated helper struct into a union-based argument parser with proper error handling and correct allocator usage.

## Explanation
The original implementation used std.mem.splitScalar to parse arguments, storing the permission path in a local variable that was allocated on the stack via main.stackAllocator. This caused a memory leak because the split iterator held references to the original args slice, but the permissionPath string itself was not properly managed after being copied or referenced elsewhere. Additionally, the Helper struct was initialized with a stack-allocated allocator (main.stackAllocator), which is inappropriate since it outlives the function call and cannot be freed by defer within execute(). The new design introduces an Args union enum to represent parsed command structures, using NeverFailingAllocator for the union itself while delegating error messages to main.stackAllocator via ListUnmanaged. This ensures that only temporary allocations are made on the stack for parsing, while persistent or potentially leaked data is handled with appropriate allocator semantics. The switch statement now directly maps parsed parameters to actions without intermediate helper structs, reducing complexity and eliminating the need for manual split management.

## Related Questions
- What is the difference between NeverFailingAllocator and main.stackAllocator in this context?
- Why was the original Helper struct using main.stackAllocator considered a bug?
- How does the new Args union handle both add/remove actions with optional player indices?
- Where are permission paths validated to ensure they start with '/'?
- What happens if ArgParser.parse fails and how is the error communicated to the user?
- Is there any risk of double-free or use-after-free in the new implementation?
- How does the code ensure that target.deinit() is always called regardless of success/failure?
- Why was std.mem.splitScalar replaced with a union-based parser instead of keeping split logic?
- What would happen if someone passed an empty args slice to execute after this refactor?
- Does the new Path struct allocate memory for its path field or does it reference existing slices?
- How are whitelist and blacklist mapped internally in the permission system?
- Is there any performance impact from using union enums instead of direct string comparisons?

*Source: unknown | chunk_id: github_pr_3112_comment_3328982446*
