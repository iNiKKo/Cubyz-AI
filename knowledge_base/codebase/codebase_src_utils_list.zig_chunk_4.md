# [hard/codebase_src_utils_list.zig] - Chunk 4

**Type:** implementation
**Keywords:** dynamic array, enum-based indexing, memory reallocation, offset management, subarray retrieval
**Symbols:** MultiArray, MultiArray.offsets, MultiArray.items, MultiArray.capacity, MultiArray.initCapacity, MultiArray.deinit, MultiArray.clearAndFree, MultiArray.clearRetainingCapacity, MultiArray.ensureCapacity, MultiArray.addMany, MultiArray.replaceRange, MultiArray.getRange, MultiArray.getEverything
**Concepts:** multi-array management, memory allocation, subarray manipulation

## Summary
Defines a `MultiArray` type that holds multiple arrays sequentially in memory, allowing individual addressing and removal of subarrays.

## Explanation
The `MultiArray` struct is designed to manage multiple arrays stored contiguously in memory. It uses an enum `Range` to define the indices for each subarray. The struct maintains offsets for each subarray's start and end positions, as well as a pointer to the underlying array of elements (`items`). Key methods include initialization (`initCapacity`), deallocation (`deinit`), clearing with capacity retention (`clearRetainingCapacity`), ensuring sufficient capacity (`ensureCapacity`), adding multiple elements (`addMany`), replacing a range of elements (`replaceRange`), retrieving a specific subarray (`getRange`), and accessing all elements (`getEverything`). The struct ensures that the enum `Range` is exhaustive and that its values are within bounds.

## Code Example
```zig
pub fn initCapacity(allocator: NeverFailingAllocator, capacity: usize) @This() {
	return .{
		.items = allocator.alloc(T, capacity)[0..0],
		.capacity = capacity,
	};
}
```

## Related Questions
- How does `MultiArray` ensure that the enum `Range` is exhaustive?
- What method is used to add multiple elements to a `MultiArray`?
- How does `MultiArray` handle memory reallocation when more capacity is needed?
- What is the purpose of the `offsets` field in `MultiArray`?
- How do you retrieve all elements from a `MultiArray` instance?
- What method should be called to clear a `MultiArray` while retaining its capacity?

*Source: unknown | chunk_id: codebase_src_utils_list.zig_chunk_4*
