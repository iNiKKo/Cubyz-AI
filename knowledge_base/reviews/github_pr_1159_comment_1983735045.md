# [src/utils.zig] - PR #1159 review diff

**Type:** review
**Keywords:** readAlloc, allocator.dupe, memory allocation, BinaryReader, NeverFailingAllocator, readSlice, modular design
**Symbols:** BinaryReader, readAlloc, NeverFailingAllocator
**Concepts:** memory management, separation of concerns

## Summary
A new method `readAlloc` is added to the `BinaryReader` struct in `utils.zig`, which reads a slice of bytes into newly allocated memory. The reviewer suggests using a simpler `readSlice` function and letting the caller handle memory allocation with `allocator.dupe`.

## Explanation
**Explanation**
The addition of `readAlloc` to the `BinaryReader` struct in `utils.zig` introduces a new method that reads a slice of bytes into newly allocated memory. The method signature is as follows:

```zig
pub fn readAlloc(self: *BinaryReader, allocator: NeverFailingAllocator, length: usize) error{OutOfBounds, IntOutOfBounds}![]u8 {
```

This method can be useful when the caller needs a separate copy of the data. However, the reviewer suggests using a simpler `readSlice` function and letting the caller handle memory allocation with `allocator.dupe`. This approach aligns with principles of separation of concerns, potentially leading to cleaner code and better performance or safety, as it allows the caller to choose the most appropriate allocator based on their specific needs.

The reviewer's suggestion could improve code maintainability by clearly separating reading and allocation responsibilities. However, it may also introduce additional complexity if not handled carefully. The use of `NeverFailingAllocator` ensures that memory allocation will never fail, which can simplify error handling in the codebase.

## Related Questions
- What is the purpose of the `readAlloc` method in `BinaryReader`?
- Why does the reviewer suggest using `allocator.dupe` instead of allocating memory within `readAlloc`?
- How might separating reading and allocation responsibilities improve code maintainability?
- Can you explain the potential benefits and drawbacks of using `NeverFailingAllocator` in this context?
- What are the implications of changing from `readAlloc` to a `readSlice` method for existing Cubyz codebase?
- How could the reviewer's suggestion impact performance or memory usage in different scenarios?

*Source: unknown | chunk_id: github_pr_1159_comment_1983735045*
