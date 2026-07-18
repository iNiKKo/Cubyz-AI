# [issues/issue_2047.md] - Issue #2047 discussion

**Type:** review
**Keywords:** item loss, unexpected closure, crafting grid, inventory synchronization, UI clarity, new players
**Symbols:** procedural crafting window, player's inventory, crafting grid, inventory slots
**Concepts:** UI design, user experience, data persistence, inventory management

## Summary
Discussion on handling item loss in procedural crafting grid during unexpected game closures.

## Explanation
The issue revolves around items being lost if the game crashes or is unexpectedly closed while items are placed in the procedural crafting grid. The main concern is ensuring that items remain in the player's inventory until they are actually crafted. Various solutions are proposed, including treating the crafting grid like a chest, using pointers to original inventory slots, and creating a separate persistent crafting inventory. However, there are concerns about UI clarity and potential confusion for new players.

## Related Questions
- How can the crafting grid be modified to prevent item loss during unexpected game closures?
- What are the potential UI impacts of treating the crafting grid like a chest?
- How could pointers to original inventory slots improve item management in the crafting grid?
- What are the implications of creating a separate persistent crafting inventory for each player?
- How can UI clarity be maintained when using pointers or placeholders in the crafting grid?
- What are the potential consequences of arbitrary item placement upon exiting the crafting grid?

*Source: unknown | chunk_id: github_issue_2047_discussion*
