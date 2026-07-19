# [issues/issue_73.md] - Issue #73 discussion

**Type:** review
**Keywords:** bag, stack, inventory, fullness, visual cues, commands, synchronization, adventure, items, capacity
**Symbols:** Bag, Stack, Inventory, furnace
**Concepts:** inventory management, stack data structure, visual cues, fullness indication

## Summary
The discussion revolves around implementing an inventory enhancement called 'The Bag', which uses a stack data structure to manage items. The main points include how to visually indicate that a slot is a bag, whether users should be able to view all items in the bag, and how to indicate fullness when the bag is part of a larger structure like a furnace.

## Explanation
The discussion revolves around implementing an inventory enhancement called 'The Bag', which uses a stack data structure to manage items. The maintainer suggests using visual cues such as symbols or color changes to indicate that a slot is a bag, and recommends showing only the top two items for clarity (the one behind slightly gray). Regarding fullness indication, the maintainer proposes changing the frame color of the inventory slot when it's full. Users comment on the practical benefits of having a bag for managing collected items during long adventures. The discussion also touches on how to implement this feature without conflicting with existing inventory systems after removing `Inventory.Type` in another issue. Specifically, there are suggestions about adding sync commands for deposit and take operations to handle synchronization between the main inventory and the bag's stack. Additionally, it is proposed that the bag could be implemented as a single item slot where you can access the top-most item or put new stuff into it, allowing for expanding the inventory while encouraging strategy in inventory management.

## Related Questions
- How can we implement visual cues such as symbols or color changes to indicate that a slot is a bag?
- What are the best practices for showing only the top two items in a bag, with the one behind slightly gray?
- How can we change the frame color of an inventory slot when it's full?
- What are the practical benefits of having a bag for managing collected items during long adventures?
- How can we add sync commands for deposit and take operations to handle synchronization between the main inventory and the bag's stack?

*Source: unknown | chunk_id: github_issue_73_discussion*
