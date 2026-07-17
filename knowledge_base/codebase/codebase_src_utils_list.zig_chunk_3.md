# [hard/codebase_src_utils_list.zig] - Chunk 3

**Type:** implementation
**Keywords:** dynamic resizing, memory allocation, element manipulation, string printing, enum handling
**Symbols:** List, List.append, List.swapRemove, List.orderedRemove, List.popOrNull, List.pop, List.replaceRange, List.print, MultiArray
**Concepts:** dynamic array, multi-array management, string formatting

## Summary
The chunk defines a generic list data structure with various operations like appending, removing, and printing elements. It also includes a MultiArray type for holding multiple arrays sequentially.

## Explanation
This chunk implements a generic list data structure with methods for appending, swapping, ordered removal, popping, replacing ranges, and printing elements. The `print` method uses an allocator to format strings into the list's buffer. Additionally, it defines a `MultiArray` type that holds multiple arrays sequentially in memory, allowing addressing and removing each subarray individually.

## Code Example
```zig
pub fn popOrNull(self: *@This()) ?T {
    if (self.items.len == 0) return null;
    const val = self.items[self.items.len - 1];
    self.items.len -= 1;
    return val;
}
```

## Related Questions
- How does the List.append method work?
- What is the purpose of the swapRemove method in the List type?
- Can you explain how the replaceRange method handles different lengths of new_items compared to the existing range?
- What happens if the buffer address changes after calling List.print?
- How does MultiArray ensure that each subarray can be addressed individually?
- What assertion checks are performed on the Range enum in MultiArray?

*Source: unknown | chunk_id: codebase_src_utils_list.zig_chunk_3*
