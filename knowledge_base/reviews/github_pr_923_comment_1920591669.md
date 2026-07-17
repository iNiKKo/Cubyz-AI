# [src/zon.zig] - PR #923 review diff

**Type:** review
**Keywords:** clone, join, ZonElement, allocator, duplication, recursion, deep copy, merge, object, array
**Symbols:** ZonElement, clone, joinGetNew, NeverFailingAllocator
**Concepts:** deep copy, merge, recursion, code duplication

## Summary
Added `clone` and `joinGetNew` methods to `ZonElement` for deep copying and merging elements, respectively. The reviewer suggests refactoring to avoid code duplication.

## Explanation
The changes introduce two new methods in the `ZonElement` union: `clone` and `joinGetNew`. The `clone` method performs a deep copy of the `ZonElement`, handling different types including strings, arrays, and objects. The `joinGetNew` method merges two `ZonElement` instances, recursively joining nested structures. The reviewer notes that the code in `join` is nearly identical to `joinGetNew`, suggesting potential for refactoring to eliminate duplication.

## Related Questions
- How does the `clone` method handle memory allocation for nested structures?
- What is the purpose of the `NeverFailingAllocator` in these methods?
- Can you explain the logic behind merging objects in the `joinGetNew` method?
- Why does the reviewer suggest refactoring to avoid code duplication?
- How does the `join` method differ from `joinGetNew`, and why is this distinction important?
- What are the potential performance implications of deep copying large structures in these methods?

*Source: unknown | chunk_id: github_pr_923_comment_1920591669*
