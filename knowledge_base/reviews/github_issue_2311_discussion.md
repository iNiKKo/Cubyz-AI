# [issues/issue_2311.md] - Issue #2311 discussion

**Type:** review
**Keywords:** hotbar, inventory, simplification, codebase, pick-blocking, shift-clicking, interactions, usability, readability, maintenance
**Concepts:** code simplification, inventory management, user interactions, feature implementation

## Summary
The discussion revolves around separating the hotbar from the inventory to simplify code, prevent slot mapping issues, and improve usability. However, maintainers are concerned about potential complications with interactions like collecting items and shift-clicking.

## Explanation
The proposal aims to separate the hotbar from the inventory to streamline codebase management and ease future feature implementations such as pick-blocking with middle click (issue #1990). Users express agreement, noting that this change would also help prevent complex slot mappings, especially for armor and accessories (issue #604). The maintainers raise concerns about how this separation might complicate interactions like collecting items and shift-clicking into the combined inventory+hotbar. They suggest that implementing these functionalities separately could be more effort than maintaining a unified system. Users counter with the idea of adding settings to prioritize one inventory over another, aiming to balance usability and code readability.

## Related Questions
- How would separating the hotbar from the inventory affect item collection?
- What are potential inconsistencies with shift-clicking between chest and hotbar inventories?
- Can adding a setting to prioritize one inventory over another resolve usability issues?
- What is the expected effort in implementing separate interactions for hotbar and inventory?
- How might this change impact backwards compatibility with existing user data?
- Are there any performance considerations when separating the hotbar from the inventory?

*Source: unknown | chunk_id: github_issue_2311_discussion*
