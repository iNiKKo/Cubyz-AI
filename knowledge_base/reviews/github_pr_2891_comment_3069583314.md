# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactoring, property access, pointer safety, arithmetic operations, use case
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** thread safety, memory management

## Summary
Refactored `getProperty` method in `ProceduralItem` struct to return a value directly and added a new `getPropertyPtr` method for pointer access.

## Explanation
The change refactors the `getProperty` method to return an `f32` value instead of a pointer, which reduces the risk of dangling pointers. A new method, `getPropertyPtr`, is introduced to provide direct pointer access when needed. The reviewer highlights that the primary concern is preventing unsafe overwriting of properties after tool initialization. The decision between using `getPtr` or `set` methods depends on the specific use case; for operations like `*=` where pointer arithmetic is beneficial, `getPtr` is preferred.

## Related Questions
- What is the purpose of the `getPropertyPtr` method in the `ProceduralItem` struct?
- How does the refactoring prevent dangling pointers?
- In what scenarios should `getPtr` be used over direct property access?
- What are the potential risks associated with overwriting properties after tool initialization?
- How does this change impact performance and correctness of item property management in Cubyz?
- Can you explain the architectural reasoning behind separating value and pointer access methods?

*Source: unknown | chunk_id: github_pr_2891_comment_3069583314*
