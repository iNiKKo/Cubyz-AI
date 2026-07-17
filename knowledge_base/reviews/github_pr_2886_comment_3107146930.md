# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** optional, tool tags, block drop, item stack, behavior specification
**Symbols:** BlockDrop, forbiddenToolTags, allowedToolTags, isDroppedWhenBrokenWithItem
**Concepts:** optional fields, default behavior, code clarity

## Summary
Added optional fields for forbidden and allowed tool tags in BlockDrop struct.

## Explanation
The change introduces two new optional fields, `forbiddenToolTags` and `allowedToolTags`, to the `BlockDrop` struct. The reviewer suggests keeping these fields optional to explicitly indicate that not specifying them is valid behavior. This approach avoids ambiguity where an empty array might be misinterpreted as allowing all tools instead of none. The reviewer emphasizes the importance of clear communication in code, ensuring that developers understand the default behaviors associated with unspecified fields.

## Related Questions
- What is the purpose of the `forbiddenToolTags` and `allowedToolTags` fields in the BlockDrop struct?
- How does the presence or absence of `allowedToolTags` affect tool validity according to the code?
- Why are the new fields marked as optional in the BlockDrop struct?
- What is the potential impact of using an empty array for `allowedToolTags` instead of leaving it null?
- How does this change improve code clarity and prevent misunderstandings about default behavior?
- Can you explain the architectural reasoning behind making these tool tag fields optional?

*Source: unknown | chunk_id: github_pr_2886_comment_3107146930*
