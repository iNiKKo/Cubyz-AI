# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactoring, multithreading, property access, pointer safety, tool creation
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** thread safety, pointer misuse

## Summary
Refactored the `getProperty` function in `ProceduralItem` to return a value instead of a pointer and added a new `getPropertyPtr` function. The reviewer expressed concerns about thread safety and potential misuse of pointers.

## Explanation
The change refactors the `getProperty` function to return an `f32` value directly rather than a pointer, which aligns with safer access patterns. A new `getPropertyPtr` function is introduced to provide pointer access if needed. The reviewer's concern revolves around thread safety and the potential for misuse of pointers, suggesting that multithreaded operations on tool creation could lead to issues. The main unresolved concern remains the modification of these values after tool creation.

## Related Questions
- What are the potential thread safety issues with the current implementation of `getProperty` and `getPropertyPtr`?
- How could storing a pointer to a `ProceduralItem` lead to misuse or bugs?
- What architectural changes would be necessary to support multithreaded tool creation in Cubyz?
- Can you explain why returning a value instead of a pointer is considered safer in this context?
- What are the implications of not resolving the concern about modifying values after tool creation?
- How could the new `getPropertyPtr` function be used safely in a multithreaded environment?

*Source: unknown | chunk_id: github_pr_2891_comment_3087585999*
