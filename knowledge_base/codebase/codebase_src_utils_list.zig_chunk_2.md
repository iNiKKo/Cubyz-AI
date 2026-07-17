# [hard/codebase_src_utils_list.zig] - Chunk 2

**Type:** implementation
**Keywords:** append-only, capacity, realloc, insertion, removal, NeverFailingAllocator, assert, swapRemove, orderedRemove, popOrNull
**Symbols:** clearAndFree, clearRetainingCapacity, shrinkAndFree, toOwnedSlice, ensureCapacity, ensureFreeCapacity, resizeAssumeCapacity, resize, addOneAssumeCapacity, addOne, addManyAssumeCapacity, addMany, appendAssumeCapacity, append, appendNTimesAssumeCapacity, appendNTimes, appendSliceAssumeCapacity, appendSlice, insertAssumeCapacity, insert, insertSliceAssumeCapacity, insertSlice, swapRemove, orderedRemove, popOrNull, pop
**Concepts:** append-only list, capacity management, memory reallocation, NeverFailingAllocator, element insertion, swap removal, ordered removal, slice detachment

## Summary
Implements a generic append-only list with capacity management and element insertion/removal operations.

## Explanation
The chunk defines methods on a list type (self: *@This()) that manage an internal items array. Capacity is handled via ensureCapacity, which asserts newCapacity >= current length before reallocating; shrinkAndFree reallocates to a smaller size; clearRetainingCapacity zeroes length without freeing memory. Memory ownership uses NeverFailingAllocator for all reallocations and frees. The list supports append (addOne, addMany), insert at arbitrary index with backward copy of remaining elements, swapRemove which replaces an element with the last one, orderedRemove which shifts subsequent elements forward, pop/popOrNull for LIFO removal, resizeAssumeCapacity to set length without allocation, and toOwnedSlice to detach a slice. All mutating operations that may reallocate or modify capacity take NeverFailingAllocator; those that assume sufficient space use *_AssumeCapacity variants with std.debug.assert checks.

## Related Questions
- What is the purpose of clearAndFree and how does it differ from clearRetainingCapacity?
- How does ensureCapacity guarantee sufficient space before reallocating memory?
- Describe the behavior of shrinkAndFree when given a newLen smaller than current capacity.
- Which methods use NeverFailingAllocator versus those that assume existing capacity is enough?
- Explain how insertAssumeCapacity handles insertion at the end versus an interior index.
- What does swapRemove do to the list length and which element value is returned?
- How does orderedRemove preserve order when removing an element from the middle of the list?
- When would you call popOrNull instead of pop in this API surface?
- What is the role of resizeAssumeCapacity compared to resize with respect to allocation?
- Does toOwnedSlice free the original backing array or just return a new slice?

*Source: unknown | chunk_id: codebase_src_utils_list.zig_chunk_2*
