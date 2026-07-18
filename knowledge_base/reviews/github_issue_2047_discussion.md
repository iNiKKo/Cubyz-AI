# [issues/issue_2047.md] - Issue #2047 discussion

**Type:** review
**Keywords:** item loss, unexpected closure, crafting grid, inventory synchronization, UI clarity, new players
**Symbols:** procedural crafting window, player's inventory, crafting grid, inventory slots
**Concepts:** UI design, user experience, data persistence, inventory management

## Summary
Discussion on handling item loss in procedural crafting grid during unexpected game closures.

## Explanation
Discussion on handling item loss in procedural crafting grid during unexpected game closures. The issue arises when items placed in the procedural crafting window are lost if the game crashes or is unexpectedly closed, as these items are not stored in the player's inventory until after an item has been crafted. Proposed solutions include treating the crafting grid like a chest to prevent item loss and using pointers to original inventory slots to maintain UI clarity. Another suggestion involves creating a separate persistent crafting inventory for each player that moves back into their primary inventory upon reconnection, with semitransparent placeholders indicating occupied slots when items are stored elsewhere. However, there is concern about the potential negative impact on user experience due to confusing UI design and unfamiliarity for new players.

## Related Questions
- How can the crafting grid be modified to prevent item loss during unexpected game closures?
- What are the potential UI impacts of treating the crafting grid like a chest?
- How could pointers to original inventory slots improve item management in the crafting grid?
- What are the implications of creating a separate persistent crafting inventory for each player?
- How can UI clarity be maintained when using pointers or placeholders in the crafting grid?
- What are the potential consequences of arbitrary item placement upon exiting the crafting grid?

*Source: unknown | chunk_id: github_issue_2047_discussion*
