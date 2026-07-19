# [issues/issue_913.md] - Issue #913 discussion

**Type:** review
**Keywords:** item stacks, quantity, inventory slots, save, reload, bug
**Concepts:** inventory management, serialization, deserialization

## Summary
The issue involves item stacks showing incorrect quantities (0 or 64) in specific inventory slots after saving and reloading the world.

## Explanation
The user reports an issue where items placed in inventory slots that were previously occupied show a quantity of 0 after saving and reloading the world. New slots display the correct quantity (64). The steps to reproduce this issue are as follows: start from a new world, add some items to your inventory using the creative menu, exit the world, re-enter the world, grab saved items, and place them back in any of the previously occupied slots. They now show 0 quantity, while other slots display the correct quantity (64). This could indicate a bug related to inventory serialization or deserialization where the state of certain slots is not correctly saved or loaded.

## Related Questions
- What is the current state of inventory serialization in Cubyz?
- Are there any known issues with deserializing specific inventory slots?
- How does Cubyz handle item stack quantities during save and load operations?
- Can you provide a detailed log of the steps taken to reproduce this issue?
- Is there any code related to inventory management that might be causing this bug?
- Have there been any recent changes in the inventory system that could affect serialization/deserialization?

*Source: unknown | chunk_id: github_issue_913_discussion*
