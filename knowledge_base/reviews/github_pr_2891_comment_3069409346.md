# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactoring, pointer manipulation, value access, API completeness, flexible access
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** API design, flexibility, symmetry

## Summary
Refactored the `ProceduralItem` struct by renaming the `getProperty` function to `getPropertyPtr` and adding a new `getProperty` function that returns a value instead of a pointer.

## Explanation
The refactoring aims to provide flexibility in accessing properties of `ProceduralItem`. The original `getProperty` method, which returned a pointer to an `f32`, has been renamed to `getPropertyPtr`. A new `getProperty` function has been added that returns the property value directly. This change allows for scenarios where only the value is needed without the overhead or potential issues associated with pointer manipulation. The reviewer suggests considering adding a corresponding `setProperty` method for completeness, indicating an intention to maintain symmetry in the API.

## Related Questions
- What is the purpose of renaming `getProperty` to `getPropertyPtr`?
- Why was a new `getProperty` function added?
- Does this change affect existing code that uses `ProceduralItem`?
- How does this refactoring improve the flexibility of accessing properties?
- Is there any potential performance impact from returning values instead of pointers?
- What are the implications of adding a `setProperty` method in future updates?

*Source: unknown | chunk_id: github_pr_2891_comment_3069409346*
