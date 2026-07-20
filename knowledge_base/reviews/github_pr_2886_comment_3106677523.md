# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** BlockDrop, tool tags, optional fields, isDroppedWhenBrokenWithItem, Tag, Item, behavior consistency, loading logic, Zon files, simplification
**Symbols:** BlockDrop, items, chance, forbiddenToolTags, allowedToolTags, isDroppedWhenBrokenWithItem, Tag, Item
**Concepts:** optional handling, code clarity, simplification, null safety

## Summary
The change introduces new fields for tool tags in the BlockDrop struct and adds a method to determine if an item can drop a block based on its tool tags. The reviewer suggests making these fields non-optional to simplify behavior and logic.

## Explanation
**Explanation**
The update to the `BlockDrop` struct includes two new optional fields, `forbiddenToolTags` and `allowedToolTags`, which are intended to control the conditions under which a block can be dropped based on the tool used. The method `isDroppedWhenBrokenWithItem` checks if an item can drop a block by considering these tags. Specifically, if `item` is not `.proceduralItem`, it returns true only if `allowedToolTags` is null. If `item` is `.proceduralItem`, the method does not perform any additional checks and returns true regardless of the value of `allowedToolTags`. The reviewer suggests making these fields non-optional to simplify behavior and logic, proposing that both empty arrays (`{}`) and non-existent fields (null) should behave the same by checking `allowedToolTags.len == 0`. This change aims to improve code clarity and reduce potential errors related to null handling. Additionally, it simplifies the loading process from Zon files by removing the need for optional checks.

## Related Questions
- What is the purpose of the `forbiddenToolTags` and `allowedToolTags` fields in the BlockDrop struct?
- How does the current implementation handle the distinction between an empty array and a non-existent field for tool tags?
- Why does the reviewer suggest making the tool tag fields non-optional?
- What changes are proposed to simplify the logic related to tool tags?
- How might this change affect the loading process from Zon files?
- What potential issues could arise from handling tool tags as optional fields?

*Source: unknown | chunk_id: github_pr_2886_comment_3106677523*
