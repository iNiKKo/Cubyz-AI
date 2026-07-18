# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** multithreading, property access, pointer safety, refactoring, architecture
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** thread safety, memory management

## Summary
Refactored `getProperty` method in `ProceduralItem` to return a value instead of a pointer, and added a new `getPropertyPtr` method. Addressed concerns about multithreading and potential misuse of pointers.

## Explanation
The change refactors the `getProperty` method to return an `f32` value directly rather than a pointer to it. This modification aims to prevent issues related to multithreading, where multiple threads might attempt to modify the same property concurrently without proper synchronization. The addition of `getPropertyPtr` provides a way to obtain a pointer if needed, but this is done with caution to avoid potential misuse and threading issues. The reviewer remains concerned about modifying properties after tool creation, indicating that further safeguards or architectural considerations may be necessary.

## Related Questions
- What are the potential risks of using `getPropertyPtr` in a multithreaded environment?
- How does this change impact the performance of property access in `ProceduralItem`?
- Are there any backward compatibility issues introduced by this refactoring?
- What additional measures should be taken to ensure thread safety when accessing properties?
- Can you explain the rationale behind changing `getProperty` to return a value instead of a pointer?
- How might this change affect existing code that relies on direct property access?

*Source: unknown | chunk_id: github_pr_2891_comment_3087585999*
