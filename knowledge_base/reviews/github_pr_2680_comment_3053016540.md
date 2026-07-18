# [src/assets.zig] - PR #2680 review diff

**Type:** review
**Keywords:** readAsset, asset reading, path fallback, unreachable, std.mem.splitScalar, std.fmt.allocPrint
**Symbols:** readAsset, NeverFailingAllocator, assetFolder, subPath, id, fileEnding
**Concepts:** error handling, fallback mechanism, directory traversal

## Summary
Added a new function `readAsset` to handle asset reading with fallback paths.

## Explanation
The change introduces a new function `readAsset` that attempts to read an asset from a specified folder and subpath, using a module and name identifier. If the initial path does not exist, it falls back to a default 'assets' directory structure. The reviewer suggests changing the error handling in the fallback path allocation to use `unreachable` instead of returning null, indicating that this situation should never occur under normal circumstances.

## Related Questions
- What is the purpose of the `NeverFailingAllocator` in this function?
- How does the function handle errors when accessing the file system?
- Why is the fallback path structured as 'assets/{s}/{s}/{s}{s}'?
- What would be the implications if the fallback path allocation fails?
- How does the use of `unreachable` differ from returning null in error handling?
- Can you explain the role of `std.mem.splitScalar` in parsing the asset ID?

*Source: unknown | chunk_id: github_pr_2680_comment_3053016540*
