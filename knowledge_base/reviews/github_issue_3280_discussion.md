# [issues/issue_3280.md] - Issue #3280 discussion

**Type:** review
**Keywords:** breaking grass, placing flowers, floating behavior, sickle tool, support blocks
**Symbols:** grass, sickle, flowers, floating foliage
**Concepts:** game mechanics, user interaction, bug tracking

## Summary
The issue involves unexpected interactions with floating foliage, such as breaking grass without a sickle and placing flowers on top of each other.

## Explanation
The problem arises from the game's mechanics allowing players to break grass without a tool like a sickle. Additionally, flowers can be placed in a way that they float above each other, creating unintended behavior. The maintainer notes that floating flowers are intentional but acknowledges it could be problematic in certain scenarios. A user points out that blocks with specific update behaviors (like checking support blocks) break when updated, which is related to another issue (#2486).

## Related Questions
- What is the intended behavior for breaking grass without a sickle?
- How does the game handle floating flowers in terms of placement and interaction?
- Is there a way to prevent floating flowers from being placed on top of each other?
- What are the implications of allowing grass to be broken without a tool?
- How does the `.onUpdate` behavior affect block interactions?
- Are there any plans to address the issue of breaking grass without a sickle in creative mode?

*Source: unknown | chunk_id: github_issue_3280_discussion*
