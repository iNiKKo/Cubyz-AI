# [issues/issue_73.md] - Issue #73 discussion

**Type:** review
**Keywords:** bag, stack, inventory, fullness, visual cues, commands, synchronization, adventure, items, capacity
**Symbols:** Bag, Stack, Inventory, furnace
**Concepts:** inventory management, stack data structure, visual cues, fullness indication

## Summary
The discussion revolves around implementing an inventory enhancement called 'The Bag', which uses a stack data structure to manage items. The main points include how to visually indicate that a slot is a bag, whether users should be able to view all items in the bag, and how to indicate fullness when the bag is part of a larger structure like a furnace.

## Explanation
The issue proposes adding a 'Bag' feature to the game's inventory system, which behaves like a stack where items can only be accessed from the top. The maintainer suggests using visual cues such as symbols or color changes to indicate that a slot is a bag and recommends showing only the top two items for clarity. Regarding fullness indication, the maintainer proposes changing the frame color of the inventory slot when it's full. The user comments on the practical benefits of having a bag for managing collected items during long adventures. The discussion also touches on how to implement this feature without conflicting with existing inventory systems, considering the removal of `Inventory.Type` in another issue.

## Related Questions
- How can we implement visual cues to indicate that a slot is a bag?
- What are the potential performance implications of using a stack for inventory management?
- How can we ensure compatibility with existing inventory systems after removing `Inventory.Type`?
- What are the best practices for implementing fullness indication in inventory slots?
- How can we handle synchronization between the main inventory and the bag's stack?
- What are the potential user experience benefits of limiting item visibility to only the top two items in a bag?

*Source: unknown | chunk_id: github_issue_73_discussion*
