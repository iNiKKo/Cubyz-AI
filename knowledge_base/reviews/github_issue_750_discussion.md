# [issues/issue_750.md] - Issue #750 discussion

**Type:** review
**Keywords:** crafting table, inventory sharing, workbench, recipe selection, tool types, user experience, conflict resolution, inventory management, button blocking, item restrictions
**Symbols:** crafting table, inventory sharing, workbench, recipe selection, tool types
**Concepts:** user experience, conflict resolution, inventory management

## Summary
Discussion on sharing the inventory of the crafting table between players, with concerns about user experience and consistency.

## Explanation
The discussion revolves around implementing a feature to share the inventory of the crafting table between multiple players. The main challenge is ensuring that the shared inventory does not lead to confusion or conflicts when different tool types are selected by different players. Several solutions are proposed, including blocking buttons if items are in the grid, linking recipe selection between players, and allowing different tool types but with restrictions on item usage.

**Technical Challenges:**
- Ensuring that the shared inventory does not lead to confusion or conflicts when different tool types are selected by different players.
- Implementing a consistent framework for bridging block entities with workstations without loads of boilerplate.

**Callback Mechanism:**
The callback mechanism for depositing items into the player's inventory when they close the workbench is discussed as part of the implementation feasibility. With #2770, the deposit is now inside a callback, and it is feasible to achieve syncing through something like commented here: https://github.com/PixelGuys/Cubyz/pull/2770#discussion_r2971323523.

**Workbench Inventory Storage:**
The discussion includes the consideration about whether the workbench should store its inventory per block or not. There is a suggestion to ideally have the workbench store its items, as many times when crafting a tool, players will be almost done but need one more thing from a chest, so they have to close the workbench, grab that item, then remake the whole tool again.

**Proposed Solutions:**
- **Blocking Buttons if Items are in the Grid:** This solution involves blocking the button if any items are in the grid. However, it is noted that this might seem weird from a user standpoint and could lead to confusion or frustration.
- **Linking Recipe Selection Between Players:** Another proposed solution is to link recipe selection between players. This would ensure that all players using the same workbench see the same recipes selected, but it also introduces potential issues with tool type restrictions.
- **Allowing Different Tool Types with Restrictions on Item Usage:** A third solution involves allowing different tool types but restricting item usage based on the selected tool. For example, if one player selects a pickaxe, they would only be able to use slots that are allowed by the pickaxe, and any other items would get a red overlay.

**User Experience Concerns:**
The discussion also addresses user experience issues such as blocking buttons and ensuring seamless switching between tool types without requiring players to remove materials from the grid. There is concern about the potential drawbacks of allowing multiple players to use the same crafting table simultaneously, such as confusion over who gets the items when the workbench is closed.

**Maintainer Comments:**
The maintainer notes that if all 'crafting' blocks share the inventory between players, it should establish a rule. However, there are concerns about having two players with the same table open but different tools selected, which could lead to confusion or conflicts. The maintainer also suggests blocking the button if any items are in the grid and linking recipe selection between players as potential solutions.

**User Comments:**
Users propose various solutions, including allowing different tool types but with restrictions on item usage, and suggest that this would introduce a little bit of rework but provide an interesting experience for players. They also mention that ideally, the workbench should store its items to avoid having to close it and remake tools when needing additional materials.

## Related Questions
- What specific technical challenges need to be addressed for inventory sharing in the crafting table?
- How does the callback mechanism work for depositing items into a player's inventory when they close the workbench?
- Why is it important to decide whether the workbench should store its inventory per block or not?
- What are the proposed solutions to handle different tool types on the same workbench without causing conflicts?
- How does blocking buttons if items are in the grid address user experience issues?
- What are the potential drawbacks of allowing multiple players to use the same crafting table simultaneously?

*Source: unknown | chunk_id: github_issue_750_discussion*
