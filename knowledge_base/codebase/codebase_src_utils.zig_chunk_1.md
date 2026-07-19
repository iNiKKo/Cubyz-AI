# [hard/codebase_src_utils.zig] - Chunk 1

**Type:** implementation
**Keywords:** Alias Method, dynamic array, random sampling, sorting, memory management
**Symbols:** AliasTable, AliasTable.AliasData, AliasTable.items, AliasTable.aliasData, AliasTable.ownsSlice, AliasTable.initAliasData, AliasTable.init, AliasTable.initFromContext, AliasTable.deinit, AliasTable.sample, SortedList, SortedList.ptr, SortedList.len, SortedList.capacity, SortedList.deinit, SortedList.items, SortedList.increaseCapacity, SortedList.insertSorted, SortedList.toOwnedSlice
**Concepts:** weighted random sampling, sorted list

## Summary
This chunk implements the Alias Method for weighted random sampling and a sorted list data structure.

## Explanation
This chunk implements the Alias Method for weighted random sampling and a sorted list data structure. The `AliasTable` type is an implementation of the Alias Method, which allows for efficient weighted random sampling. It includes methods to initialize the alias table from a list of items with associated chances, deinitialize it, and sample an item based on its chance. The `SortedList` type is a dynamic array that maintains elements in ascending order, providing methods to insert elements while keeping them sorted, convert the list to an owned slice, and deinitialize it.

### AliasTable
- **AliasData**: A struct containing `chance` (u16) and `alias` (u16).
- **items**: An array of items with associated chances.
- **aliasData**: An array of AliasData structs used for alias sampling.
- **ownsSlice**: A boolean indicating whether the `AliasTable` owns the slice of items.

**Methods**:
- **initAliasData**: Initializes the alias data based on the total chance and current chances of items. It calculates the desired chance, iterates through the items to balance probabilities, and sets up aliases accordingly.
- **init**: Initializes the `AliasTable` from a list of items with associated chances. It allocates memory for alias data, calculates total chances, and initializes alias data using `initAliasData`.
- **initFromContext**: Initializes the `AliasTable` from a context slice, converting each context to an item and then initializing it similarly to `init`.
- **deinit**: Frees the allocated memory for alias data and items if owned.
- **sample**: Samples an item based on its chance using the alias method. It generates a random index and checks the alias data to determine the final sampled item.

### SortedList
- **ptr**: A pointer to the array of elements.
- **len**: The current length of the list.
- **capacity**: The total capacity of the list.

**Methods**:
- **deinit**: Frees the allocated memory for the list.
- **items**: Returns a slice of the list's items.
- **increaseCapacity**: Increases the capacity of the list by reallocating it to a new size (8 + current capacity * 3/2).
- **insertSorted**: Inserts an element into the sorted list while maintaining order. It shifts elements as needed and inserts the new item at the correct position.
- **toOwnedSlice**: Converts the list to an owned slice, freeing the original list and returning the new slice.

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
- How does the AliasTable initialize its alias data?
- What is the purpose of the SortedList type in this chunk?
- How does the SortedList handle capacity increases when inserting elements?
- Can you explain how the sample method works in the AliasTable?
- What is the role of the ownsSlice field in the AliasTable struct?
- How does the SortedList maintain its sorted order during insertions?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_1*
