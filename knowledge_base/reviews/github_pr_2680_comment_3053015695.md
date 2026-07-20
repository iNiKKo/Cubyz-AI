# [src/assets.zig] - PR #2680 review diff

**Type:** review
**Keywords:** readAsset, allocPrint, unreachable, allocator, asset management
**Symbols:** readAsset, NeverFailingAllocator, assetFolder, subPath, id, fileEnding
**Concepts:** allocation safety, error handling

## Summary
Added a new function `readAsset` to handle asset reading with specific formatting and allocation.

## Explanation
The review introduces a new function `readAsset` designed to read assets from a specified folder, subpath, and ID with a given file ending. The function uses `std.mem.splitScalar(u8, id, ':')` to split the `id` into `mod` and `name`. If the split operation fails (i.e., there is no colon in `id`), the function returns null. The use of `NeverFailingAllocator` implies that allocations cannot fail, and thus suggests replacing the error handling with `unreachable` to indicate an internal logic error if allocation fails. This change ensures that any allocation failure is treated as a critical bug rather than a recoverable error.

The function takes several parameters: `allocator`, `assetFolder`, `subPath`, `id`, and `fileEnding`. The `id` parameter is expected to be in the format 'mod:name'. If the split operation fails, the function returns null. The use of `NeverFailingAllocator` ensures that allocations cannot fail, so any allocation failure is treated as a critical bug rather than a recoverable error.

The function constructs the asset path using `std.fmt.allocPrint(main.stackAllocator.allocator, "{s}/{s}/{s}/{s}{s}", .{assetFolder, mod, subPath, name, fileEnding})`. If this allocation fails, it is treated as an internal logic error and handled with `unreachable`.

This function fits into the overall asset management system by providing a way to read assets from specific locations with the required format.

## Related Questions
- What is the purpose of the `NeverFailingAllocator` in this context?
- How does the function handle invalid input for `id`?
- Can you explain the use of `std.mem.splitScalar` in this code?
- Why is `unreachable` used instead of returning an error?
- What potential issues could arise from using `main.stackAllocator.allocator`?
- How does this function fit into the overall asset management system?

*Source: unknown | chunk_id: github_pr_2680_comment_3053015695*
