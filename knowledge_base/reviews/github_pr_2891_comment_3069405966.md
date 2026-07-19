# [src/items.zig] - PR #2891 review diff

**Type:** review
**Keywords:** refactor, pointer safety, dangling pointers, value return, property access
**Symbols:** ProceduralItem, getProperty, ProceduralItemProperty, properties
**Concepts:** thread safety, memory safety

## Summary
Refactored the `getProperty` function in `ProceduralItem` to return a value instead of a pointer and added a new `getPropertyPtr` function for pointer access.

## Explanation
The change refactors the `getProperty` function to return an `f32` value directly rather than a pointer. This modification aims to prevent the creation of dangling pointers, which can lead to undefined behavior or memory corruption. The addition of a new `getPropertyPtr` function allows for scenarios where direct pointer access is necessary, maintaining flexibility while enhancing safety.

The original `getProperty` function now uses `@intFromEnum(prop)` to access the properties array directly instead of using a switch statement. This change simplifies the code and improves performance by avoiding the overhead of a switch statement.

The reviewer suggests renaming the original `getProperty` function to `setProperty`, but this change is not included in the provided diff.

## Related Questions
- What is the purpose of the `getPropertyPtr` function?
- How does this change impact memory safety in Cubyz?
- Why was the original `getProperty` function modified to return a value instead of a pointer?
- Is there any potential performance impact from returning values instead of pointers?
- What are the implications of adding a new `setProperty` function as suggested by the reviewer?
- How does this change affect backward compatibility with existing code?

*Source: unknown | chunk_id: github_pr_2891_comment_3069405966*
