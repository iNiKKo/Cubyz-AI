# [src/assets.zig] - PR #2680 review diff

**Type:** review
**Keywords:** readAsset, allocPrint, unreachable, allocator, asset management
**Symbols:** readAsset, NeverFailingAllocator, assetFolder, subPath, id, fileEnding
**Concepts:** allocation safety, error handling

## Summary
Added a new function `readAsset` to handle asset reading with specific formatting and allocation.

## Explanation
The review introduces a new function `readAsset` designed to read assets from a specified folder, subpath, and ID with a given file ending. The function uses `std.mem.splitScalar(u8, id, ':')` to split the `id` into `mod` and `name`. If the split operation fails (i.e., there is no colon in `id`), the function returns null. The use of `NeverFailingAllocator` implies that allocations cannot fail, and thus suggests replacing the error handling with `unreachable` to indicate an internal logic error if allocation fails. This change ensures that any allocation failure is treated as a critical bug rather than a recoverable error.

## Related Questions
- What is the purpose of the `NeverFailingAllocator` in this context?
- How does the function handle invalid input for `id`?
- Can you explain the use of `std.mem.splitScalar` in this code?
- Why is `unreachable` used instead of returning an error?
- What potential issues could arise from using `main.stackAllocator.allocator`?
- How does this function fit into the overall asset management system?

*Source: unknown | chunk_id: github_pr_2680_comment_3053015695*
