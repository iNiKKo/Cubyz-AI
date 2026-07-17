# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactoring, property access, array storage, pointer handling, syntax sugar, future-proofing, locking mechanisms
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** thread safety, memory management

## Summary
Refactored `getProperty` method to use an array for property storage and added a new `getPropertyPtr` method. The reviewer suggests adding locking mechanisms in the future without altering every call.

## Explanation
The change refactors the `ProceduralItem` struct by modifying the `getProperty` method to access properties from an array instead of using inline switch statements with field access. A new method, `getPropertyPtr`, is introduced to provide a pointer to the property value. The reviewer expresses concern about potential issues with storing pointers and questions the use of syntax sugar in Zig's design. They suggest that adding locking mechanisms later would be more future-proof without requiring changes to every call site.

## Related Questions
- What is the purpose of the `getPropertyPtr` method?
- How does the new implementation affect memory management?
- Why did the reviewer suggest adding locking mechanisms in the future?
- What are the potential risks associated with storing pointers to properties?
- How does this change impact backward compatibility?
- Can you explain the architectural reasoning behind using an array for property storage?

*Source: unknown | chunk_id: github_pr_2891_comment_3085016073*
