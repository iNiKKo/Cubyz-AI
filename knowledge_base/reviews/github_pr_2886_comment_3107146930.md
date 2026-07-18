# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** optional, tool tags, block drop, item stack, architectural review
**Symbols:** BlockDrop, forbiddenToolTags, allowedToolTags, isDroppedWhenBrokenWithItem
**Concepts:** optional fields, default behavior, code clarity

## Summary
Added optional fields for forbidden and allowed tool tags in BlockDrop struct.

## Explanation
The change introduces two new optional fields, `forbiddenToolTags` and `allowedToolTags`, to the `BlockDrop` struct. The reviewer suggests keeping these fields optional to explicitly indicate that not specifying them is valid behavior. This approach avoids ambiguity where an empty array might be misinterpreted as allowing all tools instead of none. The reviewer emphasizes the importance of clear expectations for developers reading the code, ensuring that the default behavior (allowing all tools when unspecified) is intuitive and predictable.

## Related Questions
- What is the purpose of the `forbiddenToolTags` and `allowedToolTags` fields in the BlockDrop struct?
- How does the presence or absence of these optional fields affect the behavior of block drops?
- Why was it decided to keep these fields optional instead of mandatory?
- Can you explain the default behavior when neither `forbiddenToolTags` nor `allowedToolTags` is specified?
- What potential issues could arise from interpreting an empty array as allowing all tools?
- How does this change impact the overall design and maintainability of the blocks module?

*Source: unknown | chunk_id: github_pr_2886_comment_3107146930*
