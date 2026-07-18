# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** enum, zero-byte, allocator, error, explicit type, u8
**Symbols:** SelectionRule, SelectionCapability
**Concepts:** enum optimization, allocator error prevention

## Summary
The code introduces a new enum `SelectionCapability` in place of `SelectionRule`, addressing an issue with zero-byte enums and allocator errors.

## Explanation
The reviewer points out that Zig optimizes enums with only one value to be 0 bytes, which causes issues when trying to allocate arrays of such enums. To prevent this, the enum is explicitly defined with a type (u8) to ensure it occupies at least one byte, thus avoiding allocator errors.

## Related Questions
- Why did the reviewer change `SelectionRule` to `SelectionCapability`?
- What is the purpose of explicitly defining the enum with a type (u8)?
- How does Zig handle enums with only one value by default?
- What kind of error occurs when trying to allocate an array of zero-byte elements in Zig?
- Can you explain the architectural reasoning behind this change?
- Is there any potential performance impact from explicitly defining the enum type?

*Source: unknown | chunk_id: github_pr_2987_comment_3179750006*
