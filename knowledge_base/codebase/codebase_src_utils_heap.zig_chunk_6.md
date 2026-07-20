# [hard/codebase_src_utils_heap.zig] - Chunk 6

**Type:** implementation
**Keywords:** power of two, free list, mutex locking, aligned allocation, deinitialization
**Symbols:** PowerOfTwoPoolAllocator, Node, Node.next, NodePtr, Bucket, Bucket.freeLists, Bucket.freeAllocations, Bucket.totalAllocations, Bucket.deinit, Bucket.create, Bucket.destroy, Bucket.allocNew, Self, alignment, baseShift, bucketCount
**Concepts:** memory management, pool allocator, thread safety

## Summary
Defines a memory allocator that manages fixed-size blocks of power-of-two sizes, using a pool-based approach with thread safety.

## Explanation
Defines a memory allocator that manages fixed-size blocks of power-of-two sizes, using a pool-based approach with thread safety.

The `PowerOfTwoPoolAllocator` function generates a type that implements an efficient memory allocation strategy for fixed-size blocks. It uses a series of buckets, each managing a specific size class (power of two). The allocator ensures that all allocations and deallocations are aligned to the maximum alignment specified at creation time (`maxAlignment`). Each bucket maintains a free list of nodes, which are reused when possible to reduce memory fragmentation and improve allocation speed.

The `PowerOfTwoPoolAllocator` function takes three parameters: `minSize`, `maxSize`, and `maxAlignment`. These parameters define the range of block sizes managed by the allocator and the maximum alignment required for allocations. The `minSize` must be a power of two, and it must be greater than or equal to `maxAlignment` and `@sizeOf(usize)`. The `maxSize` must also be a power of two and greater than `minSize`. Additionally, several assertions are made to ensure that these parameters meet the required conditions.

The allocator uses a mutex (`mutex`) to synchronize access across multiple threads, ensuring thread safety. Each bucket in the allocator maintains a free list of nodes (`freeLists`). When an allocation is requested, the allocator checks if there are any available nodes in the free list. If not, it allocates a new block from the arena and adds it to the free list.

The `deinit` method checks for any leaked allocations in each bucket and logs relevant statistics. It also deinitializes the arena and sets the bucket to an undefined state.

The `allocNew` function is responsible for allocating a new block of memory from the arena. It increments both `freeAllocations` and `totalAllocations` counters when a new block is allocated.

The `allocator` method returns a `NeverFailingAllocator` that uses the allocator's vtable to handle allocation, resizing, remapping, and freeing operations. The `alloc` function checks alignment constraints and size requirements before allocating a new block. The `resize`, `remap`, and `free` functions are implemented but do not perform any operations in this version of the allocator.

The calculation of `alignment` is done using `@max(maxAlignment, @sizeOf(usize))`. The `baseShift` is calculated as `std.math.log2_int(usize, minSize)`, and `bucketCount` is calculated as `std.math.log2_int(usize, maxSize) - baseShift + 1`.

The `Node` struct contains a single field: `next`, which is an optional pointer to the next node in the free list. The `NodePtr` type is a pointer to `Node` with alignment set to `alignment`. The `Bucket` struct maintains a free list of nodes (`freeLists`), counts of free and total allocations (`freeAllocations` and `totalAllocations`), and provides methods for deinitialization (`deinit`), creating new items (`create`), destroying previously created items (`destroy`), and allocating new blocks from the arena (`allocNew`).

## Code Example
```zig
pub fn deinit(self: *Bucket, size: usize) void {
	if (self.freeAllocations != self.totalAllocations) {
		std.log.err("PowerOfTwoPoolAllocator bucket of size {} leaked {} elements", .{size, self.totalAllocations - self.freeAllocations});
	} else if (self.totalAllocations != 0) {
		std.log.info("{} MiB ({} elements) in size {} PowerOfTwoPoolAllocator bucket", .{self.totalAllocations*size >> 20, self.totalAllocations, size});
	}
	self.* = undefined;
}
```

## Code Example
```zig
pub fn deinit(self: *Bucket, size: usize) void {
	if (self.freeAllocations != self.totalAllocations) {
		std.log.err("PowerOfTwoPoolAllocator bucket of size {} leaked {} elements", .{size, self.totalAllocations - self.freeAllocations});
	} else if (self.totalAllocations != 0) {
		std.log.info("{} MiB ({} elements) in size {} PowerOfTwoPoolAllocator bucket", .{self.totalAllocations*size >> 20, self.totalAllocations, size});
	}
	self.* = undefined;
}
```

## Related Questions
- What is the purpose of the `PowerOfTwoPoolAllocator` function?
- How does the allocator ensure thread safety?
- What happens if there are leaked allocations in a bucket?
- How are nodes managed within each bucket?
- What alignment constraints must be met for allocations and deallocations?
- What is the role of the mutex in this allocator?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_6*
