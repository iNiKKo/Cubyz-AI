# [src/utils/heap.zig] - PR #2320 review diff

**Type:** review
**Keywords:** allocators, globalGpa, handledGpa, std.heap, ErrorHandlingAllocator, std.testing, builtin.is_test, interface declaration, testing consistency
**Symbols:** std.heap.GeneralPurposeAllocator, ErrorHandlingAllocator, std.testing.allocator, builtin.is_test
**Concepts:** thread safety, testing allocator, error handling

## Summary
The change modifies the initialization of allocators based on whether the build is for testing or not.

## Explanation
The patch introduces conditional initialization for `globalGpa` and `handledGpa`. If the build is for testing (`builtin.is_test`), `globalGpa` is set to `undefined`, and `handledGpa` uses `std.testing.allocator`. Otherwise, it initializes `globalGpa` as a `GeneralPurposeAllocator` with thread safety enabled and wraps it in an `ErrorHandlingAllocator`. The reviewer suggests that the initialization should be done at the declaration of the interface and proposes a globally accessible testing allocator wrapped in the error handling allocator for consistency.

## Related Questions
- What is the purpose of initializing `globalGpa` to `undefined` in a test build?
- How does the patch ensure thread safety for non-test builds?
- Why is it recommended to have a globally accessible testing allocator?
- What are the potential implications of using `std.testing.allocator` directly in tests?
- How does this change affect the performance of memory allocation in test environments?
- Can you explain the role of `ErrorHandlingAllocator` in both test and non-test builds?

*Source: unknown | chunk_id: github_pr_2320_comment_2547111362*
