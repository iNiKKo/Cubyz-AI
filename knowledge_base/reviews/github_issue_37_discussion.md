# [issues/issue_37.md] - Issue #37 discussion

**Type:** review
**Keywords:** crafting bug, workbench, trashbin, chest, inventory full, fallback mechanism
**Concepts:** bug fixing, item management, inventory system

## Summary
The discussion revolves around fixing the bug where crafting items disappear when closing the workbench. The proposed solutions include storing items inside the block, dropping them on the ground, or returning them to the player.

## Explanation
The issue is related to item management during crafting in a game environment. The current implementation uses option 3 (returning items to the player) for inventory-based crafting with a fallback to option 2 (dropping items) if the inventory is full. The maintainers suggest using the same approach for the workbench but only after implementing a proper trash bin or chest to handle discarded items outside the inventory.

## Related Questions
- What is the current behavior of item management when closing the workbench?
- How does the inventory system handle crafting items when the inventory is full?
- Why is a proper trash bin or chest needed before implementing option 3 for the workbench?
- Can you explain the fallback mechanism used in the current inventory-based crafting?
- What are the potential consequences of not fixing this bug?
- How does the proposed solution address the issue of lost items during crafting?

*Source: unknown | chunk_id: github_issue_37_discussion*
