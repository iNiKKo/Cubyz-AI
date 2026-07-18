# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactoring, array lookup, property access, locking, syntax sugar, Zig design
**Symbols:** ProceduralItem, getProperty, setProperty, properties
**Concepts:** thread safety, pointer management

## Summary
Refactored the `getProperty` function to use an array lookup and added a new `getPropertyPtr` function for pointer access.

## Explanation
The change refactors the `getProperty` function in the `ProceduralItem` struct to use an array lookup instead of inline field access. This approach is more future-proof as it allows adding locking mechanisms without altering every call site. A new `getPropertyPtr` function is introduced for scenarios where a pointer to the property value is needed. The reviewer expresses concern about potential misuse of pointers and questions the design choice, suggesting that Zig typically avoids such syntax sugar.

## Related Questions
- What is the purpose of the `getPropertyPtr` function?
- How does the new array-based property access improve future-proofing?
- Why did the reviewer express concern about pointer management?
- Can you explain the potential risks associated with storing pointers to properties?
- How might adding locking mechanisms benefit the `ProceduralItem` struct?
- What are the implications of using syntax sugar in Zig's design?

*Source: unknown | chunk_id: github_pr_2891_comment_3085016073*
