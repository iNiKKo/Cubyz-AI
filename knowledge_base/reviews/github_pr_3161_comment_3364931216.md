# [src/server/command.zig] - PR #3161 review diff

**Type:** review
**Keywords:** MaskExpression, global allocator, parser, command, memory management, architectural review
**Symbols:** MaskExpression
**Concepts:** memory management, architectural design

## Summary
A new struct `MaskExpression` is introduced to handle mask expressions, but it uses the global allocator.

## Explanation
The introduction of the `MaskExpression` struct aims to provide a mechanism for handling mask expressions. However, the reviewer raises concerns about architectural separation, suggesting that memory management should be handled by the command rather than the parser structs. This approach avoids cluttering the parser with extra memory management code and aligns better with the responsibilities of each component.

## Related Questions
- What is the purpose of the `MaskExpression` struct?
- Why does it use the global allocator?
- How does this change affect memory management in the parser?
- What are the potential drawbacks of handling memory management in the command instead of the parser?
- How can we ensure that the global allocator usage is appropriate for all cases?
- Are there any performance implications of using the global allocator in this context?

*Source: unknown | chunk_id: github_pr_3161_comment_3364931216*
