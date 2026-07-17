# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactoring, memory usage, pointer manipulation, code clarity, flexibility, value return, pointer return, property access
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** Memory Management, Code Clarity, Flexibility

## Summary
Refactored the `getProperty` method in `ProceduralItem` to return a value instead of a pointer, added a new `getPropertyPtr` method for when a pointer is needed.

## Explanation
The change refactors the existing `getProperty` method to directly return an `f32` value rather than a pointer. This modification aligns with scenarios where only the value is required, optimizing memory usage and reducing potential issues related to pointer manipulation. Additionally, a new `getPropertyPtr` method was introduced to provide access to the property's pointer when necessary. The reviewer suggests that this approach maintains flexibility while improving code clarity and safety.

## Related Questions
- What is the purpose of renaming `getProperty` to return a value instead of a pointer?
- Why was a new `getPropertyPtr` method added?
- How does this change impact memory management in Cubyz?
- Can you explain the benefits of returning a value directly from `getProperty`?
- What are the potential drawbacks of using pointers in property access?
- How does this refactoring align with the overall architecture of Cubyz?

*Source: unknown | chunk_id: github_pr_2891_comment_3069409346*
