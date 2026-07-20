# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactor, pointer safety, dangling pointers, value return, property access
**Symbols:** ProceduralItem, getProperty, ProceduralItemProperty, properties
**Concepts:** thread safety, memory safety

## Summary
Refactored the `getProperty` function in `ProceduralItem` to return a value instead of a pointer and added a new `getPropertyPtr` function for pointer access.

## Explanation
Refactored the `getProperty` function in `ProceduralItem` to return an `f32` value directly rather than a pointer and added a new `getPropertyPtr` function for pointer access. The `getPropertyPtr` function allows for scenarios where direct pointer access is necessary, maintaining flexibility while enhancing safety.

## Related Questions
- What is the purpose of the `getPropertyPtr` function?

*Source: unknown | chunk_id: github_pr_2891_comment_3069405966*
