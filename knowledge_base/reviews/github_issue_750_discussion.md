# [issues/issue_750.md] - Issue #750 discussion

**Type:** review
**Keywords:** crafting table, inventory sharing, workbench, recipe selection, tool types, user experience, conflict resolution, inventory management, button blocking, item restrictions
**Symbols:** crafting table, inventory sharing, workbench, recipe selection, tool types
**Concepts:** user experience, conflict resolution, inventory management

## Summary
Discussion on sharing the inventory of the crafting table between players, with concerns about user experience and consistency.

## Explanation
The discussion revolves around implementing a feature to share the inventory of the crafting table between multiple players, focusing on technical implementation details and user experience concerns. The main challenge is ensuring that the shared inventory does not lead to confusion or conflicts when different tool types are selected by different players. Several solutions are proposed, including blocking buttons if items are in the grid, linking recipe selection between players, and allowing different tool types but with restrictions on item usage. There is also a consideration about whether the workbench should store its inventory per block or not. The callback mechanism for depositing items into the player's inventory when they close the workbench is discussed as part of the implementation feasibility. Additionally, there are concerns about user experience issues such as blocking buttons and ensuring seamless switching between tool types without requiring players to remove materials from the grid.

## Related Questions
- What specific technical challenges need to be addressed for inventory sharing in the crafting table?
- How does the callback mechanism work for depositing items into a player's inventory when they close the workbench?
- Why is it important to decide whether the workbench should store its inventory per block or not?
- What are the proposed solutions to handle different tool types on the same workbench without causing conflicts?
- How does blocking buttons if items are in the grid address user experience issues?
- What are the potential drawbacks of allowing multiple players to use the same crafting table simultaneously?

*Source: unknown | chunk_id: github_issue_750_discussion*
