# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** BlockDrop, tool tags, optional fields, isDroppedWhenBrokenWithItem, Tag, Item, behavior consistency, loading logic, Zon files, simplification
**Symbols:** BlockDrop, items, chance, forbiddenToolTags, allowedToolTags, isDroppedWhenBrokenWithItem, Tag, Item
**Concepts:** optional handling, code clarity, simplification, null safety

## Summary
The change introduces new fields for tool tags in the BlockDrop struct and adds a method to determine if an item can drop a block based on its tool tags. The reviewer suggests making these fields non-optional to simplify behavior and logic.

## Explanation
The update to the BlockDrop struct includes two new optional fields, `forbiddenToolTags` and `allowedToolTags`, which are intended to control the conditions under which a block can be dropped based on the tool used. The reviewer points out that the current implementation differentiates between an empty array (`{}`) and a non-existent field (null), suggesting this distinction is unnecessary and could lead to confusion or bugs. By making these fields non-optional, the reviewer proposes simplifying the logic in several areas, including the method `isDroppedWhenBrokenWithItem` and the loading process from Zon files. This change aims to improve code clarity and reduce potential errors related to null handling.

## Related Questions
- What is the purpose of the `forbiddenToolTags` and `allowedToolTags` fields in the BlockDrop struct?
- How does the current implementation handle the distinction between an empty array and a non-existent field for tool tags?
- Why does the reviewer suggest making the tool tag fields non-optional?
- What changes are proposed to simplify the logic related to tool tags?
- How might this change affect the loading process from Zon files?
- What potential issues could arise from handling tool tags as optional fields?

*Source: unknown | chunk_id: github_pr_2886_comment_3106677523*
