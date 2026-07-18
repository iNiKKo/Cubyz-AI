# [src/utils.zig] - PR #1425 review diff

**Type:** review
**Keywords:** format, allocator, comptime, variadic arguments, refactor, architectural decision
**Symbols:** format, NeverFailingAllocator, CastFunctionReturnToAnyopaque
**Concepts:** string formatting, memory allocation, compile-time optimizations

## Summary
A new function `format` is added to the `utils.zig` file, which formats strings using an allocator and variadic arguments.

## Explanation
The addition of the `format` function introduces a new utility for string formatting in Cubyz. The reviewer highlights that this change should be discussed further as it represents a significant architectural decision. The function uses a `NeverFailingAllocator` to allocate memory for the formatted string, ensuring that allocation failures are not handled, which could lead to undefined behavior if the allocator fails. The use of `comptime fmt` suggests that the format string is known at compile time, optimizing performance by allowing compile-time checks and optimizations. However, the reviewer cautions against integrating this change without further discussion, emphasizing that it should be part of a larger refactor or decision-making process.

## Related Questions
- What is the purpose of using `NeverFailingAllocator` in the `format` function?
- How does the use of `comptime fmt` affect performance and error handling?
- Why is the reviewer concerned about integrating this change without further discussion?
- Can you provide examples of how to use the new `format` function?
- What are the potential implications of not handling allocation failures in this context?
- How does this change impact backwards compatibility with existing Cubyz code?

*Source: unknown | chunk_id: github_pr_1425_comment_2127380619*
