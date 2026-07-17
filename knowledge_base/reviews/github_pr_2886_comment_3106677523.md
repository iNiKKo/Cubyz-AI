# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** optional fields, behavior difference, non-optional fields, simplify logic, loading processes
**Symbols:** BlockDrop, items, chance, forbiddenToolTags, allowedToolTags, isDroppedWhenBrokenWithItem
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added optional fields for forbidden and allowed tool tags to BlockDrop struct and discussed handling of these fields in a review.

## Explanation
The change introduces two new optional fields, `forbiddenToolTags` and `allowedToolTags`, to the `BlockDrop` struct. The reviewer raises concerns about the current behavior difference between an empty array and a non-existent field for `allowedToolTags`. They suggest making these fields non-optional and checking their length to simplify logic in checks and loading processes.

## Related Questions
- What is the purpose of the `forbiddenToolTags` and `allowedToolTags` fields in the BlockDrop struct?
- How does the current implementation handle the difference between an empty array and a non-existent field for allowedToolTags?
- Why does the reviewer suggest making the tool tag fields non-optional?
- What changes would be required to simplify the checks below with the proposed change?
- How would the loading logic be affected by removing the optional nature of the tool tag fields?
- Can you explain the potential impact on backwards compatibility with this change?

*Source: unknown | chunk_id: github_pr_2886_comment_3106677523*
