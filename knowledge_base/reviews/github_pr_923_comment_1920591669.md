# [src/zon.zig] - PR #923 review diff

**Type:** review
**Keywords:** clone, deep copy, merge, allocator, ZonElement, array, object, iterator, NeverFailingAllocator, consolidation
**Symbols:** ZonElement, clone, joinGetNew, NeverFailingAllocator
**Concepts:** Deep Copying, Memory Management, Code Duplication

## Summary
Added `clone` and `joinGetNew` methods to `ZonElement` for deep copying and merging elements, respectively. The reviewer suggests consolidating duplicate code between these functions.

## Explanation
The changes introduce two new methods in the `ZonElement` union: `clone` and `joinGetNew`. The `clone` method performs a deep copy of the `ZonElement`, handling different types such as integers, floats, strings, booleans, nulls, arrays, and objects. Specifically, for arrays, it iterates through each item and clones them using the provided allocator. For objects, it creates a new object, iterates through the entries, and clones or merges values based on whether they already exist in the target object.

The `joinGetNew` method merges two `ZonElement` instances, also using deep copying where necessary. It handles arrays by appending items from the other array to the current one. For objects, it iterates through the entries of the other object and either clones or recursively merges values if they already exist in the target object.

The reviewer notes that there is significant code duplication between these methods, specifically in how they handle array and object merging, and suggests finding a way to consolidate this logic to avoid redundancy.

## Related Questions
- How can the `clone` and `joinGetNew` methods be consolidated to avoid code duplication?
- What are the potential performance implications of deep copying in these methods?
- How does the `NeverFailingAllocator` ensure that memory allocation never fails?
- Can you provide an example of how to use the `join` method on two `ZonElement` instances?
- What changes would be necessary to handle additional data types in the `clone` and `joinGetNew` methods?
- How does the current implementation handle errors during memory allocation in the `clone` method?

*Source: unknown | chunk_id: github_pr_923_comment_1920591669*
