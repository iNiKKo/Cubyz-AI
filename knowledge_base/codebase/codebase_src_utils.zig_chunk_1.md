# [hard/codebase_src_utils.zig] - Chunk 1

**Type:** implementation
**Keywords:** alias table, random sampling, binary search, dynamic array resizing, memory allocation
**Symbols:** AliasSampler, AliasSampler.items, AliasSampler.aliasData, AliasSampler.init, AliasSampler.initFromContext, AliasSampler.deinit, AliasSampler.sample, SortedList, SortedList.ptr, SortedList.len, SortedList.capacity, SortedList.deinit, SortedList.items, SortedList.increaseCapacity, SortedList.insertSorted, SortedList.toOwnedSlice, Array2D, Array2D.mem, Array2D.width, Array2D.height, Array2D.init, Array2D.deinit, Array2D.get
**Concepts:** weighted random sampling, sorted list management, 2D array handling

## Summary
This chunk defines utility data structures and functions for managing sorted lists, alias sampling, and 2D arrays.

## Explanation
The chunk includes three main components: AliasSampler, SortedList, and Array2D. The AliasSampler is used for weighted random sampling with an efficient initialization and sampling process. It uses alias tables to handle overfull and underfull bins during the setup. The SortedList maintains a list of items sorted in ascending order, providing functions for insertion, deinitialization, and converting to an owned slice. The Array2D provides a 2D array structure with initialization, deinitialization, and element access methods.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator, items: []T) @This() {
	var self: @This() = .{
		.items = items,
		.aliasData = allocator.alloc(AliasData, items.len),
	};
	if (items.len == 0) return self;
	@memset(self.aliasData, AliasData{.chance = 0, .alias = 0});
	const currentChances = main.stackAllocator.alloc(f32, items.len);
	defer main.stackAllocator.free(currentChances);
	var totalChance: f32 = 0;
	for (items, 0..) |item, i| {
		totalChance += item.chance;
		currentChances[i] = item.chance;
	}

	self.initAliasData(totalChance, currentChances);

	return self;
}
```

## Related Questions
- How does the AliasSampler initialize its alias data?
- What is the purpose of the SortedList's increaseCapacity function?
- How does the Array2D structure handle memory allocation and deallocation?
- Can you explain the algorithm used in AliasSampler.sample?
- What ensures that the items in a SortedList remain sorted?
- How does the AliasSampler handle cases where an item's chance is overfull or underfull?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_1*
