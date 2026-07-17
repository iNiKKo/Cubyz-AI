# [src/assets.zig] - Chunk 3053015695

**Type:** review
**Keywords:** NeverFailingAllocator, allocPrint, catch unreachable, allocation failure, main.stackAllocator.allocator, control flow, regression prevention, type contract, unreachable path, Zig best practices
**Symbols:** readAsset, unloadAssets, NeverFailingAllocator, main.stackAllocator.allocator, std.fmt.allocPrint
**Concepts:** allocation failure semantics, never-failing allocator contract, unreachable error handling, control flow clarity, regression prevention, type safety in Zig

## Summary
The reviewer flags an allocation failure in `readAsset` as impossible given the allocator contract, and suggests replacing the generic `catch &.{}' with a more precise `catch unreachable`. This change documents that any path constructed here is guaranteed to succeed under the NeverFailingAllocator semantics.

## Explanation
The function `readAsset` uses `std.fmt.allocPrint` with `main.stackAllocator.allocator`, which is typed as `NeverFailingAllocator`. By definition, an allocation from this allocator cannot fail; therefore any error path taken by `allocPrint` is unreachable in correct execution. The original code catches the error and returns an empty slice (`&.{}'), which silently masks a logical impossibility and could mislead future maintainers into thinking failure handling is required. The reviewer's suggestion to replace that with `catch unreachable` makes the control flow explicit: if allocation fails, it indicates a bug in the allocator or surrounding assumptions rather than a recoverable condition. This aligns with Zig best practices for expressing impossible error paths and prevents regression where someone might later change the allocator type without updating the catch clause.

## Related Questions
- What is the definition of NeverFailingAllocator in this codebase?
- Where else does readAsset use main.stackAllocator.allocator for allocations?
- Does unloadAssets ever call readAsset with a non-never-failing allocator?
- Is there any path where allocPrint could fail given the current allocator type?
- What happens if someone replaces NeverFailingAllocator with a regular Allocator in readAsset?
- Are there other functions that catch errors from allocPrint and treat them as recoverable?
- Does main.stackAllocator.allocator have any documented failure modes?
- Is there a test case that verifies readAsset never returns null due to allocation failure?
- What is the expected behavior of std.fmt.allocPrint when given an empty string for assetFolder?
- Could the splitScalar on id ever produce a name that causes allocPrint to fail?

*Source: unknown | chunk_id: github_pr_2680_comment_3053015695*
