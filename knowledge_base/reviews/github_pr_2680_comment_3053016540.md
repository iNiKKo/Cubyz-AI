# [src/assets.zig] - PR #2680 review diff

**Type:** review
**Keywords:** readAsset, asset reading, path fallback, unreachable, std.fmt.allocPrint, std.fs.cwd().access
**Symbols:** readAsset, NeverFailingAllocator, assetFolder, subPath, id, fileEnding
**Concepts:** error handling, fallback mechanism, path construction

## Summary
Added a new function `readAsset` to handle asset reading with fallback paths.

## Explanation
The `readAsset` function is introduced to read assets from specified folders and subpaths. It constructs the file path using module, name, and file ending, and attempts to access the file. If the initial path fails, it falls back to a default asset folder path. The reviewer suggests changing the error handling in the fallback path to `unreachable` to ensure that any allocation failure is treated as a critical issue.

## Related Questions
- What is the purpose of the `NeverFailingAllocator` in this function?
- How does the function handle multiple path construction attempts?
- Why is the fallback path constructed differently from the initial one?
- What is the significance of using `unreachable` in the error handling of the fallback path?
- How does this function ensure that the allocated memory is properly freed?
- Can you explain the role of `std.mem.splitScalar` in parsing the asset ID?

*Source: unknown | chunk_id: github_pr_2680_comment_3053016540*
